import math
import random

from mathutils import Matrix, Vector

from .acropole_statues import ellipsoid, folds, panel, squash, tube, winged_victory
from .geometry import MeshBuilder
from .greek import relief_human

TAU = 2 * math.pi
GOLD = "gold"
IVORY = "ivory"
EBONY = "ebony"
PAINT = "greek_paint"
ELEUSIS = "eleusis"
MARBLE = "marble"

SCALE = 7.6
BASE = (6.65, 9.93, 1.0)
THRONE_Y = -0.12
BLUE = (0.10, 0.22, 0.52)
PANELS = ((0.62, 0.20, 0.12), (0.72, 0.52, 0.24), (0.20, 0.34, 0.26), (0.55, 0.30, 0.20))


def mono(source, material):
    copy = MeshBuilder()
    copy.points(source.positions)
    for indices, smooth in zip(source.polygons, source.polygon_smooth):
        copy.face(list(indices), material, smooth)
    return copy


def tinted(builder, colour, action):
    first = len(builder.polygons)
    action()
    builder.tint(first, colour)


def small_figure(builder, at, height, material, robe=None, seed=0):
    x, y, z = at
    rng = random.Random(seed)
    lean = rng.uniform(-0.08, 0.08)
    body = robe or material
    builder.lathe([(0.0, 0.0), (0.2 * height, 0.0), (0.16 * height, 0.45 * height), (0.13 * height, 0.75 * height),
                   (0.05 * height, 0.82 * height), (0.0, 0.82 * height)], 8, body, smooth=True,
                  matrix=Matrix.Translation((x, y, z)) @ Matrix.Rotation(lean, 4, "Y") @ Matrix.Diagonal((1.0, 0.8, 1.0, 1.0)))
    ellipsoid(builder, (x + lean * 0.8 * height, y, z + 0.9 * height), (0.07 * height, 0.08 * height, 0.09 * height),
              material, 8, 4)


def throne(builder):
    y0, y1 = THRONE_Y - 0.56, THRONE_Y
    x = 0.4
    seat = 0.56
    arm = 0.86
    back_top = 1.5
    post = 0.075
    for side in (-1, 1):
        for y, top in ((y1 - post / 2, arm), (y0 + post / 2, back_top)):
            builder.centered_box((side * (x - post / 2), y, top / 2), (post, post, top), EBONY)
            for k in range(4 if top < 1.0 else 6):
                z = 0.08 + k * 0.13
                builder.centered_box((side * (x - post / 2), y, z), (post + 0.012, post + 0.012, 0.02), GOLD)
        builder.centered_box((side * (x - post / 2), (y0 + y1) / 2, arm + 0.02), (post + 0.02, y1 - y0 + 0.04, 0.04),
                             EBONY)
        sphinx = Vector((side * (x - post / 2), y1 + 0.02, arm + 0.06))
        ellipsoid(builder, sphinx, (0.035, 0.07, 0.04), GOLD, 8, 4)
        ellipsoid(builder, sphinx + Vector((0.0, 0.05, 0.06)), (0.025, 0.025, 0.035), IVORY, 8, 4)
        for k in range(2):
            builder.centered_box((side * (x - post / 2), y0 + 0.15 + k * 0.22, (seat + arm) / 2), (0.03, 0.03, arm - seat),
                                 IVORY)
        tinted(builder, PANELS[(side + 1) // 2], lambda side=side: builder.centered_box(
            (side * (x - 0.012), (y0 + y1) / 2, 0.28), (0.02, y1 - y0 - post * 2, 0.4), PAINT))
        for k in range(3):
            fx = side * (0.06 + 0.1 * k)
            small_figure(builder, (fx, y0 + 0.03, back_top), 0.1, IVORY, GOLD, seed=side * 10 + k)
    builder.centered_box((0.0, (y0 + y1) / 2, seat - 0.04), (2 * x, y1 - y0, 0.08), EBONY)
    builder.centered_box((0.0, (y0 + y1) / 2, seat + 0.005), (2 * x - 0.04, y1 - y0 - 0.04, 0.012), GOLD)
    builder.centered_box((0.0, y0 + 0.03, (seat + back_top) / 2), (2 * x, 0.06, back_top - seat), EBONY)
    for k in range(5):
        builder.centered_box((0.0, y0 + 0.065, seat + 0.12 + k * 0.2), (2 * x - 0.1, 0.012, 0.03), GOLD)
    builder.centered_box((0.0, y0 + 0.03, back_top + 0.01), (2 * x + 0.04, 0.09, 0.03), GOLD)
    tinted(builder, BLUE, lambda: builder.centered_box((0.0, y1 - 0.02, 0.27), (2 * x - post * 2, 0.02, 0.42), PAINT))
    tinted(builder, PANELS[2], lambda: builder.centered_box((0.0, y0 + 0.04, 0.27), (2 * x - post * 2, 0.02, 0.42),
                                                            PAINT))
    for k in range(4):
        small_figure(builder, (-0.24 + 0.16 * k, y1 + 0.01, 0.47), 0.08, GOLD, seed=40 + k)
    builder.centered_box((0.0, y1 - 0.02, 0.5), (2 * x, 0.05, 0.03), GOLD)
    builder.centered_box((0.0, y1 + 0.22, 0.05), (0.62, 0.3, 0.1), EBONY)
    builder.centered_box((0.0, y1 + 0.37, 0.05), (0.62, 0.008, 0.08), GOLD)
    for side in (-1, 1):
        lion = Vector((side * 0.27, y1 + 0.36, 0.13))
        ellipsoid(builder, lion, (0.04, 0.07, 0.04), GOLD, 8, 4)
        ellipsoid(builder, lion + Vector((0.0, 0.06, 0.04)), (0.032, 0.03, 0.035), GOLD, 8, 4)


