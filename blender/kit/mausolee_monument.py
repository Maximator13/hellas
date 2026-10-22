import math
import random

from mathutils import Matrix, Vector

from . import figures
from . import greek
from .acropole_monuments import altar, block, scaffold
from .geometry import MeshBuilder, placement
from .greek_materials import IONIC_FLUTED, MARBLE, PAINT
from .life import wheel

BLUE_STONE = "calcaire_bleu"
TOTAL_HEIGHT = 45.0
QUADRANGLE = (19.2, 16.25)
SOCLE_STEPS = 3
SOCLE_RISE = 0.4
TIERS = [((18.6, 15.65), 1.2, 7.0), ((17.3, 14.35), 7.0, 13.2), ((16.25, 13.3), 13.2, 18.3)]
BLUE_TOP = 4.2
STYLOBATE = (16.2, 13.2)
Z_STYLOBATE = 18.9
SPACING = 3.0
COLUMNS = (11, 9)
DIAMETER = 1.0
COLUMN_HEIGHT = 10.0
PLINTH = 0.25
CELLA = (12.0, 9.0)
ENTABLATURE = 2.35
STEPS = 24
STEP_RISE = 0.3
LEDGE = 1.9
TOP_PLATFORM = (4.0, 3.0)
BASE = (3.7, 2.7, 3.0)
FRIEZE_BLUE = (0.16, 0.30, 0.62)
RED = (0.66, 0.16, 0.10)
OCHRE = (0.78, 0.56, 0.22)
CREAM = (1.0, 0.97, 0.9)
LION_BODY = (0.78, 0.62, 0.36)
LION_MANE = (0.48, 0.32, 0.18)
WHITE_HORSE = (0.97, 0.95, 0.9)
BROWN_HORSE = (0.55, 0.36, 0.22)


def axes(count):
    return [SPACING * (k - (count - 1) / 2) for k in range(count)]


def heights():
    z_columns = Z_STYLOBATE + COLUMN_HEIGHT
    z_entablature = z_columns + ENTABLATURE
    z_pyramid = z_entablature + STEP_RISE * STEPS
    z_base = z_pyramid + BASE[2]
    return {"stylobate": Z_STYLOBATE, "capitals": z_columns, "ceiling": z_columns + 1.05, "roof": z_entablature,
            "pyramid_top": z_pyramid, "base_top": z_base, "top": z_base + 3.6}


def tinted(builder, colour, action):
    first = len(builder.polygons)
    action()
    builder.tint(first, colour)


def marble_copy(source, keep=0.5, material=MARBLE):
    copy = MeshBuilder()
    copy.points(source.positions)
    copy.heights = list(source.heights)
    for indices, smooth, colour in zip(source.polygons, source.polygon_smooth, source.polygon_colors):
        base = colour or (1.0, 1.0, 1.0)
        mixed = tuple(c * keep + 1.0 * (1 - keep) for c in base)
        copy.face(list(indices), material, smooth, color=mixed)
    return copy


def ring_runs(hx, hy):
    corners = [(-hx, -hy), (hx, -hy), (hx, hy), (-hx, hy)]
    return [(corners[k], corners[(k + 1) % 4]) for k in range(4)]


def run_frame(start, end, z):
    frame, length = greek.run_frame(start, end, z)
    return frame, length


def painted_rect(builder, x0, x1, z0, z1, y, colour):
    greek.rect(builder, x0, x1, z0, z1, y, colour)


def fighter(builder, x, y, z, h, depth, facing, colour, shield=None):
    first = len(builder.polygons)
    piece = MeshBuilder()
    greek.relief_human(piece, 0.0, 0.0, 0.0, h, depth, -0.25 * facing, -1.1)
    if shield is not None:
        tinted(piece, shield, lambda: piece.centered_box((-0.12 * h, depth * 1.1, 0.62 * h),
                                                         (0.2 * h, depth * 0.5, 0.26 * h), PAINT))
    builder.merge(piece, Matrix.Translation((x, y, z)) @ Matrix.Diagonal((facing, 1.0, 1.0, 1.0)))
    builder.tint(first, colour)


