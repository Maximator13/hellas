import math

from mathutils import Matrix, Vector

from .geometry import MeshBuilder

TAU = 2 * math.pi
GOLD = "gold"
IVORY = "ivory"
BRONZE = "bronze_statue"
MARBLE = "marble"
PAINT = "greek_paint"
POROS = "poros"


def folds(count, depth, phase=0.0):
    return lambda angle: 1.0 + depth * math.sin(count * angle + phase) + 0.4 * depth * math.sin(2.3 * count * angle)


def squash(depth=0.82, at=(0.0, 0.0, 0.0)):
    return Matrix.Translation(at) @ Matrix.Diagonal((1.0, depth, 1.0, 1.0))


def tube(builder, path, radii, material, sides=12, cap=True):
    path = [Vector(p) for p in path]
    rings = []
    u = None
    for index, (point, radius) in enumerate(zip(path, radii)):
        axis = (path[min(index + 1, len(path) - 1)] - path[max(index - 1, 0)]).normalized()
        hint = u if u is not None else Vector((0.0, 0.0, 1.0))
        u = hint - axis * hint.dot(axis)
        if u.length < 1e-5:
            u = axis.orthogonal()
        u.normalize()
        v = axis.cross(u).normalized()
        rings.append([builder.point(point + (u * math.cos(TAU * k / sides) + v * math.sin(TAU * k / sides)) * radius)
                      for k in range(sides)])
    for lower, upper in zip(rings[:-1], rings[1:]):
        for k in range(sides):
            j = (k + 1) % sides
            builder.face([lower[k], lower[j], upper[j], upper[k]], material, True)
    if cap:
        builder.face(list(reversed(rings[0])), material)
        builder.face(list(rings[-1]), material)


def ellipsoid(builder, centre, radii, material, segments=16, rings=8):
    profile = [(math.sin(math.pi * k / rings), -math.cos(math.pi * k / rings)) for k in range(rings + 1)]
    builder.lathe(profile, segments, material, smooth=True,
                  matrix=Matrix.Translation(centre) @ Matrix.Diagonal((*radii, 1.0)))


def panel(builder, outline, y0, y1, material, matrix):
    piece = MeshBuilder()
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(outline, outline[1:] + outline[:1]))
    piece.prism(outline if area > 0 else list(reversed(outline)), y0, y1, material)
    swap = Matrix(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)))
    builder.merge(piece, matrix @ swap)


def helmet(builder, centre, metal, crests=3, plume=0.1):
    x, y, z = centre
    builder.lathe([(0.0, 0.125), (0.06, 0.12), (0.098, 0.085), (0.112, 0.03), (0.114, -0.02), (0.108, -0.06)], 18,
                  metal, smooth=True, matrix=Matrix.Translation((x, y - 0.006, z)) @ Matrix.Diagonal((1.0, 1.1, 1.0, 1.0)),
                  start=math.radians(150), sweep=math.radians(240))
    builder.lathe([(0.112, 0.0), (0.118, -0.11), (0.1, -0.14)], 12, metal, smooth=True,
                  matrix=Matrix.Translation((x, y - 0.01, z)), start=math.radians(200), sweep=math.radians(140))
    for k in range(crests):
        offset = (k - (crests - 1) / 2) * 0.055
        height = plume * (1.0 if offset == 0 else 0.75)
        outline = [(0.07, 0.0), (0.0, height * 0.9), (-0.08, height), (-0.17, height * 0.55), (-0.2, -0.05),
                   (-0.11, 0.0)]
        panel(builder, outline, -0.022, 0.022, metal,
              Matrix.Translation((x + offset, y + 0.02, z + 0.11)) @ Matrix.Rotation(math.pi / 2, 4, "Z"))


