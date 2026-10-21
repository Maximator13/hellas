import math
import random

from mathutils import Matrix, Vector

from .figures import box, ellipsoid, lathe, tube
from .geometry import MATTE, MeshBuilder

BARK = (0.36, 0.28, 0.20)
OAK_LEAVES = (0.20, 0.30, 0.12)
OAK_LIGHT = (0.30, 0.40, 0.16)
SHRUB = (0.26, 0.34, 0.15)
SHRUB_DRY = (0.46, 0.44, 0.24)
REED = (0.56, 0.60, 0.30)
ROCK = (0.68, 0.65, 0.58)
DARK_ROCK = (0.30, 0.27, 0.24)
STONE = (0.74, 0.68, 0.56)
WALL_STONE = (0.66, 0.60, 0.50)
LIMEWASH = (0.90, 0.86, 0.76)
ROOF = (0.70, 0.40, 0.26)
THATCH = (0.62, 0.52, 0.32)
TIMBER = (0.40, 0.29, 0.19)
LINEN = (0.92, 0.88, 0.78)
STRIPE = (0.62, 0.20, 0.16)
SAFFRON = (0.86, 0.64, 0.26)
PURPLE = (0.42, 0.16, 0.34)
GOLD = (0.88, 0.68, 0.30)
LEATHER = (0.56, 0.42, 0.28)
HIDE = (0.66, 0.54, 0.38)
MARBLE = (0.92, 0.89, 0.82)
WALL = [(-14.0, -238.0), (-24.0, -205.0), (-40.0, -180.0), (-33.0, -152.0), (-50.0, -128.0), (-60.0, -111.0)]
WALL_NORTH = [(-63.0, -97.0), (-72.0, -70.0), (-86.0, -40.0), (-95.0, -8.0), (-104.0, 30.0), (-110.0, 52.0)]


def oak():
    builder = MeshBuilder()
    tube(builder, [(0, 0, -1.5), (0.1, 0, 2.2), (0.3, 0.2, 3.6)], [0.42, 0.32, 0.22], BARK, sides=5)
    ellipsoid(builder, (0.3, 0.2, 5.4), (3.9, 3.6, 2.6), OAK_LEAVES, segments=7, rings=4)
    ellipsoid(builder, (-1.2, 0.9, 6.6), (2.4, 2.2, 1.8), OAK_LIGHT, segments=6, rings=3)
    ellipsoid(builder, (1.6, -0.8, 6.2), (2.2, 2.1, 1.6), OAK_LEAVES, segments=6, rings=3)
    return builder


def shrub(dry=False):
    builder = MeshBuilder()
    ellipsoid(builder, (0, 0, 0.5), (1.4, 1.2, 0.95), SHRUB_DRY if dry else SHRUB, segments=6, rings=3)
    ellipsoid(builder, (0.8, 0.5, 0.35), (0.8, 0.7, 0.6), SHRUB, segments=5, rings=3)
    return builder


def reeds():
    builder = MeshBuilder()
    generator = random.Random(4)
    for _ in range(7):
        x, y = generator.uniform(-0.9, 0.9), generator.uniform(-0.9, 0.9)
        height = generator.uniform(1.6, 2.6)
        lean = (generator.uniform(-0.3, 0.3), generator.uniform(-0.3, 0.3))
        first = len(builder.polygons)
        a, b, c = builder.points([(x - 0.12, y, 0.0), (x + 0.12, y, 0.0), (x + lean[0], y + lean[1], height)])
        builder.face([a, b, c], MATTE)
        builder.face([b, a, c], MATTE)
        builder.tint(first, REED)
    return builder


def boulder(dark=False):
    builder = MeshBuilder()
    ellipsoid(builder, (0, 0, 0.4), (1.6, 1.2, 1.1), DARK_ROCK if dark else ROCK, segments=6, rings=3)
    return builder


def persian_tent(colour):
    builder = MeshBuilder()
    box(builder, (0, 0, 1.0), (7.0, 5.0, 2.6), colour)
    first = len(builder.polygons)
    ridge = builder.points([(-3.6, -2.6, 2.3), (3.6, -2.6, 2.3), (3.6, 0.0, 4.0), (-3.6, 0.0, 4.0),
                            (-3.6, 2.6, 2.3), (3.6, 2.6, 2.3)])
    builder.face([ridge[0], ridge[1], ridge[2], ridge[3]], MATTE)
    builder.face([ridge[3], ridge[2], ridge[5], ridge[4]], MATTE)
    builder.face([ridge[0], ridge[3], ridge[4]], MATTE)
    builder.face([ridge[1], ridge[5], ridge[2]], MATTE)
    builder.tint(first, colour)
    return builder


