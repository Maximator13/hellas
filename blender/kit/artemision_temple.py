import math
import random

from mathutils import Matrix, Vector

from . import artemision_plan as plan
from . import figures as people
from . import greek
from .geometry import MeshBuilder
from .greek_materials import IONIC_FLUTED, MARBLE, PAINT, TERRACOTTA
from .materials import linear_color

GILT = "gold"
CYPRESS = "dark_wood"
ASH = "ash"
TAU = 2 * math.pi

STEP_RISE = plan.PLATFORM_HEIGHT / plan.STEPS
STEP_TREAD = 0.55
STYLOBATE = (plan.PLATFORM[0] - 2 * plan.STEPS * STEP_TREAD, plan.PLATFORM[1] - 2 * plan.STEPS * STEP_TREAD)
DIAMETER = 1.8
COLUMN_HEIGHT = 17.7
TOP_RATIO = 0.84
FRONT_GAPS = (6.1, 6.6, 7.2, 8.6, 7.2, 6.6, 6.1)
FLANK_COUNT = 21
BACK_COUNT = 9
BASE_PLINTH = 0.2
BASE_SPIRA = 0.45
DRUM = 1.82
PEDESTAL = 1.8
ARCHITRAVE = 1.9
ENTABLATURE = 4.0
FACE = 0.42 * DIAMETER
INNER = 0.5 * DIAMETER
SLOPE = math.radians(12.0)
SEKOS_HALF = 12.0
WALL = 1.6
ANTA_WEST = -43.0
CROSS_WALL = -27.0
NAOS_BACK = 31.6
ANTA_EAST = 43.0
DOOR = (6.0, 12.0)
STATUE_X = 25.0
STATUE_BASE = 1.3
STATUE_HEIGHT = 2.2
BEAM_TINT = (0.78, 0.74, 0.66)
WARM = (0.9, 0.87, 0.81)


def axes(gaps):
    total = sum(gaps)
    out = [-total / 2]
    for gap in gaps:
        out.append(out[-1] + gap)
    return out


def front_axes():
    return axes(FRONT_GAPS)


def back_axes():
    span = sum(FRONT_GAPS)
    return axes([span / (BACK_COUNT - 1)] * (BACK_COUNT - 1))


def flank_axes():
    margin = (STYLOBATE[1] - sum(FRONT_GAPS)) / 2
    half = STYLOBATE[0] / 2 - margin
    return [-half + 2 * half * k / (FLANK_COUNT - 1) for k in range(FLANK_COUNT)]


def asian_base(builder, d, plinth=True):
    if plinth:
        builder.box((-0.7 * d, -0.7 * d, 0.0), (0.7 * d, 0.7 * d, BASE_PLINTH * d), MARBLE, bottom=False)
    z0 = BASE_PLINTH * d if plinth else 0.0
    profile = [(0.66, 0.0), (0.66, 0.03), (0.6, 0.05), (0.565, 0.1), (0.6, 0.14), (0.625, 0.15), (0.625, 0.17),
               (0.595, 0.185), (0.56, 0.22), (0.6, 0.26), (0.625, 0.27), (0.625, 0.29), (0.6, 0.3), (0.655, 0.34),
               (0.67, 0.38), (0.645, 0.42), (0.57, 0.44), (0.5, 0.45)]
    builder.lathe([(r * d, z0 + z * d) for r, z in profile], 20, MARBLE, smooth=True, caps=False)
    return z0 + BASE_SPIRA * d


def shaft(builder, d, bottom, top, start_ratio=1.0):
    heights = greek.ring_heights(bottom, top, "medium")
    full = COLUMN_HEIGHT
    radii = [greek.entasis_radius(d / 2, TOP_RATIO, 0.006 * d, min(max(z / full, 0.0), 1.0)) * start_ratio
             for z in heights]
    greek.ring_shaft(builder, heights, radii, 32, IONIC_FLUTED, mapped=True)


def capital(builder, d, top):
    greek.ionic_capital(builder, d, top - greek.IONIC_CAPITAL * d, TOP_RATIO, "medium", MARBLE)
    first = len(builder.polygons)
    neck = d / 2 * TOP_RATIO
    z = top - greek.IONIC_CAPITAL * d
    for k in range(16):
        a0 = TAU * k / 16
        a1 = TAU * (k + 0.62) / 16
        r = neck + 0.068 * d
        builder.polygon([(r * math.cos(a0), r * math.sin(a0), z + 0.05 * d), (r * math.cos(a1), r * math.sin(a1),
                                                                               z + 0.05 * d),
                         (r * math.cos(a1), r * math.sin(a1), z + 0.11 * d),
                         (r * math.cos(a0), r * math.sin(a0), z + 0.11 * d)], PAINT)
    builder.tint(first, greek.PALETTE["blue"])