def winged_victory(builder, at, height, material):
    x, y, z = at
    s = height / 1.75
    builder.lathe([(0.0, 0.0), (0.2 * s, 0.02 * s), (0.17 * s, 0.6 * s), (0.15 * s, 1.0 * s), (0.17 * s, 1.35 * s),
                   (0.06 * s, 1.47 * s), (0.0, 1.47 * s)], 10, material, smooth=True,
                  matrix=Matrix.Translation((x, y, z)) @ Matrix.Diagonal((1.0, 0.8, 1.0, 1.0)))
    ellipsoid(builder, (x, y + 0.01 * s, z + 1.6 * s), (0.085 * s, 0.095 * s, 0.11 * s), material, 10, 6)
    for side in (-1, 1):
        wing = [(0.0, 0.0), (0.35 * s, 0.25 * s), (0.62 * s, 0.75 * s), (0.4 * s, 0.55 * s), (0.2 * s, 0.4 * s),
                (0.05 * s, 0.3 * s)]
        outline = [(side * px, pz) for px, pz in wing]
        panel(builder, outline, -0.01 * s, 0.01 * s, material,
              Matrix.Translation((x + side * 0.08 * s, y - 0.15 * s, z + 1.15 * s)) @ Matrix.Rotation(side * 0.5, 4, "Z"))


def shield(builder, centre, radius, normal, metal, reliefs, rng_seed=7):
    frame = Matrix.Translation(centre) @ Vector((0.0, 0.0, 1.0)).rotation_difference(Vector(normal)).to_matrix().to_4x4()
    builder.lathe([(0.0, 0.07 * radius), (0.5 * radius, 0.055 * radius), (0.95 * radius, 0.0), (radius, -0.02 * radius),
                   (radius * 0.96, -0.05 * radius), (0.0, -0.035 * radius)], 32, metal, smooth=True, matrix=frame)
    builder.lathe([(radius * 0.18, 0.08 * radius), (0.0, 0.1 * radius)], 16, metal, smooth=True, matrix=frame)
    if reliefs:
        for k in range(14):
            angle = TAU * k / 14 + 0.2
            for ring, size in ((0.72, 0.075), (0.42, 0.07)):
                px, py = ring * radius * math.cos(angle + ring), ring * radius * math.sin(angle + ring)
                builder.centered_box((px, py, 0.05 * radius), (size * radius, size * radius * 1.8, 0.04 * radius),
                                     metal, matrix=frame @ Matrix.Rotation(angle, 4, "Z"))