def greek_tent(colour):
    builder = MeshBuilder()
    first = len(builder.polygons)
    a, b, c, d, e, f = builder.points([(-1.6, -1.5, -0.2), (1.6, -1.5, -0.2), (0.0, -1.5, 1.9),
                                       (-1.6, 1.5, -0.2), (1.6, 1.5, -0.2), (0.0, 1.5, 1.9)])
    for face in ((a, c, b), (d, e, f), (a, d, f, c), (b, c, f, e)):
        builder.face(list(face), MATTE)
    builder.tint(first, colour)
    return builder


def house(seed):
    generator = random.Random(seed)
    builder = MeshBuilder()
    length, width, height = generator.uniform(7, 11), generator.uniform(5, 7), generator.uniform(2.8, 3.6)
    box(builder, (0, 0, height / 2 - 0.5), (length, width, height + 1.0), LIMEWASH if seed % 3 else STONE)
    first = len(builder.polygons)
    top = height - 0.05
    ridge = builder.points([(-length / 2 - 0.4, -width / 2 - 0.5, top), (length / 2 + 0.4, -width / 2 - 0.5, top),
                            (length / 2 + 0.4, 0.0, top + 1.5), (-length / 2 - 0.4, 0.0, top + 1.5),
                            (-length / 2 - 0.4, width / 2 + 0.5, top), (length / 2 + 0.4, width / 2 + 0.5, top)])
    builder.face([ridge[0], ridge[1], ridge[2], ridge[3]], MATTE)
    builder.face([ridge[3], ridge[2], ridge[5], ridge[4]], MATTE)
    builder.face([ridge[0], ridge[3], ridge[4]], MATTE)
    builder.face([ridge[1], ridge[5], ridge[2]], MATTE)
    builder.tint(first, ROOF if seed % 4 else THATCH)
    if generator.random() < 0.6:
        box(builder, (length / 2 + 4.0, 0, 0.4), (8.0, width + 4.0, 1.8), STONE)
    return builder


def shrine(length, width, columns):
    builder = MeshBuilder()
    box(builder, (0, 0, -0.4), (length + 3.0, width + 3.0, 1.8), STONE)
    box(builder, (0, 0, 0.8), (length + 2.0, width + 2.0, 0.6), MARBLE)
    box(builder, (-length * 0.1, 0, 3.6), (length * 0.6, width * 0.62, 5.0), LIMEWASH)
    spacing = length / max(1, columns - 1)
    for k in range(columns):
        for side in (-1, 1):
            x = -length / 2 + k * spacing
            lathe(builder, [(0.42, 1.1), (0.36, 5.9)], MARBLE, segments=6,
                  matrix=Matrix.Translation((x, side * width / 2, 0.0)))
    box(builder, (0, 0, 6.4), (length + 1.6, width + 1.6, 0.9), MARBLE)
    first = len(builder.polygons)
    ridge = builder.points([(-length / 2 - 0.8, -width / 2 - 0.8, 6.85), (length / 2 + 0.8, -width / 2 - 0.8, 6.85),
                            (length / 2 + 0.8, 0.0, 8.6), (-length / 2 - 0.8, 0.0, 8.6),
                            (-length / 2 - 0.8, width / 2 + 0.8, 6.85), (length / 2 + 0.8, width / 2 + 0.8, 6.85)])
    builder.face([ridge[0], ridge[1], ridge[2], ridge[3]], MATTE)
    builder.face([ridge[3], ridge[2], ridge[5], ridge[4]], MATTE)
    builder.face([ridge[0], ridge[3], ridge[4]], MATTE)
    builder.face([ridge[1], ridge[5], ridge[2]], MATTE)
    builder.tint(first, ROOF)
    return builder


def pavilion():
    builder = MeshBuilder()
    box(builder, (0, 0, 2.0), (30.0, 20.0, 5.0), PURPLE)
    for k in range(-3, 4):
        box(builder, (k * 4.2, -10.05, 2.4), (1.4, 0.2, 4.6), GOLD)
    first = len(builder.polygons)
    ridge = builder.points([(-15.5, -10.5, 4.4), (15.5, -10.5, 4.4), (15.5, 0.0, 8.5), (-15.5, 0.0, 8.5),
                            (-15.5, 10.5, 4.4), (15.5, 10.5, 4.4)])
    builder.face([ridge[0], ridge[1], ridge[2], ridge[3]], MATTE)
    builder.face([ridge[3], ridge[2], ridge[5], ridge[4]], MATTE)
    builder.face([ridge[0], ridge[3], ridge[4]], MATTE)
    builder.face([ridge[1], ridge[5], ridge[2]], MATTE)
    builder.tint(first, SAFFRON)
    for x in (-15.0, 15.0):
        tube(builder, [(x, -12.0, -0.5), (x, -12.0, 9.5)], [0.15, 0.12], TIMBER, sides=4)
    return builder