def rider(builder, x, y, z, h, depth, facing, colour):
    first = len(builder.polygons)
    greek.relief_horse(builder, x, y, z, h, depth, facing, rider=True)
    builder.tint(first, colour)


def amazonomachy(builder, length, z, height, y, rng):
    x = 0.35
    while x < length - 0.7:
        roll = rng.random()
        if roll < 0.2:
            rider(builder, x + 0.32 * height, y, z, height * 0.98, 0.09, rng.choice((-1, 1)), (1.0, 0.96, 0.9))
            x += 0.7 * height + 0.12
            continue
        fighter(builder, x + 0.1 * height, y, z, height * 0.95, 0.08, 1, (0.92, 0.82, 0.7), RED)
        fighter(builder, x + 0.42 * height, y, z, height * 0.93, 0.08, -1, (1.0, 0.95, 0.88),
                (0.86, 0.68, 0.3) if rng.random() < 0.5 else RED)
        x += 0.62 * height + rng.uniform(0.15, 0.4)


def chariot_race(builder, length, z, height, y, rng):
    x = 0.4
    while x < length - 1.4:
        for k in range(2):
            rider_colour = (1.0, 0.97, 0.92) if k == 0 else (0.84, 0.66, 0.5)
            first = len(builder.polygons)
            greek.relief_horse(builder, x + 0.3 * height + k * 0.12, y + 0.01 * k, z, height * 0.9, 0.08, 1,
                               rider=False)
            builder.tint(first, rider_colour)
        tinted(builder, RED, lambda: builder.box((x - 0.1 * height, y, z + 0.18 * height),
                                                (x + 0.08 * height, y + 0.09, z + 0.45 * height), PAINT))
        greek.relief_human(builder, x - 0.02 * height, y + 0.02, z + 0.28 * height, height * 0.62, 0.07, 0.25, 0.9)
        x += 1.15 * height + rng.uniform(0.3, 0.8)


def centauromachy(builder, length, z, height, y, rng):
    x = 0.3
    while x < length - 0.6:
        if rng.random() < 0.5:
            rider(builder, x + 0.3 * height, y, z, height, 0.08, rng.choice((-1, 1)), (0.86, 0.72, 0.56))
            x += 0.62 * height + 0.1
        else:
            fighter(builder, x + 0.12 * height, y, z, height * 0.95, 0.08, rng.choice((-1, 1)), (1.0, 0.95, 0.88), RED)
            x += 0.35 * height + 0.1


def frieze_band(builder, hx, hy, z0, z1, kind, seed, inset=0.0):
    rng = random.Random(seed)
    for start, end in ring_runs(hx, hy):
        frame, length = run_frame(start, end, 0.0)
        run = MeshBuilder()
        painted_rect(run, -inset, length + inset, z0, z1, 0.004, FRIEZE_BLUE)
        height = (z1 - z0) * 0.86
        if kind == "amazones":
            amazonomachy(run, length, z0 + 0.04, height, 0.005, rng)
        elif kind == "chars":
            chariot_race(run, length, z0 + 0.04, height, 0.005, rng)
        else:
            centauromachy(run, length, z0 + 0.04, height, 0.005, rng)
        builder.merge(run, frame)


def moulding_band(builder, hx, hy, z0, z1, pattern="kymation"):
    for start, end in ring_runs(hx, hy):
        frame, length = run_frame(start, end, 0.0)
        run = MeshBuilder()
        greek.band(run, -0.02, length + 0.02, 0.004, z0, z1, pattern, "medium")
        builder.merge(run, frame)


def stepped_block(builder, hx, hy, z0, z1, material, cap=0.12):
    builder.box((-hx, -hy, z0), (hx, hy, z1), material, bottom=False)
    if cap > 0:
        builder.box((-hx - cap, -hy - cap, z1 - 0.28), (hx + cap, hy + cap, z1), material, bottom=False)


