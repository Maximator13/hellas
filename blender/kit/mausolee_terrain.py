import math
import os

import numpy as np

from . import mausolee_plan as plan
from .acropole_terrain import (Field, blur, cached_image, decimated, land_colour, load_tile, mix, neighbourhood,
                               offset_grid, remove_inside, smoothstep, world_noise)
from .colosse_terrain import Ground, apply_pads, sun_shadow
from .materials import baked_material, download
from .terrain import polygon_mask, polyline_distance

DEM_TILES = {(37, 26): "Copernicus_DSM_COG_10_N37_00_E026_00_DEM",
             (37, 27): "Copernicus_DSM_COG_10_N37_00_E027_00_DEM",
             (36, 26): "Copernicus_DSM_COG_10_N36_00_E026_00_DEM",
             (36, 27): "Copernicus_DSM_COG_10_N36_00_E027_00_DEM"}
DEM_URL = "https://copernicus-dem-30m.s3.amazonaws.com/{0}/{0}.tif"
DEM_LICENCE = ("Copernicus DEM GLO-30 (ESA, Copernicus programme), free licence with attribution: produced using "
               "Copernicus WorldDEM-30 (c) DLR e.V. 2010-2014 and (c) Airbus Defence and Space GmbH 2014-2018 "
               "provided under COPERNICUS by the European Union and ESA")
DEM_TOP = 38.0
DEM_WEST = 26.0
DEM_STEP = 1.0 / 3600.0
MID_SPACING = 30.0
NEAR_SPACING = 5.0
MID_MESH_SPACING = 60.0
FAR_SPACING = 400.0
SEA_FLOOR = -12.0
LAND_FLOOR = 0.9
STREET = 34.0
STREET_ANGLE = math.radians(4.0)


def load_dem(cache_dir):
    tiles = {}
    for key, name in DEM_TILES.items():
        tiles[key] = load_tile(download(DEM_URL.format(name), os.path.join(cache_dir, "src", "dem", f"{name}.tif")))
    return np.vstack([np.hstack([tiles[(37, 26)], tiles[(37, 27)]]), np.hstack([tiles[(36, 26)], tiles[(36, 27)]])])


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
        sea |= polygon_mask(polygon, gx, gy) & (raw < 14.0)
    return sea


def seabed(heights, sea, spacing):
    land = np.maximum(heights, LAND_FLOOR)
    depth = blur(sea.astype(np.float64), max(int(200.0 / spacing), 2))
    return np.where(sea, SEA_FLOOR * (0.3 + 0.7 * depth) - 0.8, land)


def mid_field(dem):
    cx, cy = plan.MID_CENTRE
    field = Field(cx, cy, plan.MID_HALF + 600.0, MID_SPACING)
    raw = resample(dem, field.gx, field.gy)
    opened = neighbourhood(neighbourhood(raw, 2, np.minimum), 2, np.maximum)
    mountain = smoothstep((raw - 120.0) / 100.0)
    ground = blur(opened * (1 - mountain) + raw * mountain, 2)
    sea = sea_mask(raw, field.gx, field.gy)
    field.heights = seabed(ground, sea, MID_SPACING)
    field.sea = sea
    return field


def zephyrion(heights, gx, gy, sea):
    box = (gx > 300.0) & (gx < 620.0) & (gy < -470.0) & (gy > -860.0)
    land = blur((~sea).astype(np.float64), 4)
    inland = smoothstep((land - 0.55) / 0.3)
    plateau = plan.PALACE_PLATEAU + 1.2 * (world_noise(gx, gy, 40.0, 81, 2) - 0.5)
    rock = LAND_FLOOR + (plateau - LAND_FLOOR) * inland
    north = smoothstep((gy + 520.0) / 60.0)
    rock = rock * (1 - north) + np.maximum(heights, rock * 0.4) * north
    return np.where(box & ~sea, np.maximum(heights * (1 - inland), rock), heights)


def theatre_bowl(heights, gx, gy, orchestra, radius, level):
    dx, dy = gx - orchestra[0], gy - orchestra[1]
    r = np.hypot(dx, dy)
    inside = (dy > -6.0) & (r < radius + 10.0)
    cone = level + np.maximum(r - 11.0, 0.0) * 0.52
    weight = smoothstep(1.0 - (r - radius) / 10.0) * smoothstep((dy + 6.0) / 6.0)
    return np.where(inside, heights * (1 - weight) + np.minimum(cone, heights + 2.0) * weight, heights)


