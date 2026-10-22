import math
import random

import numpy as np

from . import acropole_plan as plan
from .acropole_terrain import outline_distance, world_noise
from .buildings import cypress, lobe, plane_tree, trunk
from .geometry import MeshBuilder, placement
from .greek_materials import TERRACOTTA
from .terrain import point_in_polygon, polyline_distance

PLASTER = "plaster"
ASHLAR = "ashlar"
WOOD = "dark_wood"
SAIL = "velum_linen"
WALL_TONES = [(1.0, 0.98, 0.94), (0.97, 0.9, 0.78), (0.93, 0.84, 0.7), (0.98, 0.93, 0.86), (0.9, 0.8, 0.66),
              (1.0, 0.96, 0.9)]
ROOF_TONES = [(1.0, 1.0, 1.0), (0.92, 0.84, 0.8), (1.04, 0.92, 0.82), (0.86, 0.76, 0.7), (0.97, 0.88, 0.78)]
EARTH_ROOF = (0.66, 0.56, 0.44)
CELL = 27.0
PIRAEUS = [(-8700.0, -3500.0), (-8200.0, -3150.0), (-7500.0, -3100.0), (-6700.0, -3050.0), (-6000.0, -3250.0),
           (-5800.0, -3700.0), (-6000.0, -4150.0), (-6700.0, -4400.0), (-7600.0, -4700.0), (-8500.0, -4500.0)]
CLEAR_CIRCLES = [((-283.0, 90.0), 85.0), ((-640.0, -15.0), 150.0), ((-392.0, -444.0), 110.0), ((-453.0, 449.0), 55.0),
                 ((574.0, -236.0), 95.0), ((-146.0, 194.0), 32.0), ((-245.0, 269.0), 18.0), ((-668.0, 775.0), 40.0),
                 ((-560.0, 250.0), 60.0)]
CLEAR_BOXES = [(30.0, 260.0, -215.0, -40.0)]


def road_lines():
    from .acropole_monuments import RAMP
    return [
        [(-668.0, 775.0), (-560.0, 680.0), (-450.0, 600.0), (-400.0, 560.0), (-320.0, 470.0), (-245.0, 340.0),
         (-200.0, 270.0), (-146.0, 194.0), (-180.0, 125.0), (-222.0, 62.0), (-240.0, 22.0), (RAMP[0], RAMP[1])],
        [(-668.0, 775.0), (-1100.0, 1150.0), (-1700.0, 1700.0), (-2400.0, 2300.0), (-3200.0, 2900.0)],
        [(-960.0, -330.0), (-1700.0, -700.0), (-2600.0, -1170.0), (-3700.0, -1760.0), (-4850.0, -2400.0),
         (-5850.0, -2950.0), (-6450.0, -3250.0)],
        [(-700.0, -760.0), (-1000.0, -1450.0), (-1250.0, -2050.0), (-1450.0, -2750.0), (-1700.0, -3450.0)],
        [(1150.0, 300.0), (2000.0, 150.0), (3000.0, -50.0), (4500.0, -400.0)],
        [(-450.0, 600.0), (-200.0, 760.0), (150.0, 900.0), (450.0, 1050.0)],
        [(-146.0, 194.0), (150.0, 300.0), (500.0, 380.0), (1150.0, 300.0)],
        [(-320.0, 470.0), (-600.0, 300.0), (-900.0, 120.0)],
    ]


def tinted(builder, colour, action):
    first = len(builder.polygons)
    action()
    builder.tint(first, colour)


def pent(builder, x0, x1, y_high, y_low, z_high, z_low, material, colour):
    corners = [(x0, y_high, z_high), (x1, y_high, z_high), (x1, y_low, z_low), (x0, y_low, z_low)]
    normal = (0.0, y_low - y_high, abs(y_low - y_high))
    tinted(builder, colour, lambda: builder.oriented(corners, normal, material))
    for x, side in ((x0, -1), (x1, 1)):
        tinted(builder, colour, lambda x=x, side=side: builder.oriented(
            [(x, y_high, z_high), (x, y_low, z_low), (x, y_low, z_high)], (side, 0, 0), material))