def podium(builder):
    qx, qy = QUADRANGLE
    for k in range(SOCLE_STEPS):
        inset = k * 0.3
        builder.box((-qx + inset, -qy + inset, -1.5 if k == 0 else k * SOCLE_RISE),
                    (qx - inset, qy - inset, (k + 1) * SOCLE_RISE), BLUE_STONE, bottom=False)
    (hx, hy), z0, z1 = TIERS[0]
    builder.box((-hx, -hy, z0), (hx, hy, BLUE_TOP), BLUE_STONE, bottom=False, top=False)
    builder.box((-hx - 0.1, -hy - 0.1, BLUE_TOP - 0.35), (hx + 0.1, hy + 0.1, BLUE_TOP), BLUE_STONE, bottom=False,
                top=False)
    stepped_block(builder, hx, hy, BLUE_TOP, z1, MARBLE)
    moulding_band(builder, hx + 0.121, hy + 0.121, z1 - 0.26, z1 - 0.04)
    for (hx, hy), z0, z1 in TIERS[1:]:
        stepped_block(builder, hx, hy, z0, z1, MARBLE)
        moulding_band(builder, hx + 0.121, hy + 0.121, z1 - 0.26, z1 - 0.04)
    hx, hy = TIERS[2][0]
    frieze_band(builder, hx, hy, 16.9, 17.95, "amazones", 7)
    sx, sy = STYLOBATE
    builder.box((-sx - 0.3, -sy - 0.3, TIERS[2][2]), (sx + 0.3, sy + 0.3, Z_STYLOBATE - 0.3), MARBLE, bottom=False)
    builder.box((-sx, -sy, Z_STYLOBATE - 0.3), (sx, sy, Z_STYLOBATE), MARBLE, bottom=False)


def column_points():
    xs, ys = axes(COLUMNS[0]), axes(COLUMNS[1])
    points = [(x, y) for x in xs for y in (ys[0], ys[-1])]
    points += [(x, y) for x in (xs[0], xs[-1]) for y in ys[1:-1]]
    return points


def plinths(builder):
    half = 0.68
    for x, y in column_points():
        builder.box((x - half, y - half, Z_STYLOBATE), (x + half, y + half, Z_STYLOBATE + PLINTH), BLUE_STONE,
                    bottom=False)


def cella(builder):
    cx, cy = CELLA
    h = heights()
    builder.box((-cx, -cy, Z_STYLOBATE), (cx, cy, h["ceiling"]), MARBLE, bottom=False, top=False)
    frieze_band(builder, cx, cy, h["capitals"] - 1.25, h["capitals"] - 0.2, "chars", 13, inset=0.0)
    moulding_band(builder, cx + 0.005, cy + 0.005, h["capitals"] - 0.2, h["capitals"] - 0.02)
    door = MeshBuilder()
    door.oriented([(-cx - 0.02, -1.4, Z_STYLOBATE), (-cx - 0.02, 1.4, Z_STYLOBATE),
                   (-cx - 0.02, 1.4, Z_STYLOBATE + 5.2), (-cx - 0.02, -1.4, Z_STYLOBATE + 5.2)], (-1, 0, 0), PAINT)
    door.tint(0, (0.3, 0.22, 0.16))
    builder.merge(door)


def coffers(builder):
    h = heights()
    z = h["ceiling"]
    xs, ys = axes(COLUMNS[0]), axes(COLUMNS[1])
    outer_x, outer_y = xs[-1] - 0.55, ys[-1] - 0.55
    cx, cy = CELLA
    for x0, x1, y0, y1 in ((-outer_x, outer_x, -outer_y, -cy), (-outer_x, outer_x, cy, outer_y),
                           (-outer_x, -cx, -cy, cy), (cx, outer_x, -cy, cy)):
        corners = [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)]
        tinted(builder, (0.20, 0.34, 0.66), lambda corners=corners: builder.oriented(corners, (0, 0, -1), PAINT))
        nx = max(int((x1 - x0) / 1.5), 1)
        ny = max(int((y1 - y0) / 1.5), 1)
        for k in range(nx + 1):
            x = x0 + (x1 - x0) * k / nx
            builder.box((x - 0.09, y0, z - 0.22), (x + 0.09, y1, z - 0.001), MARBLE, top=False)
        for k in range(ny + 1):
            y = y0 + (y1 - y0) * k / ny
            builder.box((x0, y - 0.09, z - 0.22), (x1, y + 0.09, z - 0.001), MARBLE, top=False)


