import math
import os

import bmesh
import bpy
import numpy as np
from mathutils import Matrix
from mathutils.bvhtree import BVHTree

from . import acropole_plan as plan
from .materials import baked_material, download, save_pixels
from .terrain import grid_mesh, polygon_mask, polyline_distance

DEM_TILES = {
    38: "Copernicus_DSM_COG_10_N37_00_E023_00_DEM",
    39: "Copernicus_DSM_COG_10_N38_00_E023_00_DEM",
}
DEM_URL = "https://copernicus-dem-30m.s3.amazonaws.com/{0}/{0}.tif"
DEM_LICENCE = ("Copernicus DEM GLO-30 (ESA, Copernicus programme), free licence with attribution: produced using "
               "Copernicus WorldDEM-30 (c) DLR e.V. 2010-2014 and (c) Airbus Defence and Space GmbH 2014-2018 "
               "provided under COPERNICUS by the European Union and ESA")
DEM_TOP = 39.0
DEM_WEST = 23.0
DEM_STEP = 1.0 / 3600.0
CITY_SPACING = 30.0
NEAR_SPACING = 2.5
CITY_MESH_SPACING = 50.0
FAR_SPACING = 250.0
SEA_FLOOR = -8.0
LAND_FLOOR = 0.7
FILL_BOXES = ((-4800.0, -800.0, -4800.0, -2700.0), (-8600.0, -6700.0, -3300.0, -2100.0))
ACROPOLIS_TOP = 151.4
WALL_OUTSIDE = 2.0
HILLS = [(1452.0, 1148.0, 480.0), (-392.0, -444.0, 270.0), (-283.0, 90.0, 120.0), (-625.0, -14.0, 230.0),
         (-560.0, 250.0, 200.0), (-6210.0, -3436.0, 380.0), (-472.0, 429.0, 90.0)]

RIVERS = {
    "ilissos": [(3200.0, 700.0), (2200.0, 150.0), (1500.0, -150.0), (900.0, -400.0), (500.0, -480.0),
                (100.0, -560.0), (-257.0, -641.0), (-700.0, -900.0), (-1100.0, -1500.0), (-1500.0, -2300.0),
                (-2000.0, -3000.0), (-2400.0, -3400.0)],
    "eridanos": [(1300.0, 1300.0), (900.0, 900.0), (500.0, 720.0), (0.0, 600.0), (-300.0, 590.0),
                 (-500.0, 650.0), (-700.0, 790.0), (-1200.0, 1050.0), (-2000.0, 1300.0), (-3000.0, 1250.0)],
    "cephise": [(-3400.0, 4400.0), (-3300.0, 2500.0), (-3150.0, 1000.0), (-3100.0, 0.0), (-3000.0, -1500.0),
                (-2900.0, -2700.0), (-2850.0, -3500.0)],
}


def smoothstep(t):
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3 - 2 * t)


def lattice(ix, iy, seed):
    value = (ix * 374761393 + iy * 668265263 + seed * 1442695041) & 0xFFFFFFFF
    value = ((value ^ (value >> 13)) * 1274126177) & 0xFFFFFFFF
    return ((value ^ (value >> 16)) & 0xFFFF) / 65535.0


def world_noise(xs, ys, scale, seed, octaves=4, persistence=0.5):
    total = np.zeros(np.shape(xs))
    amplitude = 1.0
    norm = 0.0
    for octave in range(octaves):
        fx = np.asarray(xs, dtype=np.float64) / scale * 2 ** octave
        fy = np.asarray(ys, dtype=np.float64) / scale * 2 ** octave
        ix = np.floor(fx).astype(np.int64)
        iy = np.floor(fy).astype(np.int64)
        tx = smoothstep(fx - ix)
        ty = smoothstep(fy - iy)
        s = seed + octave * 101
        a = lattice(ix, iy, s)
        b = lattice(ix + 1, iy, s)
        c = lattice(ix, iy + 1, s)
        d = lattice(ix + 1, iy + 1, s)
        total += amplitude * ((a * (1 - tx) + b * tx) * (1 - ty) + (c * (1 - tx) + d * tx) * ty)
        norm += amplitude
        amplitude *= persistence
    return total / norm


