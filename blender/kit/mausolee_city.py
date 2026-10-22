import math
import random

import numpy as np
from mathutils import Matrix

from . import figures
from . import greek
from . import mausolee_plan as plan
from .acropole_city import cluster, far_tree, ship, shipshed
from .acropole_monuments import altar, hip_house
from .acropole_terrain import smoothstep, world_noise
from .buildings import cypress, olive_tree, plane_tree, umbrella_pine
from .colosse_monuments import densify, land_runs
from .geometry import MeshBuilder, placement
from .greek_materials import MARBLE, POROS, TERRACOTTA
from .life import market_stall
from .mausolee_monument import BLUE_STONE, statue
from .phare_ships import fishing_boat, galley, merchant
from .terrain import point_in_polygon, polyline_distance

LIMESTONE = "limestone"
ASHLAR = "ashlar"
PLASTER = "plaster"
QUAY = "ground_quai"
SOURCE = "source"
CELL = 30.0
ANGLE = math.radians(4.0)
THEATRE_RADIUS = 52.0
GATE_RADIUS = 22.0


def rect_pad(name, point, azimuth, half_u, half_v, level=None, margin=10.0, lift=0.0):
    return {"name": name, "kind": "rect", "x": point[0], "y": point[1], "azimuth": azimuth, "half_u": half_u,
            "half_v": half_v, "level": level, "margin": margin, "raise": lift}


def circle_pad(name, point, radius, level=None, margin=10.0, lift=0.0):
    return {"name": name, "kind": "circle", "x": point[0], "y": point[1], "radius": radius, "level": level,
            "margin": margin, "raise": lift}


def theatre_centre():
    return plan.THEATRE[0], plan.THEATRE[1] - 18.0


def pads():
    tx, ty, hu, hv = plan.TERRACE
    return [
        rect_pad("terrasse", (tx, ty), 0.0, hu, hv, margin=3.0, lift=1.6),
        rect_pad("agora", plan.AGORA, 0.0, plan.AGORA_HALF[0], plan.AGORA_HALF[1], margin=12.0),
        circle_pad("goktepe", plan.GOKTEPE, 20.0, margin=14.0, lift=0.5),
        rect_pad("palais", plan.PALACE, 0.0, 38.0, 30.0, level=plan.PALACE_PLATEAU, margin=6.0),
        circle_pad("porte", plan.MYNDOS, 14.0, margin=12.0),
        rect_pad("salmakis", plan.SALMAKIS_SITE, 0.0, 13.0, 12.0, level=1.5, margin=7.0),
        circle_pad("orchestre", theatre_centre(), 11.0, margin=6.0),
    ]


def outward_normal(points, index):
    (x0, y0), (x1, y1) = points[index], points[index + 1]
    length = math.hypot(x1 - x0, y1 - y0)
    return (x1 - x0) / length, (y1 - y0) / length


def ditch(heights, gx, gy):
    near_gate = smoothstep(1.0 - (np.hypot(gx - plan.MYNDOS[0], gy - plan.MYNDOS[1]) - 260.0) / 80.0)
    line = []
    for (x0, y0), (x1, y1) in zip(plan.LAND_WALL[:-1], plan.LAND_WALL[1:]):
        length = math.hypot(x1 - x0, y1 - y0)
        nx, ny = -(y1 - y0) / length, (x1 - x0) / length
        line.append(((x0 + nx * 14.0, y0 + ny * 14.0), (x1 + nx * 14.0, y1 + ny * 14.0)))
    path = [line[0][0]] + [segment[1] for segment in line]
    distance = polyline_distance(path, gx, gy)
    road = polyline_distance(plan.AVENUE[-3:], gx, gy)
    depth = 5.0 * smoothstep(1.0 - distance / 7.0) * near_gate * smoothstep((road - 6.0) / 4.0)
    return heights - depth


def theatre_shape(heights, gx, gy):
    from .mausolee_terrain import theatre_bowl
    centre = theatre_centre()
    level = float(np.median(heights[np.hypot(gx - centre[0], gy - centre[1]) < 10.0]))
    return theatre_bowl(heights, gx, gy, centre, THEATRE_RADIUS, level)


def shaping():
    return [ditch, theatre_shape]


def level(scene, name):
    return scene.ground.near.levels[name]


def frame(point, z, azimuth=0.0, scale=1.0):
    return plan.frame(point[0], point[1], z, azimuth, scale)