ENTABLATURE_PROFILE = [(-0.7, 0.0), (0.40, 0.0), (0.40, 0.30), (0.43, 0.30), (0.43, 0.62), (0.46, 0.62), (0.46, 0.95),
                       (0.53, 1.0), (0.53, 1.05), (0.50, 1.05), (0.50, 1.40), (0.74, 1.47), (0.74, 1.50),
                       (1.06, 1.52), (1.06, 1.94), (1.0, 1.97), (1.14, 2.12), (1.16, ENTABLATURE),
                       (-0.7, ENTABLATURE)]


def entablature(builder):
    h = heights()
    z = h["capitals"]
    xs, ys = axes(COLUMNS[0]), axes(COLUMNS[1])
    path = [(xs[0], ys[0], z), (xs[-1], ys[0], z), (xs[-1], ys[-1], z), (xs[0], ys[-1], z)]
    builder.sweep(path, ENTABLATURE_PROFILE, MARBLE, closed=True)
    for start, end in ring_runs(xs[-1], ys[-1]):
        frame, length = run_frame(start, end, z)
        run = MeshBuilder()
        greek.band(run, -0.54, length + 0.54, 0.535, 0.96, 1.04, "kymation", "medium")
        count = int((length + 1.0) / 0.27)
        for k in range(count + 1):
            x = -0.5 + k * 0.27
            run.box((x - 0.08, 0.5, 1.08), (x + 0.08, 0.66, 1.38), MARBLE, bottom=False)
        greek.band(run, -1.16, length + 1.16, 1.165, 2.14, ENTABLATURE - 0.02, "kymation", "medium")
        spouts = int((length + 2.0) / 1.5)
        for k in range(spouts + 1):
            x = -1.0 + k * (length + 2.0) / spouts
            tinted(run, LION_BODY, lambda x=x: run.box((x - 0.12, 1.16, 2.16), (x + 0.12, 1.4, 2.32), MARBLE))
        builder.merge(run, frame)


def pyramid(builder):
    h = heights()
    z = h["roof"]
    xs, ys = axes(COLUMNS[0]), axes(COLUMNS[1])
    hx0, hy0 = xs[-1] + 1.1, ys[-1] + 1.1
    tx, ty = TOP_PLATFORM
    first = len(builder.polygons)
    builder.box((-hx0, -hy0, z), (hx0, hy0, z + STEP_RISE), MARBLE, bottom=False)
    sx0, sy0 = hx0 - LEDGE, hy0 - LEDGE
    for k in range(1, STEPS):
        t = (k - 1) / (STEPS - 2)
        hx = sx0 + (tx - sx0) * t
        hy = sy0 + (ty - sy0) * t
        builder.box((-hx, -hy, z + k * STEP_RISE), (hx, hy, z + (k + 1) * STEP_RISE), MARBLE, bottom=False)
    builder.tint(first, (0.97, 0.95, 0.9))
    return {"ledge": (hx0 - LEDGE / 2, hy0 - LEDGE / 2, z + STEP_RISE)}


def quadriga_base(builder):
    h = heights()
    z = h["pyramid_top"]
    bx, by, bh = BASE
    builder.box((-bx - 0.25, -by - 0.25, z), (bx + 0.25, by + 0.25, z + 0.35), MARBLE, bottom=False)
    builder.box((-bx, -by, z + 0.35), (bx, by, z + bh - 0.35), MARBLE, bottom=False, top=False)
    moulding_band(builder, bx + 0.255, by + 0.255, z + 0.1, z + 0.33)
    frieze_band(builder, bx, by, z + 1.35, z + 2.25, "centaures", 29)
    builder.box((-bx - 0.25, -by - 0.25, z + bh - 0.35), (bx + 0.25, by + 0.25, z + bh), MARBLE, bottom=False)
    moulding_band(builder, bx + 0.255, by + 0.255, z + bh - 0.33, z + bh - 0.05)


