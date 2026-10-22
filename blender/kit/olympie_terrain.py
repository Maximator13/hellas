import math
import os

import numpy as np
from mathutils.bvhtree import BVHTree

from . import olympie_plan as plan
from .acropole_terrain import (Field, blur, cached_image, decimated, load_tile, mix, neighbourhood, offset_grid,
                               remove_inside, smoothstep, world_noise)
from .materials import baked_material, download
from .terrain import point_in_polygon, polygon_mask, polyline_distance

DEM_TILE = "Copernicus_DSM_COG_10_N37_00_E021_00_DEM"
DEM_URL = "https://copernicus-dem-30m.s3.amazonaws.com/{0}/{0}.tif"
DEM_LICENCE = ("Copernicus DEM GLO-30 (ESA, Copernicus programme), free licence with attribution: produced using "
               "Copernicus WorldDEM-30 (c) DLR e.V. 2010-2014 and (c) Airbus Defence and Space GmbH 2014-2018 "
               "provided under COPERNICUS by the European Union and ESA")
DEM_TOP = 38.0
DEM_WEST = 21.0
DEM_STEP = 1.0 / 3600.0
NEAR_SPACING = 5.0
MID_SPACING = 30.0
MID_MESH_SPACING = 60.0
FAR_SPACING = 400.0
DEPOSIT = 4.0
TERRACE_RISE = 3.0
BANK_HEIGHT = 6.5
TRACK_HALF = plan.STADIUM_WIDTH / 2


def load_dem(cache_dir):
    path = download(DEM_URL.format(DEM_TILE), os.path.join(cache_dir, "src", "dem", f"{DEM_TILE}.tif"))
    return load_tile(path)


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
    passes = max(int(round(30.0 / spacing)), 1)
    opened = neighbourhood(neighbourhood(raw, passes, np.minimum), passes, np.maximum)
    return blur(opened, max(int(round(20.0 / spacing)), 1))


def ancient(heights, gx, gy, level):
    excess = heights - level
    deposit = DEPOSIT * smoothstep((excess - 0.8) / 3.0) * (1.0 - smoothstep((excess - 12.0) / 22.0))
    reach = np.hypot(gx - 100.0, gy + 100.0)
    deposit *= 1.0 - smoothstep((reach - 900.0) / 900.0)
    return heights - deposit


def river_bed(heights, gx, gy, spacing):
    out = heights
    for path, half, bank, depth in ((plan.ALPHEIOS, plan.ALPHEIOS_WIDTH / 2, 60.0, 1.6), (plan.KLADEOS, 10.0, 18.0, 1.4)):
        distance = polyline_distance(path, gx, gy)
        low = neighbourhood(out, max(int(round(half * 1.4 / spacing)), 1), np.minimum)
        bed = blur(low, max(int(round(half / spacing)), 1)) - depth
        out = mix(out[..., None], bed[..., None], smoothstep(1.0 - (distance - half) / bank))[..., 0]
    return out


def stadium_frame(gx, gy):
    a = math.radians(plan.STADIUM_AZIMUTH)
    dx, dy = gx - plan.STADIUM_WEST[0], gy - plan.STADIUM_WEST[1]
    along = dx * math.sin(a) + dy * math.cos(a)
    north = -dx * math.cos(a) + dy * math.sin(a)
    return along, north


def hippodrome_frame(gx, gy):
    a = math.radians(plan.HIPPODROME_AZIMUTH)
    dx, dy = gx - plan.HIPPODROME[0], gy - plan.HIPPODROME[1]
    return dx * math.sin(a) + dy * math.cos(a), -dx * math.cos(a) + dy * math.sin(a)


def rect_weight(u, v, half_u, half_v, margin):
    distance = np.maximum(np.abs(u) - half_u, np.abs(v) - half_v)
    return smoothstep(1.0 - distance / margin)


def treasury_frame(gx, gy):
    (x0, y0), (x1, y1) = plan.TREASURY_LINE
    length = math.hypot(x1 - x0, y1 - y0)
    tx, ty = (x1 - x0) / length, (y1 - y0) / length
    u = (gx - (x0 + x1) / 2) * tx + (gy - (y0 + y1) / 2) * ty
    v = -(gx - (x0 + x1) / 2) * ty + (gy - (y0 + y1) / 2) * tx
    return u, v, length