def shifted(values, dy, dx):
    padded = np.pad(values, 1, mode="edge")
    rows, columns = values.shape
    return padded[1 + dy:1 + dy + rows, 1 + dx:1 + dx + columns]


def neighbourhood(values, passes, reduce):
    for _ in range(passes):
        values = reduce.reduce([shifted(values, dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1)])
    return values


def blur(values, passes):
    for _ in range(passes):
        values = (shifted(values, -1, 0) + shifted(values, 1, 0) + shifted(values, 0, -1) + shifted(values, 0, 1)
                  + 4 * values) / 8
    return values


class Field:
    def __init__(self, cx, cy, half, spacing, heights=None):
        self.cx, self.cy, self.half, self.spacing = cx, cy, half, spacing
        self.count = int(round(2 * half / spacing)) + 1
        axis = np.linspace(-half, half, self.count)
        self.gx, self.gy = np.meshgrid(axis + cx, axis + cy)
        self.heights = heights

    def contains(self, x, y, margin=0.0):
        return abs(x - self.cx) <= self.half - margin and abs(y - self.cy) <= self.half - margin

    def sample(self, x, y):
        last = self.count - 1.001
        column = np.clip((np.asarray(x, dtype=np.float64) - self.cx + self.half) / self.spacing, 0, last)
        row = np.clip((np.asarray(y, dtype=np.float64) - self.cy + self.half) / self.spacing, 0, last)
        c0 = np.floor(column).astype(int)
        r0 = np.floor(row).astype(int)
        fx = column - c0
        fy = row - r0
        h = self.heights
        lower = h[r0, c0] * (1 - fx) + h[r0, c0 + 1] * fx
        upper = h[r0 + 1, c0] * (1 - fx) + h[r0 + 1, c0 + 1] * fx
        result = lower * (1 - fy) + upper * fy
        return float(result) if np.ndim(result) == 0 else result

    def slope(self):
        gy, gx = np.gradient(self.heights, self.spacing)
        return np.hypot(gx, gy)


def load_tile(path):
    image = bpy.data.images.load(path, check_existing=True)
    image.colorspace_settings.name = "Non-Color"
    width, height = image.size
    pixels = np.empty(width * height * image.channels, dtype=np.float32)
    image.pixels.foreach_get(pixels)
    grid = pixels.reshape(height, width, image.channels)[::-1, :, 0].copy()
    bpy.data.images.remove(image)
    return grid


def load_dem(cache_dir):
    rows = []
    for top in sorted(DEM_TILES, reverse=True):
        name = DEM_TILES[top]
        path = download(DEM_URL.format(name), os.path.join(cache_dir, "src", "dem", f"{name}.tif"))
        rows.append(load_tile(path))
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


def ancient_sea(raw, gx, gy):
    sea = raw <= 0.5
    for x0, x1, y0, y1 in FILL_BOXES:
        box = (gx >= x0) & (gx <= x1) & (gy >= y0) & (gy <= y1)
        sea |= box & (raw < 3.5)
    return sea


def seabed(heights, sea, spacing):
    land = np.maximum(heights, LAND_FLOOR)
    depth = blur(sea.astype(np.float64), max(int(120.0 / spacing), 2))
    return np.where(sea, SEA_FLOOR * (0.4 + 0.6 * depth) - 1.0, land)


def snapped_river(field, points, step=40.0, reach=120.0):
    path = []
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        length = math.hypot(x1 - x0, y1 - y0)
        count = max(int(length / step), 1)
        for k in range(count):
            t = k / count
            path.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, (x1 - x0) / length, (y1 - y0) / length))
    path.append((*points[-1], 0.0, 0.0))
    snapped = []
    offsets = np.linspace(-reach, reach, 25)
    for x, y, dx, dy in path:
        px, py = x - dy * offsets, y + dx * offsets
        heights = field.sample(px, py) + np.abs(offsets) * 0.02
        best = int(np.argmin(heights))
        snapped.append((float(px[best]), float(py[best])))
    smooth = list(snapped)
    for _ in range(4):
        smooth = [smooth[0]] + [((a[0] + 2 * b[0] + c[0]) / 4, (a[1] + 2 * b[1] + c[1]) / 4)
                                for a, b, c in zip(smooth[:-2], smooth[1:-1], smooth[2:])] + [smooth[-1]]
    return smooth