def wing(builder, x0, x1, y0, y1, height, wall, roof, roof_colour, facing):
    tinted(builder, wall, lambda: builder.box((x0, y0, -5.0), (x1, y1, height), PLASTER, bottom=False, top=False))
    if facing == "south":
        pent(builder, x0 - 0.3, x1 + 0.3, y1 + 0.3, y0 - 0.5, height + 0.7, height - 0.05, roof, roof_colour)
    elif facing == "east":
        corners = [(x0 - 0.3, y0 - 0.3, height + 0.7), (x0 - 0.3, y1 + 0.3, height + 0.7), (x1 + 0.5, y1 + 0.3, height),
                   (x1 + 0.5, y0 - 0.3, height)]
        tinted(builder, roof_colour, lambda: builder.oriented(corners, (1, 0, 1), roof))
    else:
        tinted(builder, roof_colour, lambda: builder.oriented(
            [(x0 - 0.2, y0 - 0.2, height + 0.15), (x1 + 0.2, y0 - 0.2, height + 0.15), (x1 + 0.2, y1 + 0.2, height + 0.15),
             (x0 - 0.2, y1 + 0.2, height + 0.15)], (0, 0, 1), PLASTER))


def house_unit(builder, rng, x0, y0, width, depth, far=False):
    wall = rng.choice(WALL_TONES)
    flat = rng.random() < 0.3
    roof = PLASTER if (flat or far) else TERRACOTTA
    roof_colour = EARTH_ROOF if flat else (rng.choice(ROOF_TONES) if not far else (0.72, 0.42, 0.28))
    north = rng.uniform(4.3, 5.6)
    tall = rng.choice((3.4, 3.6, 3.9, 6.0, 6.4))
    x1, y1 = x0 + width, y0 + depth
    wing(builder, x0, x1, y1 - north, y1, tall, wall, roof, roof_colour, "flat" if flat else "south")
    if rng.random() < 0.75:
        wing(builder, x0, x0 + rng.uniform(3.6, 4.6), y0, y1 - north, rng.choice((3.2, 3.5)), wall, roof, roof_colour,
             "flat" if flat else "east")
    if far:
        return
    tinted(builder, wall, lambda: builder.box((x0, y0, -5.0), (x1, y0 + 0.45, 2.5), PLASTER, bottom=False))
    tinted(builder, wall, lambda: builder.box((x1 - 0.45, y0 + 0.45, -5.0), (x1, y1 - north, 2.5), PLASTER,
                                              bottom=False))
    door = x0 + width * rng.uniform(0.3, 0.7)
    builder.oriented([(door - 0.6, y0 - 0.02, 0.0), (door + 0.6, y0 - 0.02, 0.0), (door + 0.6, y0 - 0.02, 2.1),
                      (door - 0.6, y0 - 0.02, 2.1)], (0, -1, 0), "shadow_void")


def cluster(seed, far=False):
    rng = random.Random(seed)
    builder = MeshBuilder()
    half = CELL / 2 - 1.6
    split_x = rng.uniform(-2.0, 2.0)
    split_y = rng.uniform(-2.0, 2.0)
    for x0, x1 in ((-half, split_x), (split_x, half)):
        for y0, y1 in ((-half, split_y), (split_y, half)):
            if rng.random() < 0.12:
                continue
            house_unit(builder, rng, x0, y0, x1 - x0 - 0.2, y1 - y0 - 0.2, far)
    return builder


def ship(kind="merchant"):
    builder = MeshBuilder()
    if kind == "trireme":
        length, beam, height = 36.0, 5.0, 2.4
    else:
        length, beam, height = 18.0, 6.0, 3.0
    half = length / 2
    rows = []
    for k in range(9):
        t = k / 8
        y = -half + length * t
        width = beam / 2 * math.sin(math.pi * (0.08 + 0.84 * t)) ** 0.7
        rows.append([(-width, y, height), (-width * 0.7, y, 0.6), (0.0, y, -0.4), (width * 0.7, y, 0.6),
                     (width, y, height)])
    tinted(builder, (0.42, 0.30, 0.20), lambda: builder.surface(rows, WOOD, facing=(0, 0, -1)))
    tinted(builder, (0.42, 0.30, 0.20), lambda: builder.surface(list(reversed(rows)), WOOD, facing=(0, 0, 1)))
    tinted(builder, (0.55, 0.42, 0.28), lambda: builder.box((-beam * 0.36, -half * 0.8, height - 0.6),
                                                            (beam * 0.36, half * 0.8, height - 0.4), WOOD))
    if kind == "trireme":
        tinted(builder, (0.1, 0.1, 0.12), lambda: builder.box((-beam / 2 - 0.05, -half * 0.75, 1.0),
                                                              (beam / 2 + 0.05, half * 0.75, 1.8), WOOD))
        for side in (-1, 1):
            for k in range(30):
                y = -half * 0.7 + k * (1.4 * half / 30)
                tinted(builder, (0.6, 0.5, 0.36), lambda y=y, side=side: builder.box(
                    (side * (beam / 2), y - 0.04, 1.2), (side * (beam / 2 + 3.2), y + 0.04, 1.28), WOOD))
        tinted(builder, (0.6, 0.6, 0.6), lambda: builder.box((-0.3, half - 0.2, -0.2), (0.3, half + 2.2, 0.6), WOOD))
        mast, sail = 10.0, (8.0, 6.0)
    else:
        mast, sail = 13.0, (11.0, 8.0)
    tinted(builder, (0.45, 0.33, 0.22), lambda: builder.box((-0.15, -0.15, 0.5), (0.15, 0.15, mast), WOOD))
    width, tall = sail
    builder.polygon([(-width / 2, 0.4, mast - 0.6 - tall), (width / 2, 0.4, mast - 0.6 - tall),
                     (width / 2, 0.4, mast - 0.6), (-width / 2, 0.4, mast - 0.6)], SAIL, color=(0.96, 0.92, 0.82))
    return builder