def throne(centre, height_at, facing):
    builder = MeshBuilder()
    x, y = centre
    z = height_at(x, y)
    frame = Matrix.Translation((x, y, z)) @ Matrix.Rotation(math.radians(90 - facing), 4, "Z")
    for local, size, colour in (((0, 0, 0.0), (12.0, 10.0, 1.6), STONE), ((0, 0, 1.2), (4.0, 3.0, 0.6), PURPLE),
                                ((-0.6, 0, 2.2), (1.2, 1.4, 1.4), GOLD), ((-1.2, 0, 3.0), (0.3, 1.4, 1.8), GOLD)):
        box(builder, local, size, colour, matrix=frame)
    first = len(builder.polygons)
    builder.lathe([(0.0, 6.2), (3.2, 5.0)], 8, MATTE, smooth=False, matrix=frame, caps=False)
    builder.tint(first, SAFFRON)
    tube(builder, [frame @ Vector((0.6, 0, 0.8)), frame @ Vector((0.6, 0, 6.2))], [0.08, 0.08], GOLD, sides=4)
    return builder


def rough_wall(points, height_at, height=3.6, thickness=2.6, seed=5):
    generator = random.Random(seed)
    builder = MeshBuilder()
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        length = math.hypot(x1 - x0, y1 - y0)
        heading = math.atan2(y1 - y0, x1 - x0)
        pieces = max(1, int(length / 3.0))
        for piece in range(pieces):
            t = (piece + 0.5) / pieces
            x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            z = height_at(x, y)
            top = height * generator.uniform(0.82, 1.08)
            frame = Matrix.Translation((x, y, z)) @ Matrix.Rotation(heading, 4, "Z")
            half = length / pieces / 2 + 0.25
            first = len(builder.polygons)
            builder.box((-half, -thickness / 2, -2.5), (half, thickness / 2, top), MATTE, matrix=frame, bottom=False)
            shade = generator.uniform(0.86, 1.06)
            builder.tint(first, tuple(c * shade for c in WALL_STONE))
    return builder


def gate_posts(height_at):
    builder = MeshBuilder()
    for x, y in ((-60.0, -111.0), (-63.0, -97.0)):
        box(builder, (x, y, height_at(x, y) + 1.2), (3.2, 3.2, 7.4), STONE)
    return builder


def altar(centre, height_at):
    builder = MeshBuilder()
    x, y = centre
    z = height_at(x, y)
    box(builder, (x, y, z + 0.2), (2.6, 1.6, 1.6), MARBLE)
    box(builder, (x, y, z + 1.05), (2.9, 1.9, 0.2), STONE)
    return builder


def pools(springs, height_at):
    builder = MeshBuilder()
    for x, y, radius in springs:
        z = height_at(x, y) + 0.12
        ring = [builder.point((x + radius * math.cos(a), y + radius * 0.7 * math.sin(a), z))
                for a in [math.tau * k / 10 for k in range(10)]]
        builder.face(ring, "water", raw=True)
    return builder


def rock(centre, height_at, size):
    builder = MeshBuilder()
    x, y = centre
    ellipsoid(builder, (x, y, height_at(x, y) + size * 0.25), (size, size * 0.8, size * 0.9), DARK_ROCK, segments=7,
              rings=4)
    return builder


def village(centre, radius, count, height_at, slope_ok, seed):
    generator = random.Random(seed)
    placed = []
    tries = 0
    while len(placed) < count and tries < count * 40:
        tries += 1
        angle = generator.uniform(0, math.tau)
        distance = radius * math.sqrt(generator.random())
        x = centre[0] + distance * math.cos(angle)
        y = centre[1] + distance * math.sin(angle)
        if not slope_ok(x, y) or any(math.hypot(x - px, y - py) < 14 for px, py, _ in placed):
            continue
        placed.append((x, y, generator.uniform(0, math.pi)))
    return [(x, y, height_at(x, y), turn) for x, y, turn in placed]
