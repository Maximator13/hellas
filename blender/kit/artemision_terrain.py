import math
import os

import bmesh
import numpy as np
from mathutils.bvhtree import BVHTree

from . import artemision_plan as plan
from .acropole_terrain import (Field, blur, cached_image, decimated, load_tile, mix, neighbourhood, offset_grid,
                               remove_inside, smoothstep, world_noise)
from .materials import baked_material, download
from .phare_terrain import segment_distance, segments
from .terrain import polygon_mask, polyline_distance

DEM_TILES = (("Copernicus_DSM_COG_10_N38_00_E026_00_DEM", "Copernicus_DSM_COG_10_N38_00_E027_00_DEM"),
             ("Copernicus_DSM_COG_10_N37_00_E026_00_DEM", "Copernicus_DSM_COG_10_N37_00_E027_00_DEM"))
DEM_URL = "https://copernicus-dem-30m.s3.amazonaws.com/{0}/{0}.tif"
DEM_LICENCE = ("Copernicus DEM GLO-30 (ESA, Copernicus programme), free licence with attribution: produced using "
               "Copernicus WorldDEM-30 (c) DLR e.V. 2010-2014 and (c) Airbus Defence and Space GmbH 2014-2018 "
               "provided under COPERNICUS by the European Union and ESA")
DEM_TOP = 39.0
DEM_WEST = 26.0
DEM_STEP = 1.0 / 3600.0
NEAR_SPACING = 5.0
MID_SPACING = 30.0
MID_MESH_SPACING = 60.0
FAR_SPACING = 250.0
FAR_MESH_SPACING = 500.0
LAND_FLOOR = 0.8
SEA_EDGE = 45.0
RIVERS = ((plan.KAYSTROS, 34.0, -0.9), (plan.KAYSTROS_BRANCH, 16.0, -0.7), (plan.SELINOUS, 9.0, -0.5),
          (plan.MARNAS, 10.0, -0.5))


def load_dem(cache_dir):
    rows = []
    for row in DEM_TILES:
        tiles = []
        for name in row:
            path = download(DEM_URL.format(name), os.path.join(cache_dir, "src", "dem", f"{name}.tif"))
            tiles.append(load_tile(path))
        rows.append(np.hstack(tiles))
    return np.vstack(rows)


def resample(dem, xs, ys):
    latitude, longitude = plan.FRAME.to_geo(xs, ys)
    rows = np.clip((DEM_TOP - latitude) / DEM_STEP, 0, dem.shape[0] - 1.001)
    columns = np.clip((longitude - DEM_WEST) / DEM_STEP, 0, dem.shape[1] - 1.001)
    r0 = rows.astype(int)
    c0 = columns.astype(int)
    fy = rows - r0
    fx = columns - c0
    top = dem[r0, c0] * (1 - fx) + dem[r0, c0 + 1] * fx
    bottom = dem[r0 + 1, c0] * (1 - fx) + dem[r0 + 1, c0 + 1] * fx
    return (top * (1 - fy) + bottom * fy).astype(np.float64)


def canopy_free(raw, spacing):
    if spacing > 60.0:
        return blur(raw, 1)
    passes = max(int(round(30.0 / spacing)), 1)
    opened = neighbourhood(neighbourhood(raw, passes, np.minimum), passes, np.maximum)
    return blur(opened, max(int(round(20.0 / spacing)), 1))


def signed(polygon, gx, gy, reach):
    starts, ends = segments([polygon], [True])
    distance = segment_distance(gx, gy, starts, ends, reach)
    return np.where(polygon_mask(polygon, gx, gy), distance, -distance)


def plain_weight(smooth):
    return 1.0 - smoothstep((smooth - 9.0) / 12.0)