def plain_column(d=DIAMETER, height=COLUMN_HEIGHT):
    builder = MeshBuilder()
    bottom = asian_base(builder, d)
    shaft(builder, d, bottom, height - greek.IONIC_CAPITAL * d)
    capital(builder, d, height)
    return builder.tint(0, WARM)


RELIEF_SETS = (
    ("hermes", "woman", "thanatos", "man", "woman_veiled", "ephebe"),
    ("woman", "man", "woman_veiled", "ephebe", "man", "woman"),
    ("thanatos", "woman_veiled", "man", "woman", "hermes", "man"),
    ("ephebe", "woman", "man", "woman_veiled", "ephebe", "woman"),
)


def relief_figure(kind):
    if kind == "hermes":
        return people.ephebe(people.WOOL_WHITE, people.WOAD, (0.62, 0.50, 0.30), people.SKIN)
    if kind == "thanatos":
        builder = people.ephebe(people.LINEN, people.CRIMSON, (0.2, 0.15, 0.1), people.SKIN)
        for side in (-1, 1):
            first = len(builder.polygons)
            builder.polygon([(side * 0.12, -0.12, 1.4), (side * 0.6, -0.22, 1.75), (side * 0.75, -0.2, 1.2),
                             (side * 0.35, -0.16, 0.85)], PAINT)
            builder.polygon([(side * 0.35, -0.18, 0.85), (side * 0.75, -0.22, 1.2), (side * 0.6, -0.24, 1.75),
                             (side * 0.12, -0.14, 1.4)], PAINT)
            builder.tint(first, (0.82, 0.74, 0.58))
        return builder
    if kind == "woman":
        return people.woman_peplos(people.WOOL_WHITE, people.MADDER, people.SKIN)
    if kind == "woman_veiled":
        return people.woman_peplos(people.LINEN, people.WOAD, people.SKIN, veil=people.MADDER)
    if kind == "ephebe":
        return people.ephebe(people.WOOL_WHITE, people.MADDER, (0.62, 0.50, 0.30), people.SKIN)
    return people.man_himation(people.WOOL_WHITE, people.SKIN, people.HAIR, people.HAIR)


def sculpted_drum(builder, d, z0, variant, height=DRUM):
    radius = 0.53 * d
    first = len(builder.polygons)
    builder.lathe([(radius, z0), (radius, z0 + height)], 24, MARBLE, smooth=True, caps=False)
    builder.tint(first, (0.93, 0.92, 0.9))
    first = len(builder.polygons)
    builder.lathe([(radius, z0 + height), (radius + 0.05, z0 + height + 0.06), (0.5 * d, z0 + height + 0.12)], 24,
                  MARBLE, smooth=True, caps=False)
    figures = RELIEF_SETS[variant % len(RELIEF_SETS)]
    scale = (height - 0.12) / 1.78
    for index, kind in enumerate(figures):
        angle = TAU * index / len(figures) + variant * 0.4
        piece = relief_figure(kind)
        frame = (Matrix.Rotation(angle - math.pi / 2, 4, "Z") @ Matrix.Translation((0.0, radius - 0.02, z0 + 0.04))
                 @ Matrix.Scale(scale, 4))
        builder.merge(piece, frame)
    return z0 + height + 0.12


def sculpted_column(variant, d=DIAMETER, height=COLUMN_HEIGHT):
    builder = MeshBuilder()
    bottom = asian_base(builder, d)
    top_of_drum = sculpted_drum(builder, d, bottom, variant)
    shaft(builder, d, top_of_drum, height - greek.IONIC_CAPITAL * d)
    capital(builder, d, height)
    return builder.tint(0, WARM)


def pedestal_column(variant, d=DIAMETER, height=COLUMN_HEIGHT):
    builder = MeshBuilder()
    side = 0.75 * d
    builder.box((-side - 0.1, -side - 0.1, 0.0), (side + 0.1, side + 0.1, 0.25), MARBLE, bottom=False)
    builder.box((-side, -side, 0.25), (side, side, PEDESTAL - 0.2), MARBLE, bottom=False, top=False)
    builder.box((-side - 0.08, -side - 0.08, PEDESTAL - 0.2), (side + 0.08, side + 0.08, PEDESTAL), MARBLE,
                bottom=False)
    for face in range(4):
        panel = MeshBuilder()
        panel.polygon([(-side + 0.1, side + 0.005, PEDESTAL - 0.28), (side - 0.1, side + 0.005, PEDESTAL - 0.28),
                       (side - 0.1, side + 0.005, 0.32), (-side + 0.1, side + 0.005, 0.32)],
                      PAINT, color=(0.22, 0.34, 0.56))
        builder.merge(panel, Matrix.Rotation(face * math.pi / 2, 4, "Z"))
    kinds = RELIEF_SETS[(variant + 1) % len(RELIEF_SETS)]
    scale = (PEDESTAL - 0.65) / 1.78
    for face in range(4):
        for k in range(2):
            piece = relief_figure(kinds[(face * 2 + k) % len(kinds)])
            frame = (Matrix.Rotation(face * math.pi / 2, 4, "Z")
                     @ Matrix.Translation(((k - 0.5) * 0.9, side - 0.02, 0.33)) @ Matrix.Scale(scale, 4))
            builder.merge(piece, frame)
    lifted = MeshBuilder()
    bottom = asian_base(lifted, d)
    shaft(lifted, d, bottom, height - PEDESTAL - greek.IONIC_CAPITAL * d)
    capital(lifted, d, height - PEDESTAL)
    builder.merge(lifted, Matrix.Translation((0.0, 0.0, PEDESTAL)))
    return builder.tint(0, WARM)