def quay_line(scene, x0, x1, y_start, step=6.0):
    points = []
    x = x0
    while x <= x1:
        y = y_start
        while y > y_start - 260.0 and scene.ground(x, y) > 0.4:
            y -= 2.0
        if y_start - 260.0 < y < y_start:
            points.append((x, y + 1.0))
        x += step
    return points


def quays(scene):
    line = quay_line(scene, -100.0, 330.0, -60.0)
    smooth = list(line)
    for _ in range(3):
        smooth = [smooth[0]] + [((a[0] + 2 * b[0] + c[0]) / 4, (a[1] + 2 * b[1] + c[1]) / 4)
                                for a, b, c in zip(smooth[:-2], smooth[1:-1], smooth[2:])] + [smooth[-1]]
    builder = MeshBuilder()
    path = [(x, y, 0.0) for x, y in smooth]
    builder.sweep(path, [(-4.0, -4.0), (-4.0, 1.6), (6.0, 1.6), (6.0, -4.0)], QUAY, caps=True)
    builder.tint(0, (0.95, 0.92, 0.85))
    scene.unique("port", builder)
    mole = MeshBuilder()
    for points, width in (([(-250.0, -700.0), (-180.0, -705.0), (-120.0, -712.0)], 12.0),
                          ([(335.0, -640.0), (270.0, -660.0), (215.0, -672.0)], 12.0)):
        dense = densify(points, 10.0)
        mole.sweep([(x, y, 0.0) for x, y in dense],
                   [(width / 2, -6.0), (width / 2 - 0.5, 1.6), (-width / 2 + 0.5, 1.6), (-width / 2, -6.0)], QUAY)
    mole.tint(0, (0.9, 0.87, 0.8))
    scene.unique("port", mole)
    return smooth


def agora(scene):
    z = level(scene, "agora")
    ax, ay = plan.AGORA
    hx, hy = plan.AGORA_HALF
    for name, point, azimuth, length in (("stoa_agora_nord", (ax, ay + hy - 3.0), 180.0, 96.0),
                                         ("stoa_agora_ouest", (ax - hx + 3.0, ay), 90.0, 58.0)):
        hall = greek.stoa(length=length, depth=9.0, column_height=4.8, diameter=0.7, roof=TERRACOTTA,
                          polychromy=True, detail="low", name=name, inner_columns=False)
        greek.place_building(hall, scene.library, scene.collection, scene.tiles, scene.root("ville"),
                             frame(point, z, azimuth))
    rng = random.Random(9)
    stalls = []
    for k in range(16):
        x = ax + rng.uniform(-hx + 14.0, hx - 6.0)
        y = ay + rng.uniform(-hy + 4.0, hy - 16.0)
        stalls.append(frame((x, y), z, rng.choice((0.0, 90.0, 180.0, 270.0))))
    scene.instances("ville", "etal", lambda: market_stall(4), stalls)
    honours = [frame((ax + dx, ay - hy + 4.0), z, 180.0, 1.1) for dx in (-20.0, 0.0, 20.0)]
    scene.instances("ville", "statue_agora", lambda: statue("statue_dynaste"), honours)
    return {"centre": [ax, ay, z]}


