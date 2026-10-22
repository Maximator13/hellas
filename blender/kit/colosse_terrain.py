import math
import os

import numpy as np
from mathutils.bvhtree import BVHTree

from . import colosse_plan as plan
from .acropole_terrain import (Field, blur, cached_image, decimated, land_colour, mix, neighbourhood, offset_grid,
                               remove_inside, smoothstep, world_noise)
from .materials import baked_material, download
from .terrain import polygon_mask

DEM_TILES = ("Copernicus_DSM_COG_10_N36_00_E027_00_DEM", "Copernicus_DSM_COG_10_N36_00_E028_00_DEM")
DEM_URL = "https://copernicus-dem-30m.s3.amazonaws.com/{0}/{0}.tif"
DEM_LICENCE = ("Copernicus DEM GLO-30 (ESA, Copernicus programme), free licence with attribution: produced using "
               "Copernicus WorldDEM-30 (c) DLR e.V. 2010-2014 and (c) Airbus Defence and Space GmbH 2014-2018 "
               "provided under COPERNICUS by the European Union and ESA")
DEM_TOP = 37.0
DEM_WEST = 27.0
DEM_STEP = 1.0 / 3600.0
MID_SPACING = 30.0
NEAR_SPACING = 5.0
MID_MESH_SPACING = 60.0
FAR_SPACING = 400.0
SEA_FLOOR = -9.0
LAND_FLOOR = 0.9
STREET = 30.0


def load_dem(cache_dir):
    from .acropole_terrain import load_tile
    tiles = []
    for name in DEM_TILES:
        path = download(DEM_URL.format(name), os.path.join(cache_dir, "src", "dem", f"{name}.tif"))
        tiles.append(load_tile(path))
    return np.hstack(tiles)


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


def sea_mask(raw, gx, gy):
    sea = raw <= 0.5
    for polygon in plan.SEA_ERASE:
        sea |= polygon_mask(polygon, gx, gy)
    return sea


def seabed(heights, sea, spacing):
    land = np.maximum(heights, LAND_FLOOR)
    depth = blur(sea.astype(np.float64), max(int(160.0 / spacing), 2))
    return np.where(sea, SEA_FLOOR * (0.35 + 0.65 * depth) - 0.8, land)


def mid_field(dem):
    cx, cy = plan.MID_CENTRE
    field = Field(cx, cy, plan.MID_HALF + 600.0, MID_SPACING)
    raw = resample(dem, field.gx, field.gy)
    opened = neighbourhood(neighbourhood(raw, 2, np.minimum), 2, np.maximum)
    mountain = smoothstep((raw - 160.0) / 120.0)
    ground = blur(opened * (1 - mountain) + raw * mountain, 2)
    sea = sea_mask(raw, field.gx, field.gy)
    field.natural = ground
    field.heights = seabed(ground, sea, MID_SPACING)
    field.sea = sea
    return field


def pad_weight(gx, gy, pad):
    if pad["kind"] == "rect":
        angle = math.radians(pad.get("azimuth", 0.0))
        dx, dy = gx - pad["x"], gy - pad["y"]
        u = dx * math.cos(angle) - dy * math.sin(angle)
        v = dx * math.sin(angle) + dy * math.cos(angle)
        distance = np.maximum(np.abs(u) - pad["half_u"], np.abs(v) - pad["half_v"])
    else:
        distance = np.hypot(gx - pad["x"], gy - pad["y"]) - pad["radius"]
    return distance, smoothstep(1.0 - distance / pad.get("margin", 8.0))


def apply_pads(heights, gx, gy, pads):
    levels = {}
    for pad in pads:
        distance, weight = pad_weight(gx, gy, pad)
        if pad["level"] is None:
            level = float(np.median(heights[distance < 0])) if (distance < 0).any() else float(heights.mean())
        else:
            level = pad["level"]
        if pad.get("raise"):
            level += pad["raise"]
        levels[pad["name"]] = level
        heights = heights * (1 - weight) + level * weight
    return heights, levels


def hill(gx, gy, centre, radius, lift):
    return lift * smoothstep(1.0 - np.hypot(gx - centre[0], gy - centre[1]) / radius)