def city_field(dem):
    cx, cy = plan.CITY_CENTRE
    field = Field(cx, cy, plan.CITY_HALF + 900.0, CITY_SPACING)
    raw = resample(dem, field.gx, field.gy)
    opened = neighbourhood(neighbourhood(raw, 2, np.minimum), 2, np.maximum)
    mountain = smoothstep((raw - 280.0) / 160.0)
    hill = np.zeros_like(raw)
    for hx, hy, radius in HILLS:
        hill = np.maximum(hill, smoothstep(1.2 - np.hypot(field.gx - hx, field.gy - hy) / radius))
    natural = np.maximum(opened, blur(raw, 1) - 4.0)
    ground = blur(opened * (1 - mountain) + raw * mountain, 2) * (1 - hill) + blur(natural, 1) * hill
    sea = ancient_sea(raw, field.gx, field.gy)
    field.heights = seabed(ground, sea, CITY_SPACING)
    field.sea = sea
    rivers = {}
    for name, points in RIVERS.items():
        rivers[name] = snapped_river(field, points)
        distance = polyline_distance(rivers[name], field.gx, field.gy)
        field.heights = field.heights - 2.0 * smoothstep(1.0 - distance / 45.0) * (~sea)
    field.rivers = rivers
    return field


def acropolis_level(x, y):
    return (ACROPOLIS_TOP - 11.0 * (1.0 - smoothstep((x + 135.0) / 120.0))
            - 1.6 * smoothstep((y - 45.0) / 40.0) - 0.8 * smoothstep((x - 60.0) / 80.0))


def masonry_height(gx, gy):
    south = smoothstep((-gy - 18.0) / 10.0) * smoothstep((gx + 125.0) / 20.0)
    drums = smoothstep((gy - 55.0) / 10.0) * (1.0 - smoothstep((np.abs(gx - 10.0) - 75.0) / 10.0))
    return 2.4 + 3.6 * south + 2.2 * drums


def rock_outcrop(gx, gy, signed, level, heights):
    masonry = masonry_height(gx, gy)
    west = smoothstep((-gx - 105.0) / 25.0)
    north = smoothstep((gy - 25.0) / 25.0)
    east = smoothstep((gx - 95.0) / 30.0)
    vary = world_noise(gx, gy, 45.0, 37, 3)
    tall = (9.0 + 16.0 * vary) * (1.0 - 0.75 * west) * (1.0 + 0.35 * north + 0.2 * east)
    steep = 3.4 - 1.6 * west
    upper, lower = 0.55 * tall, 0.45 * tall
    ledge = 2.5 + 5.0 * world_noise(gx, gy, 28.0, 41, 2)
    d = np.maximum(signed - WALL_OUTSIDE, 0.0)
    first = np.minimum(d, upper / steep)
    rest = d - first
    shelf = np.minimum(rest, ledge)
    rest = rest - shelf
    second = np.minimum(rest, lower / steep)
    scree = rest - second
    drop = first * steep + shelf * 0.28 + second * steep + scree * (0.72 - 0.25 * west)
    rough = (world_noise(gx, gy, 6.0, 31, 3) - 0.5) * 3.2 * smoothstep(d / 2.0) * smoothstep((10.0 - scree) / 10.0)
    cliff = level - masonry - drop + rough
    foot = blur(neighbourhood(heights, 10, np.minimum), 3)
    outside = np.maximum(cliff, foot)
    blend = smoothstep((d - 55.0) / 30.0)
    outside = outside * (1 - blend) + heights * blend
    return np.where(signed <= WALL_OUTSIDE, level - masonry, outside)