def column_layout():
    xs_front = front_axes()
    xs_back = back_axes()
    ys = flank_axes()
    west, east = ys[0], ys[-1]
    second_west, second_east = ys[1], ys[-2]
    outer_y = xs_front[-1]
    inner_y = xs_front[-2]
    places = {"west": [], "east": [], "flank": [], "pronaos": [], "opisthodomos": []}
    for y in xs_front:
        places["west"].append((west, y))
    for y in xs_front[1:-1]:
        places["west"].append((second_west, y))
    for y in xs_back:
        places["east"].append((east, y))
    for y in xs_back[1:-1]:
        places["east"].append((second_east, y))
    for x in ys[1:-1]:
        places["flank"] += [(x, -outer_y), (x, outer_y)]
    for x in ys[2:-2]:
        places["flank"] += [(x, -inner_y), (x, inner_y)]
    for x in (-38.0, -32.5):
        places["pronaos"] += [(x, -4.6), (x, 4.6)]
    places["opisthodomos"] = [(ANTA_EAST - 0.8, -4.6), (ANTA_EAST - 0.8, 4.6)]
    return places


def entablature_profile():
    f = FACE
    return [(-INNER, 0.0), (f, 0.0), (f, 0.55), (f + 0.07, 0.6), (f + 0.07, 1.15), (f + 0.14, 1.2), (f + 0.14, 1.66),
            (f + 0.3, 1.9), (f + 0.14, 1.92), (f + 0.14, 2.42), (f + 0.36, 2.5), (f + 1.1, 2.62), (f + 1.1, 3.2),
            (f + 1.16, 3.26), (f + 1.16, ENTABLATURE), (-INNER, ENTABLATURE)]


def ring_entablature(builder, xs, ys, z):
    x0, x1 = xs
    y0, y1 = ys
    path = [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)]
    builder.sweep(path, entablature_profile(), MARBLE, closed=True)
    corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    count = 0
    for a, b in zip(corners, corners[1:] + corners[:1]):
        frame, length = greek.run_frame(a, b, z)
        run = MeshBuilder()
        f = FACE
        reach = f + 0.14
        pitch = 0.4
        dentils = int((length + 2 * reach) / pitch)
        for k in range(dentils):
            u = -reach + (k + 0.5) * (length + 2 * reach) / dentils
            run.box((u - 0.12, f + 0.14, 1.94), (u + 0.12, f + 0.42, 2.4), MARBLE, bottom=True, top=False)
        count += dentils
        greek.band(run, -(f + 0.3), length + f + 0.3, f + 0.31, 1.7, 1.9, "kymation", "medium")
        greek.band(run, -(f + 1.17), length + f + 1.17, f + 1.165, 3.3, 3.95, "kymation", "high")
        spouts = int(length / 3.0)
        for k in range(spouts):
            u = (k + 0.5) * length / spouts
            first = len(run.polygons)
            run.lathe([(0.0, 0.0), (0.2, 0.05), (0.24, 0.25), (0.16, 0.42), (0.0, 0.46)], 8, MARBLE, smooth=True,
                      matrix=Matrix.Translation((u, f + 1.16, 3.4)) @ Matrix.Rotation(-math.pi / 2, 4, "X"))
            run.tint(first, (0.95, 0.9, 0.82))
            first = len(run.polygons)
            run.box((u - 0.07, f + 1.5, 3.55), (u + 0.07, f + 1.62, 3.66), PAINT)
            run.tint(first, greek.PALETTE["red"])
        builder.merge(run, frame)
    return count


def gable_dims():
    dims = greek.doric_dimensions(DIAMETER, 6.6, 12.0)
    dims.update(face=FACE + 0.14, recess=0.05, projection=0.96, corona=0.64, crown=0.74, sima=0.8)
    return dims


