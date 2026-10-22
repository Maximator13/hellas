import math
import random

import numpy as np
from mathutils import Matrix, Vector

from . import greek
from . import phare_plan as plan
from .acropole_city import shipshed
from .buildings import lobe, trunk
from .geometry import MeshBuilder, placement
from .terrain import point_in_polygon

PLASTER = "plaster"
LAMP = "lamp_glow"
FLAME = "flame"
VOID = "shadow_void"
WALLS = [(0.95, 0.91, 0.82), (0.9, 0.83, 0.7), (0.97, 0.95, 0.9), (0.86, 0.77, 0.63), (0.92, 0.86, 0.74)]
MUD_WALLS = [(0.66, 0.55, 0.42), (0.72, 0.6, 0.46), (0.6, 0.5, 0.38)]
ROOFS = [(0.74, 0.67, 0.55), (0.8, 0.74, 0.62), (0.68, 0.6, 0.48)]
CHUNK = (44.0, 40.0)
PALM = (0.22, 0.30, 0.14)


def painted(builder, colour, action):
    first = len(builder.polygons)
    action()
    builder.tint(first, colour)


def quad(builder, corners, normal, material, colour=None):
    first = len(builder.polygons)
    builder.oriented([Vector(c) for c in corners], normal, material)
    if colour is not None:
        builder.tint(first, colour)


def facade_openings(builder, rng, x0, x1, y, facing, height, lit, upper):
    width = x1 - x0
    count = max(1, int(width / 4.5))
    for k in range(count):
        u = x0 + width * (k + 0.5) / count + rng.uniform(-0.6, 0.6)
        for z0 in ((1.4, 4.9) if upper else (1.4,)):
            if z0 + 1.1 > height - 0.3:
                continue
            glowing = lit[0] > 0 and rng.random() < 0.5
            material = LAMP if glowing else VOID
            if glowing:
                lit[0] -= 1
            w = 0.7 if glowing else 0.8
            quad(builder, [(u - w / 2, y + facing * 0.03, z0), (u + w / 2, y + facing * 0.03, z0),
                           (u + w / 2, y + facing * 0.03, z0 + 1.0), (u - w / 2, y + facing * 0.03, z0 + 1.0)],
                 (0, facing, 0), material)


def wing(builder, rng, x0, y0, x1, y1, height, wall, roof, lit, faces):
    painted(builder, wall, lambda: builder.box((x0, y0, -1.5), (x1, y1, height), PLASTER, bottom=False, top=False))
    quad(builder, [(x0, y0, height), (x1, y0, height), (x1, y1, height), (x0, y1, height)], (0, 0, 1), PLASTER, roof)
    upper = height > 6.0
    if "south" in faces:
        facade_openings(builder, rng, x0, x1, y0, -1, height, lit, upper)
    if "north" in faces:
        facade_openings(builder, rng, x0, x1, y1, 1, height, lit, upper)


