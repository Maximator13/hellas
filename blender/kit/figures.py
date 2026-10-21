import math

from mathutils import Matrix, Vector

from .geometry import MeshBuilder
from .greek_materials import MATTE

TAU = 2 * math.pi
FRONT = math.pi / 2
UP = Vector((0.0, 0.0, 1.0))

SKIN = (0.76, 0.56, 0.42)
SKIN_SUN = (0.64, 0.45, 0.32)
SKIN_PERSIAN = (0.68, 0.48, 0.35)
HAIR = (0.15, 0.10, 0.07)
HAIR_GREY = (0.56, 0.53, 0.49)
BRONZE = (0.70, 0.50, 0.24)
GOLD = (0.88, 0.68, 0.30)
IRON = (0.46, 0.46, 0.48)
WOOD = (0.48, 0.36, 0.22)
LEATHER = (0.38, 0.26, 0.16)
LINEN = (0.90, 0.86, 0.74)
WOOL_WHITE = (0.93, 0.91, 0.85)
UNDYED = (0.78, 0.71, 0.58)
CRIMSON = (0.62, 0.10, 0.09)
MADDER = (0.70, 0.30, 0.20)
SAFFRON = (0.88, 0.66, 0.26)
WOAD = (0.30, 0.42, 0.62)
OLIVE = (0.46, 0.48, 0.30)
PURPLE = (0.42, 0.16, 0.30)
WICKER = (0.70, 0.57, 0.33)
TERRACOTTA = (0.72, 0.42, 0.27)
LAUREL = (0.30, 0.42, 0.20)
DARK = (0.06, 0.05, 0.05)


def perpendicular(axis, hint=None):
    if hint is not None:
        candidate = hint - axis * hint.dot(axis)
        if candidate.length > 1e-5:
            return candidate.normalized()
    helper = UP if abs(axis.z) < 0.9 else Vector((1.0, 0.0, 0.0))
    return axis.cross(helper).normalized()


def tube(builder, path, radii, colors, sides=5, cap=True, squash=1.0):
    path = [Vector(point) for point in path]
    colors = colors if isinstance(colors, list) else [colors] * (len(path) - 1)
    rings = []
    u = None
    for index, (point, radius) in enumerate(zip(path, radii)):
        axis = (path[min(index + 1, len(path) - 1)] - path[max(index - 1, 0)]).normalized()
        u = perpendicular(axis, u)
        v = axis.cross(u).normalized()
        if radius < 1e-6:
            rings.append([builder.point(point)] * sides)
            continue
        rings.append([builder.point(point + (u * math.cos(TAU * k / sides) + v * squash * math.sin(TAU * k / sides))
                                    * radius) for k in range(sides)])
    for segment, (lower, upper) in enumerate(zip(rings[:-1], rings[1:])):
        first = len(builder.polygons)
        for k in range(sides):
            j = (k + 1) % sides
            builder.face([lower[k], lower[j], upper[j], upper[k]], MATTE, True)
        builder.tint(first, colors[segment])
    if cap and radii[-1] > 1e-6:
        first = len(builder.polygons)
        builder.face(list(rings[-1]), MATTE)
        builder.tint(first, colors[-1])


def lathe(builder, profile, color, segments=6, matrix=None, start=0.0, sweep=TAU, both_sides=False):
    first = len(builder.polygons)
    builder.lathe(profile, segments, MATTE, smooth=True, matrix=matrix, start=start, sweep=sweep, caps=False)
    if both_sides:
        builder.lathe(list(reversed(profile)), segments, MATTE, smooth=True, matrix=matrix, start=start, sweep=sweep,
                      caps=False)
    builder.tint(first, color)


def ellipsoid(builder, center, radii, color, segments=6, rings=4):
    profile = [(math.sin(math.pi * k / rings), -math.cos(math.pi * k / rings)) for k in range(rings + 1)]
    lathe(builder, profile, color, segments, Matrix.Translation(center) @ Matrix.Diagonal((*radii, 1.0)))


def box(builder, center, size, color, bottom=False, matrix=None):
    first = len(builder.polygons)
    builder.centered_box(center, size, MATTE, matrix=matrix, bottom=bottom)
    builder.tint(first, color)