def platform(builder):
    width, depth = STYLOBATE
    greek.crepidoma(builder, -width / 2, width / 2, -depth / 2, depth / 2, plan.STEPS, STEP_RISE, STEP_TREAD,
                    MARBLE, foundation=1.6)
    first = len(builder.polygons)
    builder.box((-width / 2 + 0.3, -depth / 2 + 0.3, plan.PLATFORM_HEIGHT), (width / 2 - 0.3, depth / 2 - 0.3,
                                                                           plan.PLATFORM_HEIGHT + 0.01),
                MARBLE, bottom=False)
    builder.tint(first, (0.96, 0.95, 0.92))
    return plan.PLATFORM_HEIGHT


def wall_box(builder, x0, x1, y0, y1, z0, z1):
    builder.box((x0, y0, z0), (x1, y1, z1), MARBLE, bottom=False, top=False)


def sekos(builder, floor, ceiling):
    h, w = SEKOS_HALF, WALL
    for side in (-1, 1):
        y0, y1 = sorted((side * h, side * (h - w)))
        wall_box(builder, ANTA_WEST, ANTA_EAST, y0, y1, floor, ceiling)
        builder.box((ANTA_WEST - 0.2, y0 - 0.15, floor), (ANTA_WEST + 1.4, y1 + 0.15, floor + 0.9), MARBLE,
                    bottom=False)
        builder.box((ANTA_EAST - 1.4, y0 - 0.15, floor), (ANTA_EAST + 0.2, y1 + 0.15, floor + 0.9), MARBLE,
                    bottom=False)
    door_w, door_h = DOOR
    inner = h - w
    wall = MeshBuilder()
    greek.wall_with_doors(wall, -inner, inner, CROSS_WALL, CROSS_WALL + w, floor, ceiling, [(0.0, door_w, door_h)],
                          MARBLE, 0.45)
    builder.merge(wall, Matrix.Rotation(math.pi / 2, 4, "Z") @ Matrix.Diagonal((1.0, -1.0, 1.0, 1.0)))
    wall = MeshBuilder()
    greek.wall_with_doors(wall, -inner, inner, NAOS_BACK, NAOS_BACK + w, floor, ceiling, [(0.0, 3.6, 7.0)], MARBLE,
                          0.35)
    builder.merge(wall, Matrix.Rotation(math.pi / 2, 4, "Z") @ Matrix.Diagonal((1.0, -1.0, 1.0, 1.0)))
    first = len(builder.polygons)
    builder.oriented([(CROSS_WALL + w, -inner, floor + 0.02), (NAOS_BACK, -inner, floor + 0.02),
                      (NAOS_BACK, inner, floor + 0.02), (CROSS_WALL + w, inner, floor + 0.02)], (0, 0, 1), MARBLE)
    builder.tint(first, (0.62, 0.6, 0.56))
    first = len(builder.polygons)
    builder.oriented([(CROSS_WALL + w, -inner, ceiling - 0.02), (NAOS_BACK, -inner, ceiling - 0.02),
                      (NAOS_BACK, inner, ceiling - 0.02), (CROSS_WALL + w, inner, ceiling - 0.02)], (0, 0, -1), PAINT)
    builder.tint(first, (0.32, 0.2, 0.12))
    for side in (-1, 1):
        y = side * (inner - 0.02)
        for z0, z1, colour in ((floor, floor + 1.4, (0.46, 0.14, 0.1)), (floor + 9.0, floor + 9.6, (0.2, 0.3, 0.52))):
            first = len(builder.polygons)
            builder.oriented([(CROSS_WALL + w, y, z0), (NAOS_BACK, y, z0), (NAOS_BACK, y, z1), (CROSS_WALL + w, y, z1)],
                             (0, -side, 0), PAINT)
            builder.tint(first, colour)
    first = len(builder.polygons)
    for k in range(int((NAOS_BACK - CROSS_WALL - w) / 2.4)):
        x = CROSS_WALL + w + 1.2 + k * 2.4
        builder.box((x - 0.22, -inner, ceiling - 0.7), (x + 0.22, inner, ceiling - 0.02), CYPRESS, top=False)
    builder.tint(first, (0.55, 0.38, 0.24))
    return {"door_centre": (CROSS_WALL, 0.0, floor + door_h / 2), "door_height": door_h}


def doors(builder, floor):
    door_w, door_h = DOOR
    for side in (-1, 1):
        leaf = MeshBuilder()
        leaf.box((0.0, -0.1, 0.0), (door_w / 2, 0.1, door_h), CYPRESS, bottom=False)
        first = len(leaf.polygons)
        for row in range(6):
            for col in range(3):
                leaf.box((0.4 + col * 0.9, 0.1, 0.9 + row * 1.9), (0.55 + col * 0.9, 0.16, 1.05 + row * 1.9), "bronze",
                         bottom=False)
        leaf.tint(first, (1.0, 1.0, 1.0))
        hinge = (Matrix.Translation((CROSS_WALL + WALL + 0.15, side * door_w / 2, floor))
                 @ Matrix.Rotation(-side * math.pi / 2 + side * math.radians(75.0), 4, "Z"))
        builder.merge(leaf, hinge)