def athena(kind="parthenos"):
    builder = MeshBuilder()
    parthenos = kind == "parthenos"
    robe = GOLD if parthenos else BRONZE
    flesh = IVORY if parthenos else BRONZE
    trim = GOLD if parthenos else BRONZE
    builder.lathe([(0.29, 0.0), (0.27, 0.12), (0.25, 0.45), (0.225, 0.82), (0.2, 1.02)], 44, robe, smooth=True,
                  matrix=squash(0.8), radius_scale=folds(15, 0.05), caps=False)
    builder.lathe([(0.0, 0.0), (0.29, 0.0)], 44, robe, matrix=squash(0.8), radius_scale=folds(15, 0.05), caps=False)
    builder.lathe([(0.19, 1.34), (0.215, 1.12), (0.245, 0.86), (0.235, 0.83)], 44, robe, smooth=True,
                  matrix=squash(0.82), radius_scale=folds(11, 0.045, 1.0), caps=False)
    builder.lathe([(0.205, 0.98), (0.21, 1.04), (0.205, 1.08)], 32, trim, smooth=True, matrix=squash(0.8), caps=False)
    builder.lathe([(0.19, 1.0), (0.2, 1.2), (0.205, 1.36), (0.16, 1.44), (0.06, 1.48)], 32, robe, smooth=True,
                  matrix=squash(0.66), caps=False)
    builder.lathe([(0.13, 1.47), (0.2, 1.43), (0.245, 1.34), (0.235, 1.24)], 32, trim, smooth=True,
                  matrix=squash(0.72, (0.0, 0.004, 0.0)), radius_scale=folds(20, 0.03), caps=False)
    ellipsoid(builder, (0.0, 0.155, 1.33), (0.055, 0.02, 0.055), flesh if parthenos else BRONZE, 14, 6)
    tube(builder, [(0.0, 0.0, 1.42), (0.0, 0.006, 1.53)], [0.052, 0.048], flesh, 12)
    ellipsoid(builder, (0.0, 0.012, 1.6), (0.084, 0.094, 0.108), flesh, 18, 10)
    for side in (-1, 1):
        ellipsoid(builder, (side * 0.032, 0.09, 1.615), (0.016, 0.008, 0.009), "eye_stone", 8, 4)
    builder.lathe([(0.0, 1.705), (0.07, 1.69), (0.092, 1.64), (0.094, 1.6)], 16, trim, smooth=True,
                  matrix=Matrix.Translation((0.0, 0.0, 0.0)), start=math.radians(200), sweep=math.radians(140))
    if parthenos:
        ellipsoid(builder, (0.0, 0.03, 1.79), (0.03, 0.07, 0.04), trim, 10, 6)
        ellipsoid(builder, (0.0, 0.075, 1.815), (0.022, 0.025, 0.028), trim, 8, 5)
    builder.centered_box((0.0, -0.075, 1.45), (0.17, 0.05, 0.26), trim)
    helmet(builder, (0.0, 0.01, 1.6), trim, 3 if parthenos else 1, 0.22 if parthenos else 0.3)
    if parthenos:
        shoulder = Vector((0.22, 0.0, 1.38))
        elbow = Vector((0.29, 0.1, 1.13))
        hand = Vector((0.31, 0.38, 1.06))
        tube(builder, [shoulder, elbow], [0.06, 0.05], flesh, 12)
        tube(builder, [elbow, hand], [0.05, 0.04], flesh, 12)
        builder.lathe([(0.0, 0.0), (0.055, 0.0), (0.05, 0.02), (0.0, 0.025)], 14, flesh, smooth=True,
                      matrix=Matrix.Translation(hand + Vector((0.0, 0.03, -0.02))))
        winged_victory(builder, hand + Vector((0.0, 0.03, 0.0)), 0.31, GOLD)
        column_top = hand + Vector((0.0, 0.02, -0.06))
        builder.lathe([(0.05, 0.0), (0.045, 0.02), (0.04, column_top.z - 0.05), (0.06, column_top.z - 0.02),
                       (0.06, column_top.z)], 14, MARBLE, smooth=True,
                      matrix=Matrix.Translation((column_top.x, column_top.y, 0.0)))
        left_hand = Vector((-0.39, 0.12, 0.88))
        tube(builder, [(-0.22, 0.0, 1.38), (-0.32, 0.03, 1.12), left_hand], [0.06, 0.05, 0.04], flesh, 12)
        shield(builder, (-0.48, 0.16, 0.43), 0.415, (-0.62, 0.72, 0.3), trim, True)
        coil = [(-0.31 + 0.11 * math.cos(t), 0.08 + 0.11 * math.sin(t), 0.03 + 0.05 * t / TAU) for t in
                [k * 0.35 for k in range(36)]]
        coil += [(-0.29, 0.2, 0.32), (-0.27, 0.27, 0.48)]
        tube(builder, coil, [0.03] * (len(coil) - 1) + [0.02], trim, 8)
        tube(builder, [(-0.52, -0.06, 0.0), (-0.44, -0.04, 1.1), (-0.39, -0.03, 1.95)], [0.013, 0.012, 0.0], trim, 6)
    else:
        hand = Vector((0.3, 0.12, 1.34))
        tube(builder, [(0.22, 0.0, 1.38), (0.31, 0.04, 1.17), hand], [0.06, 0.05, 0.04], flesh, 10)
        tube(builder, [(0.3, 0.12, 0.0), (0.3, 0.12, 1.3), (0.3, 0.12, 2.6), (0.3, 0.12, 2.82)],
             [0.016, 0.016, 0.015, 0.0], BRONZE, 6)
        builder.lathe([(0.0, 2.6), (0.03, 2.66), (0.0, 2.86)], 6, GOLD, smooth=True,
                      matrix=Matrix.Translation((0.3, 0.12, 0.0)))
        left_hand = Vector((-0.36, 0.1, 0.92))
        tube(builder, [(-0.22, 0.0, 1.38), (-0.32, 0.03, 1.12), left_hand], [0.06, 0.05, 0.04], flesh, 10)
        shield(builder, (-0.46, 0.14, 0.45), 0.4, (-0.66, 0.68, 0.3), BRONZE, False)
    return builder


def painted(builder, colour, action):
    first = len(builder.polygons)
    action()
    builder.tint(first, colour)


def frame_on(centre, normal, up=(0.0, 0.0, 1.0)):
    n = Vector(normal).normalized()
    u = Vector(up) - n * n.dot(Vector(up))
    u.normalize()
    side = n.cross(u).normalized()
    matrix = Matrix((side, n, u)).transposed().to_4x4()
    matrix.translation = centre
    return matrix