def big_horse(colour, mane, raised=0.0):
    builder = MeshBuilder()
    dark = tuple(c * 0.6 for c in colour)
    s = 2.0
    body = 1.12 * s
    figures.ellipsoid(builder, (0.0, 0.0, body), (0.27 * s, 0.8 * s, 0.33 * s), colour, 10, 6)
    figures.tube(builder, [(0.0, 0.5 * s, body + 0.1 * s), (0.0, 0.78 * s, body + 0.5 * s),
                           (0.0, 0.86 * s, body + 0.66 * s)], [0.2 * s, 0.13 * s, 0.1 * s], colour, 8, cap=False)
    figures.tube(builder, [(0.0, 0.84 * s, body + 0.7 * s), (0.0, 1.0 * s, body + 0.58 * s),
                           (0.0, 1.16 * s, body + 0.36 * s)], [0.1 * s, 0.085 * s, 0.06 * s], colour, 8)
    figures.tube(builder, [(0.0, 0.42 * s, body + 0.33 * s), (0.0, 0.7 * s, body + 0.66 * s),
                           (0.0, 0.84 * s, body + 0.82 * s)], [0.04 * s, 0.05 * s, 0.03 * s], mane, 5, squash=2.2)
    for side in (-1, 1):
        figures.tube(builder, [(side * 0.05 * s, 0.9 * s, body + 0.78 * s),
                               (side * 0.07 * s, 0.87 * s, body + 0.92 * s)], [0.03 * s, 0.0], colour, 4)
    for front in (-1, 1):
        for side in (-1, 1):
            x, y = side * 0.15 * s, front * 0.5 * s
            if front > 0 and side > 0 and raised > 0:
                path = [(x, y, body - 0.1 * s), (x, y + 0.22 * s, 0.75 * s), (x, y + 0.12 * s, 0.45 * s)]
            else:
                path = [(x, y, body - 0.1 * s), (x, y, 0.45 * s), (x, y, 0.0)]
            figures.tube(builder, path, [0.1 * s, 0.055 * s, 0.05 * s], [colour, dark], 6, cap=False)
    figures.tube(builder, [(0.0, -0.78 * s, body + 0.14 * s), (0.0, -0.92 * s, body - 0.2 * s),
                           (0.0, -0.9 * s, body - 0.65 * s)], [0.06 * s, 0.07 * s, 0.025 * s], mane, 5)
    figures.tube(builder, [(0.0, 1.0 * s, body + 0.62 * s), (0.0, 0.62 * s, body + 0.2 * s)],
                 [0.012 * s, 0.012 * s], (0.62, 0.42, 0.18), 3, cap=False)
    return builder


def quadriga():
    builder = MeshBuilder()
    for index, colour in enumerate((BROWN_HORSE, WHITE_HORSE, WHITE_HORSE, BROWN_HORSE)):
        x = (index - 1.5) * 1.12
        horse = big_horse(colour, RED, raised=1.0 if index in (1, 2) else 0.0)
        builder.merge(horse, Matrix.Translation((x, 0.9, 0.0)))
    car = MeshBuilder()
    car.box((-1.15, -2.85, 0.95), (1.15, -1.75, 1.15), PAINT)
    car.box((-1.15, -1.95, 1.15), (1.15, -1.75, 2.3), PAINT)
    for side in (-1, 1):
        car.box((side * 1.15 - 0.1, -2.85, 1.15), (side * 1.15 + 0.1, -1.75, 2.0), PAINT)
    car.tint(0, RED)
    builder.merge(car)
    hub = MeshBuilder()
    for side in (-1, 1):
        wheel(hub, side * 1.3, -2.3, 1.1, 0.16, spokes=4)
    builder.merge(marble_copy(hub, 0.0, PAINT).tint(0, OCHRE))
    figures.tube(builder, [(0.0, -1.8, 1.05), (0.0, 0.2, 1.55), (0.0, 0.9, 2.4)], [0.08, 0.08, 0.07],
                 (0.62, 0.42, 0.18), 5)
    figures.tube(builder, [(-1.9, 1.2, 2.55), (1.9, 1.2, 2.55)], [0.07, 0.07], (0.62, 0.42, 0.18), 5)
    return marble_copy(builder, 1.0)