def panel(builder, corners, color):
    first = len(builder.polygons)
    builder.face(builder.points(corners), MATTE)
    builder.face(list(reversed(builder.points(corners))), MATTE)
    builder.tint(first, color)


def legs(builder, skin, stride=0.0, upper=None, lower=None, feet=LEATHER):
    for side in (-1, 1):
        foot_y = side * stride
        tube(builder, [(side * 0.09, 0.0, 0.93), (side * 0.1, foot_y * 0.5 + 0.02, 0.5), (side * 0.1, foot_y, 0.08)],
             [0.075, 0.056, 0.045], [upper or skin, lower or skin], 5)
        box(builder, (side * 0.1, foot_y + 0.05, 0.035), (0.09, 0.22, 0.07), feet)


def feet_only(builder, stride=0.0, feet=LEATHER):
    for side in (-1, 1):
        box(builder, (side * 0.09, side * stride + 0.06, 0.035), (0.09, 0.2, 0.07), feet)


def torso(builder, color, waist=0.92, squash=0.62):
    tube(builder, [(0.0, 0.0, waist), (0.0, 0.0, 1.15), (0.0, 0.01, 1.44)], [0.16, 0.17, 0.2], color, 6, squash=squash)


def skirt(builder, color, top, bottom, top_radius, bottom_radius, sides=7, squash=0.75):
    tube(builder, [(0.0, 0.0, top), (0.0, 0.0, bottom)], [top_radius, bottom_radius], color, sides, cap=False,
         squash=squash)


def arm(builder, side, hand, sleeve, skin, sleeve_to_wrist=False):
    shoulder = Vector((side * 0.22, 0.0, 1.38))
    hand = Vector(hand)
    elbow = shoulder.lerp(hand, 0.5) + Vector((side * 0.06, -0.03, -0.06))
    tube(builder, [shoulder, elbow, hand], [0.062, 0.05, 0.04], [sleeve, sleeve if sleeve_to_wrist else skin], 4)


def arms(builder, right_hand, left_hand, sleeve, skin, sleeve_to_wrist=False):
    arm(builder, 1, right_hand, sleeve, skin, sleeve_to_wrist)
    arm(builder, -1, left_hand, sleeve, skin, sleeve_to_wrist)


def head(builder, skin, hair=None, beard=None, center=(0.0, 0.01, 1.6)):
    ellipsoid(builder, center, (0.09, 0.1, 0.115), skin, 6, 4)
    if hair is not None:
        ellipsoid(builder, (center[0], center[1] - 0.022, center[2] + 0.028), (0.096, 0.1, 0.098), hair, 6, 3)
    if beard is not None:
        ellipsoid(builder, (center[0], center[1] + 0.055, center[2] - 0.075), (0.065, 0.05, 0.06), beard, 5, 2)


def sash(builder, color, start=(-0.2, 0.0, 1.46), end=(0.17, 0.0, 1.0), depth=0.42):
    start = Vector(start)
    end = Vector(end)
    direction = end - start
    frame = Matrix((Vector((0.0, 1.0, 0.0)).cross(direction).normalized(), Vector((0.0, 1.0, 0.0)),
                    direction.normalized())).transposed().to_4x4()
    frame.translation = start
    box(builder, (0.0, 0.0, direction.length / 2), (0.1, depth, direction.length), color, True, frame)


def corinthian_helmet(builder, center, crest=None):
    center = Vector(center)
    transform = Matrix.Translation(center) @ Matrix.Diagonal((0.105, 0.116, 0.122, 1.0))
    lathe(builder, [(1.12, -1.0), (1.06, -0.3), (0.92, 0.5), (0.0, 1.05)], BRONZE, 6, transform)
    y = center.y + 0.114
    for corners in ([(-0.065, y, center.z - 0.005), (0.065, y, center.z - 0.005), (0.065, y, center.z + 0.025),
                     (-0.065, y, center.z + 0.025)],
                    [(-0.012, y, center.z - 0.11), (0.012, y, center.z - 0.11), (0.012, y, center.z - 0.005),
                     (-0.012, y, center.z - 0.005)]):
        first = len(builder.polygons)
        builder.oriented(corners, (0, 1, 0), MATTE)
        builder.tint(first, DARK)
    if crest is not None:
        top = center.z + 0.125
        bottom_line = [(0.0, center.y + 0.06, top - 0.01), (0.0, center.y - 0.04, top + 0.005),
                       (0.0, center.y - 0.13, top - 0.06)]
        top_line = [(0.0, center.y + 0.07, top + 0.08), (0.0, center.y - 0.04, top + 0.15),
                    (0.0, center.y - 0.17, top + 0.02)]
        for k in range(2):
            panel(builder, [bottom_line[k], bottom_line[k + 1], top_line[k + 1], top_line[k]], crest)