def ancient_olive(height=5.0, seed=2):
    builder = MeshBuilder()
    r = height * 0.33
    trunk(builder, height * 0.5, 0.2, (0.35, 0.1))
    lobe(builder, (0.45, 0.2, height * 0.62), r, height * 0.5, "foliage_olive", 6, seed, 0.1)
    lobe(builder, (-0.5, -0.35, height * 0.52), r * 0.8, height * 0.4, "foliage_olive", 5, seed + 3, 0.1)
    return builder


def shipshed():
    builder = MeshBuilder()
    tinted(builder, (0.95, 0.9, 0.8), lambda: builder.box((-3.2, -20.0, -3.0), (3.2, 20.0, 4.0), PLASTER,
                                                          bottom=False, top=False))
    builder.oriented([(-3.2, -20.02, -1.0), (3.2, -20.02, -1.0), (3.2, -20.02, 3.2), (-3.2, -20.02, 3.2)], (0, -1, 0),
                     "shadow_void")
    for side in (-1, 1):
        tinted(builder, (0.9, 0.8, 0.74), lambda side=side: builder.oriented(
            [(side * 3.5, -20.3, 3.9), (side * 3.5, 20.3, 3.9), (0.0, 20.3, 5.4), (0.0, -20.3, 5.4)], (side, 0, 1),
            TERRACOTTA))
    return builder


def far_tree():
    builder = MeshBuilder()
    lobe(builder, (0.0, 0.0, 2.6), 2.4, 3.4, "foliage_dark", 5, 1, 0.2)
    return builder


def sweep_wall(scene, points, spacing, height, thickness, rng, tower_every=0.0, closed=False):
    path = points + points[:1] if closed else points
    dense = []
    for (x0, y0), (x1, y1) in zip(path[:-1], path[1:]):
        count = max(int(math.hypot(x1 - x0, y1 - y0) / spacing), 1)
        for k in range(count):
            dense.append((x0 + (x1 - x0) * k / count, y0 + (y1 - y0) * k / count))
    dense.append(path[-1])
    lifted = [(x, y, scene.ground.surface(x, y)) for x, y in dense]
    builder = MeshBuilder()
    profile = [(thickness / 2, -5.0), (thickness / 2, height), (-thickness / 2, height), (-thickness / 2, -5.0)]
    builder.sweep(lifted, profile, ASHLAR)
    builder.tint(0, (0.94, 0.88, 0.78))
    towers = []
    if tower_every > 0:
        walked = 0.0
        next_tower = tower_every / 2
        for a, b in zip(lifted[:-1], lifted[1:]):
            length = math.hypot(b[0] - a[0], b[1] - a[1])
            while walked + length >= next_tower:
                t = (next_tower - walked) / length
                x, y = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
                angle = math.atan2(b[1] - a[1], b[0] - a[0])
                towers.append(placement(x, y, scene.ground.surface(x, y), angle))
                next_tower += tower_every * rng.uniform(0.85, 1.15)
            walked += length
    return builder, towers, lifted


def tower():
    builder = MeshBuilder()
    builder.box((-3.2, -3.2, -5.0), (3.2, 3.2, 10.5), ASHLAR, bottom=False)
    builder.tint(0, (0.92, 0.86, 0.76))
    return builder


