import math
import os

import bmesh
import bpy
import numpy as np

from .materials import baked_material, download, principled_material, save_pixels
from .terrain import GeoFrame, polygon_mask

DEM_URL = ("https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N38_00_E022_00_DEM/"
           "Copernicus_DSM_COG_10_N38_00_E022_00_DEM.tif")
DEM_LICENCE = ("produced using Copernicus WorldDEM-30 (c) DLR e.V. 2010-2014 and (c) Airbus Defence and Space GmbH "
               "2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved")
DEM_NORTH = 39.0
DEM_WEST = 22.0
DEM_STEP = 1.0 / 3600.0
KOLONOS = (38.79577, 22.53715)
EXTENT = (-8920.0, 5080.0, -7640.0, 6360.0)
CORE = (-6040.0, 3000.0, -2520.0, 1000.0)
PASS = (-1200.0, 400.0, -360.0, 160.0)
GATES = [(-4060.0, -3360.0, 760.0, 1000.0), (2300.0, 3300.0, 720.0, 940.0)]
RING_SPACING = 80.0
CORE_SPACING = 20.0
PASS_SPACING = 4.0
GATE_SPACING = 5.0
FAR_SPACING = 400.0
FAR_REACH = (33, 42, 36, 39)
BASE_SPACING = 10.0
SKIRT = 3.0
SEA_LEVEL = 0.0
CLIFF = 1.15

SHORE = np.array([
    (-9400, 5700), (-8200, 4500), (-7200, 3500), (-6300, 2700), (-5500, 2150), (-4800, 1550), (-4300, 1180),
    (-3950, 978), (-3750, 930), (-3550, 905), (-3300, 860), (-3000, 742), (-2750, 642), (-2500, 565),
    (-2200, 470), (-1900, 345), (-1600, 220), (-1400, 120), (-1250, 60), (-1100, -40), (-1000, -120),
    (-950, -158), (-850, -170), (-700, -178), (-450, -174), (-300, -160), (-200, -122), (-130, -50), (-95, 40),
    (-60, 90), (0, 115), (100, 135), (300, 190), (600, 270), (1000, 390), (1400, 530), (1800, 650), (2100, 740),
    (2400, 815), (2700, 846), (3000, 853), (3200, 872), (3500, 1000), (3900, 1350), (4400, 1550), (5000, 1700),
    (5400, 1800)], float)
FOOT = np.array([
    (-9400, -900), (-8000, -850), (-7000, -700), (-6000, -400), (-5400, 0), (-5000, 250), (-4600, 550),
    (-4250, 800), (-3950, 898), (-3750, 900), (-3550, 872), (-3300, 818), (-3000, 692), (-2750, 578),
    (-2500, 300), (-2350, 120), (-2100, 0), (-1800, -120), (-1500, -230), (-1250, -240), (-1100, -215),
    (-900, -212), (-700, -210), (-500, -207), (-350, -200), (-200, -192), (-80, -200), (0, -190), (150, -150),
    (400, -80), (700, 0), (1000, 80), (1300, 200), (1600, 330), (1900, 470), (2200, 630), (2450, 795),
    (2700, 834), (3000, 840), (3300, 830), (3700, 820), (4200, 850), (4700, 900), (5400, 950)], float)
DROP = np.array([(-9400, 18), (-4200, 18), (-3800, 20), (-1300, 22), (-200, 22), (300, 21), (2300, 20), (3300, 20),
                 (5400, 15)], float)
ALLOWANCE = np.array([(-9400, 40, 260), (-4500, 40, 260), (-4050, 2.5, 14), (-3500, 2.5, 14), (-3100, 6, 60),
                      (-2600, 10, 160), (-1600, 10, 160), (-1150, 2.5, 20), (-300, 2.5, 20), (0, 7, 90),
                      (600, 10, 160), (2100, 8, 120), (2420, 2.2, 10), (3150, 2.2, 10), (3600, 10, 160),
                      (5400, 10, 160)], float)
ROAD = np.array([
    (-8600, 2000), (-7400, 1500), (-6500, 1000), (-5000, 700), (-4300, 905), (-3950, 930), (-3750, 917),
    (-3550, 892), (-3300, 843), (-3000, 720), (-2750, 615), (-2500, 450), (-2350, 300), (-2000, 120), (-1600, 0),
    (-1300, -90), (-1100, -170), (-900, -192), (-700, -195), (-450, -192), (-300, -180), (-150, -160),
    (-60, -105), (40, -70), (300, -10), (700, 110), (1100, 250), (1500, 420), (1900, 580), (2200, 700),
    (2450, 808), (2700, 836), (3000, 846), (3300, 870), (3800, 1150), (4300, 1300), (5300, 1500)], float)
ASOPOS = np.array([
    (-5060, 180), (-4820, 400), (-4520, 630), (-4220, 815), (-3960, 902), (-3750, 905), (-3550, 878),
    (-3300, 824), (-3000, 698), (-2800, 610), (-2700, 612), (-2640, 650)], float)
