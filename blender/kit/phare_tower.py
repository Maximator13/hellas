import math
import os
import random

import bpy
from mathutils import Matrix, Vector

from . import figures
from .geometry import MeshBuilder
from .orders import facing_text_matrix

GREEK_FONT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "node_modules",
                          "@fontsource", "eb-garamond", "files", "eb-garamond-greek-600-normal.woff")

STONE = "limestone"
WALL = "ashlar"
MARBLE = "marble"
BRONZE = "bronze_statue"
VOID = "shadow_void"
PAVING = "ground_quai"
ROCK = "terrain_ile"
FLAME = "flame"
TAU = 2 * math.pi
PLINTH = 4.0
SQUARE_TOP = 56.0
SQUARE_BASE_HALF = 15.0
SQUARE_TOP_HALF = 13.4
OCTAGON_BASE = SQUARE_TOP + 2.0
OCTAGON_TOP = 84.0
OCTAGON_BASE_HALF = 8.2
OCTAGON_TOP_HALF = 7.6
CYLINDER_TOP = 92.0
CYLINDER_RADIUS = 4.35
PILLAR_TOP = 95.6
CANOPY_TOP = 96.1
STATUE_BASE = 97.1
STATUE_HEIGHT = 5.9
BEACON_HEIGHT = CYLINDER_TOP + 1.7
DOOR = (9.6, 14.4)
WHITE = (1.0, 0.98, 0.93)
WARM = (0.98, 0.94, 0.86)
GRANITE = (0.74, 0.5, 0.46)
DEDICATION = ("ΣΩΣΤΡΑΤΟΣ ΔΕΞΙΦΑΝΟΥΣ ΚΝΙΔΙΟΣ", "ΘΕΟΙΣ ΣΩΤΗΡΣΙΝ ΥΠΕΡ ΤΩΝ ΠΛΩΙΖΟΜΕΝΩΝ")


def painted(builder, colour, action):
    first = len(builder.polygons)
    action()
    builder.tint(first, colour)