def sanctuary(heights, gx, gy, smooth, field):
    inside = blur(polygon_mask(plan.SANCTUARY, gx, gy).astype(np.float64), 4)
    heights = heights * (1 - inside) + smooth * inside
    levels = {}
    levels["terrace"] = float(field.sample(*plan.HERAION)) + TERRACE_RISE
    u, v, length = treasury_frame(gx, gy)
    terrace = rect_weight(u, v - 6.0, length / 2 + 14.0, 11.0, 4.0)
    heights = heights * (1 - terrace) + levels["terrace"] * terrace
    centre = plan.stadium_point(plan.STADIUM_LENGTH / 2, 0.0)
    levels["track"] = float(field.sample(*centre))
    along, north = stadium_frame(gx, gy)
    track = rect_weight(along - plan.STADIUM_LENGTH / 2, north, plan.STADIUM_LENGTH / 2 + 8.0, TRACK_HALF, 6.0)
    heights = heights * (1 - track) + levels["track"] * track
    side = smoothstep((np.abs(north) - TRACK_HALF - 2.0) / 9.0) * (1.0 - smoothstep((np.abs(north) - 46.0) / 16.0))
    span = smoothstep((along + 5.0) / 25.0) * (1.0 - smoothstep((along - plan.STADIUM_LENGTH - 30.0) / 20.0))
    east = smoothstep((along - plan.STADIUM_LENGTH - 6.0) / 9.0) * (1.0 - smoothstep((along - plan.STADIUM_LENGTH - 45.0) / 16.0))
    east *= 1.0 - smoothstep((np.abs(north) - 46.0) / 16.0)
    bank = np.maximum(side * span, east)
    heights = np.maximum(heights, levels["track"] + BANK_HEIGHT * bank)
    levels["hippodrome"] = float(field.sample(*plan.HIPPODROME)) - 0.3
    hu, hv = hippodrome_frame(gx, gy)
    banks = rect_weight(hu, np.abs(hv) - 92.0, 360.0, 5.0, 10.0)
    return heights + 1.5 * banks, levels


class Ground:
    def __init__(self, near, mid, far, level):
        self.near, self.mid, self.far = near, mid, far
        self.level = level
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

    def is_bed(self, x, y):
        return float(polyline_distance(plan.ALPHEIOS, np.array([x]), np.array([y]))[0]) < plan.ALPHEIOS_WIDTH / 2 + 10.0 \
            or float(polyline_distance(plan.KLADEOS, np.array([x]), np.array([y]))[0]) < 14.0


def altis_level(dem):
    field = Field(0.0, 40.0, 60.0, 5.0)
    heights = canopy_free(resample(dem, field.gx, field.gy), 5.0)
    return float(np.percentile(heights, 20))


def mid_field(dem, level):
    field = Field(0.0, 0.0, plan.MID_HALF + 600.0, MID_SPACING)
    heights = canopy_free(resample(dem, field.gx, field.gy), MID_SPACING)
    heights = ancient(heights, field.gx, field.gy, level)
    field.heights = river_bed(heights, field.gx, field.gy, MID_SPACING)
    return field


def near_field(dem, mid, level):
    cx, cy = plan.NEAR_CENTRE
    field = Field(cx, cy, plan.NEAR_HALF, NEAR_SPACING)
    gx, gy = field.gx, field.gy
    heights = canopy_free(resample(dem, gx, gy), NEAR_SPACING)
    heights = ancient(heights, gx, gy, level)
    heights = river_bed(heights, gx, gy, NEAR_SPACING)
    smooth = blur(mid.sample(gx, gy), 16)
    heights, field.levels = sanctuary(heights, gx, gy, smooth, mid)
    edge = np.maximum(np.abs(gx - cx), np.abs(gy - cy))
    rim = smoothstep((edge - plan.NEAR_HALF + 90.0) / 80.0)
    field.heights = heights * (1 - rim) + mid.sample(gx, gy) * rim
    return field


def far_field(dem, mid):
    field = Field(0.0, 0.0, plan.FAR_HALF, FAR_SPACING)
    heights = canopy_free(resample(dem, field.gx, field.gy), FAR_SPACING)
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