def walls(scene):
    rng = random.Random(97)
    info = {}
    towers = []
    for name, points, closed in (("enceinte", plan.CITY_WALL, True), ("long_mur_nord", plan.LONG_WALL_NORTH, False),
                                 ("long_mur_milieu", plan.LONG_WALL_MIDDLE, False),
                                 ("mur_de_phalere", plan.PHALERIC_WALL, False)):
        points = list(points)
        if closed:
            start = points.index((-680.0, 790.0))
            points = points[start:] + points[:start]
            gap = [(-668.0 + 24.0, 775.0 + 30.0)]
            points = gap + points[1:] + [(-668.0 - 22.0, 775.0 - 24.0)]
        builder, placed, lifted = sweep_wall(scene, points, 18.0 if closed else 30.0, 8.0 if closed else 7.5,
                                             3.2 if closed else 3.0, rng, 55.0 if closed else 75.0, False)
        scene.unique("ville", builder)
        towers.extend(placed)
        info[name] = {"length": round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(lifted[:-1],
                                                                                                 lifted[1:]))),
                      "towers": len(placed)}
    for x, y in ((-668.0 + 30.0, 775.0 + 36.0), (-668.0 - 28.0, 775.0 - 30.0)):
        towers.append(placement(x, y, scene.ground.surface(x, y), 0.7))
    scene.instances("ville", "tour", tower, towers)
    return info


def exclusion(x, y, near_signed):
    if near_signed < 55.0:
        return True
    for (cx, cy), radius in CLEAR_CIRCLES:
        if math.hypot(x - cx, y - cy) < radius:
            return True
    for x0, x1, y0, y1 in CLEAR_BOXES:
        if x0 <= x <= x1 and y0 <= y <= y1:
            return True
    return point_in_polygon(x, y, [(-410.0, 325.0), (-235.0, 315.0), (-225.0, 545.0), (-390.0, 548.0)])