def cult_statue(builder, floor):
    x = STATUE_X
    builder.box((x - 1.5, -1.5, floor), (x + 1.5, 1.5, floor + STATUE_BASE), MARBLE, bottom=False)
    first = len(builder.polygons)
    builder.box((x - 1.62, -1.62, floor + STATUE_BASE - 0.15), (x + 1.62, 1.62, floor + STATUE_BASE), PAINT,
                bottom=False)
    builder.tint(first, greek.PALETTE["red"])
    z = floor + STATUE_BASE
    h = STATUE_HEIGHT
    body = MeshBuilder()
    body.lathe([(0.0, 0.0), (0.28, 0.0), (0.26, 0.35), (0.22, 0.6), (0.21, 0.95), (0.24, 1.25), (0.25, 1.45),
                (0.18, 1.58), (0.08, 1.62), (0.0, 1.62)], 14, GILT, smooth=True, matrix=Matrix.Scale(h / 2.2, 4))
    for row in range(3):
        for k in range(5):
            a = math.radians(-60.0 + k * 30.0)
            r = 0.24 + 0.02 * row
            people.ellipsoid(body, (r * math.sin(a), r * math.cos(a), (1.32 - row * 0.1) * h / 2.2),
                             (0.05, 0.05, 0.065), people.GOLD, 6, 3)
    for row in range(5):
        people.ellipsoid(body, (0.0, 0.25, (0.4 + row * 0.17) * h / 2.2), (0.15, 0.04, 0.06), people.GOLD, 6, 3)
    people.ellipsoid(body, (0.0, 0.0, 1.76 * h / 2.2), (0.12, 0.13, 0.15), people.GOLD, 8, 5)
    body.lathe([(0.11, 1.86 * h / 2.2), (0.15, 2.12 * h / 2.2), (0.0, 2.13 * h / 2.2)], 12, GILT, smooth=True)
    for side in (-1, 1):
        people.tube(body, [(side * 0.25, 0.0, 1.45 * h / 2.2), (side * 0.3, 0.12, 1.12 * h / 2.2),
                           (side * 0.32, 0.42, 1.08 * h / 2.2)], [0.06, 0.055, 0.045], [people.GOLD, people.GOLD], 6)
        people.tube(body, [(side * 0.32, 0.42, 1.08 * h / 2.2), (side * 0.33, 0.44, 0.1 * h / 2.2)], [0.012, 0.012],
                    [(0.62, 0.42, 0.2)] * 2, 4)
    builder.merge(body, Matrix.Translation((x, 0.0, z)) @ Matrix.Rotation(math.pi / 2, 4, "Z"))
    first = len(builder.polygons)
    builder.box((x + 1.8, -2.8, floor), (x + 2.0, 2.8, floor + 6.0), "velum_linen")
    builder.tint(first, (0.42, 0.12, 0.24))
    first = len(builder.polygons)
    for side in (-1, 1):
        builder.box((x + 1.6, side * 2.8 - 0.3, floor), (x + 1.95, side * 2.8 + 0.3, floor + 6.0), "velum_linen")
    builder.tint(first, (0.88, 0.62, 0.22))
    first = len(builder.polygons)
    garland = [(x + 1.7, -2.8 + 5.6 * k / 12, floor + 5.6 - 1.2 * math.sin(math.pi * k / 12)) for k in range(13)]
    people.tube(builder, garland, [0.12] * 13, [(0.26, 0.42, 0.18)] * 12, 5)
    builder.tint(first, (1.0, 1.0, 1.0))
    for side in (-1, 1):
        first = len(builder.polygons)
        builder.lathe([(0.0, 0.0), (0.3, 0.0), (0.12, 0.08), (0.08, 1.1), (0.22, 1.2), (0.25, 1.32), (0.0, 1.3)], 10,
                      "bronze", smooth=True, matrix=Matrix.Translation((x - 3.5, side * 2.6, floor)))
        builder.tint(first, (1.0, 1.0, 1.0))
    first = len(builder.polygons)
    builder.box((x - 6.2, -1.0, floor), (x - 4.6, 1.0, floor + 0.9), MARBLE, bottom=False)
    builder.tint(first, (0.92, 0.9, 0.86))
    return {"face": (x - 0.1, 0.0, z + 1.76 * h / 2.2), "top": (x, 0.0, z + h), "front": (x - 1.5, 0.0, floor)}