def palace(scene):
    z = plan.PALACE_PLATEAU
    px, py = plan.PALACE
    root = scene.root("palais")
    terrace = MeshBuilder()
    terrace.box((-36.0, -28.0, -9.0), (36.0, 28.0, 0.4), LIMESTONE, bottom=False)
    terrace.tint(0, (0.78, 0.78, 0.76))
    terrace.box((-26.0, 0.0, 0.4), (26.0, 28.0, 4.4), BLUE_STONE, bottom=False)
    terrace.tint(len(terrace.polygons) - 10, (0.85, 0.85, 0.85))
    scene.unique("palais", terrace, frame((px, py), z))
    upper = z + 4.4
    hall = MeshBuilder()
    hip_house(hall, -14.0, 14.0, 6.0, 22.0, 8.0, MARBLE, TERRACOTTA, 0.3, 0.0, door=(-1, 0.0, 3.0, 4.8))
    hall.box((-14.5, 0.0, 0.0), (14.5, 6.0, 0.3), MARBLE, bottom=False)
    first = len(hall.polygons)
    hip_house(hall, 15.0, 25.0, 4.0, 24.0, 6.0, PLASTER, TERRACOTTA, 0.32, 0.0)
    hall.tint(first, (1.0, 0.98, 0.95))
    scene.unique("palais", hall, frame((px, py), upper))
    porch = greek.ionic_template(0.8, 7.0, "medium")
    scene.instances("palais", porch[0], porch[1], [frame((px + x, py + 3.0), upper) for x in (-10.5, -3.5, 3.5, 10.5)])
    court_z = z + 0.4
    for name, point, azimuth, length in (("palais_cour_ouest", (px - 24.0, py - 12.0), 90.0, 24.0),
                                         ("palais_cour_est", (px + 24.0, py - 12.0), 270.0, 24.0),
                                         ("palais_cour_sud", (px, py - 24.0), 0.0, 40.0)):
        hall_side = greek.stoa(length=length, depth=7.0, column_height=4.2, diameter=0.6, roof=TERRACOTTA,
                               polychromy=True, detail="low", name=name, inner_columns=False, acroteria=False)
        greek.place_building(hall_side, scene.library, scene.collection, scene.tiles, root,
                             frame(point, court_z, azimuth))
    rng = random.Random(21)
    annex = []
    garden = []
    for gx in np.arange(330.0, 620.0, 26.0):
        for gy in np.arange(-820.0, -500.0, 26.0):
            if abs(gx - px) < 48.0 and abs(gy - py) < 40.0:
                continue
            if gx < px - 60.0 and abs(gy - py - 12.0) < 30.0:
                continue
            corners = [scene.ground(gx + 10.0 * a, gy + 10.0 * b) for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            if min(corners) < 14.0 or max(corners) - min(corners) > 4.0:
                continue
            if rng.random() < 0.4:
                garden.append(placement(gx, gy, scene.ground(gx, gy) - 0.2, rng.uniform(0, 6.28), 0.9))
                continue
            annex.append(placement(gx, gy, min(corners), rng.choice((0.0, math.pi / 2))))
    scene.instances("palais", "palais_annexe", lambda: cluster(707), annex)
    scene.instances("palais", "jardin_cypres", lambda: cypress(10.0, 6), garden, occlusion=False)
    shed_point = plan.SECRET_HARBOUR
    shed = MeshBuilder()
    shed.merge(shipshed(), Matrix.Translation((0.0, 0.0, 0.0)))
    scene.unique("palais", shed, frame((shed_point[0], shed_point[1] + 18.0), 0.6, 180.0))
    hidden = galley(3, 30.0, 4.6)
    scene.unique("palais", hidden, frame((shed_point[0], shed_point[1] + 4.0), 0.4, 0.0))
    edge = px - 30.0
    while edge > px - 200.0 and scene.ground(edge, py + 12.0) > plan.PALACE_PLATEAU - 4.0:
        edge -= 2.0
    belvedere = (edge + 7.0, py + 12.0)
    lookout = MeshBuilder()
    base = scene.ground(*belvedere)
    lookout.box((-4.0, -4.0, -4.0), (4.0, 4.0, 3.3), LIMESTONE, bottom=False)
    lookout.tint(0, (0.8, 0.8, 0.78))
    scene.unique("palais", lookout, frame(belvedere, base))
    return {"terrace": [px, py, z], "upper": upper, "hall_door": [px, py + 6.0, upper],
            "belvedere": [belvedere[0], belvedere[1], scene.ground(*belvedere)]}


def naiskos():
    builder = MeshBuilder()
    builder.box((-3.6, -5.5, -2.0), (3.6, 5.5, 0.6), MARBLE, bottom=False)
    hip_house(builder, -3.0, 3.0, -4.6, 3.6, 5.0, MARBLE, TERRACOTTA, 0.3, 0.6, door=(1, 0.0, 1.6, 3.0))
    return builder


def salmakis(scene):
    spot = plan.SALMAKIS_SITE
    z = 1.5
    site = MeshBuilder()
    site.box((-12.0, -4.0, -6.0), (12.0, 9.0, 0.0), LIMESTONE, bottom=False)
    site.tint(0, (0.9, 0.88, 0.82))
    cliff = MeshBuilder()
    cliff.box((-7.0, -11.0, -6.0), (7.0, -4.0, 5.5), LIMESTONE, bottom=False)
    cliff.tint(0, (0.66, 0.62, 0.55))
    site.merge(cliff)
    site.oriented([(-2.2, -3.98, 0.0), (2.2, -3.98, 0.0), (1.6, -3.98, 3.4), (-1.6, -3.98, 3.4)], (0, 1, 0),
                  "shadow_void")
    site.box((-4.0, -3.9, 0.0), (4.0, -0.6, 0.7), MARBLE, bottom=False, top=False)
    site.box((-3.7, -3.6, -0.2), (3.7, -0.9, 0.55), SOURCE, bottom=False)
    site.merge(naiskos(), Matrix.Translation((-9.0, 0.5, 0.0)) @ Matrix.Rotation(math.pi / 2, 4, "Z")
               @ Matrix.Scale(0.8, 4))
    scene.unique("salmakis", site, frame(spot, z, 90.0))
    columns = greek.ionic_template(0.4, 3.6, "low")
    porch = [frame(plan.to_world(spot, 90.0, -9.0 + 0.8 * 4.2 * side, 0.5 + 0.8 * 4.4), z + 0.48, 90.0)
             for side in (-0.35, 0.35)]
    scene.instances("salmakis", columns[0], columns[1], porch)
    altar_block = MeshBuilder()
    altar(altar_block, 1.6, 1.1, 1.0, MARBLE, 1)
    altar_point = plan.to_world(spot, 90.0, -6.0, 6.0)
    scene.unique("salmakis", altar_block, frame(altar_point, z, 90.0))
    basin = plan.to_world(spot, 90.0, 0.0, -2.2)
    planes = [placement(*plan.to_world(spot, 90.0, 9.0, -6.0), z + 8.0, 0.4, 0.8),
              placement(*plan.to_world(spot, 90.0, 13.0, 2.0), z, 1.4, 0.7)]
    scene.instances("salmakis", "platane", lambda: plane_tree(14.0, 2), planes, occlusion=False)
    return {"temple": [*plan.to_world(spot, 90.0, -9.0, 0.5), z], "basin": [*basin, z],
            "altar": [*altar_point, z + 1.2]}


def ionic_shrine(name, columns=4, width=9.0, length=15.0, height=6.4, diameter=0.7):
    building = greek.Building(name)
    b = building.body
    z = greek.crepidoma(b, -width / 2, width / 2, -length / 2, length / 2, 3, 0.3, 0.4)
    spacing = (width - 1.2) / (columns - 1)
    xs = [-width / 2 + 0.6 + k * spacing for k in range(columns)]
    building.add_columns(greek.ionic_template(diameter, height, "medium"),
                         greek.placements([(x, length / 2 - 0.7) for x in xs], z))
    b.box((-width / 2 + 0.3, -length / 2 + 0.3, z), (width / 2 - 0.3, length / 2 - 3.2, z + height + 0.6), MARBLE,
          bottom=False, top=False)
    greek.door_frame(b, -1.1, 1.1, length / 2 - 3.3, length / 2 - 3.1, z, 4.2, 0.3)
    b.oriented([(-1.1, length / 2 - 3.18, z), (1.1, length / 2 - 3.18, z), (1.1, length / 2 - 3.18, z + 4.2),
                (-1.1, length / 2 - 3.18, z + 4.2)], (0, 1, 0), "shadow_void")
    dims = greek.doric_dimensions(diameter, spacing, 15.0, architrave=0.5, frieze=0.45, face=0.3, inner=0.5)
    greek.entablature(b, greek.rectangle(xs[0], xs[-1], -length / 2 + 0.7, length / 2 - 0.7), z + height, dims,
                      frieze="ionic", regulae=False, detail="medium", seed=3)
    levels = greek.entablature_levels(dims)
    half_span = xs[-1] + dims["face"] + dims["projection"]
    greek.gable(b, Matrix.Translation((0.0, 0.0, z + height + levels["top"])), half_span, length - 1.4, dims, True,
                "medium", TERRACOTTA, 0.6, acroteria=True, antefixes=False, seed=9)
    return building


def ares(scene):
    z = level(scene, "goktepe")
    gx, gy = plan.GOKTEPE
    temple = ionic_shrine("temple_ares")
    greek.place_building(temple, scene.library, scene.collection, scene.tiles, scene.root("goktepe"),
                         frame((gx, gy + 3.0), z, 180.0))
    block = MeshBuilder()
    altar(block, 3.0, 1.8, 1.2, POROS, 1)
    altar_point = (gx, gy - 12.0)
    scene.unique("goktepe", block, frame(altar_point, z, 180.0))
    return {"temple": [gx, gy + 3.0, z], "altar": [altar_point[0], altar_point[1], z + 1.5], "level": z}


def theatre(scene):
    cx, cy = theatre_centre()
    z = level(scene, "orchestre")
    rows = MeshBuilder()
    for row in range(16):
        radius = 12.0 + row * 0.8
        lift = (radius - 11.0) * 0.52
        arc = []
        for k in range(29):
            angle = math.radians(-6.0 + 192.0 * k / 28)
            arc.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle), z + lift))
        rows.sweep(arc, [(0.0, -0.9), (0.0, 0.42), (0.8, 0.42), (0.8, -0.9)], LIMESTONE, caps=True)
    rows.tint(0, (0.97, 0.94, 0.88))
    stage = MeshBuilder()
    stage.box((cx - 11.0, cy - 15.0, z - 1.0), (cx + 11.0, cy - 11.5, z + 3.2), POROS, bottom=False)
    stage.oriented([(cx - 1.2, cy - 11.48, z), (cx + 1.2, cy - 11.48, z), (cx + 1.2, cy - 11.48, z + 2.6),
                    (cx - 1.2, cy - 11.48, z + 2.6)], (0, 1, 0), "shadow_void")
    rows.merge(stage)
    orchestra = MeshBuilder()
    orchestra.lathe([(0.0, 0.08), (10.5, 0.08), (10.5, -0.5)], 28, POROS, smooth=False)
    rows.merge(orchestra, Matrix.Translation((cx, cy, z)))
    scene.unique("theatre", rows)
    return {"orchestra": [cx, cy, z], "rows": 16}