def ancient(raw, gx, gy, spacing):
    smooth = canopy_free(raw, spacing)
    plainness = plain_weight(smooth)
    reach = np.hypot(gx + 40.0, gy)
    deposit = 2.5 + 2.6 * (1.0 - smoothstep((reach - 1800.0) / 3500.0))
    land = np.maximum(smooth - deposit * plainness, LAND_FLOOR)
    pad = sanctuary_pad(gx, gy)
    land = land * (1 - pad) + plan.GROUND_LEVEL * pad
    noise = world_noise(gx, gy, 220.0, 41, 4)
    sea_distance = signed(plan.SEA, gx, gy, 3000.0)
    open_water = -1.4 - 8.0 * smoothstep(sea_distance / 1800.0) - 1.2 * smoothstep(sea_distance / 120.0)
    sea = smooth - plainness * (smooth - open_water)
    modern_sea = raw <= 0.4
    sea = np.where(modern_sea, np.minimum(sea, -6.0), sea)
    heights = mix(land[..., None], sea[..., None], smoothstep((sea_distance + 12.0) / SEA_EDGE))[..., 0]
    marsh_distance = signed(plan.MARSH, gx, gy, 600.0)
    fine = world_noise(gx, gy, 45.0, 43, 3)
    marsh = 0.32 + 1.7 * (noise - 0.5) + 0.8 * (fine - 0.5)
    marsh_weight = smoothstep((marsh_distance + 30.0) / 90.0) * plainness * (1 - pad)
    heights = mix(heights[..., None], marsh[..., None], marsh_weight)[..., 0]
    for path, width, depth in RIVERS:
        distance = polyline_distance(path, gx, gy)
        floor = np.where(heights > 3.0, heights - 1.4, np.minimum(heights, depth))
        weight = smoothstep(1.0 - (distance - width / 2) / max(spacing * 1.5, 6.0)) * plainness
        heights = heights * (1 - weight) + floor * weight
    heights = np.where(modern_sea & (sea_distance < 0), np.minimum(heights, -4.0), heights)
    return heights, sea_distance, marsh_distance, plainness, pad


def sanctuary_pad(gx, gy):
    u = np.maximum(np.abs(gx + 30.0) - 175.0, 0.0)
    v = np.maximum(np.abs(gy) - 150.0, 0.0)
    outer = np.hypot(u, v)
    west = smoothstep((gx + 205.0) / 20.0)
    return smoothstep(1.0 - outer / 70.0) * west


class Ground:
    def __init__(self, near, mid, far):
        self.near, self.mid, self.far = near, mid, far
        self.trees = []

    def __call__(self, x, y):
        if self.near.contains(x, y, 6.0):
            return self.near.sample(x, y)
        if self.mid.contains(x, y, 700.0):
            return self.mid.sample(x, y)
        return self.far.sample(x, y)

    def grid(self, xs, ys):
        heights = self.far.sample(xs, ys)
        in_mid = (np.abs(xs - self.mid.cx) < self.mid.half - 700.0) & (np.abs(ys - self.mid.cy) < self.mid.half - 700.0)
        heights = np.where(in_mid, self.mid.sample(xs, ys), heights)
        in_near = (np.abs(xs - self.near.cx) < self.near.half - 6.0) & (np.abs(ys - self.near.cy) < self.near.half - 6.0)
        return np.where(in_near, self.near.sample(xs, ys), heights)

    def is_water(self, x, y, margin=0.25):
        return self(x, y) < margin

    def add_surface(self, objects):
        for obj in objects:
            mesh = obj.data
            matrix = obj.matrix_world
            vertices = [matrix @ v.co for v in mesh.vertices]
            self.trees.append(BVHTree.FromPolygons(vertices, [p.vertices[:] for p in mesh.polygons]))

    def surface(self, x, y, hint=None, reach=6.0):
        base = self(x, y) if hint is None else hint
        best = None
        for tree in self.trees:
            hit = tree.ray_cast((x, y, base + reach), (0.0, 0.0, -1.0), reach + 60.0)
            if hit[0] is not None and (best is None or hit[0].z > best):
                best = hit[0].z
        return best if best is not None else self(x, y)


def mid_field(dem):
    field = Field(0.0, 0.0, plan.MID_HALF + 600.0, MID_SPACING)
    raw = resample(dem, field.gx, field.gy)
    field.heights, field.sea, field.marsh, field.plain, _ = ancient(raw, field.gx, field.gy, MID_SPACING)
    return field