def apelles(builder, floor):
    first = len(builder.polygons)
    y = SEKOS_HALF - WALL - 0.02
    x0, x1 = -40.5, -36.0
    builder.polygon([(x0, y, floor + 3.0), (x1, y, floor + 3.0), (x1, y, floor + 8.0), (x0, y, floor + 8.0)], PAINT)
    builder.tint(first, (0.42, 0.3, 0.2))
    first = len(builder.polygons)
    y -= 0.03
    builder.polygon([(x0 + 0.3, y, floor + 3.3), (x1 - 0.3, y, floor + 3.3), (x1 - 0.3, y, floor + 7.7),
                     (x0 + 0.3, y, floor + 7.7)], PAINT)
    builder.tint(first, (0.36, 0.26, 0.18))
    first = len(builder.polygons)
    y -= 0.03
    builder.polygon([(x0 + 1.4, y, floor + 3.8), (x1 - 1.4, y, floor + 3.8), (x1 - 1.2, y, floor + 7.0),
                     (x0 + 1.2, y, floor + 7.0)], PAINT)
    builder.tint(first, (0.62, 0.42, 0.26))
    first = len(builder.polygons)
    builder.polygon([(x1 - 1.6, y - 0.01, floor + 6.6), (x1 - 0.7, y - 0.01, floor + 7.4), (x1 - 0.9, y - 0.01,
                                                                                           floor + 6.4)], PAINT)
    builder.tint(first, (0.95, 0.78, 0.35))


def offerings(builder, floor, rng):
    for k in range(10):
        side = 1 if k % 2 else -1
        x = -24.0 + k * 4.2
        if abs(x - STATUE_X) < 4.0:
            continue
        y = side * (SEKOS_HALF - WALL - 1.0)
        first = len(builder.polygons)
        builder.box((x - 0.5, y - 0.5, floor), (x + 0.5, y + 0.5, floor + 1.1), MARBLE, bottom=False)
        builder.tint(first, (0.94, 0.92, 0.88))
        piece = rng.choice((people.man_himation, people.woman_peplos, people.ephebe))()
        statue = MeshBuilder()
        greek.statue(statue, piece, Matrix.Identity(4))
        statue.tint(0, (0.96, 0.94, 0.9))
        builder.merge(statue, Matrix.Translation((x, y, floor + 1.1))
                      @ Matrix.Rotation(math.pi if side > 0 else 0.0, 4, "Z"))


def ceilings(builder, xs, ys, z):
    first = len(builder.polygons)
    builder.oriented([(xs[0] + INNER, ys[0] + INNER, z), (xs[1] - INNER, ys[0] + INNER, z),
                      (xs[1] - INNER, ys[1] - INNER, z), (xs[0] + INNER, ys[1] - INNER, z)], (0, 0, -1), PAINT)
    builder.tint(first, (0.3, 0.36, 0.5))
    first = len(builder.polygons)
    step = 3.0
    count_x = int((xs[1] - xs[0]) / step)
    for k in range(count_x + 1):
        x = xs[0] + INNER + k * (xs[1] - xs[0] - 2 * INNER) / count_x
        builder.box((x - 0.18, ys[0] + INNER, z - 0.5), (x + 0.18, ys[1] - INNER, z), MARBLE, top=False)
    builder.tint(first, BEAM_TINT)