def lion():
    builder = MeshBuilder()
    figures.ellipsoid(builder, (0.0, 0.0, 0.62), (0.26, 0.62, 0.27), LION_BODY, 8, 5)
    figures.ellipsoid(builder, (0.0, 0.48, 0.78), (0.34, 0.3, 0.36), LION_MANE, 8, 5)
    figures.ellipsoid(builder, (0.0, 0.74, 0.86), (0.17, 0.2, 0.17), LION_BODY, 7, 4)
    figures.ellipsoid(builder, (0.0, 0.92, 0.8), (0.08, 0.08, 0.06), (0.7, 0.24, 0.16), 5, 3)
    for front, lift in ((1, 0.0), (-1, 0.0)):
        for side in (-1, 1):
            stride = 0.12 * side * front
            figures.tube(builder, [(side * 0.14, front * 0.4, 0.55), (side * 0.14, front * 0.4 + stride, 0.25),
                                   (side * 0.14, front * 0.4 + stride, 0.0)], [0.1, 0.07, 0.07], LION_BODY, 6,
                         cap=False)
    figures.tube(builder, [(0.0, -0.6, 0.7), (0.0, -0.95, 0.45), (0.0, -1.1, 0.58)], [0.04, 0.035, 0.05],
                 LION_MANE, 4)
    return marble_copy(builder, 1.0)


STATUE_KINDS = {
    "statue_dynaste": lambda: figures.man_himation(figures.PURPLE, figures.SKIN, figures.HAIR, figures.HAIR,
                                                   right_hand=(0.3, 0.3, 1.32)),
    "statue_reine": lambda: figures.woman_peplos(figures.WOAD, figures.MADDER, veil=figures.CRIMSON),
    "statue_dame": lambda: figures.woman_peplos(figures.SAFFRON, figures.MADDER, veil=figures.WOOL_WHITE),
    "statue_guerrier": lambda: figures.hoplite(),
    "statue_perse": lambda: figures.persian_archer(),
    "statue_cavalier": lambda: figures.persian_rider(),
    "statue_pretre": lambda: figures.priest(figures.WOOL_WHITE, figures.MADDER),
    "statue_chasseur": lambda: figures.ephebe(figures.WOOL_WHITE, figures.CRIMSON),
}


def statue(kind):
    source = STATUE_KINDS[kind]()
    lowest = min(p[2] for p in source.positions)
    base = MeshBuilder()
    base.box((-0.35, -0.35, 0.0), (0.35, 0.35, 0.22), BLUE_STONE, bottom=False)
    figure = marble_copy(source, 0.55)
    base.merge(figure, Matrix.Translation((0.0, 0.0, 0.22 - lowest)))
    return base


def perimeter_points(hx, hy, spacing, margin):
    points = []
    for (x0, y0), (x1, y1) in ring_runs(hx, hy):
        length = math.hypot(x1 - x0, y1 - y0)
        count = max(int((length - 2 * margin) / spacing), 1)
        dx, dy = (x1 - x0) / length, (y1 - y0) / length
        outward = math.atan2(dx, -dy)
        for k in range(count + 1):
            t = margin + (length - 2 * margin) * k / count
            points.append((x0 + dx * t, y0 + dy * t, outward))
    return points