def near_field(dem, mid):
    cx, cy = plan.NEAR_CENTRE
    field = Field(cx, cy, plan.NEAR_HALF, NEAR_SPACING)
    gx, gy = field.gx, field.gy
    raw = resample(dem, gx, gy)
    heights, field.sea, field.marsh, field.plain, field.pad = ancient(raw, gx, gy, NEAR_SPACING)
    edge = np.maximum(np.abs(gx - cx), np.abs(gy - cy))
    rim = smoothstep((edge - plan.NEAR_HALF + 90.0) / 80.0)
    field.heights = heights * (1 - rim) + mid.sample(gx, gy) * rim
    return field


def far_field(dem, mid):
    field = Field(0.0, 0.0, plan.FAR_HALF, FAR_SPACING)
    raw = resample(dem, field.gx, field.gy)
    heights, _, _, _, _ = ancient(raw, field.gx, field.gy, FAR_SPACING)
    inside = (np.abs(field.gx - mid.cx) < mid.half - 400.0) & (np.abs(field.gy - mid.cy) < mid.half - 400.0)
    field.heights = np.where(inside, mid.sample(field.gx, field.gy), heights)
    return field


def sun_shadow(field, xs, ys, heights, steps=30, reach=4000.0):
    azimuth, elevation = math.radians(plan.SUN[0]), math.radians(plan.SUN[1])
    dx, dy = math.sin(azimuth), math.cos(azimuth)
    slope = math.tan(elevation)
    clearance = np.full(heights.shape, np.inf)
    for step in range(1, steps + 1):
        distance = reach * (step / steps) ** 1.6
        ahead = field.sample(xs + dx * distance, ys + dy * distance)
        clearance = np.minimum(clearance, heights + distance * slope - ahead)
    return np.clip(clearance / 10.0 + 0.5, 0.0, 1.0)


def land_colour(xs, ys, heights, slope):
    noise = world_noise(xs, ys, 600.0, 3, 4)
    fine = world_noise(xs, ys, 25.0, 4, 3)
    grain = world_noise(xs, ys, 5.0, 5, 2)
    angle = math.radians(14.0)
    u = xs * math.cos(angle) - ys * math.sin(angle)
    v = xs * math.sin(angle) + ys * math.cos(angle)
    pu = np.floor(u / 90.0).astype(np.int64)
    pv = np.floor(v / 55.0).astype(np.int64)
    parcel = ((pu * 73856093) ^ (pv * 19349663)) % 1000 / 1000.0
    crops = np.array([[0.46, 0.55, 0.26], [0.52, 0.58, 0.30], [0.60, 0.62, 0.34], [0.42, 0.50, 0.24],
                      [0.66, 0.60, 0.40], [0.50, 0.56, 0.28]])
    colour = crops[(parcel * len(crops)).astype(int) % len(crops)] * (0.9 + 0.16 * fine)[..., None]
    meadow = np.array([0.44, 0.52, 0.25]) * (0.88 + 0.2 * grain)[..., None]
    colour = mix(colour, meadow, smoothstep((world_noise(xs, ys, 300.0, 7, 3) - 0.55) / 0.1) * 0.8)
    flowers = (world_noise(xs, ys, 3.0, 8, 2) > 0.74) & (world_noise(xs, ys, 80.0, 9, 2) > 0.55)
    colour = np.where(flowers[..., None], np.array([0.78, 0.32, 0.20]) * (0.9 + 0.2 * grain)[..., None], colour)
    scrub = np.array([0.40, 0.44, 0.27]) * (0.85 + 0.3 * fine)[..., None]
    garrigue = np.array([0.56, 0.54, 0.38]) * (0.88 + 0.2 * grain)[..., None]
    upland = mix(garrigue, scrub, smoothstep((world_noise(xs, ys, 35.0, 10, 3) - 0.45) / 0.15))
    pines = np.array([0.20, 0.29, 0.16]) * (0.85 + 0.3 * grain)[..., None]
    upland = mix(upland, pines, smoothstep((heights - 260.0) / 200.0) * smoothstep((noise - 0.4) / 0.2))
    hill = np.maximum(smoothstep((heights - 22.0) / 25.0), smoothstep((slope - 0.14) / 0.12))
    colour = mix(colour, upland, hill)
    rock = np.array([0.66, 0.62, 0.55]) * (0.84 + 0.22 * fine)[..., None]
    colour = mix(colour, rock, smoothstep((slope - 0.7) / 0.4) * (0.55 + 0.45 * (grain > 0.45)))
    far = np.array([0.44, 0.47, 0.32]) * (0.88 + 0.2 * noise)[..., None]
    colour = mix(colour, far, smoothstep((heights - 500.0) / 400.0) * 0.6)
    return colour * (0.93 + 0.12 * noise)[..., None]