MELAS = np.array([(-8800, -700), (-8650, 300), (-8500, 1400), (-8380, 2600), (-8240, 3800), (-8180, 4600)], float)
PHOINIX = np.array([(-3660, 560), (-3680, 700), (-3700, 820), (-3720, 896)], float)
ANOPAIA = np.array([
    (-5000, 300), (-5400, -60), (-5800, -500), (-6000, -1000), (-6200, -1500), (-6650, -2500), (-7000, -3400),
    (-6300, -3700), (-5500, -3800), (-4500, -3650), (-3500, -3550), (-2000, -3100), (-500, -2700), (300, -2480),
    (1000, -2300), (1600, -2150), (2000, -2000), (2400, -1800), (2650, -1500), (2850, -800), (3000, -500),
    (2900, 200), (2760, 600), (2700, 820)], float)
COURSES = {"asopos": ASOPOS, "melas": MELAS, "phoinix": PHOINIX}
RIVERS = {"asopos": (7.0, 1.2, 20.0), "melas": (6.0, 0.8, 30.0), "phoinix": (2.0, 0.6, 6.0)}
SPRINGS = [(-940.0, -217.0, 7.0), (-880.0, -216.0, 5.0), (-805.0, -214.0, 6.0), (-760.0, -213.0, 4.0)]
PERSIAN_CAMP = np.array([(-8600, -300), (-4700, -100), (-4500, 700), (-4900, 1500), (-5700, 2150),
                         (-6800, 2650), (-8600, 2700)], float)
KOLONOS_RADIUS = 70.0
KOLONOS_TOP = 16.0