def temple(scene):
    level = scene.ground_level
    matrix = Matrix.Translation((0.0, 0.0, level))
    body = MeshBuilder()
    floor = platform(body)
    places = column_layout()
    ys = flank_axes()
    xs_front = front_axes()
    column_top = floor + COLUMN_HEIGHT
    ceiling = column_top + ARCHITRAVE
    ring_x = (ys[0], ys[-1])
    ring_y = (xs_front[0], xs_front[-1])
    dentils = ring_entablature(body, ring_x, ring_y, column_top)
    inner_x = (ys[1], ys[-2])
    inner_y = (xs_front[1], xs_front[-2])
    for (a, b) in (((inner_x[0], inner_y[0]), (inner_x[1], inner_y[0])), ((inner_x[0], inner_y[1]),
                                                                          (inner_x[1], inner_y[1])),
                   ((inner_x[0], inner_y[0]), (inner_x[0], inner_y[1])), ((inner_x[1], inner_y[0]),
                                                                          (inner_x[1], inner_y[1]))):
        greek.beam(body, a, b, 0.84 * DIAMETER, column_top, ceiling)
    for (x0, x1) in ((-38.0, -38.0), (-32.5, -32.5)):
        greek.beam(body, (x0, -SEKOS_HALF + WALL), (x1, SEKOS_HALF - WALL), 0.8 * DIAMETER, column_top, ceiling)
    ceilings(body, ring_x, ring_y, ceiling)
    info = sekos(body, floor, ceiling)
    doors(body, floor)
    statue = cult_statue(body, floor)
    apelles(body, floor)
    offerings(body, floor, random.Random(7))
    dims = gable_dims()
    half_span = ring_y[1] + dims["face"] + dims["projection"] + 0.03 * DIAMETER
    z_eave = column_top + 3.26
    gable_frame = Matrix.Translation((0.0, 0.0, z_eave)) @ Matrix.Rotation(math.pi / 2, 4, "Z")
    rise = greek.gable(body, gable_frame, half_span, ring_x[1] - ring_x[0], dims, True, "medium", TERRACOTTA, 0.72,
                       figures=False, acroteria=True, antefixes=False, seed=9)
    body.tint(0, WARM)
    scene.unique("temple", body, matrix)
    variant = 0
    plain = []
    sculpted = {k: [] for k in range(len(RELIEF_SETS))}
    pedestals = {k: [] for k in range(2)}
    for key in ("west", "east", "pronaos", "opisthodomos", "flank"):
        for x, y in places[key]:
            m = Matrix.Translation((x, y, floor))
            if key == "pronaos":
                pedestals[variant % 2].append(m)
                variant += 1
            elif key == "flank":
                plain.append(m)
            else:
                sculpted[variant % len(RELIEF_SETS)].append(m @ Matrix.Rotation(variant * 0.7, 4, "Z"))
                variant += 1
    scene.add_instances("temple", "colonne_ionique", plain_column, [matrix @ m for m in plain])
    for k, matrices in sculpted.items():
        scene.add_instances("temple", f"colonne_sculptee_{k}", lambda k=k: sculpted_column(k),
                            [matrix @ m for m in matrices])
    for k, matrices in pedestals.items():
        scene.add_instances("temple", f"colonne_socle_{k}", lambda k=k: pedestal_column(k),
                            [matrix @ m for m in matrices])
    world = lambda p: tuple(matrix @ Vector(p))
    counts = {"plain": len(plain), "sculpted": sum(len(v) for v in sculpted.values()),
              "pedestal": sum(len(v) for v in pedestals.values())}
    counts["total"] = sum(counts.values())
    return {"level": level, "floor": level + floor, "column_top": level + column_top, "ceiling": level + ceiling,
            "ridge": level + z_eave + rise, "dentils": dentils, "columns": counts,
            "front_axes": [round(v, 2) for v in xs_front], "flank_axes": [round(v, 2) for v in ys],
            "door_centre": world(info["door_centre"]), "door_height": info["door_height"],
            "statue_face": world(statue["face"]), "statue_top": world(statue["top"]),
            "statue_front": world(statue["front"]), "facade_x": -plan.PLATFORM[0] / 2,
            "naos": [world((CROSS_WALL + WALL, 0.0, floor)), world((NAOS_BACK, 0.0, floor))],
            "stylobate": STYLOBATE}


def altar_columns(builder, path, z, height, d, spacing):
    count = 0
    for a, b in zip(path[:-1], path[1:]):
        length = (Vector(b) - Vector(a)).length
        n = max(int(length / spacing), 1)
        for k in range(n + 1):
            if k == 0 and count:
                continue
            p = Vector(a).lerp(Vector(b), k / n)
            column = MeshBuilder()
            bottom = asian_base(column, d, plinth=False)
            shaft(column, d, bottom, height - greek.IONIC_CAPITAL * d)
            greek.ionic_capital(column, d, height - greek.IONIC_CAPITAL * d, TOP_RATIO, "low", MARBLE)
            builder.merge(column, Matrix.Translation((p.x, p.y, z)))
            count += 1
    return count