def aspis(builder, center, diameter, color):
    radius = diameter / 2
    transform = Matrix.Translation(center) @ Matrix.Rotation(-math.pi / 2, 4, "X")
    lathe(builder, [(0.0, 0.07), (radius * 0.55, 0.055), (radius, 0.0), (radius, -0.025), (0.0, -0.025)], color, 8,
          transform)


def spear(builder, butt, tip, radius, shaft_color=WOOD, head_length=0.25, head_color=BRONZE):
    butt = Vector(butt)
    tip = Vector(tip)
    neck = tip - (tip - butt).normalized() * head_length
    tube(builder, [butt, neck, tip], [radius, radius, 0.0], [shaft_color, head_color], 3)


def hoplite(spartan=False):
    builder = MeshBuilder()
    legs(builder, SKIN_SUN, lower=BRONZE, feet=SKIN_SUN)
    skirt(builder, CRIMSON if spartan else MADDER, 0.98, 0.66, 0.18, 0.23)
    skirt(builder, LINEN, 1.0, 0.8, 0.178, 0.215)
    torso(builder, LINEN)
    arms(builder, (0.27, 0.22, 1.05), (-0.17, 0.3, 1.1), LINEN, SKIN_SUN)
    corinthian_helmet(builder, (0.0, 0.01, 1.6), DARK if spartan else (0.30, 0.20, 0.12))
    aspis(builder, (-0.24, 0.36, 1.08), 0.9, BRONZE)
    spear(builder, (0.27, 0.16, 0.03), (0.27, 0.36, 2.52), 0.016)
    if spartan:
        box(builder, (0.0, -0.11, 1.4), (0.15, 0.05, 0.16), HAIR)
        lathe(builder, [(0.2, 1.43), (0.25, 1.0), (0.29, 0.56)], CRIMSON, 4, Matrix.Diagonal((1.0, 0.72, 1.0, 1.0)),
              start=math.radians(195), sweep=math.radians(150), both_sides=True)
    return builder


def pilos(builder, color, center=(0.0, 0.0, 1.6)):
    x, y, z = center
    lathe(builder, [(0.105, z + 0.02), (0.09, z + 0.1), (0.0, z + 0.22)], color, 6, Matrix.Translation((x, y, 0.0)))


def psilos():
    builder = MeshBuilder()
    legs(builder, SKIN_SUN, feet=SKIN_SUN)
    skirt(builder, UNDYED, 0.98, 0.62, 0.18, 0.23)
    torso(builder, SKIN_SUN)
    sash(builder, UNDYED)
    hand = Vector((0.26, -0.12, 1.62))
    arms(builder, hand, (-0.2, 0.28, 1.05), SKIN_SUN, SKIN_SUN)
    head(builder, SKIN_SUN, HAIR, HAIR)
    pilos(builder, (0.52, 0.40, 0.26))
    spear(builder, hand + Vector((0.0, -0.75, -0.12)), hand + Vector((0.0, 0.8, 0.14)), 0.012, head_length=0.12,
          head_color=IRON)
    for offset in (-0.03, 0.03):
        spear(builder, (-0.2 + offset, 0.3, 0.25), (-0.2 + offset, 0.42, 1.8), 0.011, head_length=0.12,
              head_color=IRON)
    return builder