def near_field(dem, mid, pads):
    cx, cy = plan.NEAR_CENTRE
    field = Field(cx, cy, plan.NEAR_HALF, NEAR_SPACING)
    gx, gy = field.gx, field.gy
    raw = resample(dem, gx, gy)
    natural = mid.sample(gx, gy)
    natural = np.where(raw > 0.5, np.maximum(natural, LAND_FLOOR + 0.3 * np.clip(raw, 0, 3)), natural)
    natural = natural + hill(gx, gy, plan.STATUE, 260.0, 6.0)
    sea = sea_mask(raw, gx, gy)
    coast = blur((~sea).astype(np.float64), 2)
    natural = natural * smoothstep((coast - 0.25) / 0.6) + LAND_FLOOR * (1 - smoothstep((coast - 0.25) / 0.6))
    heights = seabed(natural, sea, NEAR_SPACING)
    heights, levels = apply_pads(heights, gx, gy, pads)
    heights = np.where(sea, np.minimum(heights, -0.6), heights)
    field.heights = heights
    field.sea = sea
    field.levels = levels
    return field


def far_field(dem, mid):
    field = Field(0.0, 0.0, plan.FAR_HALF, FAR_SPACING)
    raw = resample(dem, field.gx, field.gy)
    sea = raw <= 0.5
    heights = seabed(raw, sea, FAR_SPACING)
    inside = (np.abs(field.gx - mid.cx) < mid.half - 400.0) & (np.abs(field.gy - mid.cy) < mid.half - 400.0)
    field.heights = np.where(inside, mid.sample(field.gx, field.gy), heights)
    field.sea = sea
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


def streets(colour, xs, ys, inside):
    u = np.abs((xs + STREET / 2) % STREET - STREET / 2)
    v = np.abs((ys + STREET / 2) % STREET - STREET / 2)
    line = np.minimum(u, v) < 2.4
    return mix(colour, np.array([0.80, 0.73, 0.60]), line * inside * 0.85)


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
        inside = blur(polygon_mask(plan.CITY_WALL, xs, ys).astype(np.float64), 3)
        colour = land_colour(xs, ys, heights, slope, inside)
        colour = finish(colour, xs, ys, heights, inside)
        out[start:start + chunk] = colour[start - lo:start - lo + min(chunk, resolution - start)]
    return np.clip(out, 0, 1)


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

    def is_sea(self, x, y):
        return self(x, y) < -0.3

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


def face_materials(mesh, materials):
    centres = np.empty(len(mesh.polygons) * 3)
    mesh.polygons.foreach_get("center", centres)
    normals = np.empty(len(mesh.polygons) * 3)
    mesh.polygons.foreach_get("normal", normals)
    centres = centres.reshape(-1, 3)
    normals = normals.reshape(-1, 3)
    inside = polygon_mask(plan.CITY_WALL, centres[:, 0], centres[:, 1])
    index = np.zeros(len(centres), dtype=np.int64)
    index[inside & (normals[:, 2] > 0.9) & (centres[:, 2] > 1.5)] = 2
    index[normals[:, 2] < 0.75] = 1
    for material in materials:
        mesh.materials.append(material)
    mesh.polygons.foreach_set("material_index", index)
    return {material.name: int((index == k).sum()) for k, material in enumerate(materials)}