def outline_distance(points, gx, gy):
    distance = polyline_distance(points + points[:1], gx, gy)
    inside = polygon_mask(points, gx, gy)
    return np.where(inside, -distance, distance)


def apply_pad(heights, gx, gy, pad):
    kind = pad["kind"]
    if kind == "rect":
        angle = math.radians(pad.get("azimuth", 0.0))
        dx, dy = gx - pad["x"], gy - pad["y"]
        u = dx * math.cos(angle) - dy * math.sin(angle)
        v = dx * math.sin(angle) + dy * math.cos(angle)
        distance = np.maximum(np.abs(u) - pad["half_u"], np.abs(v) - pad["half_v"])
    else:
        distance = np.hypot(gx - pad["x"], gy - pad["y"]) - pad["radius"]
    weight = smoothstep(1.0 - distance / pad.get("margin", 6.0))
    if pad.get("smooth"):
        target = blur(heights, pad["smooth"])
    elif pad["level"] is None:
        target = float(np.median(heights[distance < 0])) if (distance < 0).any() else float(heights.mean())
    else:
        target = pad["level"]
    return heights * (1 - weight) + target * weight


def near_field(city, pads, ramp):
    cx, cy = plan.NEAR_CENTRE
    field = Field(cx, cy, plan.NEAR_HALF, NEAR_SPACING)
    gx, gy = field.gx, field.gy
    heights = city.sample(gx, gy)
    signed = outline_distance(plan.ACROPOLIS_EDGE, gx, gy)
    level = acropolis_level(gx, gy)
    heights = np.where(signed <= 0.8, level, rock_outcrop(gx, gy, signed, level, heights))
    for name, points in city.rivers.items():
        distance = polyline_distance(points, gx, gy)
        heights = heights - 1.4 * smoothstep(1.0 - (distance - 2.0) / 10.0)
    x0, y0, x1, y1, z0, z1, width = ramp
    if z0 is None:
        z0 = float(city.sample(x0, y0))
    length = math.hypot(x1 - x0, y1 - y0)
    tx, ty = (x1 - x0) / length, (y1 - y0) / length
    along = (gx - x0) * tx + (gy - y0) * ty
    across = np.abs(-(gx - x0) * ty + (gy - y0) * tx)
    t = np.clip(along / length, 0.0, 1.0)
    ramp_height = z0 + (z1 - z0) * t
    weight = smoothstep(1.0 - (across - width / 2) / 6.0) * smoothstep((along + 12.0) / 12.0) * smoothstep(
        (length + 4.0 - along) / 4.0)
    heights = heights * (1 - weight) + ramp_height * weight
    for pad in pads:
        heights = apply_pad(heights, gx, gy, pad)
    field.heights = heights
    field.signed = signed
    return field


def far_field(dem, city):
    field = Field(0.0, 0.0, plan.FAR_HALF, FAR_SPACING)
    raw = resample(dem, field.gx, field.gy)
    sea = raw <= 0.5
    heights = seabed(raw, sea, FAR_SPACING)
    inside = (np.abs(field.gx - city.cx) < city.half - 300.0) & (np.abs(field.gy - city.cy) < city.half - 300.0)
    heights = np.where(inside, city.sample(field.gx, field.gy), heights)
    field.heights = heights
    field.sea = sea
    return field


def mix(colour, other, weight):
    weight = np.clip(weight, 0.0, 1.0)[..., None]
    return colour * (1 - weight) + np.asarray(other) * weight