def drape_profile():
    profile = []
    for k in range(29):
        x = -0.31 + 0.62 * k / 28
        leg = max(0.105 * math.sqrt(max(0.0, 1.0 - ((x - side * 0.13) / 0.12) ** 2)) for side in (-1, 1))
        sag = 0.045 * (1.0 - abs(x) / 0.31)
        edge = max(0.0, min(1.0, (abs(x) - 0.2) / 0.1))
        bulge = max(leg, sag) - 0.07 * edge * edge + 0.007 * math.sin(x * 70.0)
        profile.append((x, -bulge))
    return profile


def double_sided(builder, piece):
    builder.merge(piece)
    flipped = MeshBuilder()
    flipped.points(piece.positions)
    for indices, material, smooth in zip(piece.polygons, piece.polygon_materials, piece.polygon_smooth):
        flipped.face(list(reversed(indices)), piece.materials[material], smooth)
    builder.merge(flipped)


def figure(builder):
    yc = THRONE_Y - 0.26
    hip = 0.64
    knee_y = THRONE_Y + 0.12
    for side in (-1, 1):
        knee = Vector((side * 0.13, knee_y, hip - 0.02))
        ankle = Vector((side * 0.14, THRONE_Y + 0.2, 0.16))
        tube(builder, [knee, ankle], [0.07, 0.05], IVORY, 12)
        toe = Vector((side * 0.15, THRONE_Y + 0.36, 0.12))
        tube(builder, [ankle, toe], [0.045, 0.035], IVORY, 10)
        builder.centered_box(((ankle.x + toe.x) / 2, (ankle.y + toe.y) / 2 + 0.01, 0.11), (0.1, 0.22, 0.025), GOLD)
    path = [(0.0, yc - 0.03, hip + 0.01), (0.0, (yc + knee_y) / 2, hip + 0.005), (0.0, knee_y - 0.02, hip - 0.005),
            (0.0, knee_y + 0.05, hip - 0.06), (0.0, knee_y + 0.08, hip - 0.2), (0.0, knee_y + 0.1, 0.4),
            (0.0, knee_y + 0.12, 0.18)]
    lap = MeshBuilder()
    lap.sweep(path, drape_profile(), GOLD, facade_normal=(1.0, 0.0, 0.0), caps=False, smooth=True)
    double_sided(builder, lap)
    builder.lathe([(0.19, hip - 0.08), (0.222, hip), (0.205, hip + 0.1), (0.175, hip + 0.16)], 28, GOLD, smooth=True,
                  matrix=squash(0.78, (0.0, yc, 0.0)), radius_scale=folds(12, 0.05), caps=False)
    builder.lathe([(0.17, hip + 0.1), (0.18, hip + 0.22), (0.2, hip + 0.34), (0.235, hip + 0.44),
                   (0.228, hip + 0.49), (0.12, hip + 0.535), (0.0, hip + 0.54)], 28, IVORY, smooth=True,
                  matrix=squash(0.62, (0.0, yc + 0.01, 0.0)))
    ellipsoid(builder, (0.075, yc + 0.11, hip + 0.4), (0.075, 0.03, 0.045), IVORY, 10, 5)
    ellipsoid(builder, (0.0, yc + 0.1, hip + 0.22), (0.1, 0.03, 0.09), IVORY, 10, 5)
    builder.lathe([(0.2, hip + 0.04), (0.215, hip + 0.3), (0.245, hip + 0.46), (0.2, hip + 0.52), (0.1, hip + 0.545)],
                  24, GOLD, smooth=True, matrix=squash(0.68, (0.0, yc - 0.004, 0.0)), radius_scale=folds(10, 0.06),
                  start=math.radians(100), sweep=math.radians(200), caps=False)
    ellipsoid(builder, (-0.215, yc, hip + 0.48), (0.085, 0.095, 0.065), GOLD, 12, 6)
    tube(builder, [(-0.15, yc + 0.12, hip + 0.47), (-0.17, yc + 0.16, hip + 0.25), (-0.2, yc + 0.17, hip + 0.03)],
         [0.045, 0.06, 0.075], GOLD, 10)
    ellipsoid(builder, (0.232, yc, hip + 0.45), (0.07, 0.068, 0.08), IVORY, 12, 6)
    neck = hip + 0.54
    tube(builder, [(0.0, yc, neck - 0.02), (0.0, yc + 0.01, neck + 0.08)], [0.058, 0.052], IVORY, 12)
    head = Vector((0.0, yc + 0.02, neck + 0.17))
    ellipsoid(builder, head, (0.085, 0.095, 0.108), IVORY, 26, 14)
    ellipsoid(builder, head + Vector((0.0, -0.016, 0.034)), (0.092, 0.096, 0.098), GOLD, 24, 12)
    ellipsoid(builder, head + Vector((0.0, -0.035, -0.04)), (0.095, 0.08, 0.09), GOLD, 14, 7)
    ellipsoid(builder, head + Vector((0.0, 0.03, -0.092)), (0.072, 0.058, 0.082), GOLD, 20, 10)
    ellipsoid(builder, head + Vector((0.0, 0.05, -0.15)), (0.045, 0.035, 0.05), GOLD, 12, 6)
    ellipsoid(builder, head + Vector((0.0, 0.088, -0.038)), (0.042, 0.014, 0.012), GOLD, 8, 4)
    ellipsoid(builder, head + Vector((0.0, 0.092, -0.008)), (0.012, 0.022, 0.02), IVORY, 6, 3)
    for side in (-1, 1):
        ellipsoid(builder, head + Vector((side * 0.032, 0.083, 0.014)), (0.015, 0.006, 0.008), "eye_stone", 8, 4)
    wreath = [head + Vector((0.098 * math.cos(a), 0.105 * math.sin(a) - 0.014, 0.05)) for a in
              [TAU * k / 16 for k in range(17)]]
    tube(builder, wreath, [0.014] * len(wreath), GOLD, 6, cap=False)
    for k in range(20):
        a = TAU * k / 20
        ellipsoid(builder, head + Vector((0.106 * math.cos(a), 0.112 * math.sin(a) - 0.014, 0.056)),
                  (0.022, 0.012, 0.009), GOLD, 5, 3)
    shoulder = Vector((0.235, yc, hip + 0.46))
    elbow = Vector((0.3, yc + 0.05, hip + 0.22))
    hand = Vector((0.31, THRONE_Y + 0.1, hip + 0.22))
    tube(builder, [shoulder, elbow], [0.062, 0.05], IVORY, 12)
    tube(builder, [elbow, hand], [0.05, 0.038], IVORY, 12)
    ellipsoid(builder, hand + Vector((0.0, 0.03, 0.0)), (0.042, 0.055, 0.022), IVORY, 10, 5)
    nike = hand + Vector((0.0, 0.03, 0.02))
    winged_victory(builder, nike, 0.27, GOLD)
    unit = 0.27 / 1.75
    ellipsoid(builder, nike + Vector((0.0, 0.01 * unit, 1.6 * unit)), (0.092 * unit, 0.1 * unit, 0.115 * unit), IVORY,
              10, 6)
    tube(builder, [nike + Vector((0.12 * unit, 0.05 * unit, 1.35 * unit)), nike + Vector((0.3 * unit, 0.3 * unit, 1.2 * unit))],
         [0.04 * unit, 0.03 * unit], IVORY, 6)
    left_shoulder = Vector((-0.235, yc, hip + 0.46))
    left_elbow = Vector((-0.36, yc + 0.04, hip + 0.3))
    left_hand = Vector((-0.45, THRONE_Y + 0.07, neck - 0.02))
    tube(builder, [left_shoulder, left_elbow], [0.072, 0.062], GOLD, 12)
    tube(builder, [left_elbow, left_hand], [0.048, 0.04], IVORY, 12)
    ellipsoid(builder, left_hand, (0.045, 0.045, 0.06), IVORY, 10, 5)
    foot = Vector((-0.47, THRONE_Y + 0.09, 0.0))
    top = Vector((-0.45, THRONE_Y + 0.07, 1.55))
    tube(builder, [foot, top], [0.02, 0.018], GOLD, 8)
    for k in range(9):
        z = 0.12 + k * 0.16
        tinted(builder, PANELS[k % 4], lambda z=z: tube(builder, [foot.lerp(top, z / 1.55),
                                                                  foot.lerp(top, (z + 0.03) / 1.55)],
                                                        [0.024, 0.024], PAINT, 8))
    eagle = top + Vector((0.0, 0.0, 0.05))
    ellipsoid(builder, eagle, (0.035, 0.06, 0.045), GOLD, 8, 4)
    ellipsoid(builder, eagle + Vector((0.0, 0.05, 0.05)), (0.022, 0.026, 0.024), GOLD, 6, 3)
    for side in (-1, 1):
        panel(builder, [(0.0, 0.0), (side * 0.06, 0.06), (side * 0.085, 0.025), (side * 0.04, -0.03)], -0.006, 0.006,
              GOLD, Matrix.Translation(eagle + Vector((side * 0.02, -0.01, 0.0))))