def gorgoneion(builder, matrix, radius, flesh, metal):
    builder.lathe([(0.0, 0.32 * radius), (0.6 * radius, 0.25 * radius), (radius, 0.0)], 16, flesh, smooth=True,
                  matrix=matrix @ Matrix.Rotation(-math.pi / 2, 4, "X"))
    for k in range(10):
        angle = TAU * k / 10
        a = Vector((math.cos(angle) * radius * 0.9, 0.02 * radius, math.sin(angle) * radius * 0.9))
        b = Vector((math.cos(angle + 0.3) * radius * 1.45, 0.0, math.sin(angle + 0.3) * radius * 1.45))
        tube(builder, [matrix @ a, matrix @ b], [0.12 * radius, 0.0], metal, 5, cap=False)


def shield_reliefs(radius):
    from .greek import relief_horse, relief_human
    piece = MeshBuilder()
    for ring, count, size in ((0.66, 12, 0.22), (0.38, 7, 0.18)):
        for k in range(count):
            angle = TAU * k / count + ring
            x, z = ring * radius * math.cos(angle), ring * radius * math.sin(angle)
            height = size * radius
            dome = 0.07 * radius * (1.0 - (ring / 0.95) ** 2) + 0.004
            if k % 3 == 2:
                relief_horse(piece, x - 0.2 * height, dome, z - 0.4 * height, height * 0.9, 0.012 * radius,
                             1 if k % 2 else -1, True)
            else:
                relief_human(piece, x, dome, z - 0.45 * height, height, 0.012 * radius, 0.35 * math.sin(k * 1.7),
                             -0.9 if k % 2 else 0.9)
    return piece


def monochrome(source, material):
    copy = MeshBuilder()
    copy.points(source.positions)
    for indices, smooth in zip(source.polygons, source.polygon_smooth):
        copy.face(list(indices), material, smooth)
    return copy


