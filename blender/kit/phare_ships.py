import math
import random

from mathutils import Matrix

from .geometry import MeshBuilder

WOOD = "dark_wood"
SAIL = "velum_linen"
HULL = (0.36, 0.26, 0.18)
DECK = (0.58, 0.45, 0.3)
PITCH = (0.16, 0.13, 0.11)


def painted(builder, colour, action):
    first = len(builder.polygons)
    action()
    builder.tint(first, colour)


def hull(builder, length, beam, freeboard, draft, sheer, colour=HULL, stations=10, sharp=0.6):
    half = length / 2
    rows = []
    for k in range(stations + 1):
        t = k / stations
        y = -half + length * t
        width = beam / 2 * max(math.sin(math.pi * (0.04 + 0.92 * t)), 0.02) ** sharp
        top = freeboard + sheer * (2 * t - 1) ** 2
        rows.append([(-width, y, top), (-width * 0.85, y, 0.3), (0.0, y, -draft), (width * 0.85, y, 0.3),
                     (width, y, top)])
    painted(builder, colour, lambda: builder.surface(rows, WOOD, facing=(0, 0, -1)))
    deck_z = freeboard - 0.35
    outline = [(-max(beam / 2 * math.sin(math.pi * (0.1 + 0.8 * k / 8)) ** sharp - 0.15, 0.05), -half * 0.86 + k *
                (1.72 * half / 8), deck_z) for k in range(9)]
    outline += [(-x, y, z) for x, y, z in reversed(outline)]
    painted(builder, DECK, lambda: builder.polygon(outline, WOOD))
    return deck_z


def mast(builder, y, z0, height, radius=0.16):
    painted(builder, (0.42, 0.32, 0.22), lambda: builder.lathe([(radius, z0), (radius * 0.7, z0 + height)], 5, WOOD,
                                                               smooth=True, matrix=Matrix.Translation((0.0, y, 0.0))))


def square_sail(builder, y, top, span, drop, belly, set_sail=True):
    painted(builder, (0.4, 0.3, 0.2), lambda: builder.box((-span / 2 - 0.4, y - 0.1, top - 0.1),
                                                          (span / 2 + 0.4, y + 0.1, top + 0.1), WOOD))
    if not set_sail:
        painted(builder, (0.88, 0.83, 0.72), lambda: builder.lathe([(0.3, -span / 2), (0.3, span / 2)], 6, SAIL,
                                                                   matrix=Matrix.Translation((0.0, y, top - 0.35))
                                                                   @ Matrix.Rotation(math.pi / 2, 4, "Y")))
        return
    columns, rows = 5, 3
    grid = []
    for r in range(rows + 1):
        v = r / rows
        row = []
        for c in range(columns + 1):
            u = c / columns
            bulge = belly * math.sin(math.pi * u) * math.sin(math.pi * (0.15 + 0.85 * v))
            row.append((-span / 2 + span * u, y + bulge, top - drop * v))
        grid.append(row)
    painted(builder, (0.92, 0.87, 0.76), lambda: builder.surface(grid, SAIL))


def stern_post(builder, half, z, scale):
    path = [(0.0, -half + 0.3, z), (0.0, -half - 0.6 * scale, z + 1.0 * scale), (0.0, -half - 0.4 * scale,
                                                                                  z + 2.2 * scale),
            (0.0, -half + 0.4 * scale, z + 2.6 * scale)]
    painted(builder, PITCH, lambda: builder.sweep(path, [(0.18, -0.18), (0.18, 0.18), (-0.18, 0.18), (-0.18, -0.18)],
                                                  WOOD))


def steering_oars(builder, half, beam, z):
    for side in (-1, 1):
        painted(builder, (0.45, 0.34, 0.22), lambda side=side: builder.box(
            (side * beam / 2 - 0.12, -half + 1.0, z - 2.6), (side * beam / 2 + 0.12, -half + 1.4, z + 1.2), WOOD))