def base_reliefs(builder, width, depth, height):
    rng = random.Random(11)
    figures = MeshBuilder()
    count = 19
    for k in range(count):
        x = -width / 2 + 0.55 + k * (width - 1.1) / (count - 1)
        relief_human(figures, x, depth / 2, 0.22, height - 0.42, 0.06, rng.uniform(-0.15, 0.15),
                     rng.choice((-0.9, 0.9, -0.3)))
    builder.merge(mono(figures, GOLD))


def statue():
    builder = MeshBuilder()
    width, depth, height = BASE
    builder.box((-width / 2 - 0.12, -depth / 2 - 0.12, 0.0), (width / 2 + 0.12, depth / 2 + 0.12, 0.18), ELEUSIS,
                bottom=False)
    builder.box((-width / 2, -depth / 2, 0.18), (width / 2, depth / 2, height - 0.14), ELEUSIS, bottom=False,
                top=False)
    builder.box((-width / 2 - 0.1, -depth / 2 - 0.1, height - 0.14), (width / 2 + 0.1, depth / 2 + 0.1, height),
                ELEUSIS, bottom=False)
    base_reliefs(builder, width, depth, height)
    body = MeshBuilder()
    throne(body)
    figure(body)
    builder.merge(body, Matrix.Translation((0.0, 0.25, height)) @ Matrix.Scale(SCALE, 4))
    return builder


def statue_height():
    return BASE[2] + SCALE * 1.6


def face_height():
    return BASE[2] + SCALE * (0.64 + 0.54 + 0.17)


def face_offset():
    return 0.25 + SCALE * (THRONE_Y - 0.26 + 0.02)