def land_colour(xs, ys, heights, slope, level):
    noise = world_noise(xs, ys, 600.0, 3, 4)
    fine = world_noise(xs, ys, 25.0, 4, 3)
    grain = world_noise(xs, ys, 5.0, 5, 2)
    straw = np.array([0.80, 0.70, 0.47]) * (0.9 + 0.16 * fine)[..., None] * (0.94 + 0.1 * grain)[..., None]
    olive = np.array([0.55, 0.53, 0.36]) * (0.9 + 0.2 * grain)[..., None]
    colour = mix(straw, olive, smoothstep((world_noise(xs, ys, 120.0, 7, 3) - 0.55) / 0.12) * 0.7)
    scrub = np.array([0.36, 0.40, 0.25]) * (0.85 + 0.3 * fine)[..., None]
    pines = np.array([0.20, 0.28, 0.15]) * (0.85 + 0.3 * grain)[..., None]
    rise = heights - level
    hill = np.maximum(smoothstep((rise - 18.0) / 25.0), smoothstep((slope - 0.12) / 0.12))
    upland = mix(scrub, pines, smoothstep((world_noise(xs, ys, 40.0, 9, 3) - 0.48) / 0.12))
    colour = mix(colour, upland, hill * (0.55 + 0.45 * smoothstep((noise - 0.35) / 0.3)))
    rock = np.array([0.70, 0.64, 0.52]) * (0.86 + 0.2 * fine)[..., None]
    colour = mix(colour, rock, smoothstep((slope - 0.75) / 0.4) * 0.6)
    far = np.array([0.46, 0.48, 0.34]) * (0.88 + 0.2 * noise)[..., None]
    colour = mix(colour, far, smoothstep((heights - 300.0) / 300.0) * 0.6)
    for path, half, green in ((plan.ALPHEIOS, plan.ALPHEIOS_WIDTH / 2, 70.0), (plan.KLADEOS, 10.0, 30.0)):
        distance = polyline_distance(path, xs, ys)
        trees = np.array([0.24, 0.33, 0.16]) * (0.8 + 0.4 * grain)[..., None]
        colour = mix(colour, trees, smoothstep(1.0 - (distance - half) / green) * (0.55 + 0.45 * (fine > 0.45)))
        gravel = np.array([0.82, 0.79, 0.72]) * (0.88 + 0.18 * grain)[..., None] * (0.94 + 0.1 * fine)[..., None]
        colour = mix(colour, gravel, smoothstep(1.0 - (distance - half + 4.0) / 6.0))
    return np.clip(colour * (0.93 + 0.12 * noise)[..., None], 0, 1)


def sanctuary_colour(colour, xs, ys, heights, level):
    grain = world_noise(xs, ys, 3.0, 31, 2)
    fine = world_noise(xs, ys, 18.0, 32, 3)
    sand = np.array([0.82, 0.73, 0.57]) * (0.92 + 0.12 * grain)[..., None] * (0.95 + 0.08 * fine)[..., None]
    inside = blur(polygon_mask(plan.SANCTUARY, xs, ys).astype(np.float64), 3)
    altis = blur(polygon_mask(plan.ALTIS, xs, ys).astype(np.float64), 4)
    dust = np.array([0.74, 0.66, 0.50]) * (0.9 + 0.16 * fine)[..., None]
    colour = mix(colour, dust, inside * 0.35)
    colour = mix(colour, sand, altis * 0.92)
    along, north = stadium_frame(xs, ys)
    track = rect_weight(along - plan.STADIUM_LENGTH / 2, north, plan.STADIUM_LENGTH / 2, TRACK_HALF - 1.0, 1.0)
    colour = mix(colour, np.array([0.86, 0.76, 0.58]) * (0.95 + 0.08 * grain)[..., None], track)
    banks = smoothstep((heights - level - 0.6) / 1.5) * rect_weight(along - plan.STADIUM_LENGTH / 2, north,
                                                                   plan.STADIUM_LENGTH / 2 + 50.0, 60.0, 10.0)
    dry = np.array([0.78, 0.68, 0.44]) * (0.9 + 0.18 * fine)[..., None]
    colour = mix(colour, dry, banks * 0.9)
    hu, hv = hippodrome_frame(xs, ys)
    course = rect_weight(hu, hv, 360.0, 70.0, 20.0)
    colour = mix(colour, np.array([0.80, 0.72, 0.56]) * (0.92 + 0.12 * fine)[..., None], course * 0.3)
    trampled = np.zeros(xs.shape)
    for (cx, cy), radius in plan.CAMPS + [plan.ARGIVE_CAMP]:
        trampled = np.maximum(trampled, smoothstep(1.0 - (np.hypot(xs - cx, ys - cy) - radius * 0.8) / (radius * 0.5)))
    return mix(colour, dust, trampled * 0.45 * (1 - inside))


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
        colour = land_colour(xs, ys, heights, slope, ground.level)
        colour = finish(colour, xs, ys, heights)
        out[start:start + chunk] = colour[start - lo:start - lo + min(chunk, resolution - start)]
    return np.clip(out, 0, 1)


def face_materials(mesh, materials, level):
    count = len(mesh.polygons)
    centres = np.empty(count * 3)
    mesh.polygons.foreach_get("center", centres)
    centres = centres.reshape(-1, 3)
    xs, ys, zs = centres[:, 0], centres[:, 1], centres[:, 2]
    index = np.zeros(count, dtype=np.int64)
    kronion = (np.hypot(xs - plan.KRONION[0], ys - plan.KRONION[1]) < 320.0) & (zs > level + 6.0)
    index[kronion] = 1
    index[polygon_mask(plan.SANCTUARY, xs, ys)] = 2
    along, north = stadium_frame(xs, ys)
    index[(along > -2.0) & (along < plan.STADIUM_LENGTH + 2.0) & (np.abs(north) < TRACK_HALF)] = 3
    bed = (polyline_distance(plan.ALPHEIOS, xs, ys) < plan.ALPHEIOS_WIDTH / 2) | (
        polyline_distance(plan.KLADEOS, xs, ys) < 10.0)
    index[bed] = 4
    for material in materials:
        mesh.materials.append(material)
    mesh.polygons.foreach_set("material_index", index)
    return {material.name: int((index == k).sum()) for k, material in enumerate(materials)}