def build(collection, parent, cache_dir, pads, new_object, report, reuse_textures=False):
    texture_dir = os.path.join(cache_dir, "textures")
    os.makedirs(texture_dir, exist_ok=True)
    dem = load_dem(cache_dir)
    mid = mid_field(dem)
    far = far_field(dem, mid)
    near = near_field(dem, mid, pads)
    del dem
    ground = Ground(near, mid, far)
    report["levels"] = {key: round(value, 2) for key, value in near.levels.items()}
    report["heights"] = {name: round(float(ground(*point)), 1) for name, point in
                         (("statue", plan.STATUE), ("apollon", plan.APOLLO), ("stade", plan.STADIUM),
                          ("athena", plan.ATHENA_TEMPLE), ("agora", plan.AGORA))}
    mesh_field = Field(mid.cx, mid.cy, plan.MID_HALF, MID_MESH_SPACING)
    mid_heights = mid.sample(mesh_field.gx, mesh_field.gy)
    under = (np.abs(mesh_field.gx - near.cx) < near.half + 80.0) & (np.abs(mesh_field.gy - near.cy) < near.half + 80.0)
    mid_heights = np.where(under, mid_heights - 8.0, mid_heights)
    far_heights = far.heights.copy()
    far_under = (np.abs(far.gx - mid.cx) < plan.MID_HALF + 400.0) & (np.abs(far.gy - mid.cy) < plan.MID_HALF + 400.0)
    far_heights = np.where(far_under, far_heights - 12.0, far_heights)

    def near_finish(colour, xs, ys, heights, inside):
        quay = inside * smoothstep((5.0 - heights) / 3.0) * (heights > 0.3)
        colour = mix(colour, np.array([0.76, 0.68, 0.55]) * (0.92 + 0.1 * world_noise(xs, ys, 4.0, 62, 2))[..., None],
                     quay)
        (zx, zy), radius = plan.ACROPOLIS_ZONE
        open_ground = smoothstep(1.0 - (np.hypot(xs - zx, ys - zy) - radius) / 40.0)
        colour = streets(colour, xs, ys, inside * smoothstep((heights - 1.2) / 1.5) * (1.0 - open_ground))
        terrace = smoothstep(1.0 - (np.hypot(xs - plan.STATUE[0], ys - plan.STATUE[1]) - plan.HELIOS_TERRACE) / 4.0)
        colour = mix(colour, np.array([0.82, 0.78, 0.70]) * (0.94 + 0.08 * world_noise(xs, ys, 3.0, 61, 2))[..., None],
                     terrace)
        return colour * (0.78 + 0.22 * sun_shadow(mid, xs, ys, heights, 24, 2500.0))[..., None]

    def mid_finish(colour, xs, ys, heights, inside):
        colour = streets(colour, xs, ys, inside * smoothstep((heights - 2.0) / 2.0) * 0.6)
        return colour * (0.72 + 0.28 * sun_shadow(mid, xs, ys, heights))[..., None]

    def far_finish(colour, xs, ys, heights, inside):
        return colour * (0.68 + 0.32 * sun_shadow(far, xs, ys, heights, 30, 14000.0))[..., None]

    near_image = cached_image("terrain_core", os.path.join(texture_dir, "terrain_core.jpg"), reuse_textures,
                              lambda: baked_colour(ground, near.cx, near.cy, near.half, 4096, near_finish))
    mid_image = cached_image("terrain_ring", os.path.join(texture_dir, "terrain_ring.jpg"), reuse_textures,
                             lambda: baked_colour(ground, mid.cx, mid.cy, plan.MID_HALF, 2048, mid_finish))
    far_image = cached_image("terrain_far_colour", os.path.join(texture_dir, "terrain_far.jpg"), reuse_textures,
                             lambda: baked_colour(ground, 0.0, 0.0, plan.FAR_HALF, 1024, far_finish))
    near_materials = [baked_material(name, near_image, 0.95) for name in
                      ("terrain_pentes", "terrain_rocher", "ground_ville")]
    near_mesh = decimated(offset_grid("terrain", near, near.heights, 20.0), 0.2)
    report["near_faces"] = face_materials(near_mesh, near_materials)
    near_object = new_object("terrain_proche", near_mesh, collection, parent)
    mid_mesh = offset_grid("terrain_ile", mesh_field, mid_heights, 30.0)
    remove_inside(mid_mesh, near.cx, near.cy, near.half - MID_MESH_SPACING)
    mid_mesh = decimated(mid_mesh, 0.4)
    mid_mesh.materials.append(baked_material("terrain_ile", mid_image, 0.95))
    mid_object = new_object("terrain_ile", mid_mesh, collection, parent)
    mid_object["cast_shadow"] = False
    far_grid = Field(0.0, 0.0, plan.FAR_HALF, FAR_SPACING)
    far_mesh = offset_grid("terrain_far", far_grid, far_heights, 0.0)
    remove_inside(far_mesh, mid.cx, mid.cy, plan.MID_HALF - FAR_SPACING)
    far_mesh = decimated(far_mesh, 0.4)
    far_mesh.materials.append(baked_material("terrain_far", far_image, 0.95))
    far_object = new_object("terrain_far", far_mesh, collection, parent)
    far_object["cast_shadow"] = False
    for obj in (near_object, mid_object, far_object):
        report.setdefault("triangles", {})[obj.name] = sum(len(p.vertices) - 2 for p in obj.data.polygons)
    ground.add_surface([near_object, mid_object, far_object])
    ground.objects = {"near": near_object, "mid": mid_object, "far": far_object}
    return ground