def statue_placements(rng):
    out = {}
    families = list(STATUE_KINDS)
    for (tier_index, scale, spacing, inset) in ((0, 1.0, 4.4, 0.8), (1, 1.32, 4.6, 0.75)):
        (hx, hy), _, z1 = TIERS[tier_index]
        nx, ny = TIERS[tier_index + 1][0]
        ledge = ((hx - nx) / 2, (hy - ny) / 2)
        for x, y, angle in perimeter_points(nx + ledge[0], ny + ledge[1], spacing, 2.2):
            key = rng.choice(families)
            if key == "statue_cavalier" and scale > 1.2:
                key = "statue_guerrier"
            out.setdefault(key, []).append(Matrix.Translation((x, y, z1)) @ Matrix.Rotation(angle + math.pi / 2, 4, "Z")
                                           @ Matrix.Scale(scale, 4))
    xs, ys = axes(COLUMNS[0]), axes(COLUMNS[1])
    gaps = [((a + b) / 2, ys[0] + 1.5, -math.pi / 2) for a, b in zip(xs[::2], xs[1::2])]
    gaps += [((a + b) / 2, ys[-1] - 1.5, math.pi / 2) for a, b in zip(xs[1::2], xs[2::2])]
    gaps += [(xs[0] + 1.5, (a + b) / 2, math.pi) for a, b in zip(ys[::2], ys[1::2])]
    gaps += [(xs[-1] - 1.5, (a + b) / 2, 0.0) for a, b in zip(ys[1::2], ys[2::2])]
    for x, y, angle in gaps:
        key = rng.choice(("statue_dynaste", "statue_reine", "statue_dame", "statue_pretre"))
        out.setdefault(key, []).append(Matrix.Translation((x, y, Z_STYLOBATE)) @ Matrix.Rotation(angle - math.pi / 2,
                                                                                                4, "Z")
                                       @ Matrix.Scale(1.6, 4))
    return out


def build(scene, origin, level):
    rng = random.Random(345)
    root_matrix = Matrix.Translation((origin[0], origin[1], level))
    body = MeshBuilder()
    podium(body)
    plinths(body)
    cella(body)
    coffers(body)
    entablature(body)
    ledge = pyramid(body)
    quadriga_base(body)
    scene.unique("mausolee", body, root_matrix)
    h = heights()
    column = greek.ionic_template(DIAMETER, COLUMN_HEIGHT - PLINTH, "medium")
    matrices = [root_matrix @ Matrix.Translation((x, y, Z_STYLOBATE + PLINTH)) for x, y in column_points()]
    scene.instances("mausolee", column[0], column[1], matrices)
    team = quadriga()
    scene.unique("mausolee", team, root_matrix @ Matrix.Translation((0.0, 0.0, h["base_top"]))
                 @ Matrix.Rotation(-math.pi / 2, 4, "Z"))
    lx, ly, lz = ledge["ledge"]
    lions = []
    for x, y, angle in perimeter_points(lx, ly, 3.1, 1.4):
        lions.append(root_matrix @ Matrix.Translation((x, y, lz)) @ Matrix.Rotation(angle + math.pi / 2, 4, "Z"))
    scene.instances("mausolee", "lion_du_toit", lion, lions)
    for key, matrices in statue_placements(rng).items():
        scene.instances("mausolee", key, lambda key=key: statue(key), [root_matrix @ m for m in matrices])
    return {"level": level, "heights": {k: round(level + v, 2) for k, v in h.items()},
            "total_height": round(h["top"], 2), "columns": len(column_points()), "lions": len(lions),
            "statues": sum(len(v) for v in statue_placements(random.Random(345)).values())}