def near_field(dem, mid, pads, shaping):
    cx, cy = plan.NEAR_CENTRE
    field = Field(cx, cy, plan.NEAR_HALF, NEAR_SPACING)
    gx, gy = field.gx, field.gy
    raw = resample(dem, gx, gy)
    natural = mid.sample(gx, gy)
    natural = np.where(raw > 0.5, np.maximum(natural, LAND_FLOOR + 0.3 * np.clip(raw, 0, 3)), natural)
    sea = sea_mask(raw, gx, gy)
    coast = blur((~sea).astype(np.float64), 2)
    natural = natural * smoothstep((coast - 0.25) / 0.6) + LAND_FLOOR * (1 - smoothstep((coast - 0.25) / 0.6))
    natural = zephyrion(natural, gx, gy, sea)
    heights = seabed(natural, sea, NEAR_SPACING)
    for shape in shaping:
        heights = shape(heights, gx, gy)
    heights, levels = apply_pads(heights, gx, gy, pads)
    heights = np.where(sea, np.minimum(heights, -0.7), heights)
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


def streets(colour, xs, ys, inside):
    u = xs * math.cos(STREET_ANGLE) + ys * math.sin(STREET_ANGLE)
    v = -xs * math.sin(STREET_ANGLE) + ys * math.cos(STREET_ANGLE)
    du = np.abs((u + STREET / 2) % STREET - STREET / 2)
    dv = np.abs((v + STREET / 2) % STREET - STREET / 2)
    line = np.minimum(du, dv) < 2.2
    return mix(colour, np.array([0.80, 0.72, 0.58]), line * inside * 0.8)


def rect_mask(xs, ys, cx, cy, hu, hv, grow=0.0):
    return (np.abs(xs - cx) < hu + grow) & (np.abs(ys - cy) < hv + grow)


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
        colour = land_colour(xs, ys, heights, slope, inside * 0.85)
        colour = finish(colour, xs, ys, heights, slope, inside)
        out[start:start + chunk] = colour[start - lo:start - lo + min(chunk, resolution - start)]
    return np.clip(out, 0, 1)


def face_materials(mesh, materials):
    centres = np.empty(len(mesh.polygons) * 3)
    mesh.polygons.foreach_get("center", centres)
    normals = np.empty(len(mesh.polygons) * 3)
    mesh.polygons.foreach_get("normal", normals)
    centres = centres.reshape(-1, 3)
    normals = normals.reshape(-1, 3)
    xs, ys = centres[:, 0], centres[:, 1]
    inside = polygon_mask(plan.CITY_WALL, xs, ys)
    tx, ty, hu, hv = plan.TERRACE
    index = np.zeros(len(centres), dtype=np.int64)
    index[inside & (normals[:, 2] > 0.9) & (centres[:, 2] > 1.5)] = 2
    index[normals[:, 2] < 0.75] = 1
    index[rect_mask(xs, ys, tx, ty, hu, hv)] = 3
    for material in materials:
        mesh.materials.append(material)
    mesh.polygons.foreach_set("material_index", index)
    return {material.name: int((index == k).sum()) for k, material in enumerate(materials)}