def water_edges(colour, xs, ys, heights, plainness):
    grain = world_noise(xs, ys, 4.0, 15, 2)
    fine = world_noise(xs, ys, 30.0, 16, 3)
    marsh_distance = signed(plan.MARSH, xs, ys, 400.0)
    reeds = np.array([0.34, 0.40, 0.18]) * (0.8 + 0.3 * grain)[..., None] * (0.9 + 0.2 * fine)[..., None]
    mud = np.array([0.52, 0.48, 0.38]) * (0.88 + 0.16 * grain)[..., None]
    marsh = mix(reeds, mud, smoothstep((0.35 - heights) / 0.35) * 0.7)
    in_marsh = smoothstep((marsh_distance + 40.0) / 80.0) * plainness
    colour = mix(colour, marsh, in_marsh)
    sea_distance = signed(plan.SEA, xs, ys, 400.0)
    beach = np.array([0.70, 0.64, 0.50]) * (0.9 + 0.14 * grain)[..., None]
    shore = smoothstep((1.6 - heights) / 1.0) * (heights > -0.5) * plainness * smoothstep((sea_distance + 90.0) / 60.0)
    colour = mix(colour, beach, shore * 0.85 * (1.0 - in_marsh))
    under = np.array([0.36, 0.40, 0.34])
    colour = mix(colour, under, smoothstep((0.1 - heights) / 1.0))
    for path, width, _ in RIVERS:
        distance = polyline_distance(path, xs, ys)
        trees = np.array([0.24, 0.33, 0.16]) * (0.8 + 0.4 * grain)[..., None]
        colour = mix(colour, trees, smoothstep(1.0 - (distance - width / 2) / 26.0) * (fine > 0.42) * 0.8)
        colour = mix(colour, np.array([0.55, 0.52, 0.42]), smoothstep(1.0 - (distance - width / 2) / 4.0))
    return colour


def sanctuary_colour(colour, xs, ys, heights):
    grain = world_noise(xs, ys, 3.0, 31, 2)
    fine = world_noise(xs, ys, 18.0, 32, 3)
    pad = sanctuary_pad(xs, ys)
    trodden = np.array([0.66, 0.60, 0.46]) * (0.9 + 0.14 * grain)[..., None] * (0.95 + 0.08 * fine)[..., None]
    grass = np.array([0.48, 0.54, 0.28]) * (0.88 + 0.2 * grain)[..., None]
    ground = mix(trodden, grass, smoothstep((world_noise(xs, ys, 40.0, 33, 3) - 0.5) / 0.15) * 0.6)
    near = smoothstep(1.0 - (np.hypot(np.maximum(np.abs(xs + 90.0) - 90.0, 0), np.maximum(np.abs(ys) - 55.0, 0))) / 30.0)
    ground = mix(ground, trodden, near)
    colour = mix(colour, ground, pad)
    city = smoothstep(signed(plan.CITY_WALL, xs, ys, 300.0) / 40.0)
    town = np.array([0.66, 0.58, 0.44]) * (0.9 + 0.16 * fine)[..., None] * (0.94 + 0.1 * grain)[..., None]
    town = mix(town, np.array([0.42, 0.46, 0.28]) * (0.9 + 0.2 * grain)[..., None],
               smoothstep((world_noise(xs, ys, 25.0, 34, 2) - 0.62) / 0.06) * 0.7)
    steep = smoothstep((heights - 120.0) / 60.0)
    colour = mix(colour, town, city * (1.0 - steep) * smoothstep((heights - 1.5) / 1.5))
    for path, half in ((((-1200.0, -560.0), (-700.0, -420.0), (-380.0, -280.0), (-230.0, -120.0)), 3.0),
                       (((-1160.0, -1690.0), (-760.0, -1000.0), (-420.0, -520.0), (-160.0, -120.0)), 3.0)):
        distance = polyline_distance(path, xs, ys)
        colour = mix(colour, np.array([0.70, 0.64, 0.50]), smoothstep(1.0 - (distance - half) / 2.0) * 0.8)
    return colour