def wall_tower():
    builder = MeshBuilder()
    builder.box((-4.2, -3.6, -6.0), (4.2, 4.4, 11.0), ASHLAR, bottom=False)
    for k in range(4):
        x = -3.2 + k * 2.13
        builder.box((x - 0.55, 3.8, 11.0), (x + 0.55, 4.4, 12.0), ASHLAR, bottom=False)
    builder.tint(0, (0.9, 0.88, 0.82))
    return builder


def walls(scene):
    rng = random.Random(97)
    towers = []
    total = 0.0
    gate = plan.MYNDOS
    for run in land_runs(scene, plan.LAND_WALL, step=10.0, closed=False):
        pieces = [[]]
        for point in run:
            if math.hypot(point[0] - gate[0], point[1] - gate[1]) < GATE_RADIUS:
                if pieces[-1]:
                    pieces.append([])
                continue
            pieces[-1].append(point)
        for piece in pieces:
            if len(piece) < 2:
                continue
            builder = MeshBuilder()
            builder.sweep(piece, [(1.6, -6.0), (1.6, 7.0), (-1.6, 7.0), (-1.6, -6.0)], ASHLAR)
            builder.tint(0, (0.9, 0.88, 0.82))
            scene.unique("murs", builder)
            walked = 0.0
            next_tower = 25.0
            for a, b in zip(piece[:-1], piece[1:]):
                length = math.hypot(b[0] - a[0], b[1] - a[1])
                while walked + length >= next_tower:
                    t = (next_tower - walked) / length
                    x, y = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
                    angle = math.atan2(b[1] - a[1], b[0] - a[0])
                    towers.append(placement(x, y, scene.ground.surface(x, y), angle))
                    next_tower += 70.0 * rng.uniform(0.85, 1.15)
                walked += length
            total += walked
    scene.instances("murs", "tour", wall_tower, towers)
    z = level(scene, "porte")
    index = min(range(len(plan.LAND_WALL) - 1), key=lambda i: math.hypot(plan.LAND_WALL[i][0] - gate[0],
                                                                         plan.LAND_WALL[i][1] - gate[1]))
    (x0, y0), (x1, y1) = plan.LAND_WALL[index - 1], plan.LAND_WALL[index + 1]
    angle = math.atan2(y1 - y0, x1 - x0)
    gatehouse = MeshBuilder()
    for side in (-1, 1):
        gatehouse.box((side * 9.5 - 5.5, -6.0, -3.0), (side * 9.5 + 5.5, 7.0, 14.0), ASHLAR, bottom=False)
        for k in range(3):
            x = side * 9.5 - 4.0 + k * 4.0
            gatehouse.box((x - 0.8, -6.0, 14.0), (x + 0.8, -5.2, 15.2), ASHLAR, bottom=False)
    gatehouse.box((-4.0, -1.6, 6.0), (4.0, 1.6, 9.0), ASHLAR, bottom=False)
    gatehouse.box((-4.0, -1.6, 9.0), (4.0, 1.6, 10.6), ASHLAR, bottom=False)
    for side in (-1, 1):
        gatehouse.oriented([(-4.0, side * 1.62, 0.0), (4.0, side * 1.62, 0.0), (4.0, side * 1.62, 6.0),
                            (-4.0, side * 1.62, 6.0)], (0, side, 0), "shadow_void")
    gatehouse.tint(0, (0.9, 0.88, 0.82))
    scene.unique("murs", gatehouse, Matrix.Translation((gate[0], gate[1], z)) @ Matrix.Rotation(angle, 4, "Z"))
    outward = (-math.sin(angle), math.cos(angle))
    return {"length": round(total), "towers": len(towers), "gate": [gate[0], gate[1], z], "gate_angle": angle,
            "outward": outward}