def outcrop_colour(colour, xs, ys, heights, slope, signed):
    near = smoothstep((95.0 - signed) / 35.0) * (signed > 0.0)
    fine = world_noise(xs, ys, 3.0, 52, 2)
    bands = 0.5 + 0.5 * np.sin(heights * 2 * math.pi / 1.7 + 6.0 * world_noise(xs, ys, 30.0, 51, 2))
    rock = np.array([0.69, 0.64, 0.56]) * (0.82 + 0.2 * bands)[..., None] * (0.9 + 0.16 * fine)[..., None]
    rock = mix(rock, np.array([0.72, 0.56, 0.40]), smoothstep((world_noise(xs, ys, 14.0, 53, 3) - 0.6) / 0.08) * 0.7)
    rock = mix(rock, np.array([0.46, 0.44, 0.40]), smoothstep((world_noise(xs, ys, 5.0, 54, 2) - 0.68) / 0.06) * 0.6)
    scree = np.array([0.69, 0.64, 0.55]) * (0.84 + 0.24 * world_noise(xs, ys, 1.2, 55, 2))[..., None]
    scrub = np.array([0.42, 0.44, 0.30]) * (0.85 + 0.3 * fine)[..., None]
    slope_zone = mix(scree, scrub, smoothstep((world_noise(xs, ys, 9.0, 56, 2) - 0.55) / 0.1) * 0.8)
    colour = mix(colour, slope_zone, near * smoothstep((slope - 0.35) / 0.2))
    return mix(colour, rock, near * smoothstep((slope - 1.0) / 0.5))


def land_colour(xs, ys, heights, slope, city_inside, acropolis=None, agora=None, outcrop=None):
    noise = world_noise(xs, ys, 700.0, 3, 4)
    fine = world_noise(xs, ys, 30.0, 4, 3)
    grain = world_noise(xs, ys, 6.0, 5, 2)
    angle = math.radians(32.0)
    u = xs * math.cos(angle) - ys * math.sin(angle)
    v = xs * math.sin(angle) + ys * math.cos(angle)
    pu = np.floor(u / 110.0).astype(np.int64)
    pv = np.floor(v / 70.0).astype(np.int64)
    parcel = ((pu * 73856093) ^ (pv * 19349663)) % 1000 / 1000.0
    crops = np.array([[0.84, 0.72, 0.46], [0.78, 0.68, 0.46], [0.72, 0.64, 0.46], [0.82, 0.74, 0.52],
                      [0.70, 0.62, 0.44], [0.80, 0.70, 0.48]])
    colour = crops[(parcel * len(crops)).astype(int) % len(crops)] * (0.92 + 0.14 * fine)[..., None]
    soil = np.array([0.66, 0.54, 0.38]) * (0.9 + 0.2 * grain)[..., None]
    trees = world_noise(xs, ys, 9.0, 12, 2) > 0.56
    olive = np.where(trees[..., None], np.array([0.30, 0.36, 0.20]) * (0.85 + 0.3 * grain)[..., None], soil)
    grove = ((parcel > 0.45) & (parcel < 0.85)) | (world_noise(xs, ys, 900.0, 14, 2) > 0.62)
    colour = np.where(grove[..., None], olive, colour)
    vine = parcel >= 0.85
    rows = np.sin(u * 2 * math.pi / 2.2) > 0.2
    vines = np.where(rows[..., None], np.array([0.36, 0.44, 0.18]), soil)
    colour = np.where(vine[..., None], vines, colour)
    edge = (np.abs((u / 110.0) % 1.0 - 0.5) > 0.49) | (np.abs((v / 70.0) % 1.0 - 0.5) > 0.485)
    colour = np.where(edge[..., None], colour * 0.9, colour)
    wild = smoothstep((world_noise(xs, ys, 1500.0, 15, 3) - 0.58) / 0.08)
    garrigue = mix(np.array([0.62, 0.58, 0.44]) * (0.85 + 0.25 * fine)[..., None],
                   np.array([0.34, 0.38, 0.24]), smoothstep((fine - 0.45) / 0.2) * 0.7)
    pines = np.array([0.20, 0.28, 0.15]) * (0.85 + 0.3 * fine)[..., None]
    rock = np.array([0.68, 0.63, 0.55]) * (0.84 + 0.22 * noise[..., None]) * (0.92 + 0.12 * grain[..., None])
    hill = np.maximum(np.maximum(smoothstep((heights - 170.0) / 120.0), smoothstep((slope - 0.18) / 0.14)), wild)
    upland = mix(garrigue, pines, smoothstep((heights - 650.0) / 250.0) * smoothstep((noise - 0.35) / 0.2))
    colour = mix(colour, upland, hill)
    colour = mix(colour, rock, np.maximum(smoothstep((slope - 0.6) / 0.35), smoothstep((heights - 900.0) / 200.0))
                 * (0.6 + 0.4 * (fine > 0.4)))
    town = np.array([0.72, 0.62, 0.48]) * (0.9 + 0.16 * fine)[..., None] * (0.94 + 0.1 * grain)[..., None]
    town = mix(town, np.array([0.46, 0.48, 0.30]) * (0.9 + 0.2 * grain)[..., None],
               smoothstep((world_noise(xs, ys, 25.0, 21, 2) - 0.66) / 0.06) * 0.8)
    colour = mix(colour, town, city_inside * (1.0 - smoothstep((slope - 0.5) / 0.3)))
    sand = np.array([0.86, 0.78, 0.60]) * (0.92 + 0.12 * grain)[..., None]
    colour = mix(colour, sand, smoothstep((5.0 - heights) / 3.0) * (heights > -0.5))
    under = np.array([0.40, 0.46, 0.44])
    colour = mix(colour, under, smoothstep((0.2 - heights) / 1.5))
    if outcrop is not None:
        colour = outcrop_colour(colour, xs, ys, heights, slope, outcrop)
    if acropolis is not None:
        plateau = np.array([0.72, 0.66, 0.56]) * (0.88 + 0.18 * fine)[..., None] * (0.94 + 0.1 * grain)[..., None]
        plateau = mix(plateau, np.array([0.78, 0.76, 0.70]), smoothstep((world_noise(xs, ys, 7.0, 22, 2) - 0.6) / 0.08))
        colour = mix(colour, plateau, acropolis)
    if agora is not None:
        square = np.array([0.80, 0.72, 0.58]) * (0.94 + 0.08 * fine)[..., None]
        colour = mix(colour, square, agora)
    return np.clip(colour * (0.93 + 0.12 * noise)[..., None], 0, 1)