def baked_colour(ground, cx, cy, half, resolution, finish, chunk=512):
    axis = np.linspace(-half, half, resolution)
    step = axis[1] - axis[0]
    out = np.empty((resolution, resolution, 3))
    for start in range(0, resolution, chunk):
        lo, hi = max(start - 4, 0), min(start + chunk + 4, resolution)
        xs, ys = np.meshgrid(axis + cx, axis[lo:hi] + cy)
        heights = ground.grid(xs, ys)
        gy, gx = np.gradient(heights, step)
        slope = np.hypot(gx, gy)
        plainness = plain_weight(heights + 3.0)
        colour = land_colour(xs, ys, heights, slope)
        colour = water_edges(colour, xs, ys, heights, plainness)
        colour = finish(colour, xs, ys, heights)
        out[start:start + chunk] = colour[start - lo:start - lo + min(chunk, resolution - start)]
    return np.clip(out, 0, 1)


def drop_seabed(mesh, cx, cy, half, floor=-2.4):
    work = bmesh.new()
    work.from_mesh(mesh)
    keep = half - 40.0
    doomed = [face for face in work.faces if all(v.co.z < floor and abs(v.co.x - cx) < keep
                                                 and abs(v.co.y - cy) < keep for v in face.verts)]
    bmesh.ops.delete(work, geom=doomed, context="FACES")
    loose = [v for v in work.verts if not v.link_faces]
    bmesh.ops.delete(work, geom=loose, context="VERTS")
    work.to_mesh(mesh)
    work.free()
    mesh.update()


def face_materials(mesh, materials):
    count = len(mesh.polygons)
    centres = np.empty(count * 3)
    mesh.polygons.foreach_get("center", centres)
    normals = np.empty(count * 3)
    mesh.polygons.foreach_get("normal", normals)
    centres = centres.reshape(-1, 3)
    normals = normals.reshape(-1, 3)
    xs, ys, zs = centres[:, 0], centres[:, 1], centres[:, 2]
    index = np.zeros(count, dtype=np.int64)
    index[(normals[:, 2] < 0.85) | (zs > 30.0)] = 1
    index[signed(plan.MARSH, xs, ys, 300.0) > -20.0] = 2
    index[sanctuary_pad(xs, ys) > 0.5] = 3
    for material in materials:
        mesh.materials.append(material)
    mesh.polygons.foreach_set("material_index", index)
    return {material.name: int((index == k).sum()) for k, material in enumerate(materials)}