def excluded(x, y, eyes):
    tx, ty, hu, hv = plan.TERRACE
    if abs(x - tx) < hu + 14.0 and abs(y - ty) < hv + 14.0:
        return True
    if 30.0 < x < 160.0 and -70.0 < y < 40.0:
        return True
    ax, ay = plan.AGORA
    if abs(x - ax) < plan.AGORA_HALF[0] + 10.0 and abs(y - ay) < plan.AGORA_HALF[1] + 10.0:
        return True
    cx, cy = theatre_centre()
    if math.hypot(x - cx, y - cy) < THEATRE_RADIUS + 18.0 and y > cy - 25.0:
        return True
    if math.hypot(x - plan.GOKTEPE[0], y - plan.GOKTEPE[1]) < 60.0:
        return True
    if point_in_polygon(x, y, plan.KAPLAN) or point_in_polygon(x, y, plan.ZEPHYRION):
        return True
    if math.hypot(x - plan.MYNDOS[0], y - plan.MYNDOS[1]) < 60.0:
        return True
    if float(polyline_distance(plan.AVENUE, np.array([x]), np.array([y]))[0]) < plan.AVENUE_WIDTH / 2 + 12.0:
        return True
    return any(math.hypot(x - ex, y - ey) < 22.0 for ex, ey in eyes)