def house_chunk(seed, mud=False, lights=3, courts=0.35, roofs=0.2):
    rng = random.Random(seed)
    builder = MeshBuilder()
    half_x, half_y = CHUNK[0] / 2, CHUNK[1] / 2
    lit = [lights]
    splits = sorted(rng.uniform(-half_x + 9, half_x - 9) for _ in range(rng.choice((1, 2))))
    xs = [-half_x] + splits + [half_x]
    for x0, x1 in zip(xs[:-1], xs[1:]):
        for y0, y1, outer in ((-half_y, 0.0, "south"), (0.0, half_y, "north")):
            if rng.random() < 0.1:
                continue
            a, b = x0 + 0.25, x1 - 0.25
            c, d = y0 + 0.25, y1 - 0.25
            wall = rng.choice(MUD_WALLS if mud else WALLS)
            roof = rng.choice(ROOFS)
            tall = rng.choice((3.6, 4.2) if mud else (4.2, 4.6, 7.6, 8.2))
            depth = rng.uniform(5.5, 8.0)
            side = rng.uniform(4.0, 6.0)
            if outer == "north":
                wing(builder, rng, a, d - depth, b, d, tall, wall, roof, lit, ("north",))
                if rng.random() < 0.7:
                    wing(builder, rng, a, c, a + side, d - depth, min(tall, 4.4), wall, roof, lit, ())
                court = ((a + side + b) / 2, (c + d - depth) / 2)
            else:
                wing(builder, rng, a, c, b, c + depth, tall, wall, roof, lit, ("south",))
                if rng.random() < 0.7:
                    wing(builder, rng, b - side, c + depth, b, d, min(tall, 4.4), wall, roof, lit, ())
                court = ((a + b - side) / 2, (c + depth + d) / 2)
            if rng.random() < courts:
                x, y = court
                quad(builder, [(x - 1.6, y - 1.6, 0.2), (x + 1.6, y - 1.6, 0.2), (x + 1.6, y + 1.6, 0.2),
                               (x - 1.6, y + 1.6, 0.2)], (0, 0, 1), LAMP)
            if rng.random() < roofs:
                x = rng.uniform(a + 1.5, b - 1.5)
                y = d - depth / 2 if outer == "north" else c + depth / 2
                quad(builder, [(x - 1.3, y - 1.3, tall + 0.15), (x + 1.3, y - 1.3, tall + 0.15),
                               (x + 1.3, y + 1.3, tall + 0.15), (x - 1.3, y + 1.3, tall + 0.15)], (0, 0, 1), LAMP)
    return builder


def lamp_post(height=2.4):
    builder = MeshBuilder()
    painted(builder, (0.3, 0.22, 0.16), lambda: builder.box((-0.07, -0.07, -0.2), (0.07, 0.07, height), "dark_wood",
                                                            bottom=False))
    builder.lathe([(0.16, 0.0), (0.12, 0.25), (0.05, 0.5), (0.0, 0.62)], 6, FLAME, smooth=True,
                  matrix=Matrix.Translation((0.0, 0.0, height)))
    return builder


def palm(height=12.0, seed=0):
    rng = random.Random(seed)
    builder = MeshBuilder()
    lean = Vector((rng.uniform(-0.6, 0.6), rng.uniform(-0.6, 0.6), 0.0))
    path = [Vector((0.0, 0.0, -0.3)), lean * 0.3 + Vector((0.0, 0.0, height * 0.5)), lean + Vector((0.0, 0.0, height))]
    from .figures import tube
    tube(builder, path, [0.3, 0.24, 0.2], [(0.42, 0.34, 0.24), (0.46, 0.38, 0.28)], 5, cap=False)
    top = path[-1]
    for k in range(8):
        angle = 2 * math.pi * k / 8 + rng.uniform(-0.2, 0.2)
        direction = Vector((math.cos(angle), math.sin(angle), 0.0))
        side = Vector((-direction.y, direction.x, 0.0))
        length = rng.uniform(3.6, 4.6)
        rise = rng.uniform(0.6, 1.4)
        points = [top, top + direction * length * 0.5 + Vector((0, 0, rise)),
                  top + direction * length + Vector((0, 0, rise - 1.8))]
        widths = [0.15, 0.75, 0.1]
        for (p0, w0), (p1, w1) in zip(zip(points[:-1], widths[:-1]), zip(points[1:], widths[1:])):
            corners = [p0 - side * w0, p1 - side * w1, p1 + side * w1, p0 + side * w0]
            first = len(builder.polygons)
            builder.polygon(corners, "foliage_dark")
            builder.polygon(list(reversed(corners)), "foliage_dark")
            builder.tint(first, (1.0, 1.15, 1.0))
    return builder


def broad_tree(height=8.0, seed=0):
    builder = MeshBuilder()
    trunk(builder, height * 0.5, 0.3)
    lobe(builder, (0.0, 0.0, height * 0.62), height * 0.45, height * 0.6, "foliage_plane", 6, seed, 0.1)
    return builder


def stoa_body(scene, group, building, matrix):
    scene.unique(group, building.body, matrix)
    for key, (build, matrices) in building.columns.items():
        scene.add_instances(group, key, build, [matrix @ m for m in matrices])