def houses(scene, eyes):
    ground = scene.ground
    near = ground.near
    xs = np.arange(-1250.0, 1250.0, CELL)
    ys = np.arange(-950.0, 1300.0, CELL)
    gx, gy = np.meshgrid(xs, ys)
    jitter = np.random.default_rng(5)
    gx = gx + jitter.uniform(-2.5, 2.5, gx.shape)
    gy = gy + jitter.uniform(-2.5, 2.5, gy.shape)
    inside = np.array([point_in_polygon(x, y, plan.CITY_WALL) for x, y in zip(gx.ravel(), gy.ravel())])
    signed = outline_distance(plan.ACROPOLIS_OUTLINE, gx.ravel(), gy.ravel())
    roads = road_lines()
    road_distance = np.min([polyline_distance(points, gx.ravel(), gy.ravel()) for points in roads], axis=0)
    river_distance = np.min([polyline_distance(points, gx.ravel(), gy.ravel()) for points in ground.city.rivers.values()],
                            axis=0)
    angle_noise = world_noise(gx.ravel(), gy.ravel(), 260.0, 71, 2)
    gaps = world_noise(gx.ravel(), gy.ravel(), 40.0, 73, 2)
    slope_field = ground.city.slope()
    slopes = sample_grid(ground.city, slope_field, gx.ravel(), gy.ravel())
    near_matrices = {k: [] for k in range(12)}
    far_matrices = {k: [] for k in range(4)}
    rng = random.Random(13)
    for index, (x, y) in enumerate(zip(gx.ravel(), gy.ravel())):
        if not inside[index] or road_distance[index] < 17.0 or river_distance[index] < 18.0:
            continue
        if slopes[index] > 0.22 or gaps[index] < 0.3 or exclusion(x, y, signed[index]):
            continue
        if any(math.hypot(x - ex, y - ey) < 22.0 for ex, ey in eyes):
            continue
        angle = math.radians(8.0 + 30.0 * (angle_noise[index] - 0.5))
        corners = [(x + 12.0 * c, y + 12.0 * s) for c, s in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
        heights = [ground(cx, cy) for cx, cy in corners]
        z = min(heights) + 0.3 * (max(heights) - min(heights))
        matrix = placement(x, y, z, angle + rng.choice((0.0, math.pi / 2, math.pi, -math.pi / 2)))
        if near.contains(x, y, 30.0):
            near_matrices[rng.randrange(12)].append(matrix)
        else:
            far_matrices[rng.randrange(4)].append(matrix)
    return near_matrices, far_matrices


def sample_grid(field, values, xs, ys):
    column = np.clip(np.round((xs - field.cx + field.half) / field.spacing).astype(int), 0, field.count - 1)
    row = np.clip(np.round((ys - field.cy + field.half) / field.spacing).astype(int), 0, field.count - 1)
    return values[row, column]


def region_houses(scene, polygon, angle, cell, density, seed):
    ground = scene.ground
    rng = random.Random(seed)
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    matrices = {k: [] for k in range(4)}
    cos, sin = math.cos(angle), math.sin(angle)
    span = max(max(xs) - min(xs), max(ys) - min(ys))
    cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
    steps = int(span / cell) + 2
    for i in range(-steps, steps):
        for j in range(-steps, steps):
            x = cx + i * cell * cos - j * cell * sin
            y = cy + i * cell * sin + j * cell * cos
            if not point_in_polygon(x, y, polygon) or rng.random() > density:
                continue
            z = ground(x, y)
            if z < 2.0 or abs(ground(x + 12.0, y) - ground(x - 12.0, y)) > 7.0:
                continue
            matrices[rng.randrange(4)].append(placement(x, y, min(z, ground(x + 10, y + 10), ground(x - 10, y - 10)),
                                                        angle))
    return matrices


def trees(scene, eyes):
    ground = scene.ground
    rng = np.random.default_rng(31)
    near_trees = {"olivier": [], "cypres": [], "platane": []}
    far_trees = []
    for points in ground.city.rivers.values():
        for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
            if rng.random() < 0.55:
                continue
            t = rng.random()
            x = x0 + (x1 - x0) * t + rng.uniform(-14.0, 14.0)
            y = y0 + (y1 - y0) * t + rng.uniform(-14.0, 14.0)
            if ground(x, y) < 1.5:
                continue
            key = "platane" if ground.near.contains(x, y, 20.0) or math.hypot(x, y) < 3500 else None
            if key:
                near_trees[key].append(placement(x, y, ground.surface(x, y) - 0.2, rng.uniform(0, 6.28)))
    count = 0
    attempts = 0
    while count < 2600 and attempts < 40000:
        attempts += 1
        x, y = rng.uniform(-5200.0, 2600.0), rng.uniform(-2600.0, 4200.0)
        if point_in_polygon(x, y, plan.CITY_WALL):
            continue
        if point_in_polygon(x, y, [(-1100.0, -150.0), (-6600.0, -3100.0), (-6500.0, -3450.0), (-850.0, -500.0)]):
            continue
        noise = world_noise(np.array(x), np.array(y), 9.0, 12, 2)
        parcel_noise = world_noise(np.array(x), np.array(y), 600.0, 8, 2)
        if parcel_noise < 0.45:
            continue
        z = ground(x, y)
        if z < 2.0 or z > 260.0:
            continue
        if any(math.hypot(x - ex, y - ey) < 25.0 for ex, ey in eyes):
            continue
        count += 1
        if math.hypot(x + 300.0, y - 300.0) < 2200.0:
            near_trees["olivier"].append(placement(x, y, ground.surface(x, y) - 0.2, rng.uniform(0, 6.28),
                                                   rng.uniform(0.8, 1.2)))
        else:
            far_trees.append(placement(x, y, ground(x, y) - 0.3, rng.uniform(0, 6.28), rng.uniform(0.8, 1.2)))
    for x, y in ((-700.0, 820.0), (-760.0, 760.0), (-740.0, 840.0), (-800.0, 800.0), (-690.0, 900.0),
                 (-820.0, 720.0), (-150.0, 230.0), (-120.0, 170.0), (60.0, -170.0), (150.0, -175.0), (520.0, -330.0)):
        near_trees["cypres"].append(placement(x, y, ground.surface(x, y) - 0.2, rng.uniform(0, 6.28),
                                              rng.uniform(0.8, 1.15)))
    return near_trees, far_trees


def ships(scene):
    rng = random.Random(53)
    merchant, trireme = [], []
    spots = [(-7650.0, -3500.0, 40), (-6900.0, -3900.0, 10), (-6050.0, -3950.0, 8), (-2600.0, -3900.0, 6),
             (-4000.0, -4600.0, 4), (-9500.0, -4200.0, 3), (-5000.0, -6000.0, 3)]
    for x0, y0, count in spots:
        for k in range(count):
            for attempt in range(20):
                x = x0 + rng.uniform(-350.0, 350.0)
                y = y0 + rng.uniform(-250.0, 250.0)
                if scene.ground(x, y) < -2.5 and scene.ground(x + 20.0, y) < -1.5 and scene.ground(x - 20.0, y) < -1.5:
                    matrix = placement(x, y, 0.0, rng.uniform(0, 6.28))
                    (trireme if rng.random() < 0.3 else merchant).append(matrix)
                    break
    scene.instances("mer", "navire_marchand", lambda: ship("merchant"), merchant, cast_shadow=False)
    scene.instances("mer", "triere", lambda: ship("trireme"), trireme, cast_shadow=False)
    return {"merchant": len(merchant), "trireme": len(trireme)}


def shipsheds(scene):
    ground = scene.ground
    sheds = []
    for (cx, cy), count, start, sweep in (((-6860.0, -3840.0), 26, 0.0, 360.0), ((-5890.0, -3920.0), 14, 120.0, 220.0)):
        for k in range(count):
            angle = math.radians(start + sweep * (k + 0.5) / count)
            dx, dy = math.cos(angle), math.sin(angle)
            shore = None
            for step in range(4, 120):
                if ground(cx + dx * step * 5.0, cy + dy * step * 5.0) > 1.0:
                    shore = step * 5.0
                    break
            if shore is None:
                continue
            x, y = cx + dx * (shore + 14.0), cy + dy * (shore + 14.0)
            sheds.append(placement(x, y, max(ground(x, y), 0.4), angle - math.pi / 2))
    scene.instances("ville_loin", "loge_trieres", shipshed, sheds, cast_shadow=False)
    return len(sheds)


def rivers(scene):
    info = {}
    builder = MeshBuilder()
    widths = {"ilissos": 3.5, "eridanos": 2.5, "cephise": 7.0}
    for name, points in scene.ground.city.rivers.items():
        dense = []
        for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
            count = max(int(math.hypot(x1 - x0, y1 - y0) / 8.0), 1)
            for k in range(count):
                dense.append((x0 + (x1 - x0) * k / count, y0 + (y1 - y0) * k / count))
        dense.append(points[-1])
        lifted = [(x, y, scene.ground.surface(x, y) + 0.15) for x, y in dense]
        half = widths[name] / 2
        builder.sweep(lifted, [(-half, 0.0), (half, 0.0)], "river", caps=False)
        info[name] = len(lifted)
    scene.unique("eau", builder, occlusion=False)
    scene.shadowless.add("eau")
    return info


def build(scene):
    from .acropole_life import eye_points
    eyes = eye_points()
    info = {"murs": walls(scene)}
    near_houses, far_houses = houses(scene, eyes)
    for key, matrices in near_houses.items():
        scene.instances("ville", f"maison_{key}", lambda key=key: cluster(100 + key), matrices)
    piraeus = region_houses(scene, PIRAEUS, math.radians(18.0), 30.0, 0.72, 19)
    phaleron = region_houses(scene, [(-2000.0, -3550.0), (-1500.0, -3500.0), (-1450.0, -3800.0), (-1950.0, -3850.0)],
                             math.radians(-20.0), 32.0, 0.5, 23)
    for key in far_houses:
        matrices = far_houses[key] + piraeus[key] + phaleron[key]
        scene.instances("ville_loin", f"maison_loin_{key}", lambda key=key: cluster(200 + key, True), matrices,
                        cast_shadow=False)
    scene.shadowless.add("ville_loin")
    near_trees, far_trees = trees(scene, eyes)
    builds = {"olivier": ancient_olive, "cypres": lambda: cypress(11.0, 4),
              "platane": lambda: plane_tree(15.0, 5)}
    for key, matrices in near_trees.items():
        scene.instances("vegetation", f"arbre_{key}", builds[key], matrices, occlusion=False)
    scene.instances("vegetation", "arbre_loin", far_tree, far_trees, cast_shadow=False, occlusion=False)
    info["maisons"] = {"proches": sum(len(v) for v in near_houses.values()),
                       "lointaines": sum(len(v) for v in far_houses.values()),
                       "piree": sum(len(v) for v in piraeus.values()), "phalere": sum(len(v) for v in phaleron.values())}
    info["arbres"] = {key: len(v) for key, v in near_trees.items()}
    info["arbres"]["loin"] = len(far_trees)
    info["navires"] = ships(scene)
    info["loges"] = shipsheds(scene)
    info["rivieres"] = rivers(scene)
    return info