def great_altar(scene):
    level = scene.ground_level
    cx, cy = plan.ALTAR
    length, width = plan.ALTAR_COURT
    x0, x1 = cx - length / 2, cx + length / 2
    y0, y1 = cy - width / 2, cy + width / 2
    b = MeshBuilder()
    first = len(b.polygons)
    b.box((x0 - 1.0, y0 - 1.0, -0.8), (x1 + 1.0, y1 + 1.0, 0.35), MARBLE, bottom=False)
    b.tint(first, (0.9, 0.88, 0.84))
    for k in range(3):
        b.box((x0 - 1.0 - (k + 1) * 0.45, y0 - 1.0, -0.8), (x0 - 1.0 - k * 0.45, y1 + 1.0, 0.35 - (k + 1) * 0.11),
              MARBLE, bottom=False)
    socle = 1.6
    for side in (-1, 1):
        ya, yb = sorted((side * (width / 2), side * (width / 2 - 1.2)))
        b.box((x0, cy + ya, 0.35), (x1, cy + yb, 0.35 + socle), MARBLE, bottom=False)
    b.box((x1 - 1.2, y0, 0.35), (x1, y1, 0.35 + socle), MARBLE, bottom=False)
    z_col = 0.35 + socle
    height = 4.2
    d = 0.46
    inset = 0.6
    path = [(x0 + 0.6, y0 + inset), (x1 - inset, y0 + inset), (x1 - inset, y1 - inset), (x0 + 0.6, y1 - inset)]
    count = altar_columns(b, path, z_col, height, d, 2.4)
    top = z_col + height
    for a, c in zip(path[:-1], path[1:]):
        greek.beam(b, a, c, 0.5, top, top + 0.55)
        first = len(b.polygons)
        greek.beam(b, a, c, 0.56, top + 0.55, top + 0.75)
        b.tint(first, greek.PALETTE["blue"])
    first = len(b.polygons)
    for (ax, ay), (bx, by), outward in (((x0, y0), (x1, y0), (0.0, -1.0)), ((x1, y0), (x1, y1), (1.0, 0.0)),
                                        ((x1, y1), (x0, y1), (0.0, 1.0))):
        ix, iy = ax - outward[0] * 4.0, ay - outward[1] * 4.0
        jx, jy = bx - outward[0] * 4.0, by - outward[1] * 4.0
        b.box((min(ax, bx, ix, jx) - 0.2, min(ay, by, iy, jy) - 0.2, top + 0.74),
              (max(ax, bx, ix, jx) + 0.2, max(ay, by, iy, jy) + 0.2, top + 0.95), TERRACOTTA)
    b.tint(first, (0.92, 0.9, 0.86))
    for side in (-1, 1):
        ya, yb = sorted((side * width / 2, side * (width / 2 - 4.0)))
        b.box((x0, cy + ya, 0.35 + socle), (x1, cy + yb, 0.35 + socle + 0.02), MARBLE, bottom=False)
    rng = random.Random(23)
    models = (people.man_himation, people.woman_peplos, lambda: people.woman_peplos(veil=people.WOOL_WHITE),
              people.ephebe)
    for k in range(9):
        side = 1 if k % 2 else -1
        x = x0 + 3.6 + (k // 2) * 6.2
        if x > x1 - 3.0:
            continue
        statue = MeshBuilder()
        greek.statue(statue, rng.choice(models)(), Matrix.Identity(4))
        statue.tint(0, (0.97, 0.95, 0.9))
        y = cy + side * (width / 2 - 2.6)
        b.box((x - 0.5, y - 0.5, z_col), (x + 0.5, y + 0.5, z_col + 0.6), MARBLE, bottom=False)
        b.merge(statue, Matrix.Translation((x, y, z_col + 0.6)) @ Matrix.Rotation(math.pi if side > 0 else 0.0, 4, "Z")
                @ Matrix.Scale(1.15, 4))
    ax = x1 - 6.0
    first = len(b.polygons)
    b.box((ax - 2.4, cy - 5.0, 0.35), (ax + 2.4, cy + 5.0, 1.9), MARBLE, bottom=False)
    b.box((ax - 2.6, cy - 5.2, 1.9), (ax + 2.6, cy + 5.2, 2.15), MARBLE, bottom=False)
    for k in range(3):
        b.box((ax - 2.4 - (k + 1) * 0.4, cy - 3.0, 0.35), (ax - 2.4 - k * 0.4, cy + 3.0, 0.35 + (3 - k) * 0.5), MARBLE,
              bottom=False)
    b.tint(first, (0.96, 0.94, 0.9))
    first = len(b.polygons)
    b.box((ax - 1.6, cy - 3.6, 2.15), (ax + 1.6, cy + 3.6, 2.3), ASH)
    b.tint(first, (0.32, 0.28, 0.26))
    b.lathe([(0.9, 2.3), (0.6, 2.75), (0.0, 2.9)], 10, "flame", smooth=True, matrix=Matrix.Translation((ax, cy, 0.0)))
    first = len(b.polygons)
    b.polygon([(x0 - 2.4, y0, 0.36), (x1, y0, 0.36), (x1, y1, 0.36), (x0 - 2.4, y1, 0.36)], "ground_parvis")
    b.tint(first, (0.86, 0.84, 0.8))
    scene.unique("autel", b, Matrix.Translation((0.0, 0.0, level)))
    return {"top": (ax, cy, level + 2.3), "court": (cx, cy, level + 0.35), "columns": count,
            "entrance": (x0 - 3.0, cy, level)}


def parvis(scene):
    level = scene.ground_level
    x0, x1, y0, y1 = plan.PARVIS
    b = MeshBuilder()
    b.box((x0, y0, -0.6), (x1, y1, 0.08), "ground_parvis", bottom=False)
    scene.unique("autel", b, Matrix.Translation((0.0, 0.0, level)))


def materials(tiles, principled_material):
    principled_material(ASH, linear_color((0.52, 0.50, 0.47)), 0.97)
    tiles[ASH] = 2.0
    return tiles