def parthenos_figure():
    builder = MeshBuilder()
    gold, flesh = GOLD, IVORY
    builder.lathe([(0.3, 0.0), (0.285, 0.1), (0.262, 0.45), (0.236, 0.82), (0.21, 1.0)], 64, gold, smooth=True,
                  matrix=squash(0.8), radius_scale=folds(22, 0.07), caps=False)
    builder.lathe([(0.0, 0.0), (0.3, 0.0)], 64, gold, matrix=squash(0.8), radius_scale=folds(22, 0.07), caps=False)
    for side in (-1, 1):
        builder.centered_box((side * 0.1, 0.2, 0.03), (0.09, 0.14, 0.06), gold)
    builder.lathe([(0.2, 1.33), (0.222, 1.12), (0.252, 0.88), (0.258, 0.82), (0.24, 0.8)], 64, gold, smooth=True,
                  matrix=squash(0.82), radius_scale=folds(14, 0.06, 1.0), caps=False)
    builder.lathe([(0.213, 0.97), (0.218, 1.03), (0.212, 1.07)], 40, gold, smooth=True, matrix=squash(0.8),
                  caps=False)
    builder.lathe([(0.2, 1.0), (0.208, 1.2), (0.212, 1.35), (0.165, 1.44), (0.06, 1.49)], 40, gold, smooth=True,
                  matrix=squash(0.68), radius_scale=folds(9, 0.03), caps=False)
    builder.lathe([(0.12, 1.48), (0.2, 1.44), (0.25, 1.35), (0.258, 1.22), (0.24, 1.18)], 40, gold, smooth=True,
                  matrix=squash(0.74, (0.0, 0.005, 0.0)), radius_scale=folds(26, 0.035), caps=False)
    for k in range(14):
        angle = math.radians(25 + 130 * k / 13)
        base = Vector((0.25 * math.cos(angle), 0.185 * math.sin(angle) + 0.005, 1.19))
        tube(builder, [base, base + Vector((0.01 * math.cos(angle), 0.02, -0.035)),
                       base + Vector((0.025 * math.cos(angle), 0.01, -0.05))], [0.009, 0.008, 0.0], gold, 5)
    gorgoneion(builder, Matrix.Translation((0.0, 0.17, 1.33)), 0.045, flesh, gold)
    tube(builder, [(0.0, 0.0, 1.42), (0.0, 0.008, 1.53)], [0.052, 0.047], flesh, 14)
    ellipsoid(builder, (0.0, 0.012, 1.6), (0.082, 0.094, 0.106), flesh, 24, 12)
    ellipsoid(builder, (0.0, 0.06, 1.535), (0.04, 0.035, 0.03), flesh, 12, 6)
    panel(builder, [(0.088, 1.632), (0.116, 1.584), (0.1, 1.571)], -0.013, 0.013, flesh,
          Matrix.Rotation(math.pi / 2, 4, "Z"))
    for side in (-1, 1):
        ellipsoid(builder, (side * 0.032, 0.088, 1.612), (0.017, 0.007, 0.01), "eye_stone", 10, 5)
        painted(builder, (0.30, 0.20, 0.12), lambda side=side: builder.centered_box(
            (side * 0.034, 0.091, 1.636), (0.036, 0.008, 0.006), PAINT,
            matrix=Matrix.Rotation(-side * 0.12, 4, "Y")))
        tube(builder, [(side * 0.075, 0.02, 1.62), (side * 0.095, 0.03, 1.5), (side * 0.11, 0.04, 1.4)],
             [0.024, 0.022, 0.012], gold, 8)
    painted(builder, (0.62, 0.26, 0.22), lambda: builder.centered_box((0.0, 0.095, 1.553), (0.032, 0.006, 0.009),
                                                                       PAINT))
    builder.lathe([(0.0, 1.705), (0.07, 1.69), (0.092, 1.64), (0.094, 1.6)], 20, gold, smooth=True,
                  start=math.radians(200), sweep=math.radians(140))
    builder.centered_box((0.0, -0.075, 1.45), (0.17, 0.05, 0.26), gold)
    helmet(builder, (0.0, 0.01, 1.6), gold, 3, 0.24)
    builder.lathe([(0.108, 0.035), (0.112, 0.06), (0.104, 0.07)], 20, gold, smooth=True,
                  matrix=Matrix.Translation((0.0, 0.01, 1.6)), start=math.radians(20), sweep=math.radians(140))
    ellipsoid(builder, (0.0, 0.0, 1.765), (0.026, 0.07, 0.032), gold, 12, 6)
    ellipsoid(builder, (0.0, 0.066, 1.81), (0.019, 0.022, 0.026), gold, 10, 5)
    for side in (-1, 1):
        x = side * 0.062
        ellipsoid(builder, (x, -0.005, 1.745), (0.02, 0.055, 0.026), gold, 10, 5)
        tube(builder, [(x, 0.04, 1.75), (x, 0.065, 1.795)], [0.012, 0.01], gold, 6)
        ellipsoid(builder, (x, 0.075, 1.8), (0.01, 0.02, 0.011), gold, 8, 4)
        panel(builder, [(0.0, 0.0), (side * 0.05, 0.035), (side * 0.07, 0.07), (side * 0.03, 0.045)], -0.004, 0.004,
              gold, Matrix.Translation((x, 0.0, 1.755)))
        panel(builder, [(0.0, 0.0), (side * 0.04, 0.03), (side * 0.05, 0.06), (side * 0.02, 0.035)], -0.004, 0.004,
              gold, Matrix.Translation((side * 0.012, 0.0, 1.78)))
    shoulder = Vector((0.22, 0.0, 1.38))
    elbow = Vector((0.29, 0.1, 1.13))
    hand = Vector((0.31, 0.38, 1.06))
    tube(builder, [shoulder + Vector((0.0, 0.0, 0.03)), shoulder.lerp(elbow, 0.45)], [0.075, 0.068], gold, 14)
    for k in range(5):
        start = shoulder.lerp(elbow, 0.1 + 0.08 * k)
        tube(builder, [start + Vector((0.05, -0.04 + 0.02 * k, 0.03)), start + Vector((0.06, -0.03 + 0.02 * k, -0.07))],
             [0.012, 0.0], gold, 5)
    tube(builder, [shoulder, elbow], [0.058, 0.05], flesh, 16)
    tube(builder, [elbow, hand], [0.05, 0.04], flesh, 16)
    tube(builder, [elbow.lerp(hand, 0.85), hand], [0.043, 0.043], gold, 12, cap=False)
    builder.lathe([(0.0, 0.0), (0.055, 0.0), (0.05, 0.02), (0.0, 0.025)], 16, flesh, smooth=True,
                  matrix=Matrix.Translation(hand + Vector((0.0, 0.03, -0.02))))
    winged_victory(builder, hand + Vector((0.0, 0.03, 0.0)), 0.31, GOLD)
    column_top = hand + Vector((0.0, 0.02, -0.06))
    builder.lathe([(0.05, 0.0), (0.045, 0.02), (0.04, column_top.z - 0.05), (0.06, column_top.z - 0.02),
                   (0.06, column_top.z)], 16, MARBLE, smooth=True,
                  matrix=Matrix.Translation((column_top.x, column_top.y, 0.0)))
    left_shoulder = Vector((-0.22, 0.0, 1.38))
    left_elbow = Vector((-0.32, 0.03, 1.12))
    left_hand = Vector((-0.39, 0.12, 0.88))
    tube(builder, [left_shoulder + Vector((0.0, 0.0, 0.03)), left_shoulder.lerp(left_elbow, 0.45)], [0.075, 0.068],
         gold, 14)
    tube(builder, [left_shoulder, left_elbow, left_hand], [0.058, 0.05, 0.04], flesh, 16)
    centre = Vector((-0.5, 0.18, 0.43))
    normal = Vector((-0.62, 0.72, 0.3))
    shield(builder, centre, 0.415, normal, gold, False)
    plate = frame_on(centre, normal)
    builder.merge(monochrome(shield_reliefs(0.415), gold), plate)
    gorgoneion(builder, plate @ Matrix.Translation((0.0, 0.075, 0.0)), 0.075, flesh, gold)
    inner = centre - normal.normalized() * 0.16
    coil = [(inner.x + 0.12 * math.cos(t), inner.y + 0.12 * math.sin(t), 0.035 + 0.045 * t / TAU)
            for t in [k * 0.3 for k in range(46)]]
    coil += [(inner.x + 0.05, inner.y + 0.06, 0.36), (inner.x + 0.08, inner.y + 0.1, 0.52)]
    tube(builder, coil, [0.034] * (len(coil) - 1) + [0.024], gold, 10)
    ellipsoid(builder, (inner.x + 0.09, inner.y + 0.12, 0.54), (0.03, 0.045, 0.024), gold, 10, 5)
    tube(builder, [(-0.56, -0.08, 0.0), (-0.46, -0.05, 1.1), (-0.4, -0.03, 1.95)], [0.014, 0.013, 0.0], gold, 8)
    return builder