def build(collection, parent, cache_dir, new_object, report, reuse_textures=False):
    texture_dir = os.path.join(cache_dir, "textures")
    os.makedirs(texture_dir, exist_ok=True)
    dem = load_dem(cache_dir)
    level = altis_level(dem)
    mid = mid_field(dem, level)
    far = far_field(dem, mid)
    near = near_field(dem, mid, level)
    del dem
    ground = Ground(near, mid, far, level)
    ground.levels = near.levels
    report["altis_level"] = round(level, 2)
    report["levels"] = {key: round(value, 2) for key, value in near.levels.items()}
    report["heights"] = {name: round(float(ground(*point)), 1) for name, point in
                         (("temple", plan.TEMPLE), ("heraion", plan.HERAION), ("kronion", plan.KRONION),
                          ("stade", plan.stadium_point(100.0, 0.0)), ("atelier", plan.WORKSHOP),
                          ("hippodrome", plan.HIPPODROME), ("alphee", (200.0, -500.0)))}
    mesh_field = Field(mid.cx, mid.cy, plan.MID_HALF, MID_MESH_SPACING)
    mid_heights = mid.sample(mesh_field.gx, mesh_field.gy)
    under = (np.abs(mesh_field.gx - near.cx) < near.half + 80.0) & (np.abs(mesh_field.gy - near.cy) < near.half + 80.0)
    mid_heights = np.where(under, mid_heights - 8.0, mid_heights)
    far_heights = far.heights.copy()
    far_under = (np.abs(far.gx - mid.cx) < plan.MID_HALF + 400.0) & (np.abs(far.gy - mid.cy) < plan.MID_HALF + 400.0)
    far_heights = np.where(far_under, far_heights - 12.0, far_heights)

    def near_finish(colour, xs, ys, heights):
        colour = sanctuary_colour(colour, xs, ys, heights, near.levels["track"])
        return colour * (0.8 + 0.2 * sun_shadow(mid, xs, ys, heights, 24, 2500.0))[..., None]

    def mid_finish(colour, xs, ys, heights):
        colour = sanctuary_colour(colour, xs, ys, heights, near.levels["track"])
        return colour * (0.72 + 0.28 * sun_shadow(mid, xs, ys, heights))[..., None]

    def far_finish(colour, xs, ys, heights):
        return colour * (0.68 + 0.32 * sun_shadow(far, xs, ys, heights, 30, 14000.0))[..., None]

    near_image = cached_image("terrain_core", os.path.join(texture_dir, "terrain_core.jpg"), reuse_textures,
                              lambda: baked_colour(ground, near.cx, near.cy, near.half, 2048, near_finish))
    mid_image = cached_image("terrain_ring", os.path.join(texture_dir, "terrain_ring.jpg"), reuse_textures,
                             lambda: baked_colour(ground, mid.cx, mid.cy, plan.MID_HALF, 2048, mid_finish))
    far_image = cached_image("terrain_far_colour", os.path.join(texture_dir, "terrain_far.jpg"), reuse_textures,
                             lambda: baked_colour(ground, 0.0, 0.0, plan.FAR_HALF, 1024, far_finish))
    near_materials = [baked_material(name, near_image, 0.95) for name in
                      ("terrain_collines", "terrain_kronion", "ground_altis", "ground_stade", "ground_galets")]
    near_mesh = decimated(offset_grid("terrain", near, near.heights, 20.0), 0.22)
    report["near_faces"] = face_materials(near_mesh, near_materials, level)
    near_object = new_object("terrain_proche", near_mesh, collection, parent)
    mid_mesh = offset_grid("terrain_vallee", mesh_field, mid_heights, 30.0)
    remove_inside(mid_mesh, near.cx, near.cy, near.half - MID_MESH_SPACING)
    mid_mesh = decimated(mid_mesh, 0.4)
    mid_mesh.materials.append(baked_material("terrain_vallee", mid_image, 0.95))
    mid_object = new_object("terrain_vallee", mid_mesh, collection, parent)
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
    ground.add_surface([near_object])
    ground.objects = {"near": near_object, "mid": mid_object, "far": far_object}
    return ground


def inside_altis(x, y):
    return point_in_polygon(x, y, plan.ALTIS)


def inside_sanctuary(x, y):
    return point_in_polygon(x, y, plan.SANCTUARY)