def houses(scene, eyes):
    ground = scene.ground
    near_matrices = {k: [] for k in range(10)}
    far_matrices = {k: [] for k in range(3)}
    rng = random.Random(13)
    c, s = math.cos(ANGLE), math.sin(ANGLE)
    for v in np.arange(-700.0, 1300.0, CELL) + CELL / 2:
        for u in np.arange(-1300.0, 1300.0, CELL) + CELL / 2:
            x, y = u * c - v * s, u * s + v * c
            if not point_in_polygon(x, y, plan.CITY_WALL) or excluded(x, y, eyes):
                continue
            corners = [ground(x + 12.0 * a, y + 12.0 * b) for a, b in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            if min(corners) < 1.4 or max(corners) - min(corners) > 7.5:
                continue
            density = world_noise(np.array(x), np.array(y), 90.0, 73, 2)
            far_out = math.hypot(x - 0.0, y + 100.0) > 650.0
            if density < (0.42 if far_out else 0.28) or rng.random() < 0.05:
                continue
            z = min(corners) + 0.3 * (max(corners) - min(corners))
            matrix = placement(x, y, z, ANGLE + rng.choice((0.0, math.pi / 2, math.pi, -math.pi / 2)))
            if not far_out:
                near_matrices[rng.randrange(10)].append(matrix)
            else:
                far_matrices[rng.randrange(3)].append(matrix)
    for key, matrices in near_matrices.items():
        scene.instances("ville", f"maison_{key}", lambda key=key: cluster(500 + key), matrices)
    for key, matrices in far_matrices.items():
        scene.instances("ville_loin", f"maison_loin_{key}", lambda key=key: cluster(600 + key, True), matrices,
                        cast_shadow=False)
    scene.shadowless.add("ville_loin")
    return {"proches": sum(len(v) for v in near_matrices.values()),
            "lointaines": sum(len(v) for v in far_matrices.values())}


def trees(scene, eyes):
    ground = scene.ground
    rng = np.random.default_rng(31)
    groups = {"olivier": [], "pin": [], "cypres": [], "loin": []}
    attempts = 0
    while sum(len(v) for v in groups.values()) < 3600 and attempts < 90000:
        attempts += 1
        x, y = rng.uniform(-7000.0, 7000.0), rng.uniform(-3000.0, 6000.0)
        if attempts % 3 == 0:
            x, y = rng.uniform(-1600.0, 1600.0), rng.uniform(-1200.0, 1600.0)
        z = ground(x, y)
        if z < 3.0 or z > 600.0:
            continue
        inside = point_in_polygon(x, y, plan.CITY_WALL)
        if inside and not (math.hypot(x - plan.GOKTEPE[0], y - plan.GOKTEPE[1]) < 220.0 and rng.random() < 0.5):
            continue
        if any(math.hypot(x - ex, y - ey) < 30.0 for ex, ey in eyes) or excluded(x, y, []):
            continue
        if world_noise(np.array(x), np.array(y), 400.0, 8, 2) < 0.42:
            continue
        near = math.hypot(x, y) < 2600.0
        if not near:
            groups["loin"].append(placement(x, y, z - 0.3, rng.uniform(0, 6.28), rng.uniform(0.8, 1.3)))
            continue
        key = "pin" if z > 40.0 or rng.random() < 0.35 else "olivier"
        if rng.random() < 0.04:
            key = "cypres"
        groups[key].append(placement(x, y, ground.surface(x, y) - 0.2, rng.uniform(0, 6.28), rng.uniform(0.8, 1.2)))
    builds = {"olivier": lambda: olive_tree(5.0, 2), "pin": lambda: umbrella_pine(11.0, 3),
              "cypres": lambda: cypress(11.0, 4)}
    for key in ("olivier", "pin", "cypres"):
        scene.instances("vegetation", f"arbre_{key}", builds[key], groups[key], occlusion=False)
    scene.instances("vegetation", "arbre_loin", far_tree, groups["loin"], cast_shadow=False, occlusion=False)
    return {key: len(value) for key, value in groups.items()}


def sea_spot(scene, rng, box, clearance=14.0):
    x0, x1, y0, y1 = box
    for _ in range(400):
        x, y = rng.uniform(x0, x1), rng.uniform(y0, y1)
        if all(scene.ground(x + ox, y + oy) < -1.5 for ox, oy in
               ((0, 0), (clearance, 0), (-clearance, 0), (0, clearance), (0, -clearance))):
            return x, y
    return None


def ships(scene, quay):
    rng = random.Random(53)
    placed = {"marchand": [], "triere": [], "barque": [], "voilier": []}
    for k in range(5):
        x, y = quay[int(len(quay) * (0.35 + 0.12 * k)) % len(quay)]
        placed["marchand"].append(frame((x + rng.uniform(-3, 3), y - 13.0), 0.0, 90.0 + rng.uniform(-6, 6)))
    for k in range(6):
        y = -270.0 - 30.0 * k
        x = 40.0
        while x > -400.0 and scene.ground(x, y) < 0.4:
            x -= 2.0
        placed["triere"].append(frame((x + 15.0, y), 0.3, 270.0 + rng.uniform(-4, 4))
                                @ Matrix.Rotation(0.03, 4, "X"))
    for box, count, key in (((-120.0, 300.0, -460.0, -260.0), 9, "barque"), ((-200.0, 500.0, -1400.0, -800.0), 3,
                                                                             "voilier"),
                            ((-6000.0, 3000.0, -12000.0, -2500.0), 9, "voilier"), ((-1500.0, 1500.0, -2500.0,
                                                                                   -1000.0), 4, "barque")):
        for _ in range(count):
            spot = sea_spot(scene, rng, box)
            if spot:
                placed[key].append(frame(spot, 0.0, rng.uniform(0.0, 360.0)))
    arrival = sea_spot(scene, rng, (-600.0, 400.0, -2600.0, -1700.0), 30.0)
    if arrival:
        placed["triere"].append(frame(arrival, 0.0, 15.0))
    scene.instances("mer", "navire_marchand", lambda: merchant(1, False), placed["marchand"], cast_shadow=False)
    scene.instances("mer", "voilier", lambda: merchant(2, True), placed["voilier"], cast_shadow=False)
    scene.instances("mer", "triere", lambda: ship("trireme"), placed["triere"], cast_shadow=False)
    scene.instances("mer", "barque", lambda: fishing_boat(4), placed["barque"], cast_shadow=False)
    return {key: len(value) for key, value in placed.items()}


def walkable(scene):
    return [obj for name, obj in scene.statics.items() if name in ("port", "terrasse", "palais", "theatre",
                                                                    "salmakis", "goktepe")]