def paint_lines(colour, xs, ys, lines, tone, width):
    for points in lines:
        distance = polyline_distance(points, xs, ys)
        colour = mix(colour, tone, smoothstep(1.0 - (distance - width / 2) / 2.5))
    return colour


def paint_rivers(colour, xs, ys, rivers):
    for points in rivers.values():
        distance = polyline_distance(points, xs, ys)
        colour = mix(colour, np.array([0.30, 0.38, 0.20]), smoothstep(1.0 - (distance - 6.0) / 14.0) * 0.8)
        colour = mix(colour, np.array([0.70, 0.67, 0.58]), smoothstep(1.0 - (distance - 3.0) / 3.0))
    return colour


def sun_shadow(field, xs, ys, heights, steps=36, reach=4000.0):
    azimuth, elevation = math.radians(plan.SUN[0]), math.radians(plan.SUN[1])
    dx, dy = math.sin(azimuth), math.cos(azimuth)
    slope = math.tan(elevation)
    clearance = np.full(heights.shape, np.inf)
    for step in range(1, steps + 1):
        distance = reach * (step / steps) ** 1.6
        ahead = field.sample(xs + dx * distance, ys + dy * distance)
        clearance = np.minimum(clearance, heights + distance * slope - ahead)
    return np.clip(clearance / 10.0 + 0.5, 0.0, 1.0)


def baked_colour(cx, cy, half, resolution, ground, extras, finish, chunk=512):
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
        colour = land_colour(xs, ys, heights, slope, inside, **extras(xs, ys, heights))
        colour = finish(colour, xs, ys, heights)
        out[start:start + chunk] = colour[start - lo:start - lo + min(chunk, resolution - start)]
    return np.clip(out, 0, 1)


def offset_grid(name, field, heights, skirt):
    mesh = grid_mesh(name, heights, field.half, skirt_depth=skirt)
    mesh.transform(Matrix.Translation((field.cx, field.cy, 0.0)))
    return mesh