def tiara(builder, color, center=(0.0, 0.01, 1.6)):
    x, y, z = center
    profile = [(0.106, z - 0.12), (0.112, z), (0.098, z + 0.09), (0.0, z + 0.16)]
    lathe(builder, profile, color, 5, Matrix.Translation((x, y - 0.012, 0.0)) @ Matrix.Diagonal((1.0, 1.05, 1.0, 1.0)),
          start=FRONT + math.radians(55), sweep=math.radians(250))


def gorytos(builder, color=LEATHER, at=(-0.24, -0.02, 0.86)):
    box(builder, at, (0.07, 0.16, 0.42), color, True)


def persian_body(builder, tunic, trousers, torso_color, sleeve, cap, right_hand, left_hand, hem=0.55):
    legs(builder, trousers, upper=trousers, lower=trousers, feet=LEATHER)
    skirt(builder, tunic, 1.0, hem, 0.18, 0.24)
    torso(builder, torso_color)
    arms(builder, right_hand, left_hand, sleeve, SKIN_PERSIAN, sleeve_to_wrist=True)
    head(builder, SKIN_PERSIAN, None, HAIR)
    tiara(builder, cap)


def sparabara():
    builder = MeshBuilder()
    persian_body(builder, MADDER, WOAD, IRON, MADDER, UNDYED, (0.27, 0.25, 1.05), (-0.14, 0.3, 1.05))
    box(builder, (-0.14, 0.42, 0.67), (0.62, 0.035, 1.22), WICKER, True)
    spear(builder, (0.27, 0.18, 0.15), (0.27, 0.34, 2.12), 0.016, head_length=0.2, head_color=IRON)
    gorytos(builder)
    return builder


def bow(builder, grip, height=1.15, bend=0.1):
    grip = Vector(grip)
    tips = [grip + Vector((0.0, -bend, side * height / 2)) for side in (-1, 1)]
    tube(builder, [tips[0], grip, tips[1]], [0.012, 0.018, 0.012], [WOOD, WOOD], 3, cap=False)
    return tips


def persian_archer():
    builder = MeshBuilder()
    grip = (-0.1, 0.56, 1.36)
    persian_body(builder, SAFFRON, (0.36, 0.30, 0.42), SAFFRON, (0.36, 0.30, 0.42), WOOL_WHITE, (0.05, 0.18, 1.38),
                 grip)
    tips = bow(builder, grip)
    tube(builder, [tips[0], (0.05, 0.18, 1.38), tips[1]], [0.004, 0.004, 0.004], [UNDYED, UNDYED], 3, cap=False)
    gorytos(builder, (0.52, 0.30, 0.18))
    return builder


def immortal():
    builder = MeshBuilder()
    persian_body(builder, SAFFRON, PURPLE, WOOL_WHITE, PURPLE, WOOL_WHITE, (0.06, 0.26, 1.02), (-0.06, 0.26, 1.32),
                 hem=0.42)
    spear(builder, (0.0, 0.27, 0.11), (0.0, 0.27, 2.12), 0.016, head_length=0.2, head_color=GOLD)
    ellipsoid(builder, (0.0, 0.27, 0.06), (0.045, 0.045, 0.05), GOLD, 5, 2)
    tube(builder, [(0.12, -0.17, 0.98), (-0.08, -0.19, 1.6)], [0.065, 0.075], [(0.60, 0.40, 0.20)], 5)
    bow(builder, (0.18, -0.2, 1.35), 0.95, -0.08)
    return builder


def horse(builder, color, scale=1.0):
    s = scale
    dark = tuple(c * 0.55 for c in color)
    body_z = 1.12 * s
    ellipsoid(builder, (0.0, 0.0, body_z), (0.26 * s, 0.78 * s, 0.32 * s), color, 6, 3)
    tube(builder, [(0.0, 0.55 * s, body_z + 0.13 * s), (0.0, 0.85 * s, body_z + 0.55 * s)], [0.17 * s, 0.11 * s],
         color, 5, cap=False)
    tube(builder, [(0.0, 0.82 * s, body_z + 0.6 * s), (0.0, 1.12 * s, body_z + 0.32 * s)], [0.1 * s, 0.06 * s], color,
         5)
    for front in (-1, 1):
        for side in (-1, 1):
            x, y = side * 0.14 * s, front * 0.5 * s
            tube(builder, [(x, y, body_z - 0.1 * s), (x, y, 0.45 * s), (x, y, 0.0)], [0.09 * s, 0.05 * s, 0.045 * s],
                 [color, dark], 4, cap=False)
    tube(builder, [(0.0, -0.76 * s, body_z + 0.15 * s), (0.0, -0.9 * s, body_z - 0.2 * s),
                   (0.0, -0.88 * s, body_z - 0.6 * s)], [0.05 * s, 0.06 * s, 0.02 * s], dark, 4, cap=False)
    return body_z + 0.3 * s