PARTHENOS_SCALE = 10.1 / 1.75
PARTHENOS_BASE = (8.065, 4.10, 1.4)


def parthenos_group():
    builder = MeshBuilder()
    width, depth, height = PARTHENOS_BASE
    builder.box((-width / 2 - 0.15, -depth / 2 - 0.15, 0.0), (width / 2 + 0.15, depth / 2 + 0.15, 0.25), MARBLE,
                bottom=False)
    builder.box((-width / 2, -depth / 2, 0.25), (width / 2, depth / 2, height - 0.2), POROS, bottom=False, top=False)
    builder.box((-width / 2 - 0.12, -depth / 2 - 0.12, height - 0.2), (width / 2 + 0.12, depth / 2 + 0.12, height),
                MARBLE, bottom=False)
    first = len(builder.polygons)
    builder.polygon([(-width / 2 + 0.2, depth / 2 + 0.005, 0.4), (width / 2 - 0.2, depth / 2 + 0.005, 0.4),
                     (width / 2 - 0.2, depth / 2 + 0.005, height - 0.3), (-width / 2 + 0.2, depth / 2 + 0.005,
                                                                          height - 0.3)], PAINT)
    builder.tint(first, (0.14, 0.18, 0.32))
    for k in range(21):
        x = -width / 2 + 0.55 + k * (width - 1.1) / 20
        builder.centered_box((x, depth / 2 + 0.03, 0.85), (0.16, 0.05, 0.62), GOLD)
    figure = parthenos_figure()
    builder.merge(figure, Matrix.Translation((0.0, 0.0, height)) @ Matrix.Scale(PARTHENOS_SCALE, 4))
    return builder


def promachos(height=8.0):
    builder = MeshBuilder()
    builder.box((-3.0, -3.0, -1.5), (3.0, 3.0, 0.35), MARBLE, bottom=False)
    builder.box((-2.6, -2.6, 0.35), (2.6, 2.6, 1.55), MARBLE, bottom=False, top=False)
    builder.box((-2.8, -2.8, 1.55), (2.8, 2.8, 1.85), MARBLE, bottom=False)
    builder.merge(athena("promachos"), Matrix.Translation((0.0, 0.0, 1.85)) @ Matrix.Scale(height / 1.75, 4))
    return builder