def build(collection, parent, cache_dir, pads, shaping, new_object, report, reuse_textures=False):
    texture_dir = os.path.join(cache_dir, "textures")
    os.makedirs(texture_dir, exist_ok=True)
    dem = load_dem(cache_dir)
    mid = mid_field(dem)
    far = far_field(dem, mid)
    near = near_field(dem, mid, pads, shaping)
    del dem
    ground = Ground(near, mid, far)
    report["levels"] = {key: round(value, 2) for key, value in near.levels.items()}
    report["heights"] = {name: round(float(ground(*point)), 1) for name, point in
                         (("mausolee", plan.MAUSOLEUM), ("palais", plan.PALACE), ("theatre", plan.THEATRE),
                          ("salmakis", plan.SALMAKIS), ("myndos", plan.MYNDOS), ("agora", plan.AGORA))}
    mesh_field = Field(mid.cx, mid.cy, plan.MID_HALF, MID_MESH_SPACING)
    mid_heights = mid.sample(mesh_field.gx, mesh_field.gy)
    under = (np.abs(mesh_field.gx - near.cx) < near.half + 80.0) & (np.abs(mesh_field.gy - near.cy) < near.half + 80.0)
    mid_heights = np.where(under, mid_heights - 8.0, mid_heights)
    far_heights = far.heights.copy()
    far_under = (np.abs(far.gx - mid.cx) < plan.MID_HALF + 400.0) & (np.abs(far.gy - mid.cy) < plan.MID_HALF + 400.0)
    far_heights = np.where(far_under, far_heights - 12.0, far_heights)
    tx, ty, hu, hv = plan.TERRACE
    ax, ay = plan.AGORA
    ahu, ahv = plan.AGORA_HALF

    def near_finish(colour, xs, ys, heights, slope, inside):
        fine = world_noise(xs, ys, 4.0, 62, 2)
        quay = inside * smoothstep((4.0 - heights) / 2.5) * (heights > 0.3)
        colour = mix(colour, np.array([0.78, 0.70, 0.56]) * (0.92 + 0.1 * fine)[..., None], quay)
        open_ground = np.maximum(rect_mask(xs, ys, tx, ty, hu, hv, 6.0), rect_mask(xs, ys, ax, ay, ahu, ahv, 4.0))
        colour = streets(colour, xs, ys, inside * smoothstep((heights - 1.5) / 1.5) * (1.0 - open_ground)
                         * (1.0 - smoothstep((slope - 0.35) / 0.2)))
        avenue = polyline_distance(plan.AVENUE, xs, ys) < plan.AVENUE_WIDTH / 2
        colour = mix(colour, np.array([0.82, 0.76, 0.63]) * (0.93 + 0.1 * fine)[..., None], avenue * 0.9)
        terrace = rect_mask(xs, ys, tx, ty, hu, hv)
        garden = np.array([0.52, 0.55, 0.34]) * (0.85 + 0.25 * world_noise(xs, ys, 7.0, 64, 2))[..., None]
        court = np.array([0.86, 0.82, 0.74]) * (0.95 + 0.07 * fine)[..., None]
        near_tomb = rect_mask(xs, ys, 0.0, 0.0, 30.0, 27.0)
        colour = mix(colour, np.where(near_tomb[..., None], court, garden), terrace)
        agora = rect_mask(xs, ys, ax, ay, ahu, ahv)
        paving = np.array([0.84, 0.79, 0.68]) * (0.93 + 0.1 * world_noise(xs, ys, 2.0, 66, 2))[..., None]
        colour = mix(colour, paving, agora)
        return colour * (0.78 + 0.22 * sun_shadow(mid, xs, ys, heights, 24, 2500.0))[..., None]

    def mid_finish(colour, xs, ys, heights, slope, inside):
        colour = streets(colour, xs, ys, inside * smoothstep((heights - 2.0) / 2.0) * 0.6)
        return colour * (0.72 + 0.28 * sun_shadow(mid, xs, ys, heights))[..., None]

    def far_finish(colour, xs, ys, heights, slope, inside):
        return colour * (0.68 + 0.32 * sun_shadow(far, xs, ys, heights, 30, 14000.0))[..., None]

    near_image = cached_image("terrain_core", os.path.join(texture_dir, "terrain_core.jpg"), reuse_textures,
                              lambda: baked_colour(ground, near.cx, near.cy, near.half, 4096, near_finish))
    mid_image = cached_image("terrain_ring", os.path.join(texture_dir, "terrain_ring.jpg"), reuse_textures,
                             lambda: baked_colour(ground, mid.cx, mid.cy, plan.MID_HALF, 2048, mid_finish))
    far_image = cached_image("terrain_far_colour", os.path.join(texture_dir, "terrain_far.jpg"), reuse_textures,
                             lambda: baked_colour(ground, 0.0, 0.0, plan.FAR_HALF, 1024, far_finish))
    near_materials = [baked_material(name, near_image, 0.95) for name in
                      ("terrain_collines", "terrain_falaises", "ground_ville", "ground_terrasse")]
    near_mesh = decimated(offset_grid("terrain", near, near.heights, 20.0), 0.22)
    report["near_faces"] = face_materials(near_mesh, near_materials)
    near_object = new_object("terrain_proche", near_mesh, collection, parent)
    mid_mesh = offset_grid("terrain_golfe", mesh_field, mid_heights, 30.0)
    remove_inside(mid_mesh, near.cx, near.cy, near.half - MID_MESH_SPACING)
    mid_mesh = decimated(mid_mesh, 0.4)
    mid_mesh.materials.append(baked_material("terrain_golfe", mid_image, 0.95))
    mid_object = new_object("terrain_golfe", mid_mesh, collection, parent)
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