def peristyle(scene, centre, z, size, height, diameter, turn, seed):
    matrices = []
    for k in range(4):
        angle = turn + k * math.pi / 2
        offset = Vector((math.sin(angle), -math.cos(angle), 0.0)) * (size / 2)
        matrices.append(Matrix.Translation((centre.x + offset.x, centre.y + offset.y, z))
                        @ Matrix.Rotation(angle, 4, "Z"))
    building = greek.stoa(length=size - 8.0, depth=7.0, column_height=height, diameter=diameter, steps=2,
                          step_rise=0.25, step_tread=0.4, inner_columns=False, detail="low", name=f"palais_{seed}",
                          acroteria=False)
    for matrix in matrices:
        stoa_body(scene, "palais", building, matrix)
    return building.info


def lamps_around(centre, z, size, count, turn):
    frames = []
    for k in range(count):
        angle = turn + 2 * math.pi * k / count
        radius = size / 2 - 9.0
        frames.append(placement(centre.x + radius * math.cos(angle), centre.y + radius * math.sin(angle), z))
    return frames


PALACES = [
    dict(t=1180.0, n=1080.0, size=64.0, height=6.2),
    dict(t=900.0, n=None, size=56.0, height=5.6),
    dict(t=600.0, n=None, size=48.0, height=5.4),
    dict(t=1040.0, n=None, size=44.0, height=5.0, back=120.0),
]


def palace_sites():
    sites = []
    for spec in PALACES:
        n = spec["n"]
        if n is None:
            n = plan.coast_n(spec["t"]) - spec["size"] / 2 - 28.0 - spec.get("back", 0.0)
        sites.append(dict(spec, n=n))
    return sites