def persian_rider():
    builder = MeshBuilder()
    seat = horse(builder, (0.44, 0.30, 0.18))
    for side in (-1, 1):
        tube(builder, [(side * 0.12, 0.0, seat + 0.05), (side * 0.3, 0.25, seat - 0.25), (side * 0.28, 0.12, seat - 0.68)],
             [0.07, 0.055, 0.045], [WOAD, WOAD], 4)
    tube(builder, [(0.0, 0.0, seat - 0.05), (0.0, 0.0, seat + 0.2), (0.0, 0.02, seat + 0.5)], [0.17, 0.17, 0.19],
         [MADDER, MADDER], 6, squash=0.62)
    centre = (0.0, 0.03, seat + 0.66)
    shoulder_z = seat + 0.44
    for side, hand in ((1, (0.27, 0.32, shoulder_z - 0.25)), (-1, (-0.2, 0.3, shoulder_z - 0.3))):
        shoulder = Vector((side * 0.21, 0.0, shoulder_z))
        elbow = shoulder.lerp(Vector(hand), 0.5) + Vector((side * 0.05, -0.03, -0.05))
        tube(builder, [shoulder, elbow, hand], [0.06, 0.05, 0.04], [MADDER, MADDER], 4)
    head(builder, SKIN_PERSIAN, None, HAIR, centre)
    tiara(builder, UNDYED, centre)
    for offset in (0.0, 0.05):
        spear(builder, (0.27 + offset, -0.45, shoulder_z - 0.4), (0.27 + offset, 1.15, shoulder_z - 0.05), 0.012,
              head_length=0.14, head_color=IRON)
    gorytos(builder, LEATHER, (-0.3, -0.25, seat - 0.15))
    return builder


def far_infantry(body, torso_color, head_color, shield=None, shield_size=(0.6, 0.06, 0.9), spear_color=WOOD):
    builder = MeshBuilder()
    box(builder, (0.0, 0.0, 0.47), (0.32, 0.22, 0.94), body)
    box(builder, (0.0, 0.0, 1.2), (0.38, 0.24, 0.52), torso_color)
    box(builder, (0.0, 0.0, 1.6), (0.22, 0.24, 0.26), head_color)
    if shield is not None:
        box(builder, (-0.18, 0.3, 1.0 if shield_size[2] < 1.0 else 0.66), shield_size, shield)
    if spear_color is not None:
        box(builder, (0.27, 0.25, 1.25), (0.04, 0.04, 2.4), spear_color)
    return builder


def far_rider():
    builder = MeshBuilder()
    box(builder, (0.0, 0.0, 1.12), (0.5, 1.6, 0.6), (0.44, 0.30, 0.18))
    for y in (-0.5, 0.5):
        box(builder, (0.0, y, 0.42), (0.36, 0.24, 0.84), (0.30, 0.20, 0.12))
    box(builder, (0.0, 0.95, 1.6), (0.22, 0.5, 0.6), (0.44, 0.30, 0.18))
    box(builder, (0.0, 0.0, 1.85), (0.4, 0.3, 0.7), MADDER)
    box(builder, (0.0, 0.03, 2.33), (0.22, 0.24, 0.26), UNDYED)
    return builder