def build(collection, parent, cache_dir, new_object, report, reuse_textures=False):
    texture_dir = os.path.join(cache_dir, "textures")
    os.makedirs(texture_dir, exist_ok=True)
    dem = load_dem(cache_dir)
    mid = mid_field(dem)
    far = far_field(dem, mid)
    near = near_field(dem, mid)
    del dem
    ground = Ground(near, mid, far)
    report["heights"] = {name: round(float(ground(*point)), 1) for name, point in
                         (("temple", (0.0, 0.0)), ("autel", plan.ALTAR), ("ayasoluk", plan.AYASOLUK),
                          ("ville", plan.CITY), ("porte", plan.MAGNESIA_GATE), ("port_sacre", (-300.0, 60.0)),
                          ("panayirdag", (-1300.0, -1050.0)), ("bulbuldag", (-2300.0, -2150.0)),
                          ("quai", (-236.0, 30.0)), ("marais", (100.0, 900.0)))}
    mesh_field = Field(mid.cx, mid.cy, plan.MID_HALF, MID_MESH_SPACING)
    mid_heights = mid.sample(mesh_field.gx, mesh_field.gy)
    under = (np.abs(mesh_field.gx - near.cx) < near.half + 1.0) & (np.abs(mesh_field.gy - near.cy) < near.half + 1.0)
    inner = (np.abs(mesh_field.gx - near.cx) < near.half - 40.0) & (np.abs(mesh_field.gy - near.cy) < near.half - 40.0)
    mid_heights = np.where(inner, mid_heights - 6.0, np.where(under, mid_heights - 0.8, mid_heights))
    far_grid = Field(0.0, 0.0, plan.FAR_HALF, FAR_MESH_SPACING)
    far_heights = far.sample(far_grid.gx, far_grid.gy)
    far_under = (np.abs(far_grid.gx) < plan.MID_HALF + 1.0) & (np.abs(far_grid.gy) < plan.MID_HALF + 1.0)
    far_inner = (np.abs(far_grid.gx) < plan.MID_HALF - 600.0) & (np.abs(far_grid.gy) < plan.MID_HALF - 600.0)
    far_heights = np.where(far_inner, far_heights - 10.0, np.where(far_under, far_heights - 1.5, far_heights))

    def near_finish(colour, xs, ys, heights):
        colour = sanctuary_colour(colour, xs, ys, heights)
        return colour * (0.8 + 0.2 * sun_shadow(mid, xs, ys, heights, 24, 2500.0))[..., None]

    def mid_finish(colour, xs, ys, heights):
        colour = sanctuary_colour(colour, xs, ys, heights)
        return colour * (0.72 + 0.28 * sun_shadow(mid, xs, ys, heights))[..., None]

    def far_finish(colour, xs, ys, heights):
        return colour * (0.68 + 0.32 * sun_shadow(far, xs, ys, heights, 30, 14000.0))[..., None]

    near_image = cached_image("terrain_core", os.path.join(texture_dir, "terrain_core.jpg"), reuse_textures,
                              lambda: baked_colour(ground, near.cx, near.cy, near.half, 4096, near_finish))
    mid_image = cached_image("terrain_ring", os.path.join(texture_dir, "terrain_ring.jpg"), reuse_textures,
                             lambda: baked_colour(ground, mid.cx, mid.cy, plan.MID_HALF, 2048, mid_finish))
    far_image = cached_image("terrain_far_colour", os.path.join(texture_dir, "terrain_far.jpg"), reuse_textures,
                             lambda: baked_colour(ground, 0.0, 0.0, plan.FAR_HALF, 1024, far_finish))
    near_materials = [baked_material(name, near_image, 0.95) for name in
                      ("terrain_plaine", "terrain_collines", "terrain_marais", "ground_temenos")]
    near_mesh = offset_grid("terrain", near, near.heights, 12.0)
    drop_seabed(near_mesh, near.cx, near.cy, near.half)
    near_mesh = decimated(near_mesh, 0.2)
    report["near_faces"] = face_materials(near_mesh, near_materials)
    near_object = new_object("terrain_proche", near_mesh, collection, parent)
    mid_mesh = offset_grid("terrain_golfe", mesh_field, mid_heights, 20.0)
    remove_inside(mid_mesh, near.cx, near.cy, near.half - MID_MESH_SPACING)
    drop_seabed(mid_mesh, mid.cx, mid.cy, plan.MID_HALF, -3.0)
    mid_mesh = decimated(mid_mesh, 0.4)
    mid_mesh.materials.append(baked_material("terrain_golfe", mid_image, 0.95))
    mid_object = new_object("terrain_golfe", mid_mesh, collection, parent)
    mid_object["cast_shadow"] = False
    far_mesh = offset_grid("terrain_far", far_grid, far_heights, 0.0)
    remove_inside(far_mesh, mid.cx, mid.cy, plan.MID_HALF - FAR_MESH_SPACING)
    drop_seabed(far_mesh, 0.0, 0.0, plan.FAR_HALF, -4.0)
    far_mesh = decimated(far_mesh, 0.5)
    far_mesh.materials.append(baked_material("terrain_far", far_image, 0.95))
    far_object = new_object("terrain_far", far_mesh, collection, parent)
    far_object["cast_shadow"] = False
    for obj in (near_object, mid_object, far_object):
        report.setdefault("triangles", {})[obj.name] = sum(len(p.vertices) - 2 for p in obj.data.polygons)
    ground.add_surface([near_object])
    ground.objects = {"near": near_object, "mid": mid_object, "far": far_object}
    return ground