def remove_inside(mesh, cx, cy, half):
    work = bmesh.new()
    work.from_mesh(mesh)
    doomed = [face for face in work.faces
              if all(abs(v.co.x - cx) <= half + 0.5 and abs(v.co.y - cy) <= half + 0.5 for v in face.verts)]
    bmesh.ops.delete(work, geom=doomed, context="FACES")
    work.to_mesh(mesh)
    work.free()
    mesh.update()


def decimated(mesh, ratio):
    holder = bpy.data.objects.new(f"{mesh.name}_tmp", mesh)
    bpy.context.scene.collection.objects.link(holder)
    modifier = holder.modifiers.new("lod", "DECIMATE")
    modifier.ratio = ratio
    depsgraph = bpy.context.evaluated_depsgraph_get()
    result = bpy.data.meshes.new_from_object(holder.evaluated_get(depsgraph))
    bpy.data.objects.remove(holder)
    name = mesh.name
    bpy.data.meshes.remove(mesh)
    result.name = name
    result.polygons.foreach_set("use_smooth", [True] * len(result.polygons))
    return result


def face_centres(mesh):
    centres = np.empty(len(mesh.polygons) * 3)
    mesh.polygons.foreach_get("center", centres)
    normals = np.empty(len(mesh.polygons) * 3)
    mesh.polygons.foreach_get("normal", normals)
    return centres.reshape(-1, 3), normals.reshape(-1, 3)


def near_materials(mesh, materials, agora_polygon):
    centres, normals = face_centres(mesh)
    xs, ys = centres[:, 0], centres[:, 1]
    steep = normals[:, 2] < 0.72
    plateau = polygon_mask(plan.ACROPOLIS_EDGE, xs, ys)
    agora = polygon_mask(agora_polygon, xs, ys)
    index = np.zeros(len(xs), dtype=np.int64)
    index[steep] = 1
    index[agora & ~steep] = 3
    index[plateau] = 2
    for material in materials:
        mesh.materials.append(material)
    mesh.polygons.foreach_set("material_index", index)
    return {name.name: int((index == k).sum()) for k, name in enumerate(materials)}


class Ground:
    def __init__(self, near, city, far):
        self.near, self.city, self.far = near, city, far
        self.trees = []

    def __call__(self, x, y):
        if self.near.contains(x, y, 6.0):
            return self.near.sample(x, y)
        if self.city.contains(x, y, 950.0):
            return self.city.sample(x, y)
        return self.far.sample(x, y)

    def grid(self, xs, ys):
        heights = self.far.sample(xs, ys)
        in_city = (np.abs(xs - self.city.cx) < self.city.half - 950.0) & (np.abs(ys - self.city.cy) < self.city.half - 950.0)
        heights = np.where(in_city, self.city.sample(xs, ys), heights)
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


def cached_image(name, path, reuse, build):
    if reuse and os.path.exists(path):
        image = bpy.data.images.load(path, check_existing=True)
        image.name = name
        return image
    return save_pixels(name, build(), path, quality=88)