TROOPS = {
    "hoplite": (hoplite, lambda: far_infantry(MADDER, LINEN, BRONZE, BRONZE, (0.9, 0.08, 0.9))),
    "hoplite-spartiate": (lambda: hoplite(True),
                          lambda: far_infantry(CRIMSON, CRIMSON, BRONZE, BRONZE, (0.9, 0.08, 0.9))),
    "psilos": (psilos, lambda: far_infantry(UNDYED, SKIN_SUN, (0.52, 0.40, 0.26), None)),
    "perse-sparabara": (sparabara, lambda: far_infantry(WOAD, IRON, UNDYED, WICKER, (0.62, 0.05, 1.22))),
    "perse-archer": (persian_archer, lambda: far_infantry((0.36, 0.30, 0.42), SAFFRON, WOOL_WHITE, None,
                                                          spear_color=None)),
    "immortel": (immortal, lambda: far_infantry(PURPLE, WOOL_WHITE, WOOL_WHITE, None, spear_color=GOLD)),
    "cavalier-perse": (persian_rider, far_rider),
}


def petasos(builder, color, center=(0.0, 0.01, 1.6)):
    x, y, z = center
    frame = Matrix.Translation((x, y, 0.0))
    lathe(builder, [(0.21, z + 0.08), (0.1, z + 0.1)], color, 8, frame)
    lathe(builder, [(0.1, z + 0.095), (0.21, z + 0.075)], tuple(c * 0.8 for c in color), 8, frame)
    lathe(builder, [(0.1, z + 0.1), (0.092, z + 0.16), (0.0, z + 0.18)], color, 8, frame)


def wreath(builder, color=LAUREL, center=(0.0, 0.01, 1.6)):
    x, y, z = center
    lathe(builder, [(0.098, z + 0.035), (0.112, z + 0.05), (0.1, z + 0.066)], color, 8, Matrix.Translation((x, y, 0.0)))


def amphora(builder, matrix, tone=TERRACOTTA):
    lathe(builder, [(0.0, -0.05), (0.04, 0.02), (0.15, 0.25), (0.16, 0.5), (0.07, 0.72), (0.05, 0.9), (0.0, 0.9)],
          tone, 6, matrix)


def phiale(builder, at, color=GOLD):
    lathe(builder, [(0.0, 0.0), (0.08, 0.008), (0.095, 0.03)], color, 8, Matrix.Translation(at))


def man_himation(mantle=WOOL_WHITE, skin=SKIN, hair=HAIR, beard=HAIR, stride=0.0, right_hand=(0.3, 0.06, 0.86)):
    builder = MeshBuilder()
    legs(builder, skin, stride)
    torso(builder, skin)
    tube(builder, [(0.0, 0.0, 1.36), (0.0, 0.0, 0.98), (0.0, 0.0, 0.3)], [0.2, 0.205, 0.25], [mantle, mantle], 7,
         cap=False, squash=0.74)
    sash(builder, mantle)
    arm(builder, 1, right_hand, skin, skin)
    arm(builder, -1, (-0.24, 0.12, 1.0), mantle, skin, True)
    head(builder, skin, hair, beard)
    return builder


def woman_peplos(dress=SAFFRON, belt=MADDER, skin=SKIN, hair=HAIR, stride=0.0, veil=None, carry=None):
    builder = MeshBuilder()
    feet_only(builder, stride)
    skirt(builder, dress, 1.0, 0.04, 0.19, 0.25, 8)
    skirt(builder, dress, 1.36, 0.84, 0.2, 0.235, 8)
    skirt(builder, belt, 1.03, 0.99, 0.212, 0.214, 8)
    torso(builder, dress, waist=0.95)
    raised = carry == "hydria"
    hands = ((0.14, 0.02, 1.86), (-0.14, 0.02, 1.86)) if raised else ((0.25, 0.08, 0.88), (-0.25, 0.08, 0.88))
    arms(builder, hands[0], hands[1], skin, skin)
    head(builder, skin, hair)
    ellipsoid(builder, (0.0, -0.1, 1.6), (0.05, 0.045, 0.045), hair, 5, 3)
    if veil is not None:
        lathe(builder, [(0.21, 1.38), (0.13, 1.5), (0.115, 1.64), (0.0, 1.75)], veil, 6,
              Matrix.Translation((0.0, -0.015, 0.0)), start=FRONT + 0.75, sweep=TAU - 1.5)
    if raised:
        amphora(builder, Matrix.Translation((0.0, 0.02, 1.74)) @ Matrix.Diagonal((0.9, 0.9, 0.5, 1.0)))
    return builder