def royal_quarter(scene, ground, eyes):
    info = {}
    lamps = []
    palms = []
    rng = random.Random(41)
    sites = palace_sites()
    for index, spec in enumerate(sites):
        centre = plan.grid_point(spec["t"], spec["n"])
        if not plan.is_land(centre.x, centre.y):
            continue
        z = ground(centre.x, centre.y) + 0.1
        info[f"palais_{index}"] = peristyle(scene, centre, z, spec["size"], spec["height"], spec["height"] / 7.0,
                                            plan.GRID_ANGLE, index)
        garden = MeshBuilder()
        half = spec["size"] / 2 - 9.0
        corners = [centre + plan.D * a * half + plan.N * b * half for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        garden.polygon([(p.x, p.y, z + 0.05) for p in corners], "foliage_dark", color=(1.1, 1.25, 1.0))
        scene.unique("palais", garden, occlusion=False)
        lamps.extend(lamps_around(centre, z, spec["size"], 8, plan.GRID_ANGLE + math.pi / 8))
        for k in range(6):
            p = centre + plan.D * rng.uniform(-half + 3, half - 3) + plan.N * rng.uniform(-half + 3, half - 3)
            palms.append(placement(p.x, p.y, z, rng.uniform(0, 6.28), rng.uniform(0.8, 1.1)))
    for t in np.arange(plan.ROYAL_T[0], plan.ROYAL_T[1], 26.0):
        for n in np.arange(plan.ROYAL_N, 1300.0, 26.0):
            p = plan.grid_point(t, n)
            if not plan.is_land(p.x, p.y) or ground.shore(p.x, p.y) < 30.0:
                continue
            if any((p - plan.grid_point(s["t"], s["n"])).length < s["size"] / 2 + 14.0 for s in sites):
                continue
            if any(math.hypot(p.x - ex, p.y - ey) < 20.0 for ex, ey in eyes):
                continue
            if rng.random() < 0.45:
                q = p + plan.D * rng.uniform(-8, 8) + plan.N * rng.uniform(-8, 8)
                palms.append(placement(q.x, q.y, ground(q.x, q.y) - 0.2, rng.uniform(0, 6.28), rng.uniform(0.8, 1.15)))
            elif rng.random() < 0.35:
                scene.palace_wings.append(plan.grid_frame(t, n, ground(p.x, p.y) - 0.2, rng.choice((0.0, math.pi))))
    scene.add_instances("palais", "palais_aile", lambda: palace_wing(), scene.palace_wings)
    info["ailes"] = len(scene.palace_wings)
    return info, lamps, palms


def palace_wing():
    builder = MeshBuilder()
    painted(builder, (0.98, 0.95, 0.88), lambda: builder.box((-11.0, -6.0, -1.5), (11.0, 6.0, 7.0), PLASTER,
                                                             bottom=False, top=False))
    quad(builder, [(-11.6, -6.6, 7.0), (11.6, -6.6, 7.0), (11.6, 6.6, 7.0), (-11.6, 6.6, 7.0)], (0, 0, 1), PLASTER,
         (0.86, 0.8, 0.7))
    for u in (-7.0, -2.3, 2.3, 7.0):
        quad(builder, [(u - 0.6, -6.03, 2.0), (u + 0.6, -6.03, 2.0), (u + 0.6, -6.03, 3.4), (u - 0.6, -6.03, 3.4)],
             (0, -1, 0), LAMP if u in (-2.3, 7.0) else VOID)
    return builder


def houses(scene, ground, eyes):
    rng = random.Random(7)
    wall = plan.city_wall()
    near = {k: [] for k in range(10)}
    mud = {k: [] for k in range(4)}
    r = plan.RHAKOTIS
    for t in np.arange(plan.CITY_T[0] + 30.0, plan.CITY_T[1] - 30.0, CHUNK[0] + 4.0):
        for n in np.arange(plan.lake_n(t) + 160.0, plan.CITY_N[1], CHUNK[1] + 4.0):
            if abs(n - plan.CANOPIC_N) < 26.0 or abs(t) < 22.0:
                continue
            if (t % plan.BLOCK_T) < 12.0 or (n % plan.BLOCK_N) < 12.0:
                continue
            if plan.in_royal(t, n):
                continue
            p = plan.grid_point(t, n)
            if not point_in_polygon(p.x, p.y, wall):
                continue
            if ground.shore(p.x, p.y) < 34.0 or not plan.is_land(p.x, p.y):
                continue
            if any(math.hypot(p.x - ex, p.y - ey) < 30.0 for ex, ey in eyes):
                continue
            in_rhakotis = math.hypot(t - r["t"], n - r["n"]) < 520.0
            if math.hypot(t - r["t"], n - r["n"]) < 95.0:
                continue
            density = 0.92 if in_rhakotis else 0.78 - 0.25 * (abs(t - 200.0) > 2000.0)
            if rng.random() > density:
                continue
            corners = [p + plan.D * a * 20.0 + plan.N * b * 18.0 for a, b in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
            z = min(ground(c.x, c.y) for c in corners) - 0.1
            turn = rng.choice((0.0, math.pi)) if not in_rhakotis else rng.choice((0.0, math.pi / 2, math.pi))
            matrix = plan.grid_frame(t, n, z, turn)
            if in_rhakotis:
                mud[rng.randrange(4)].append(matrix)
            else:
                near[rng.randrange(10)].append(matrix)
    for key, matrices in near.items():
        scene.add_instances("ville", f"maisons_{key}", lambda key=key: house_chunk(100 + key, lights=2 + key % 3),
                            matrices)
    for key, matrices in mud.items():
        scene.add_instances("ville", f"maisons_rhakotis_{key}", lambda key=key: house_chunk(200 + key, True, 1 + key % 2),
                            matrices)
    return {"maisons": sum(len(v) for v in near.values()), "rhakotis": sum(len(v) for v in mud.values())}


def wall_runs(points, ground, step=12.0):
    path = points + points[:1]
    dense = []
    for (x0, y0), (x1, y1) in zip(path[:-1], path[1:]):
        count = max(int(math.hypot(x1 - x0, y1 - y0) / step), 1)
        for k in range(count):
            dense.append((x0 + (x1 - x0) * k / count, y0 + (y1 - y0) * k / count))
    runs, current = [], []
    for x, y in dense:
        if plan.is_land(x, y) and ground.shore(x, y) > 6.0 and not plan.in_royal(*plan.grid_coords(x, y)):
            current.append((x, y))
        elif current:
            runs.append(current)
            current = []
    if current:
        runs.append(current)
    return [run for run in runs if len(run) > 4]


def city_walls(scene, ground):
    builder = MeshBuilder()
    towers = []
    length = 0.0
    for run in wall_runs(plan.city_wall(), ground):
        lifted = [(x, y, ground(x, y)) for x, y in run]
        first = len(builder.polygons)
        builder.sweep(lifted, [(1.5, -3.0), (1.5, 9.0), (-1.5, 9.0), (-1.5, -3.0)], "ashlar")
        builder.tint(first, (0.92, 0.86, 0.74))
        for k in range(0, len(lifted), 5):
            x, y, z = lifted[k]
            towers.append(placement(x, y, z))
        length += sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(lifted[:-1], lifted[1:]))
    scene.unique("ville", builder)
    scene.add_instances("ville", "tour_enceinte", wall_tower, towers)
    return {"longueur": round(length), "tours": len(towers)}


def wall_tower():
    builder = MeshBuilder()
    painted(builder, (0.9, 0.84, 0.72), lambda: builder.box((-4.0, -4.0, -3.0), (4.0, 4.0, 12.5), "ashlar",
                                                            bottom=False))
    return builder


def heptastadion(scene):
    start, end = plan.HEPTASTADION
    axis = end - start
    length = axis.length
    axis.normalize()
    frame = Matrix.Translation((start.x, start.y, 0.0)) @ Matrix.Rotation(math.atan2(axis.y, axis.x) - math.pi / 2,
                                                                         4, "Z")
    builder = MeshBuilder()
    half = plan.HEPTASTADION_WIDTH / 2
    top = plan.HEPTASTADION_TOP
    gap = plan.BRIDGE_GAP
    cuts = [0.0]
    for fraction in plan.HEPTASTADION_BRIDGES:
        cuts.extend([fraction * length - gap / 2, fraction * length + gap / 2])
    cuts.append(length)
    for y0, y1 in zip(cuts[0::2], cuts[1::2]):
        painted(builder, (0.9, 0.85, 0.74), lambda y0=y0, y1=y1: builder.box((-half, y0, -6.0), (half, y1, top - 0.02),
                                                                              "ashlar", bottom=False, top=False))
        painted(builder, (0.96, 0.92, 0.84), lambda y0=y0, y1=y1: builder.box((-half, y0, top - 0.3), (half, y1, top),
                                                                              "ground_quai", bottom=False))
        for x in (-half + 0.3, half - 0.3):
            painted(builder, (0.92, 0.88, 0.78), lambda x=x, y0=y0, y1=y1: builder.box(
                (x - 0.3, y0, top), (x + 0.3, y1, top + 0.9), "limestone", bottom=False))
        painted(builder, (0.88, 0.82, 0.7), lambda y0=y0, y1=y1: builder.box((5.6, y0, top), (7.0, y1, top + 1.2),
                                                                             "limestone", bottom=False))
    for fraction in plan.HEPTASTADION_BRIDGES:
        y0, y1 = fraction * length - gap / 2 - 1.0, fraction * length + gap / 2 + 1.0
        painted(builder, (0.66, 0.54, 0.4), lambda y0=y0, y1=y1: builder.box((-half + 2.0, y0, top - 0.8),
                                                                              (half - 2.0, y1, top), "dark_wood"))
        for x in (-half + 2.3, half - 2.3):
            painted(builder, (0.45, 0.34, 0.24), lambda x=x, y0=y0, y1=y1: builder.box(
                (x - 0.15, y0, top), (x + 0.15, y1, top + 1.0), "dark_wood", bottom=False))
        for y in np.linspace(y0 + 2.0, y1 - 2.0, 3):
            for x in (-half + 3.0, 0.0, half - 3.0):
                painted(builder, (0.4, 0.3, 0.22), lambda x=x, y=y: builder.box((x - 0.3, y - 0.3, -4.0),
                                                                                 (x + 0.3, y + 0.3, top - 0.8),
                                                                                 "dark_wood", bottom=False))
    scene.unique("heptastade", builder, frame)
    lamps = [frame @ placement(side * (half - 0.9), y, top) for y in np.arange(30.0, length - 20.0, 60.0)
             for side in (-1, 1)]
    return frame, length, lamps


def rhakotis(scene, ground):
    r = plan.RHAKOTIS
    centre = plan.grid_point(r["t"], r["n"])
    z = ground(centre.x, centre.y)
    builder = MeshBuilder()
    frame = Matrix.Translation((centre.x, centre.y, z)) @ Matrix.Rotation(plan.GRID_ANGLE, 4, "Z")
    for x0, y0, x1, y1 in ((-24.0, -18.0, 24.0, -16.6), (-24.0, 16.6, 24.0, 18.0), (-24.0, -18.0, -22.6, 18.0),
                           (22.6, -18.0, 24.0, -3.0), (22.6, 3.0, 24.0, 18.0)):
        painted(builder, (0.8, 0.7, 0.55), lambda x0=x0, y0=y0, x1=x1, y1=y1: builder.box(
            (x0, y0, -2.0), (x1, y1, 3.6), PLASTER, matrix=frame, bottom=False))
    for side in (-1, 1):
        painted(builder, (0.84, 0.76, 0.62), lambda side=side: builder.box(
            (22.0, side * 3.0 - 2.5, -2.0), (25.5, side * 3.0 + 2.5, 6.5), PLASTER, matrix=frame, bottom=False))
    painted(builder, (0.9, 0.84, 0.72), lambda: builder.box((-16.0, -6.0, -1.0), (-4.0, 6.0, 5.2), "limestone",
                                                            matrix=frame, bottom=False))
    quad(builder, [frame @ Vector(p) for p in ((-4.0, -1.4, 0.0), (-4.0, 1.4, 0.0), (-4.0, 1.4, 3.2),
                                               (-4.0, -1.4, 3.2))], frame.to_3x3() @ Vector((1, 0, 0)), LAMP)
    painted(builder, (0.88, 0.82, 0.72), lambda: builder.box((16.0, -12.2, -0.5), (18.4, -9.8, 1.2), "limestone",
                                                             matrix=frame, bottom=False))
    painted(builder, (0.82, 0.74, 0.6), lambda: builder.box((-23.0, -17.0, -0.6), (23.0, 17.0, 0.05), "ground_quai",
                                                            matrix=frame, bottom=False))
    scene.unique("rhakotis", builder)
    altar = frame @ Vector((17.2, -11.0, 1.4))
    palms = [frame @ placement(x, y, 0.0, k * 1.3) for k, (x, y) in
             enumerate(((-19.0, 13.0), (19.0, 13.0), (-19.0, -13.0)))]
    return altar, palms, frame


def antirhodos(scene, ground):
    xs = [p[0] for p in plan.ANTIRHODOS]
    ys = [p[1] for p in plan.ANTIRHODOS]
    centre = Vector((sum(xs) / len(xs), sum(ys) / len(ys)))
    z = ground(centre.x, centre.y)
    building = greek.stoa(length=14.0, depth=6.0, column_height=4.6, diameter=0.62, steps=2, step_rise=0.22,
                          step_tread=0.38, inner_columns=False, detail="low", name="antirhodos", acroteria=False)
    matrix = Matrix.Translation((centre.x, centre.y, z)) @ Matrix.Rotation(math.radians(-60.0), 4, "Z")
    stoa_body(scene, "palais", building, matrix)
    rng = random.Random(29)
    palms = []
    for k in range(30):
        x, y = centre.x + rng.uniform(-110.0, 110.0), centre.y + rng.uniform(-110.0, 110.0)
        if point_in_polygon(x, y, plan.ANTIRHODOS) and ground.shore(x, y) > 14.0 and (Vector((x, y)) - centre).length > 16:
            palms.append(placement(x, y, ground(x, y) - 0.2, rng.uniform(0, 6.28), rng.uniform(0.8, 1.1)))
    return palms


def necropolis(scene, ground):
    rng = random.Random(17)
    tombs = []
    wall = plan.city_wall()
    centre = plan.grid_point(1850.0, plan.coast_n(1850.0) - 160.0)
    for k in range(240):
        x = centre.x + rng.uniform(-170.0, 170.0)
        y = centre.y + rng.uniform(-170.0, 170.0)
        if not plan.is_land(x, y) or ground.shore(x, y) < 25.0 or point_in_polygon(x, y, wall):
            continue
        tombs.append(placement(x, y, ground(x, y) - 0.1, rng.uniform(0, 6.28), rng.uniform(0.7, 1.3)))
    scene.add_instances("ville", "tombe", tomb, tombs, cast_shadow=False)
    return len(tombs)


def tomb():
    builder = MeshBuilder()
    painted(builder, (0.88, 0.84, 0.76), lambda: builder.box((-1.4, -1.0, -0.5), (1.4, 1.0, 1.1), "limestone",
                                                             bottom=False))
    painted(builder, (0.92, 0.88, 0.8), lambda: builder.box((-0.35, 1.0, -0.3), (0.35, 1.2, 1.9), "limestone",
                                                            bottom=False))
    return builder


def lake_port(scene, ground):
    frames = []
    for k in range(5):
        t = plan.LAKE_PORT["t"] - 200.0 + k * 95.0
        n = plan.lake_n(t) + 45.0
        p = plan.grid_point(t, n)
        frames.append(plan.grid_frame(t, n, ground(p.x, p.y) - 0.2))
    scene.add_instances("ville", "entrepot", warehouse, frames)
    return len(frames)


def warehouse():
    builder = MeshBuilder()
    painted(builder, (0.86, 0.78, 0.64), lambda: builder.box((-36.0, -9.0, -1.5), (36.0, 9.0, 6.0), PLASTER,
                                                             bottom=False, top=False))
    quad(builder, [(-36.4, -9.4, 6.0), (36.4, -9.4, 6.0), (36.4, 9.4, 6.0), (-36.4, 9.4, 6.0)], (0, 0, 1), PLASTER,
         (0.74, 0.66, 0.54))
    for u in np.arange(-30.0, 31.0, 10.0):
        quad(builder, [(u - 1.6, -9.03, 0.0), (u + 1.6, -9.03, 0.0), (u + 1.6, -9.03, 3.4), (u - 1.6, -9.03, 3.4)],
             (0, -1, 0), VOID)
    return builder


def arsenals(scene, ground):
    frames = []
    a = Vector(plan.MAINLAND_SEA[14])
    b = Vector(plan.MAINLAND_SEA[16])
    direction = (b - a).normalized()
    inland = Vector((-direction.y, direction.x))
    if ground.shore(*(a + inland * 20.0)) < 0:
        inland = -inland
    for k in range(7):
        p = a + direction * (40.0 + k * 9.0) + inland * 18.0
        frames.append(Matrix.Translation((p.x, p.y, 0.4)) @ Matrix.Rotation(math.atan2(inland.y, inland.x) -
                                                                             math.pi / 2, 4, "Z"))
    scene.add_instances("ville", "loge_navire", shipshed, frames)
    return len(frames)


def countryside_trees(scene, ground, eyes):
    rng = random.Random(23)
    wall = plan.city_wall()
    palms, broads = [], []
    for k in range(9000):
        x = rng.uniform(-3300.0, 5300.0)
        y = rng.uniform(-4900.0, 800.0)
        if not plan.is_land(x, y) or ground.shore(x, y) < 20.0:
            continue
        t, n = plan.grid_coords(x, y)
        inside = point_in_polygon(x, y, wall)
        lake = abs(n - plan.lake_n(t))
        chance = 0.04 if inside else (0.5 if lake < 400.0 else 0.2)
        if rng.random() > chance:
            continue
        if any(math.hypot(x - ex, y - ey) < 25.0 for ex, ey in eyes):
            continue
        matrix = placement(x, y, ground(x, y) - 0.2, rng.uniform(0, 6.28), rng.uniform(0.75, 1.2))
        (palms if rng.random() < 0.72 else broads).append(matrix)
    return palms, broads