def build(collection, parent, cache_dir, pads, ramp, agora_polygon, new_object, report, reuse_textures=False):
    texture_dir = os.path.join(cache_dir, "textures")
    os.makedirs(texture_dir, exist_ok=True)
    dem = load_dem(cache_dir)
    city = city_field(dem)
    far = far_field(dem, city)
    del dem
    near = near_field(city, pads, ramp)
    ground = Ground(near, city, far)
    report["heights"] = {name: round(ground(*plan.local(name)), 1) for name in
                         ("acropole", "propylees", "areopage", "pnyx", "mouseion", "agora", "hephaisteion",
                          "theatre", "odeon", "lycabette", "dipylon", "olympieion", "piree", "mounichie",
                          "hymette")}
    city_mesh_field = Field(city.cx, city.cy, plan.CITY_HALF, CITY_MESH_SPACING)
    city_heights = city.sample(city_mesh_field.gx, city_mesh_field.gy)
    under = (np.abs(city_mesh_field.gx - near.cx) < near.half + 60.0) & (
        np.abs(city_mesh_field.gy - near.cy) < near.half + 60.0)
    city_heights = np.where(under, city_heights - 6.0, city_heights)
    far_heights = far.heights.copy()
    far_under = (np.abs(far.gx - city.cx) < plan.CITY_HALF + 300.0) & (np.abs(far.gy - city.cy) < plan.CITY_HALF + 300.0)
    far_heights = np.where(far_under, far_heights - 10.0, far_heights)

    def near_extras(xs, ys, heights):
        signed = outline_distance(plan.ACROPOLIS_EDGE, xs, ys)
        return {"acropolis": smoothstep((1.0 - signed) / 2.0), "outcrop": signed,
                "agora": blur(polygon_mask(agora_polygon, xs, ys).astype(np.float64), 4)}

    roads = report.get("roads", [])

    def near_finish(colour, xs, ys, heights):
        colour = paint_rivers(colour, xs, ys, city.rivers)
        return paint_lines(colour, xs, ys, roads, np.array([0.80, 0.72, 0.58]), 5.0)

    def city_finish(colour, xs, ys, heights):
        colour = paint_lines(paint_rivers(colour, xs, ys, city.rivers), xs, ys, roads, np.array([0.78, 0.70, 0.56]),
                             5.0)
        return colour * (0.72 + 0.28 * sun_shadow(city, xs, ys, heights))[..., None]

    def far_finish(colour, xs, ys, heights):
        return colour * (0.68 + 0.32 * sun_shadow(far, xs, ys, heights, 30, 12000.0))[..., None]

    near_image = cached_image("terrain_core", os.path.join(texture_dir, "terrain_core.jpg"), reuse_textures,
                              lambda: baked_colour(near.cx, near.cy, near.half, 4096, ground, near_extras, near_finish))
    city_image = cached_image("terrain_ring", os.path.join(texture_dir, "terrain_ring.jpg"), reuse_textures,
                              lambda: baked_colour(city.cx, city.cy, plan.CITY_HALF, 4096, ground,
                                                   lambda a, b, c: {}, city_finish))
    far_image = cached_image("terrain_far_colour", os.path.join(texture_dir, "terrain_far.jpg"), reuse_textures,
                             lambda: baked_colour(0.0, 0.0, plan.FAR_HALF, 2048, ground, lambda a, b, c: {},
                                                  far_finish))
    near_materials_list = [baked_material(name, near_image, 0.95) for name in
                           ("terrain_pentes", "terrain_rocher", "ground_plateau", "ground_agora")]
    near_mesh = decimated(offset_grid("terrain", near, near.heights, 25.0), 0.3)
    report["near_faces"] = near_materials(near_mesh, near_materials_list, agora_polygon)
    near_object = new_object("terrain_proche", near_mesh, collection, parent)
    city_mesh = offset_grid("terrain_ville", city_mesh_field, city_heights, 40.0)
    remove_inside(city_mesh, near.cx, near.cy, near.half - CITY_MESH_SPACING)
    city_mesh = decimated(city_mesh, 0.45)
    city_mesh.materials.append(baked_material("terrain_ville", city_image, 0.95))
    city_object = new_object("terrain_ville", city_mesh, collection, parent)
    city_object["cast_shadow"] = False
    far_grid = Field(0.0, 0.0, plan.FAR_HALF, FAR_SPACING)
    far_mesh = offset_grid("terrain_far", far_grid, far_heights, 0.0)
    remove_inside(far_mesh, city.cx, city.cy, plan.CITY_HALF - FAR_SPACING)
    far_mesh = decimated(far_mesh, 0.4)
    far_mesh.materials.append(baked_material("terrain_far", far_image, 0.95))
    far_object = new_object("terrain_far", far_mesh, collection, parent)
    far_object["cast_shadow"] = False
    for obj in (near_object, city_object, far_object):
        report.setdefault("triangles", {})[obj.name] = sum(len(p.vertices) - 2 for p in obj.data.polygons)
    ground.add_surface([near_object, city_object, far_object])
    ground.objects = {"near": near_object, "city": city_object, "far": far_object}
    return ground