def smoothstep(edge0, edge1, value):
    t = np.clip((value - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def chaikin(points, passes=3):
    points = np.asarray(points, float)
    for _ in range(passes):
        quarter = 0.75 * points[:-1] + 0.25 * points[1:]
        three_quarter = 0.25 * points[:-1] + 0.75 * points[1:]
        middle = np.empty((2 * len(quarter), 2))
        middle[0::2] = quarter
        middle[1::2] = three_quarter
        points = np.vstack([points[:1], middle, points[-1:]])
    return points


def densify(points, step):
    result = [np.asarray(points[0], float)]
    for start, end in zip(points[:-1], points[1:]):
        start = np.asarray(start, float)
        end = np.asarray(end, float)
        pieces = max(1, int(np.linalg.norm(end - start) / step))
        result.extend(start + (end - start) * (k / pieces) for k in range(1, pieces + 1))
    return np.array(result)


def polyline_distance(points, x, y, reach=None):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    distance = np.full(x.shape, np.inf)
    along = np.zeros(x.shape)
    if reach is not None:
        near = ((x > points[:, 0].min() - reach) & (x < points[:, 0].max() + reach)
                & (y > points[:, 1].min() - reach) & (y < points[:, 1].max() + reach))
        if not near.any():
            return distance, along
        inner, inner_along = polyline_distance(points, x[near], y[near])
        distance[near] = inner
        along[near] = inner_along
        return distance, along
    travelled = 0.0
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        dx, dy = x1 - x0, y1 - y0
        length = math.hypot(dx, dy)
        t = np.clip(((x - x0) * dx + (y - y0) * dy) / max(length * length, 1e-9), 0, 1)
        current = np.hypot(x - (x0 + t * dx), y - (y0 + t * dy))
        closer = current < distance
        distance = np.where(closer, current, distance)
        along = np.where(closer, travelled + t * length, along)
        travelled += length
    return distance, along


def lattice_noise(x, y, cell, seed):
    gx = np.asarray(x, float) / cell
    gy = np.asarray(y, float) / cell
    x0 = np.floor(gx)
    y0 = np.floor(gy)
    fx = gx - x0
    fy = gy - y0
    fx = fx * fx * (3 - 2 * fx)
    fy = fy * fy * (3 - 2 * fy)

    def hashed(ix, iy):
        value = np.sin(ix * 127.1 + iy * 311.7 + seed * 74.7) * 43758.5453
        return value - np.floor(value)
    top = hashed(x0, y0) * (1 - fx) + hashed(x0 + 1, y0) * fx
    bottom = hashed(x0, y0 + 1) * (1 - fx) + hashed(x0 + 1, y0 + 1) * fx
    return top * (1 - fy) + bottom * fy


def world_noise(x, y, cell, seed, octaves=3):
    total = 0.0
    weight = 0.0
    amplitude = 1.0
    for octave in range(octaves):
        total = total + amplitude * lattice_noise(x, y, cell / 2 ** octave, seed + octave * 17)
        weight += amplitude
        amplitude *= 0.5
    return total / weight


def shifted(values, dy, dx):
    padded = np.pad(values, 1, mode="edge")
    rows, columns = values.shape
    return padded[1 + dy:1 + dy + rows, 1 + dx:1 + dx + columns]


def blur(values, passes):
    for _ in range(passes):
        values = (shifted(values, -1, 0) + shifted(values, 1, 0) + shifted(values, 0, -1) + shifted(values, 0, 1)
                  + 4 * values) / 8
    return values


def bilinear(grid, x0, y0, spacing, x, y):
    rows, columns = grid.shape
    column = np.clip((np.asarray(x, float) - x0) / spacing, 0, columns - 1.001)
    row = np.clip((np.asarray(y, float) - y0) / spacing, 0, rows - 1.001)
    c0 = column.astype(int)
    r0 = row.astype(int)
    fx = column - c0
    fy = row - r0
    top = grid[r0, c0] * (1 - fx) + grid[r0, c0 + 1] * fx
    bottom = grid[r0 + 1, c0] * (1 - fx) + grid[r0 + 1, c0 + 1] * fx
    return top * (1 - fy) + bottom * fy


class Relief:
    def __init__(self, cache_dir):
        self.frame = GeoFrame(*KOLONOS)
        path = download(DEM_URL, os.path.join(cache_dir, "glo30_N38_E022.tif"))
        image = bpy.data.images.load(path, check_existing=True)
        image.colorspace_settings.name = "Non-Color"
        width, height = image.size
        pixels = np.empty(width * height * image.channels, dtype=np.float32)
        image.pixels.foreach_get(pixels)
        dem = pixels.reshape(height, width, image.channels)[::-1, :, 0]
        bpy.data.images.remove(image)
        north, south, west, east = 39.0, 38.55, 22.25, 22.85
        r0, r1 = int((DEM_NORTH - north) / DEM_STEP), int((DEM_NORTH - south) / DEM_STEP)
        c0, c1 = int((west - DEM_WEST) / DEM_STEP), int((east - DEM_WEST) / DEM_STEP)
        crop = dem[r0:r1 + 1, c0:c1 + 1].astype(np.float32)
        self.crop_north = DEM_NORTH - r0 * DEM_STEP
        self.crop_west = DEM_WEST + c0 * DEM_STEP
        self.dem = self.despeckle(crop)
        self.levels = {}
        x0, x1, y0, y1 = EXTENT
        xs = np.arange(x0, x1 + BASE_SPACING / 2, BASE_SPACING)
        ys = np.arange(y0, y1 + BASE_SPACING / 2, BASE_SPACING)
        grid_x, grid_y = np.meshgrid(xs, ys)
        self.base = blur(self.modern_far(grid_x, grid_y), 3)
        gradient_y, gradient_x = np.gradient(self.base, BASE_SPACING)
        self.slope = np.hypot(gradient_x, gradient_y)
        self.shore_field = self.signed_field(chaikin(SHORE), xs, ys, grid_x, grid_y, 2600.0)
        self.foot_field = self.signed_field(chaikin(FOOT), xs, ys, grid_x, grid_y, 800.0)

    def signed_field(self, line, xs, ys, grid_x, grid_y, reach):
        distance = np.minimum(grid_distance(line, xs, ys, reach), 1e5)
        return np.where(grid_y < np.interp(grid_x, line[:, 0], line[:, 1]), distance, -distance)

    def despeckle(self, dem):
        stack = np.stack([shifted(dem, dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1)])
        median = np.median(stack, axis=0)
        cell_x = DEM_STEP * self.frame.metres_per_degree_longitude
        cell_y = DEM_STEP * self.frame.metres_per_degree_latitude
        gradient_y, gradient_x = np.gradient(median, cell_y, cell_x)
        gentle = smoothstep(0.35, 0.2, np.hypot(gradient_x, gradient_y))
        return dem * (1 - gentle) + median * gentle

    def modern_far(self, x, y):
        latitude, longitude = self.frame.to_geo(np.asarray(x, float), np.asarray(y, float))
        rows, columns = self.dem.shape
        row = np.clip((self.crop_north - latitude) / DEM_STEP, 0, rows - 1.001)
        column = np.clip((longitude - self.crop_west) / DEM_STEP, 0, columns - 1.001)
        r0 = row.astype(int)
        c0 = column.astype(int)
        fy = row - r0
        fx = column - c0
        h = self.dem
        top = h[r0, c0] * (1 - fx) + h[r0, c0 + 1] * fx
        bottom = h[r0 + 1, c0] * (1 - fx) + h[r0 + 1, c0 + 1] * fx
        return (top * (1 - fy) + bottom * fy).astype(np.float64)

    def modern(self, x, y):
        return bilinear(self.base, EXTENT[0], EXTENT[2], BASE_SPACING, x, y)

    def modern_slope(self, x, y):
        return bilinear(self.slope, EXTENT[0], EXTENT[2], BASE_SPACING, x, y)

    def evaluate(self, x, y, fields=False, rivers=True):
        x = np.asarray(x, float)
        y = np.asarray(y, float)
        base = self.modern(x, y)
        shore_signed = bilinear(self.shore_field, EXTENT[0], EXTENT[2], BASE_SPACING, x, y)
        foot_signed = bilinear(self.foot_field, EXTENT[0], EXTENT[2], BASE_SPACING, x, y)
        shore_distance = np.abs(shore_signed)
        foot_distance = np.abs(foot_signed)
        land = shore_signed > 0
        mountain = foot_signed > 0
        drop = np.interp(x, DROP[:, 0], DROP[:, 1])
        allowance = np.interp(x, ALLOWANCE[:, 0], ALLOWANCE[:, 1])
        ramp = np.interp(x, ALLOWANCE[:, 0], ALLOWANCE[:, 2])
        floor = 0.6 + np.minimum(shore_distance * 0.006, 2.5)
        strip = np.clip(base - drop, floor, floor + allowance * smoothstep(0.0, ramp, shore_distance))
        strip = 0.6 + (strip - 0.6) * smoothstep(0.0, np.minimum(18.0, ramp), shore_distance)
        cliff = np.minimum(np.maximum(base, strip), strip + CLIFF * foot_distance)
        on_land = np.where(mountain, cliff, strip)
        depth = (1.6 * np.clip(shore_distance / 40, 0, 1) + 3.4 * np.clip((shore_distance - 40) / 260, 0, 1)
                 + 10.0 * np.clip((shore_distance - 300) / 1700, 0, 1))
        sea = 0.1 - depth
        sea = sea + (base - sea) * smoothstep(55.0, 85.0, base)
        rough = (world_noise(x, y, 150.0, 21) - 0.5) * 2.0 * 7.0 + (world_noise(x, y, 36.0, 23) - 0.5) * 2.0 * 3.0
        rugged = smoothstep(0.3, 0.8, self.modern_slope(x, y)) * smoothstep(8.0, 45.0, foot_distance)
        on_land = on_land + rough * rugged * mountain
        h = np.where(land, on_land, sea)
        kolonos = np.hypot(x, y / 0.96)
        mound = 3.0 + (KOLONOS_TOP - 3.0) * (1 - smoothstep(18.0, KOLONOS_RADIUS, kolonos))
        h = np.where(land & (kolonos < KOLONOS_RADIUS + 10), np.maximum(h, mound), h)
        river = np.full(x.shape, np.inf)
        if rivers:
            for name, (half, depth, bank) in RIVERS.items():
                h, distance = self.carve(name, x, y, h, half, depth, bank)
                river = np.minimum(river, distance)
        if not fields:
            return h
        return dict(h=h, base=base, land=land, shore=shore_distance, foot=foot_distance, river=river)

    def river(self, name):
        if name not in self.levels:
            path = densify(chaikin(COURSES[name]), 20.0)
            heights = self.evaluate(path[:, 0], path[:, 1], rivers=False)
            level = np.minimum.accumulate(heights - 0.8)
            kernel = np.ones(9) / 9
            level = np.convolve(np.pad(level, 4, mode="edge"), kernel, "valid")
            self.levels[name] = (path, np.maximum(level, SEA_LEVEL + 0.15))
        return self.levels[name]

    def carve(self, name, x, y, h, half, depth, bank):
        path, level = self.river(name)
        distance, along = polyline_distance(path, x, y, reach=half + bank + 5)
        steps = np.concatenate([[0.0], np.cumsum(np.hypot(*np.diff(path, axis=0).T))])
        surface = np.interp(along, steps, level)
        channel = surface - 0.25 - depth * (1 - (np.minimum(distance, half) / half) ** 2)
        banks = surface + 0.35 + np.maximum(distance - half, 0) * 0.35
        carved = np.where(distance < half + bank, np.minimum(h, np.where(distance < half, channel, banks)), h)
        return carved, distance

    def far(self, x, y):
        base = self.modern_far(x, y)
        gulf = (x > -9300) & (y > 3000) & (base < 12.0)
        return np.where(gulf, -8.0, base)


def level_grid(bounds, spacing):
    x0, x1, y0, y1 = bounds
    xs = np.arange(x0, x1 + spacing / 2, spacing)
    ys = np.arange(y0, y1 + spacing / 2, spacing)
    return xs, ys


def match_border(heights, xs, ys, ratio):
    for row in (0, -1):
        heights[row, :] = np.interp(xs, xs[::ratio], heights[row, ::ratio])
    for column in (0, -1):
        heights[:, column] = np.interp(ys, ys[::ratio], heights[::ratio, column])
    return heights


def inside(bounds, x, y):
    x0, x1, y0, y1 = bounds
    return (x > x0) & (x < x1) & (y > y0) & (y < y1)


class GroundMesh:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.materials = []
        self.count = 0

    def add_grid(self, xs, ys, heights, material, holes, skirt):
        grid_x, grid_y = np.meshgrid(xs, ys)
        rows, columns = heights.shape
        index = np.arange(rows * columns).reshape(rows, columns) + self.count
        self.vertices.append(np.column_stack([grid_x.ravel(), grid_y.ravel(), heights.ravel()]))
        quads = np.stack([index[:-1, :-1], index[:-1, 1:], index[1:, 1:], index[1:, :-1]], axis=-1)
        centre_x = (grid_x[:-1, :-1] + grid_x[:-1, 1:]) / 2
        centre_y = (grid_y[:-1, :-1] + grid_y[1:, :-1]) / 2
        keep = np.ones(centre_x.shape, bool)
        for hole in holes:
            keep &= ~inside(hole, centre_x, centre_y)
        kept = quads[keep]
        self.faces.append(kept)
        self.materials.append(np.full(len(kept), material))
        self.count += rows * columns
        if skirt:
            border = np.concatenate([index[0, :], index[1:, -1], index[-1, -2::-1], index[-2:0:-1, 0]])
            top = np.vstack(self.vertices)[border]
            lowered = top.copy()
            lowered[:, 2] -= SKIRT
            self.vertices.append(np.vstack([top, lowered]))
            start = self.count
            count = len(border)
            following = np.roll(np.arange(count), -1)
            upper = start + np.arange(count)
            strip = np.column_stack([upper[following], upper, start + count + np.arange(count),
                                     start + count + following])
            self.faces.append(strip)
            self.materials.append(np.full(len(strip), material))
            self.count += 2 * count

    def build(self, name, materials, uv_rects):
        vertices = np.vstack(self.vertices)
        faces = np.vstack(self.faces)
        material_index = np.concatenate(self.materials)
        mesh = bpy.data.meshes.new(name)
        mesh.vertices.add(len(vertices))
        mesh.vertices.foreach_set("co", vertices.astype(np.float32).ravel())
        mesh.loops.add(len(faces) * 4)
        mesh.loops.foreach_set("vertex_index", faces.astype(np.int32).ravel())
        mesh.polygons.add(len(faces))
        mesh.polygons.foreach_set("loop_start", (np.arange(len(faces)) * 4).astype(np.int32))
        mesh.polygons.foreach_set("loop_total", np.full(len(faces), 4, np.int32))
        mesh.polygons.foreach_set("material_index", material_index.astype(np.int32))
        mesh.polygons.foreach_set("use_smooth", np.ones(len(faces), bool))
        for material in materials:
            mesh.materials.append(material)
        loop_vertices = faces.ravel()
        loop_materials = np.repeat(material_index, 4)
        uv = np.zeros((len(loop_vertices), 2))
        for slot, (x0, x1, y0, y1) in enumerate(uv_rects):
            chosen = loop_materials == slot
            points = vertices[loop_vertices[chosen]]
            uv[chosen, 0] = (points[:, 0] - x0) / (x1 - x0)
            uv[chosen, 1] = (points[:, 1] - y0) / (y1 - y0)
        layer = mesh.uv_layers.new(name="UVMap")
        layer.data.foreach_set("uv", uv.astype(np.float32).ravel())
        mesh.update()
        mesh.validate()
        return mesh


class Ground:
    def __init__(self, relief):
        self.relief = relief
        self.levels = []

    def heights(self, bounds, spacing, parent_spacing):
        xs, ys = level_grid(bounds, spacing)
        grid_x, grid_y = np.meshgrid(xs, ys)
        heights = self.relief.evaluate(grid_x, grid_y)
        if parent_spacing:
            heights = match_border(heights, xs, ys, int(round(parent_spacing / spacing)))
        self.levels.append((bounds, spacing, heights))
        return xs, ys, heights

    def sample(self, x, y):
        x = np.asarray(x, float)
        y = np.asarray(y, float)
        result = np.zeros(x.shape)
        for bounds, spacing, heights in self.levels:
            chosen = inside(bounds, x, y) | (bounds == EXTENT)
            if chosen.any():
                result = np.where(chosen, bilinear(heights, bounds[0], bounds[2], spacing, x, y), result)
        return result

    def engine_height(self, x, y):
        cell = 10.0
        gx = np.floor(np.asarray(x, float) / cell) * cell
        gy = np.floor(np.asarray(y, float) / cell) * cell
        fx = (np.asarray(x, float) - gx) / cell
        fy = (np.asarray(y, float) - gy) / cell
        a = self.sample(gx, gy)
        b = self.sample(gx + cell, gy)
        c = self.sample(gx, gy + cell)
        d = self.sample(gx + cell, gy + cell)
        return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy

    def build(self, materials, collection, new_object):
        mesh = GroundMesh()
        xs, ys, heights = self.heights(EXTENT, RING_SPACING, FAR_SPACING)
        mesh.add_grid(xs, ys, heights, 0, [CORE], False)
        xs, ys, heights = self.heights(CORE, CORE_SPACING, RING_SPACING)
        mesh.add_grid(xs, ys, heights, 1, [PASS, *GATES], True)
        xs, ys, heights = self.heights(PASS, PASS_SPACING, CORE_SPACING)
        mesh.add_grid(xs, ys, heights, 2, [], True)
        for gate in GATES:
            xs, ys, heights = self.heights(gate, GATE_SPACING, CORE_SPACING)
            mesh.add_grid(xs, ys, heights, 1, [], True)
        data = mesh.build("ground", materials, [EXTENT, CORE, PASS])
        ground = new_object("ground", data, collection)
        ground["cast_shadow"] = False
        return ground, mesh.count


def far_ground(relief, ground, collection, new_object, material):
    x0, x1, y0, y1 = EXTENT
    west, east, south, north = FAR_REACH
    xs = np.arange(x0 - west * FAR_SPACING, x1 + east * FAR_SPACING + 1, FAR_SPACING)
    ys = np.arange(y0 - south * FAR_SPACING, y1 + north * FAR_SPACING + 1, FAR_SPACING)
    grid_x, grid_y = np.meshgrid(xs, ys)
    heights = relief.far(grid_x, grid_y)
    border = ((np.isclose(grid_x, x0) | np.isclose(grid_x, x1)) & (grid_y >= y0 - 1) & (grid_y <= y1 + 1)) | (
        (np.isclose(grid_y, y0) | np.isclose(grid_y, y1)) & (grid_x >= x0 - 1) & (grid_x <= x1 + 1))
    heights[border] = ground.sample(grid_x[border], grid_y[border])
    ground.far = (xs, ys, heights)
    mesh = GroundMesh()
    mesh.add_grid(xs, ys, heights, 0, [EXTENT], False)
    data = mesh.build("terrain_far", [material], [(xs[0], xs[-1], ys[0], ys[-1])])
    far = new_object("terrain_far", data, collection)
    far["cast_shadow"] = False
    return far


SAND = np.array([0.86, 0.76, 0.55])
WET_SAND = np.array([0.62, 0.56, 0.42])
SEABED = np.array([0.50, 0.50, 0.38])
SALT_MEADOW = np.array([0.50, 0.56, 0.30])
REEDS = np.array([0.42, 0.52, 0.24])
DRY_GRASS = np.array([0.84, 0.69, 0.40])
PASTURE = np.array([0.70, 0.66, 0.34])
TRAMPLED = np.array([0.66, 0.52, 0.36])
TRACK = np.array([0.84, 0.74, 0.54])
MAQUIS = np.array([0.22, 0.32, 0.13])
GARRIGUE = np.array([0.60, 0.56, 0.32])
LIMESTONE = np.array([0.66, 0.58, 0.46])
SCREE = np.array([0.76, 0.70, 0.60])
RED_EARTH = np.array([0.70, 0.42, 0.26])
OAK_FLOOR = np.array([0.18, 0.28, 0.11])
UPLAND = np.array([0.60, 0.62, 0.30])
TRAVERTINE = np.array([0.93, 0.91, 0.84])
PATH = np.array([0.76, 0.64, 0.46])


def mix(colour, target, weight):
    return colour + (np.asarray(target) - colour) * np.asarray(weight)[..., None]


def grid_distance(points, xs, ys, reach):
    distance = np.full((len(ys), len(xs)), np.inf)
    step_x = xs[1] - xs[0]
    step_y = ys[1] - ys[0]
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        c0 = max(0, int(np.floor((min(x0, x1) - reach - xs[0]) / step_x)))
        c1 = min(len(xs), int(np.ceil((max(x0, x1) + reach - xs[0]) / step_x)) + 1)
        r0 = max(0, int(np.floor((min(y0, y1) - reach - ys[0]) / step_y)))
        r1 = min(len(ys), int(np.ceil((max(y0, y1) + reach - ys[0]) / step_y)) + 1)
        if c0 >= c1 or r0 >= r1:
            continue
        gx, gy = np.meshgrid(xs[c0:c1], ys[r0:r1])
        dx, dy = x1 - x0, y1 - y0
        t = np.clip(((gx - x0) * dx + (gy - y0) * dy) / max(dx * dx + dy * dy, 1e-9), 0, 1)
        window = distance[r0:r1, c0:c1]
        np.minimum(window, np.hypot(gx - (x0 + t * dx), gy - (y0 + t * dy)), out=window)
    return distance


def ground_pixels(relief, bounds, width, height, chunk=192):
    x0, x1, y0, y1 = bounds
    xs = x0 + (np.arange(width) + 0.5) * (x1 - x0) / width
    ys = y0 + (np.arange(height) + 0.5) * (y1 - y0) / height
    road = grid_distance(densify(chaikin(ROAD), 10.0), xs, ys, 12.0)
    path = grid_distance(densify(chaikin(ANOPAIA), 15.0), xs, ys, 10.0)
    result = np.zeros((height, width, 3))
    for start in range(0, height, chunk):
        stop = min(height, start + chunk)
        low = max(0, start - 4)
        high = min(height, stop + 4)
        block = block_pixels(relief, xs, ys[low:high], road[low:high], path[low:high], (x1 - x0) / width)
        result[start:stop] = block[start - low:start - low + stop - start]
    return result


def block_pixels(relief, xs, ys, road, path, pixel):
    grid_x, grid_y = np.meshgrid(xs, ys)
    fields = relief.evaluate(grid_x, grid_y, fields=True)
    h = fields["h"]
    if pixel < 6.0:
        reach = 6.0
        gradient_x = (relief.evaluate(grid_x + reach, grid_y) - relief.evaluate(grid_x - reach, grid_y)) / (2 * reach)
        gradient_y = (relief.evaluate(grid_x, grid_y + reach) - relief.evaluate(grid_x, grid_y - reach)) / (2 * reach)
    else:
        gradient_y, gradient_x = np.gradient(h, ys[1] - ys[0], xs[1] - xs[0])
    slope = blur(np.hypot(gradient_x, gradient_y), 2)
    shore = fields["shore"]
    land = fields["land"]
    coarse = world_noise(grid_x, grid_y, 900.0, 3)
    medium = world_noise(grid_x, grid_y, 160.0, 5)
    fine = world_noise(grid_x, grid_y, 24.0, 9, octaves=2)
    colour = np.broadcast_to(DRY_GRASS, h.shape + (3,)).copy()
    colour = mix(colour, PASTURE, smoothstep(0.42, 0.62, coarse) * 0.7)
    colour = mix(colour, GARRIGUE, smoothstep(30.0, 90.0, h) * 0.8)
    colour = mix(colour, RED_EARTH, smoothstep(0.58, 0.74, medium) * smoothstep(40, 120, h) * 0.55)
    colour = mix(colour, MAQUIS, smoothstep(0.1, 0.3, slope) * smoothstep(0.35, 0.6, medium + 0.25 * fine) * 0.8)
    colour = mix(colour, UPLAND, smoothstep(550.0, 700.0, h) * smoothstep(0.35, 0.15, slope))
    colour = mix(colour, OAK_FLOOR, smoothstep(600.0, 760.0, h) * smoothstep(0.4, 0.6, medium + 0.25 * coarse))
    colour = mix(colour, LIMESTONE, smoothstep(0.55, 1.0, slope) * smoothstep(0.25, 0.55, fine + 0.3 * medium))
    colour = mix(colour, SCREE, smoothstep(0.75, 1.2, slope) * smoothstep(0.62, 0.8, fine) * 0.6)
    colour = mix(colour, SALT_MEADOW, smoothstep(220.0, 40.0, shore) * land * smoothstep(12.0, 3.0, h) * 0.8)
    colour = mix(colour, REEDS, smoothstep(0.55, 0.75, medium) * smoothstep(90.0, 20.0, shore) * land
                 * smoothstep(3.0, 1.0, h))
    colour = mix(colour, SAND, smoothstep(14.0, 2.0, shore) * smoothstep(3.5, 1.5, h))
    river = fields["river"]
    colour = mix(colour, REEDS, smoothstep(30.0, 8.0, river) * 0.7)
    colour = mix(colour, WET_SAND, smoothstep(9.0, 4.0, river))
    ring = np.vstack([PERSIAN_CAMP, PERSIAN_CAMP[:1]])
    edge, _ = polyline_distance(ring, grid_x, grid_y)
    camp = polygon_mask(PERSIAN_CAMP, grid_x, grid_y) & land
    colour = mix(colour, TRAMPLED, camp * smoothstep(0.0, 350.0, edge) * smoothstep(0.3, 0.6, medium + 0.3 * fine)
                 * 0.75)
    colour = mix(colour, TRACK, smoothstep(5.0, 2.0, road) * 0.85)
    colour = mix(colour, PATH, smoothstep(max(2.5, pixel * 0.9), 1.0, path) * 0.85)
    for sx, sy, radius in SPRINGS:
        spring = np.hypot(grid_x - sx, grid_y - sy)
        runoff = np.hypot((grid_x - sx) / 2.5, np.maximum(grid_y - sy, 0) * 0.35 + np.minimum(grid_y - sy, 0) * 2)
        colour = mix(colour, TRAVERTINE, np.maximum(smoothstep(radius * 4, radius, spring),
                                                    smoothstep(radius * 3, radius, runoff) * 0.8))
    colour = mix(colour, SEABED, ~land * smoothstep(0.2, -1.5, h))
    colour *= (0.86 + 0.18 * fine)[..., None]
    return np.clip(colour, 0, 1)


def ground_materials(relief, work_dir, sizes):
    materials = []
    for name, bounds, (width, height) in (("terrain_ring", EXTENT, sizes[0]), ("terrain_core", CORE, sizes[1]),
                                         ("terrain_pass", PASS, sizes[2])):
        pixels = ground_pixels(relief, bounds, width, height)
        image = save_pixels(name, pixels, os.path.join(work_dir, f"{name}.jpg"), quality=92)
        materials.append(baked_material(name, image, roughness=0.96))
    return materials


def far_material(relief, work_dir):
    return principled_material("terrain_far", color=(0.40, 0.38, 0.22), roughness=0.97, vertex_color=False)


def clip_wet(points):
    result = []
    for index, (x, y, h) in enumerate(points):
        nx, ny, nh = points[(index + 1) % len(points)]
        if h < 0:
            result.append((x, y))
        if (h < 0) != (nh < 0):
            t = h / (h - nh)
            result.append((x + (nx - x) * t, y + (ny - y) * t))
    return result


def wet_mesh(name, xs, ys, heights, holes):
    grid_x, grid_y = np.meshgrid(xs, ys)
    centre_x = (grid_x[:-1, :-1] + grid_x[:-1, 1:]) / 2
    centre_y = (grid_y[:-1, :-1] + grid_y[1:, :-1]) / 2
    keep = np.ones(centre_x.shape, bool)
    for hole in holes:
        keep &= ~inside(hole, centre_x, centre_y)
    corners = [heights[:-1, :-1], heights[:-1, 1:], heights[1:, 1:], heights[1:, :-1]]
    wet = keep & (np.maximum.reduce(corners) < 0)
    mixed = keep & ~wet & (np.minimum.reduce(corners) < 0)
    vertices = []
    faces = []
    for row, column in zip(*np.nonzero(wet)):
        start = len(vertices)
        vertices += [(xs[column], ys[row]), (xs[column + 1], ys[row]), (xs[column + 1], ys[row + 1]),
                     (xs[column], ys[row + 1])]
        faces.append(tuple(range(start, start + 4)))
    for row, column in zip(*np.nonzero(mixed)):
        quad = [(xs[column], ys[row], heights[row, column]), (xs[column + 1], ys[row], heights[row, column + 1]),
                (xs[column + 1], ys[row + 1], heights[row + 1, column + 1]),
                (xs[column], ys[row + 1], heights[row + 1, column])]
        for triangle in ((quad[0], quad[1], quad[2]), (quad[0], quad[2], quad[3])):
            polygon = clip_wet(triangle)
            if len(polygon) >= 3:
                start = len(vertices)
                vertices += polygon
                faces.append(tuple(range(start, start + len(polygon))))
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata([(x, y, SEA_LEVEL) for x, y in vertices], [], faces)
    work = bmesh.new()
    work.from_mesh(mesh)
    bmesh.ops.remove_doubles(work, verts=work.verts, dist=0.01)
    bmesh.ops.dissolve_limit(work, angle_limit=0.01, verts=work.verts, edges=work.edges)
    work.to_mesh(mesh)
    work.free()
    mesh.update()
    return mesh


def water_surfaces(relief, ground, collection, new_object):
    sea_material = principled_material("sea", color=(0.04, 0.20, 0.30), roughness=0.08, vertex_color=False)
    river_material = principled_material("river", color=(0.12, 0.24, 0.22), roughness=0.12, vertex_color=False)
    rivers = []
    children = {EXTENT: [CORE], CORE: [PASS, *GATES]}
    layers = [(bounds, *level_grid(bounds, spacing), heights, children.get(bounds, []))
              for bounds, spacing, heights in ground.levels]
    layers.append((None, *ground.far, [EXTENT]))
    for index, (bounds, xs, ys, heights, holes) in enumerate(layers):
        name = "sea" if index == 0 else f"sea_{index}"
        mesh = wet_mesh(name, xs, ys, heights, holes)
        mesh.materials.append(sea_material)
        sea = new_object(name, mesh, collection)
        sea["cast_shadow"] = False
        rivers.append(sea)
    for name, width in (("asopos", 12.0), ("melas", 10.0)):
        path, level = relief.river(name)
        tangents = np.gradient(path, axis=0)
        tangents /= np.linalg.norm(tangents, axis=1)[:, None]
        normals = np.column_stack([-tangents[:, 1], tangents[:, 0]])
        left = path + normals * width / 2
        right = path - normals * width / 2
        count = len(path)
        vertices = [(*left[k], level[k]) for k in range(count)] + [(*right[k], level[k]) for k in range(count)]
        faces = [(k, k + 1, count + k + 1, count + k) for k in range(count - 1)]
        mesh = bpy.data.meshes.new(name)
        mesh.from_pydata(vertices, [], faces)
        mesh.materials.append(river_material)
        stream = new_object(name, mesh, collection)
        stream["cast_shadow"] = False
        rivers.append(stream)
    return rivers


def scatter(relief, ground, bounds, spacing, seed, rule):
    generator = np.random.default_rng(seed)
    x0, x1, y0, y1 = bounds
    xs = np.arange(x0 + spacing / 2, x1, spacing)
    ys = np.arange(y0 + spacing / 2, y1, spacing)
    grid_x, grid_y = np.meshgrid(xs, ys)
    x = (grid_x + generator.uniform(-0.45, 0.45, grid_x.shape) * spacing).ravel()
    y = (grid_y + generator.uniform(-0.45, 0.45, grid_y.shape) * spacing).ravel()
    fields = relief.evaluate(x, y, fields=True)
    probe = 6.0
    east = relief.evaluate(x + probe, y)
    north = relief.evaluate(x, y + probe)
    fields["slope"] = np.hypot(east - fields["h"], north - fields["h"]) / probe
    fields["noise"] = world_noise(x, y, 260.0, seed)
    fields["random"] = generator.random(len(x))
    chosen = rule(x, y, fields)
    z = ground.sample(x[chosen], y[chosen])
    return np.column_stack([x[chosen], y[chosen], z])