def merchant(seed=0, set_sail=True, length=22.0, beam=7.0):
    rng = random.Random(seed)
    builder = MeshBuilder()
    deck = hull(builder, length, beam, 2.6, 1.6, 0.9, sharp=0.5)
    half = length / 2
    stern_post(builder, half, deck + 0.6, 1.4)
    steering_oars(builder, half, beam, deck)
    painted(builder, (0.5, 0.38, 0.26), lambda: builder.box((-beam * 0.3, -half * 0.75, deck),
                                                            (beam * 0.3, -half * 0.45, deck + 1.8), WOOD))
    mast(builder, 1.0, deck, 13.0)
    square_sail(builder, 1.0, deck + 12.2, 11.0 + rng.uniform(-1, 1), 8.0, 1.2, set_sail)
    for k in range(rng.randint(4, 8)):
        x, y = rng.uniform(-beam * 0.25, beam * 0.25), rng.uniform(-half * 0.3, half * 0.6)
        painted(builder, (0.72, 0.44, 0.28), lambda x=x, y=y: builder.lathe(
            [(0.0, 0.0), (0.18, 0.15), (0.2, 0.5), (0.08, 0.85), (0.0, 0.9)], 5, "matte",
            matrix=Matrix.Translation((x, y, deck))))
    return builder


def galley(seed=0, length=37.0, beam=5.4):
    builder = MeshBuilder()
    deck = hull(builder, length, beam, 2.2, 1.1, 0.6, sharp=0.7)
    half = length / 2
    painted(builder, PITCH, lambda: builder.box((-beam / 2 - 0.3, -half * 0.7, 1.0), (beam / 2 + 0.3, half * 0.7, 1.9),
                                                WOOD))
    painted(builder, (0.55, 0.42, 0.26), lambda: builder.box((-0.35, half - 0.4, -0.4), (0.35, half + 2.4, 0.4),
                                                             "bronze_statue"))
    stern_post(builder, half, deck + 0.4, 1.6)
    steering_oars(builder, half, beam, deck)
    for side in (-1, 1):
        for k in range(18):
            y = -half * 0.65 + k * (1.3 * half / 18)
            painted(builder, (0.6, 0.48, 0.32), lambda y=y, side=side: builder.box(
                (min(side * beam / 2, side * (beam / 2 + 3.6)), y - 0.05, 1.05),
                (max(side * beam / 2, side * (beam / 2 + 3.6)), y + 0.05, 1.15), WOOD))
    painted(builder, (0.82, 0.78, 0.68), lambda: builder.box((-beam * 0.32, -half * 0.6, deck),
                                                             (beam * 0.32, half * 0.5, deck + 0.3), SAIL))
    return builder


def fishing_boat(seed=0, length=7.0, beam=2.1):
    builder = MeshBuilder()
    deck = hull(builder, length, beam, 0.9, 0.5, 0.35, colour=(0.42, 0.32, 0.22), stations=6)
    mast(builder, 0.8, deck, 5.0, 0.08)
    painted(builder, (0.86, 0.8, 0.68), lambda: builder.lathe([(0.12, -2.0), (0.12, 2.0)], 5, SAIL,
                                                              matrix=Matrix.Translation((0.0, 0.8, deck + 4.6))
                                                              @ Matrix.Rotation(math.pi / 2, 4, "Y")))
    return builder


def lighter(seed=0, length=11.0, beam=3.6):
    rng = random.Random(seed)
    builder = MeshBuilder()
    deck = hull(builder, length, beam, 1.2, 0.6, 0.3, stations=6, sharp=0.35)
    for k in range(rng.randint(5, 9)):
        x, y = rng.uniform(-1.0, 1.0), rng.uniform(-3.5, 3.5)
        painted(builder, (0.78, 0.72, 0.58), lambda x=x, y=y: builder.box((x - 0.4, y - 0.3, deck),
                                                                          (x + 0.4, y + 0.3, deck + 0.5), SAIL))
    return builder


def nile_barge(seed=0, length=18.0, beam=5.0):
    builder = MeshBuilder()
    deck = hull(builder, length, beam, 1.3, 0.5, 1.1, stations=8, sharp=0.3)
    half = length / 2
    painted(builder, (0.62, 0.5, 0.34), lambda: builder.box((-beam * 0.32, -half * 0.6, deck),
                                                            (beam * 0.32, -half * 0.2, deck + 2.0), WOOD))
    mast(builder, 1.5, deck, 11.0, 0.14)
    square_sail(builder, 1.5, deck + 10.5, 6.0, 7.5, 0.8, True)
    return builder


KINDS = {
    "navire_voile": lambda: merchant(1, True),
    "navire_amarre": lambda: merchant(2, False, 20.0, 6.6),
    "navire_guerre": lambda: galley(3),
    "barque": lambda: fishing_boat(4),
    "allege": lambda: lighter(5),
    "barge_nil": lambda: nile_barge(6),
}


def heading_matrix(x, y, bearing_degrees, z=0.0):
    return Matrix.Translation((x, y, z)) @ Matrix.Rotation(-math.radians(bearing_degrees), 4, "Z")