def worker(tunic=UNDYED, skin=SKIN_SUN, hair=HAIR, stride=0.0, carry=None):
    builder = MeshBuilder()
    legs(builder, skin, stride)
    skirt(builder, tunic, 1.0, 0.56, 0.18, 0.23)
    torso(builder, skin)
    sash(builder, tunic, depth=0.36)
    skirt(builder, LEATHER, 1.0, 0.95, 0.182, 0.184, 6)
    if carry == "amphora":
        arms(builder, (0.24, -0.02, 1.62), (-0.24, 0.1, 0.88), skin, skin)
        amphora(builder, Matrix.Translation((0.17, -0.02, 1.52)) @ Matrix.Rotation(math.radians(-70), 4, "Y"))
    else:
        arms(builder, (0.28, 0.12, 0.95), (-0.26, 0.08, 0.88), skin, skin)
        spear(builder, (0.28, -0.05, 0.75), (0.28, 0.3, 1.1), 0.018, WOOD, 0.08, IRON)
    head(builder, skin, hair, hair)
    return builder


def ephebe(chiton=WOOL_WHITE, chlamys=MADDER, hat=(0.62, 0.50, 0.30), skin=SKIN, stride=0.0):
    builder = MeshBuilder()
    legs(builder, skin, stride, lower=LEATHER)
    skirt(builder, chiton, 1.0, 0.64, 0.18, 0.22)
    torso(builder, chiton)
    arms(builder, (0.29, 0.06, 0.88), (-0.25, 0.1, 0.9), chiton, skin)
    lathe(builder, [(0.21, 1.45), (0.25, 1.15), (0.27, 0.78)], chlamys, 5, Matrix.Diagonal((1.0, 0.75, 1.0, 1.0)),
          start=math.radians(120), sweep=math.radians(230), both_sides=True)
    head(builder, skin, HAIR)
    petasos(builder, hat)
    return builder


def priest(chiton=WOOL_WHITE, mantle=(0.86, 0.80, 0.66), skin=SKIN):
    builder = MeshBuilder()
    feet_only(builder)
    skirt(builder, chiton, 1.0, 0.04, 0.18, 0.24, 8)
    torso(builder, chiton)
    tube(builder, [(0.0, 0.0, 1.3), (0.0, 0.0, 0.95), (0.0, 0.0, 0.42)], [0.205, 0.21, 0.255], [mantle, mantle], 7,
         cap=False, squash=0.74)
    sash(builder, mantle)
    arms(builder, (0.22, 0.34, 1.08), (-0.24, 0.12, 0.98), chiton, skin)
    phiale(builder, (0.22, 0.42, 1.06))
    head(builder, skin, HAIR_GREY, HAIR_GREY)
    wreath(builder)
    return builder


CIVILIANS = {
    "fig_citoyen-himation": lambda: man_himation(),
    "fig_citoyen-himation-couleur": lambda: man_himation(WOAD, SKIN_SUN, HAIR_GREY, HAIR_GREY,
                                                         right_hand=(0.3, 0.3, 1.32)),
    "fig_femme-peplos": lambda: woman_peplos(),
    "fig_femme-hydrie": lambda: woman_peplos(OLIVE, LINEN, carry="hydria"),
    "fig_femme-voilee": lambda: woman_peplos(WOOL_WHITE, MADDER, veil=MADDER),
    "fig_ephebe-chlamyde": lambda: ephebe(),
    "fig_ouvrier": lambda: worker(),
    "fig_porteur": lambda: worker(MADDER, carry="amphora"),
    "fig_pretre": lambda: priest(),
    "fig_pretresse": lambda: woman_peplos(WOOL_WHITE, SAFFRON, veil=WOOL_WHITE),
}

WALKERS = {
    "walker_citoyen": lambda: man_himation(stride=0.16),
    "walker_femme": lambda: woman_peplos(MADDER, LINEN, stride=0.12),
    "walker_ouvrier": lambda: worker(OLIVE, stride=0.2),
    "walker_ephebe": lambda: ephebe(stride=0.18),
}


def lowest_point(builder):
    return min(position[2] for position in builder.positions)