def terrace_walls(scene, ground, level):
    from . import mausolee_plan as plan
    tx, ty, hu, hv = plan.TERRACE
    retaining = MeshBuilder()
    enclosure_wall = MeshBuilder()
    corners = [(tx - hu, ty - hv), (tx + hu, ty - hv), (tx + hu, ty + hv), (tx - hu, ty + hv)]
    px, py = plan.PROPYLON
    gate = 7.0
    for (x0, y0), (x1, y1) in zip(corners, corners[1:] + corners[:1]):
        length = math.hypot(x1 - x0, y1 - y0)
        dx, dy = (x1 - x0) / length, (y1 - y0) / length
        nx, ny = dy, -dx
        steps = max(int(length / 6.0), 1)
        for k in range(steps):
            a = k * length / steps
            b = (k + 1) * length / steps
            ax, ay = x0 + dx * a, y0 + dy * a
            bx, by = x0 + dx * b, y0 + dy * b
            low = min(ground(ax + nx * 3.0, ay + ny * 3.0), ground(bx + nx * 3.0, by + ny * 3.0)) - 1.5
            quad = [(ax, ay), (bx, by), (bx + nx * 1.2, by + ny * 1.2), (ax + nx * 1.2, ay + ny * 1.2)]
            retaining.prism(quad, min(low, level - 1.0), level + 0.25, BLUE_STONE, bottom=False)
            mid_x, mid_y = (ax + bx) / 2, (ay + by) / 2
            if abs(x1 - x0) < 1.0 and x0 > tx and abs(mid_y - py) < gate / 2 + 3.0:
                continue
            wall = [(ax, ay), (bx, by), (bx - nx * 0.8, by - ny * 0.8), (ax - nx * 0.8, ay - ny * 0.8)]
            enclosure_wall.prism(wall, level, level + 2.56, MARBLE, bottom=False)
            enclosure_wall.prism([(ax + nx * 0.05, ay + ny * 0.05), (bx + nx * 0.05, by + ny * 0.05),
                                  (bx - nx * 0.85, by - ny * 0.85), (ax - nx * 0.85, ay - ny * 0.85)],
                                 level + 2.56, level + 2.78, MARBLE, bottom=False)
    retaining.tint(0, (0.92, 0.96, 1.0))
    scene.unique("terrasse", retaining)
    scene.unique("terrasse", enclosure_wall)
    return corners


def propylon_site(scene, ground, level):
    from . import mausolee_plan as plan
    rng = random.Random(77)
    px, py = plan.PROPYLON
    site = MeshBuilder()
    site.box((-3.0, -8.0, -5.0), (6.0, 8.0, 0.35), BLUE_STONE, bottom=False)
    for side in (-1, 1):
        site.box((-2.6, side * 4.2 - 1.0, 0.35), (5.4, side * 4.2 + 1.0, 0.35 + rng.choice((2.2, 3.4))), MARBLE,
                 bottom=False)
    for x in (-1.5, 4.3):
        site.box((x - 0.6, -2.4, 0.35), (x + 0.6, -1.2, 0.6), BLUE_STONE, bottom=False)
    scaffold(site, -2.8, 5.6, 6.5, (2.4, 4.6), 0.2, rng, Matrix.Translation((0.0, 5.4, 0.0)))
    scaffold(site, -2.8, 5.6, 6.5, (2.4, 4.6), 0.2, rng, Matrix.Translation((0.0, -7.4, 0.0)))
    crane = MeshBuilder()
    for side in (-1, 1):
        figures.tube(crane, [(side * 1.6, -1.0, 0.0), (0.0, 1.2, 8.5)], [0.14, 0.11], figures.WOOD, 5)
    figures.tube(crane, [(0.0, -2.8, 0.0), (0.0, 1.2, 8.5)], [0.12, 0.1], figures.WOOD, 5)
    figures.tube(crane, [(0.0, 1.2, 8.5), (0.0, 1.6, 2.0)], [0.02, 0.02], (0.7, 0.62, 0.48), 3)
    figures.tube(crane, [(-0.9, -1.4, 1.3), (0.9, -1.4, 1.3)], [0.12, 0.12], figures.WOOD, 6)
    site.merge(crane, Matrix.Translation((-8.0, -3.0, 0.0)))
    scene.unique("terrasse", site, Matrix.Translation((px, py, level)))
    blocks = []
    for k in range(9):
        bx = px + rng.uniform(8.0, 24.0)
        by = py + rng.uniform(-12.0, 12.0)
        blocks.append(placement(bx, by, ground(bx, by) - 0.05, rng.uniform(-0.3, 0.3)))
    scene.instances("terrasse", "bloc_en_attente", lambda: block((1.6, 0.8, 0.7)), blocks)
    rest = MeshBuilder()
    altar(rest, 3.0, 2.0, 1.2, MARBLE, 1)
    altar_point = (28.0, -32.0)
    scene.unique("terrasse", rest, Matrix.Translation((altar_point[0], altar_point[1], level)))
    return {"gate": [px, py, level], "altar": [altar_point[0], altar_point[1], level + 1.5]}