def ring(sides, half, z):
    if sides == 4:
        return [(half * sx, half * sy, z) for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    radius = half / math.cos(math.pi / sides)
    return [(radius * math.cos(math.pi / sides + TAU * k / sides),
             radius * math.sin(math.pi / sides + TAU * k / sides), z) for k in range(sides)]


def frustum(builder, sides, half0, half1, z0, z1, material, top=False, bottom=False):
    lower = builder.points(ring(sides, half0, z0))
    upper = builder.points(ring(sides, half1, z1))
    for k in range(sides):
        j = (k + 1) % sides
        builder.face([lower[k], lower[j], upper[j], upper[k]], material)
    if top:
        builder.face(upper, material)
    if bottom:
        builder.face(list(reversed(lower)), material)


def band(builder, sides, half, z0, z1, material, projection):
    frustum(builder, sides, half + projection, half + projection, z0, z1, material, top=True, bottom=True)


def cornice(builder, sides, half, z, material, scale=1.0):
    rows = [(0.0, 0.0), (0.35, 0.25), (0.45, 0.55), (0.9, 0.85), (1.15, 1.25), (1.2, 1.55), (0.0, 1.55)]
    previous = None
    for offset, height in rows:
        current = builder.points(ring(sides, half + offset * scale, z + height * scale))
        if previous is not None:
            for k in range(sides):
                j = (k + 1) % sides
                builder.face([previous[k], previous[j], current[j], current[k]], material)
        previous = current
    builder.face(previous, material)


def parapet(builder, sides, half, z, height, thickness, material):
    outer_lower = builder.points(ring(sides, half, z))
    outer_upper = builder.points(ring(sides, half, z + height))
    inner_lower = builder.points(ring(sides, half - thickness, z))
    inner_upper = builder.points(ring(sides, half - thickness, z + height))
    for k in range(sides):
        j = (k + 1) % sides
        builder.face([outer_lower[k], outer_lower[j], outer_upper[j], outer_upper[k]], material)
        builder.face([inner_lower[j], inner_lower[k], inner_upper[k], inner_upper[j]], material)
        builder.face([outer_upper[k], outer_upper[j], inner_upper[j], inner_upper[k]], material)


def face_point(normal, side, half0, half1, z0, z1, u, z, push=0.04):
    half = half0 + (half1 - half0) * (z - z0) / (z1 - z0)
    return normal * (half + push) + side * u + Vector((0.0, 0.0, z))


def window(builder, normal, side, half0, half1, z0, z1, u, z, width, height, arched=False):
    corners = [face_point(normal, side, half0, half1, z0, z1, u + du, z + dz)
               for du, dz in ((-width / 2, 0.0), (width / 2, 0.0), (width / 2, height), (-width / 2, height))]
    builder.oriented(corners, normal, VOID)
    if arched:
        top = [face_point(normal, side, half0, half1, z0, z1, u + width / 2 * math.cos(math.pi * k / 4),
                          z + height + width / 2 * math.sin(math.pi * k / 4)) for k in range(5)]
        builder.oriented(top, normal, VOID)


FACES = [Vector((0, -1, 0)), Vector((1, 0, 0)), Vector((0, 1, 0)), Vector((-1, 0, 0))]


def square_tier(builder):
    z0, z1 = PLINTH, SQUARE_TOP
    painted(builder, WHITE, lambda: frustum(builder, 4, SQUARE_BASE_HALF, SQUARE_TOP_HALF, z0, z1, WALL))
    for z in (19.0, 32.0, 45.0):
        half = SQUARE_BASE_HALF + (SQUARE_TOP_HALF - SQUARE_BASE_HALF) * (z - z0) / (z1 - z0)
        painted(builder, WARM, lambda half=half, z=z: band(builder, 4, half, z, z + 0.55, STONE, 0.28))
    painted(builder, WARM, lambda: band(builder, 4, SQUARE_BASE_HALF, z0, z0 + 1.2, STONE, 0.45))
    for normal in FACES:
        side = Vector((-normal.y, normal.x, 0.0))
        for level, z in enumerate((10.0, 14.5, 23.0, 27.5, 36.0, 40.5, 49.0, 53.0)):
            for u in (-8.5, 0.0, 8.5):
                if normal.y < 0 and u == 0.0 and z < 27.0:
                    continue
                window(builder, normal, side, SQUARE_BASE_HALF, SQUARE_TOP_HALF, z0, z1, u, z, 0.9, 1.7,
                       arched=level % 2 == 0)
    normal, side = FACES[0], Vector((1, 0, 0))
    door = [face_point(normal, side, SQUARE_BASE_HALF, SQUARE_TOP_HALF, z0, z1, u, z, 0.05)
            for u, z in ((-1.6, DOOR[0]), (1.6, DOOR[0]), (1.6, DOOR[1]), (-1.6, DOOR[1]))]
    builder.oriented(door, normal, VOID)
    surround = [face_point(normal, side, SQUARE_BASE_HALF, SQUARE_TOP_HALF, z0, z1, u, z, 0.2)
                for u, z in ((-2.4, DOOR[0] - 0.2), (2.4, DOOR[0] - 0.2), (2.4, DOOR[1] + 1.0),
                             (-2.4, DOOR[1] + 1.0))]
    painted(builder, GRANITE, lambda: builder.oriented(surround, normal, STONE))
    plaque = [face_point(normal, side, SQUARE_BASE_HALF, SQUARE_TOP_HALF, z0, z1, u, z, 0.12)
              for u, z in ((-11.5, 16.4), (11.5, 16.4), (11.5, 18.8), (-11.5, 18.8))]
    painted(builder, (1.04, 1.02, 0.98), lambda: builder.oriented(plaque, normal, MARBLE))
    painted(builder, WARM, lambda: cornice(builder, 4, SQUARE_TOP_HALF, SQUARE_TOP, STONE, 1.1))
    painted(builder, WHITE, lambda: frustum(builder, 4, SQUARE_TOP_HALF + 1.32, SQUARE_TOP_HALF + 1.32,
                                            SQUARE_TOP + 1.7, OCTAGON_BASE, STONE, top=True))
    painted(builder, WARM, lambda: parapet(builder, 4, SQUARE_TOP_HALF + 1.3, OCTAGON_BASE, 1.15, 0.5, STONE))


def word_mesh(word, size, depth):
    curve = bpy.data.curves.new("dedication_word", type="FONT")
    curve.font = bpy.data.fonts.load(GREEK_FONT, check_existing=True)
    curve.body = word
    curve.size = size
    curve.extrude = depth / 2
    curve.resolution_u = 2
    holder = bpy.data.objects.new("dedication_word", curve)
    bpy.context.scene.collection.objects.link(holder)
    mesh = bpy.data.meshes.new_from_object(holder.evaluated_get(bpy.context.evaluated_depsgraph_get()))
    builder = MeshBuilder()
    for vertex in mesh.vertices:
        builder.point(vertex.co)
    for polygon in mesh.polygons:
        builder.face(list(polygon.vertices), BRONZE)
    xs = [vertex.co.x for vertex in mesh.vertices] or [0.0]
    bpy.data.objects.remove(holder)
    bpy.data.curves.remove(curve)
    bpy.data.meshes.remove(mesh)
    return builder, max(xs)


def text_line(line, size, depth=0.06):
    words = [word_mesh(word, size, depth) for word in line.split()]
    gap = size * 0.55
    total = sum(width for _, width in words) + gap * (len(words) - 1)
    builder = MeshBuilder()
    x = -total / 2
    for word, width in words:
        builder.merge(word, Matrix.Translation((x, 0.0, 0.0)))
        x += width + gap
    return builder, total


def dedication():
    builder = MeshBuilder()
    normal = Vector((0.0, -1.0, 0.0))
    for line, z in zip(DEDICATION, (17.75, 16.75)):
        text, width = text_line(line, 0.95)
        scale = min(1.0, 21.5 / max(width, 1e-3))
        half = SQUARE_BASE_HALF + (SQUARE_TOP_HALF - SQUARE_BASE_HALF) * (z - PLINTH) / (SQUARE_TOP - PLINTH)
        frame = facing_text_matrix(Vector((0.0, -(half + 0.17), z)), normal) @ Matrix.Diagonal((scale, 1.0, 1.0, 1.0))
        builder.merge(text, frame)
    return builder


def octagon_tier(builder):
    z0, z1 = OCTAGON_BASE, OCTAGON_TOP
    painted(builder, WHITE, lambda: frustum(builder, 8, OCTAGON_BASE_HALF, OCTAGON_TOP_HALF, z0, z1, WALL))
    painted(builder, WARM, lambda: band(builder, 8, OCTAGON_BASE_HALF, z0, z0 + 0.9, STONE, 0.35))
    mid = (z0 + z1) / 2
    half_mid = (OCTAGON_BASE_HALF + OCTAGON_TOP_HALF) / 2
    painted(builder, WARM, lambda: band(builder, 8, half_mid, mid, mid + 0.45, STONE, 0.25))
    for k in range(8):
        angle = TAU * k / 8
        normal = Vector((math.cos(angle), math.sin(angle), 0.0))
        side = Vector((-normal.y, normal.x, 0.0))
        for z in (z0 + 4.0, z0 + 15.0, z0 + 21.0):
            window(builder, normal, side, OCTAGON_BASE_HALF, OCTAGON_TOP_HALF, z0, z1, 0.0, z, 0.8, 1.8, True)
    painted(builder, WARM, lambda: cornice(builder, 8, OCTAGON_TOP_HALF, OCTAGON_TOP, STONE, 0.75))
    painted(builder, WHITE, lambda: frustum(builder, 8, OCTAGON_TOP_HALF + 0.9, OCTAGON_TOP_HALF + 0.9,
                                            OCTAGON_TOP + 1.0, OCTAGON_TOP + 1.16, STONE, top=True))
    painted(builder, WARM, lambda: parapet(builder, 8, OCTAGON_TOP_HALF + 0.85, OCTAGON_TOP + 1.16, 0.95, 0.4,
                                           STONE))


def cylinder_tier(builder):
    z0 = OCTAGON_TOP + 1.16
    profile = [(CYLINDER_RADIUS + 0.3, z0), (CYLINDER_RADIUS + 0.3, z0 + 0.6), (CYLINDER_RADIUS, z0 + 0.7),
               (CYLINDER_RADIUS, CYLINDER_TOP - 0.6), (CYLINDER_RADIUS + 0.5, CYLINDER_TOP - 0.3),
               (CYLINDER_RADIUS + 0.7, CYLINDER_TOP), (0.0, CYLINDER_TOP)]
    painted(builder, WHITE, lambda: builder.lathe(profile, 24, WALL, smooth=True))
    for k in range(6):
        angle = TAU * (k + 0.5) / 6
        normal = Vector((math.cos(angle), math.sin(angle), 0.0))
        side = Vector((-normal.y, normal.x, 0.0))
        corners = [normal * (CYLINDER_RADIUS + 0.03) + side * du + Vector((0, 0, z0 + 2.0 + dz))
                   for du, dz in ((-0.4, 0.0), (0.4, 0.0), (0.4, 1.6), (-0.4, 1.6))]
        builder.oriented(corners, normal, VOID)


def foyer(builder):
    floor = CYLINDER_TOP
    radius = 3.45
    for k in range(8):
        angle = TAU * (k + 0.5) / 8
        centre = Vector((radius * math.cos(angle), radius * math.sin(angle), 0.0))
        frame = Matrix.Translation(centre) @ Matrix.Rotation(angle, 4, "Z")
        painted(builder, WHITE, lambda frame=frame: builder.box((-0.4, -0.4, floor), (0.4, 0.4, PILLAR_TOP - 0.35),
                                                                STONE, matrix=frame, bottom=False, top=False))
        painted(builder, WARM, lambda frame=frame: builder.box((-0.55, -0.55, PILLAR_TOP - 0.35),
                                                               (0.55, 0.55, PILLAR_TOP), STONE, matrix=frame,
                                                               bottom=False, top=False))
    painted(builder, (0.32, 0.27, 0.22), lambda: builder.lathe(
        [(0.0, floor + 0.05), (1.6, floor + 0.05), (1.8, floor + 0.55), (1.65, floor + 0.95), (1.3, floor + 1.0),
         (1.2, floor + 0.65), (0.0, floor + 0.6)], 14, BRONZE, smooth=True))
    painted(builder, WARM, lambda: builder.lathe([(0.0, PILLAR_TOP), (radius + 0.9, PILLAR_TOP),
                                                  (radius + 0.9, CANOPY_TOP), (0.0, CANOPY_TOP)], 24, STONE,
                                                 smooth=False))
    painted(builder, WHITE, lambda: builder.lathe([(radius + 0.7, CANOPY_TOP), (1.4, CANOPY_TOP + 0.5),
                                                   (0.0, CANOPY_TOP + 0.5)], 24, STONE, smooth=False))
    painted(builder, WARM, lambda: builder.box((-1.0, -1.0, CANOPY_TOP + 0.3), (1.0, 1.0, STATUE_BASE), MARBLE,
                                               bottom=False))


def flames():
    builder = MeshBuilder()
    rng = random.Random(5)
    base = CYLINDER_TOP + 0.75
    for k in range(7):
        angle = TAU * k / 7 + rng.uniform(-0.3, 0.3)
        reach = 0.0 if k == 0 else rng.uniform(0.5, 1.0)
        centre = Matrix.Translation((reach * math.cos(angle), reach * math.sin(angle), base))
        height = rng.uniform(2.4, 3.0) if k == 0 else rng.uniform(1.3, 2.2)
        width = rng.uniform(0.6, 0.9)
        builder.lathe([(width, 0.0), (width * 0.8, height * 0.35), (width * 0.35, height * 0.75), (0.0, height)], 7,
                      FLAME, smooth=True, matrix=centre @ Matrix.Rotation(rng.uniform(-0.15, 0.15), 4, "X"))
    return builder


def bronze(builder):
    builder.materials = [BRONZE for _ in builder.materials]
    return builder


def zeus():
    body = figures.man_himation((1.0, 1.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 1.0),
                                right_hand=(0.32, 0.22, 1.18))
    figures.tube(body, [(-0.25, 0.14, 0.02), (-0.25, 0.14, 1.0), (-0.25, 0.14, 2.05)], [0.022, 0.02, 0.018],
                 (1.0, 1.0, 1.0), 6)
    figures.ellipsoid(body, (-0.25, 0.14, 2.08), (0.05, 0.05, 0.07), (1.0, 1.0, 1.0), 6, 3)
    for k in range(3):
        figures.tube(body, [(0.32, 0.22, 1.18), (0.36 + 0.05 * k, 0.3, 1.24 + 0.05 * k)], [0.012, 0.008],
                     (1.0, 1.0, 1.0), 4)
    scale = STATUE_HEIGHT / 1.72
    statue = MeshBuilder()
    statue.merge(bronze(body), Matrix.Scale(scale, 4))
    return statue


def triton(seed=0):
    builder = MeshBuilder()
    white = (1.0, 1.0, 1.0)
    figures.torso(builder, white, waist=0.95)
    figures.head(builder, white, white, white)
    figures.arms(builder, (0.08, 0.22, 1.56), (-0.08, 0.24, 1.52), white, white)
    path = [Vector((0.0, 0.0, 0.98)), Vector((0.0, -0.02, 0.76)), Vector((0.0, 0.06, 0.52)), Vector((0.0, 0.24, 0.3)),
            Vector((0.0, 0.48, 0.24)), Vector((0.0, 0.66, 0.36)), Vector((0.0, 0.72, 0.58)), Vector((0.0, 0.66, 0.76))]
    radii = [0.17, 0.165, 0.15, 0.13, 0.105, 0.08, 0.055, 0.03]
    figures.tube(builder, path, radii, white, 8, cap=False)
    tip = path[-1]
    for side in (-1, 1):
        figures.panel(builder, [tip, tip + Vector((side * 0.34, 0.06, 0.2)), tip + Vector((side * 0.3, -0.04, 0.32))],
                      white)
    conch = (Matrix.Translation((0.0, 0.2, 1.6)) @ Matrix.Rotation(math.radians(-55 + seed * 4), 4, "X"))
    figures.lathe(builder, [(0.0, 0.0), (0.03, 0.03), (0.07, 0.2), (0.11, 0.33), (0.0, 0.4)], white, 8, conch)
    return bronze(builder)


def tritons():
    builder = MeshBuilder()
    corner = SQUARE_TOP_HALF + 1.05
    seat = OCTAGON_BASE + 1.15
    for k in range(4):
        angle = math.radians(45 + 90 * k)
        cx = corner * math.copysign(1, math.cos(angle))
        cy = corner * math.copysign(1, math.sin(angle))
        painted(builder, WARM, lambda cx=cx, cy=cy: builder.box((cx - 0.9, cy - 0.9, seat - 0.05),
                                                                (cx + 0.9, cy + 0.9, seat + 0.55), STONE,
                                                                bottom=False))
        frame = (Matrix.Translation((cx, cy, seat + 0.55)) @ Matrix.Rotation(angle - math.pi / 2, 4, "Z")
                 @ Matrix.Scale(2.4, 4))
        builder.merge(triton(k), frame)
    builder.merge(zeus(), Matrix.Translation((0.0, 0.0, STATUE_BASE)) @ Matrix.Rotation(math.radians(-15), 4, "Z"))
    return builder


def tower():
    builder = MeshBuilder()
    painted(builder, WARM, lambda: builder.box((-18.0, -18.0, -0.6), (18.0, 18.0, 1.6), STONE, bottom=False))
    painted(builder, WHITE, lambda: builder.box((-16.6, -16.6, 1.6), (16.6, 16.6, PLINTH), STONE, bottom=False))
    painted(builder, WARM, lambda: band(builder, 4, 16.6, PLINTH - 0.5, PLINTH, STONE, 0.3))
    square_tier(builder)
    octagon_tier(builder)
    cylinder_tier(builder)
    foyer(builder)
    return builder


def arcade(builder, start, end, width, z_start, z_end, spans, material, colour, foot=-0.5, parapet_height=1.0):
    direction = (end - start).normalized()
    length = (end - start).length
    side = Vector((-direction.y, direction.x, 0.0))
    pier = 1.8
    span = (length - pier) / spans

    def at(s, offset, z):
        p = start + direction * s + side * offset
        return Vector((p.x, p.y, z))

    def deck(s):
        return z_start + (z_end - z_start) * s / length

    first = len(builder.polygons)
    for k in range(spans + 1):
        s0 = k * span
        s1 = s0 + pier
        corners = [at(s0, -width / 2, foot), at(s1, -width / 2, foot), at(s1, width / 2, foot), at(s0, width / 2, foot),
                   at(s0, -width / 2, deck(s0)), at(s1, -width / 2, deck(s1)), at(s1, width / 2, deck(s1)),
                   at(s0, width / 2, deck(s0))]
        indices = builder.points(corners)
        for quad in ((0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)):
            builder.face([indices[q] for q in quad], material)
    for k in range(spans):
        a = k * span + pier
        b = (k + 1) * span
        half = (b - a) / 2
        middle = a + half
        spring = max(min(deck(a), deck(b)) - 0.9 - half, foot + 0.5)
        arc = [(middle - half * math.cos(math.pi * i / 8), spring + half * math.sin(math.pi * i / 8))
               for i in range(9)]
        for offset, normal in ((-width / 2, -side), (width / 2, side)):
            for (sa, za), (sb, zb) in zip(arc[:-1], arc[1:]):
                builder.oriented([at(sa, offset, za), at(sb, offset, zb), at(sb, offset, deck(sb)),
                                  at(sa, offset, deck(sa))], normal, material)
        for (sa, za), (sb, zb) in zip(arc[:-1], arc[1:]):
            builder.oriented([at(sa, -width / 2, za), at(sb, -width / 2, zb), at(sb, width / 2, zb),
                              at(sa, width / 2, za)], Vector((0, 0, -1)), material)
    builder.tint(first, colour)
    first = len(builder.polygons)
    top_quad = [at(0.0, -width / 2, deck(0.0)), at(length, -width / 2, deck(length)),
                at(length, width / 2, deck(length)), at(0.0, width / 2, deck(0.0))]
    builder.oriented(top_quad, Vector((0, 0, 1)), PAVING)
    if parapet_height > 0:
        for offset in (-width / 2 + 0.25, width / 2 - 0.25):
            builder.sweep([at(0.0, offset, deck(0.0)), at(length, offset, deck(length))],
                          [(-0.25, 0.0), (0.25, 0.0), (0.25, parapet_height), (-0.25, parapet_height)], material,
                          caps=True)
    builder.tint(first, colour)


def ramp(length, foot_level):
    builder = MeshBuilder()
    start = Vector((0.0, -SQUARE_BASE_HALF - 0.3, 0.0))
    end = Vector((0.0, -SQUARE_BASE_HALF - 0.3 - length, 0.0))
    arcade(builder, start, end, 8.0, DOOR[0], foot_level, int(length / 11.0), STONE, WARM, foot=-7.0)
    return builder


def rock_base(outline):
    builder = MeshBuilder()
    lower = [(x * 1.12, y * 1.12) for x, y in outline]
    count = len(outline)
    top = builder.points([(x, y, 0.0) for x, y in outline])
    bottom = builder.points([(x, y, -7.5) for x, y in lower])
    for k in range(count):
        j = (k + 1) % count
        builder.face([bottom[k], bottom[j], top[j], top[k]], ROCK)
    builder.face(top, ROCK)
    builder.tint(0, (0.78, 0.74, 0.68))
    return builder


def enclosure(half=50.0, height=4.5):
    builder = MeshBuilder()
    corners = [Vector((-half, -half, 0.0)), Vector((half, -half, 0.0)), Vector((half, half, 0.0)),
               Vector((-half, half, 0.0))]
    thick = 2.4
    first = len(builder.polygons)
    for k in range(4):
        a, b = corners[k], corners[(k + 1) % 4]
        direction = (b - a).normalized()
        frame = Matrix.Translation((a.x, a.y, 0.0)) @ Matrix.Rotation(math.atan2(direction.y, direction.x), 4, "Z")
        length = (b - a).length
        if k == 0:
            gate = length / 2
            builder.box((0.0, -thick / 2, -6.0), (gate - 5.0, thick / 2, height), WALL, matrix=frame, bottom=False)
            builder.box((gate + 5.0, -thick / 2, -6.0), (length, thick / 2, height), WALL, matrix=frame,
                        bottom=False)
        else:
            builder.box((0.0, -thick / 2, -6.0), (length, thick / 2, height), WALL, matrix=frame, bottom=False)
        builder.box((0.0, -thick / 2 - 0.25, height), (length, thick / 2 + 0.25, height + 0.45), STONE, matrix=frame)
    for corner in corners:
        builder.box((corner.x - 2.8, corner.y - 2.8, -6.0), (corner.x + 2.8, corner.y + 2.8, height + 2.0), WALL,
                    bottom=False)
    builder.tint(first, WARM)
    first = len(builder.polygons)
    builder.box((-half + thick / 2, -half + thick / 2, -0.4), (half - thick / 2, half - thick / 2, 0.0), PAVING,
                bottom=False)
    builder.tint(first, (0.98, 0.94, 0.86))
    rng = random.Random(9)
    for x0, y0, x1, y1 in ((-half + 3.0, half - 14.0, -half + 30.0, half - 3.0),
                           (half - 26.0, half - 14.0, half - 3.0, half - 3.0)):
        painted(builder, (0.98, 0.9, 0.76), lambda x0=x0, y0=y0, x1=x1, y1=y1: builder.box(
            (x0, y0, 0.0), (x1, y1, 5.0), "plaster", bottom=False))
    for k in range(9):
        x = rng.uniform(22.0, 40.0) * (1 if k % 2 else -1)
        y = rng.uniform(-40.0, -22.0)
        w, d, h = rng.uniform(1.4, 2.4), rng.uniform(0.9, 1.4), rng.uniform(0.8, 1.2)
        painted(builder, WHITE, lambda x=x, y=y, w=w, d=d, h=h: builder.box((x, y, 0.0), (x + w, y + d, h), WALL,
                                                                            bottom=False))
    shed = Matrix.Translation((-38.0, -30.0, 0.0))
    painted(builder, (0.55, 0.42, 0.3), lambda: builder.box((-4.0, -3.0, 0.0), (4.0, 3.0, 2.6), "dark_wood",
                                                            matrix=shed, bottom=False, top=False))
    painted(builder, (0.6, 0.48, 0.34), lambda: builder.oriented(
        [shed @ Vector(p) for p in ((-4.4, -3.5, 2.4), (4.4, -3.5, 2.4), (4.4, 3.5, 3.4), (-4.4, 3.5, 3.4))],
        (0, -0.4, 1), "dark_wood"))
    return builder


def beacon_position():
    return Vector((0.0, 0.0, BEACON_HEIGHT))


def total_height():
    return STATUE_BASE + STATUE_HEIGHT
