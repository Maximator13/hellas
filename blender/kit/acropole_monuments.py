import math
import random

import bpy
from mathutils import Matrix, Vector

from . import acropole_plan as plan
from . import acropole_statues as statues
from . import greek
from .acropole_terrain import acropolis_level
from .buildings import plane_tree
from .geometry import MeshBuilder, placement
from .greek_materials import MARBLE, PAINT, POROS, TERRACOTTA
from .life import ox_cart
from .orders import gable_roof

LIMESTONE = "limestone"
ASHLAR = "ashlar"
PLASTER = "plaster"
WOOD = "dark_wood"
BRONZE_DARK = "bronze"
GOLD = "gold"

PARTHENON = (0.0, 0.0)
PROPYLAEA = (-130.0, 20.0)
OLD_TEMPLE = (-26.0, 38.0)
PROMACHOS = (-81.0, 29.0)
BRAURONION = (-95.0, -22.0)
BRAURONION_AZIMUTH = 14.0
PANDROSEION = (-31.0, 60.0)
OLIVE = (-28.0, 56.0)
GREAT_ALTAR = (23.0, 43.0)
ZEUS_POLIEUS = (58.0, 33.0)
ARREPHORION = (-54.0, 74.0)
WORKSHOP = (122.0, -6.0)
THEATRE = (100.0, -132.0)
ODEON = (184.0, -128.0)
HEPHAISTEION = (-453.0, 449.0)
POIKILE = (-341.0, 538.0)
ROYAL_STOA = (-372.0, 507.0)
BOULEUTERION = (-396.0, 407.0)
THOLOS = (-408.0, 368.0)
FOUNTAIN = (-245.0, 269.0)
TWELVE_GODS = (-336.0, 470.0)
TYRANNICIDES = (-305.0, 420.0)
ELEUSINION = (-146.0, 194.0)
PNYX = (-618.0, -8.0)
BEMA = (-596.0, 8.0)
HELIOTROPION = (-648.0, -26.0)
OLYMPIEION = (574.0, -236.0)

PARTHENON_LEVEL = acropolis_level(*PARTHENON) - 0.15
PROPYLAEA_LEVEL = acropolis_level(*PROPYLAEA)
RAMP = (*plan.to_world(PROPYLAEA, plan.PROPYLAEA_AZIMUTH, 0.0, 100.0),
        *plan.to_world(PROPYLAEA, plan.PROPYLAEA_AZIMUTH, 0.0, 20.0), None, PROPYLAEA_LEVEL - 0.05, 12.0)
AGORA_POLYGON = [(-390.0, 345.0), (-255.0, 335.0), (-245.0, 525.0), (-370.0, 528.0)]

PARTHENON_SPEC = dict(greek.PARTHENON)
PARTHENON_SPEC.update(status="432 BC state, dimensions from docs/scenes/acropole.md",
                      sekos=dict(greek.PARTHENON["sekos"], windows=((-5.7, 2.5, 2.8, 2.7), (5.7, 2.5, 2.8, 2.7))))

HEPHAISTEION_SPEC = {
    "status": "432 BC state: unroofed, rafters and scaffolding",
    "stylobate": (13.71, 31.78), "columns": (6, 13), "steps": 3, "step_rise": 0.36, "step_tread": 0.48,
    "column_height": 5.71, "diameter": 1.02, "corner_diameter": 1.04, "top_ratio": 0.78, "spacing": 2.59,
    "corner_spacing": 2.39, "flank_spacing": None, "slope_degrees": 13.0, "roof": None, "tile_pitch": 0.6,
    "sekos": {"width": 9.3, "wall": 0.8, "front_porch": 4.4, "back_porch": 3.0, "naos": 12.2, "back_room": 0.0,
              "raised": 0.3, "raised_steps": 1, "porch_columns": 2, "porch_diameter": 0.95, "architrave": 0.7,
              "frieze": 0.66, "door": (2.6, 5.0), "back_door": (2.2, 4.2)},
    "inner_colonnade": None, "back_room_columns": None, "metope_reliefs": False, "pediment_figures": False,
    "acroteria": False, "antefixes": False,
}


def frame(point, z, azimuth=0.0, scale=1.0):
    return plan.frame(point[0], point[1], z, azimuth, scale)


def rect_pad(point, azimuth, half_u, half_v, level, margin=6.0, smooth=None):
    pad = {"kind": "rect", "x": point[0], "y": point[1], "azimuth": azimuth, "half_u": half_u, "half_v": half_v,
           "level": level, "margin": margin}
    if smooth:
        pad["smooth"] = smooth
    return pad


def circle_pad(point, radius, level, margin=6.0, smooth=None):
    pad = {"kind": "circle", "x": point[0], "y": point[1], "radius": radius, "level": level, "margin": margin}
    if smooth:
        pad["smooth"] = smooth
    return pad


def pads():
    return [
        rect_pad(plan.to_world(PROPYLAEA, plan.PROPYLAEA_AZIMUTH, 9.0, 3.0), plan.PROPYLAEA_AZIMUTH, 22.0, 23.0,
                 PROPYLAEA_LEVEL - 0.05, 5.0),
        rect_pad(PARTHENON, plan.PARTHENON_AZIMUTH, 18.5, 37.8, PARTHENON_LEVEL - 0.05, 6.0),
        rect_pad(OLD_TEMPLE, plan.PARTHENON_AZIMUTH, 11.6, 22.6, acropolis_level(*OLD_TEMPLE) - 0.05, 5.0),
        rect_pad(plan.to_world(BRAURONION, BRAURONION_AZIMUTH, 0.0, -2.0), BRAURONION_AZIMUTH, 21.0, 6.5,
                 acropolis_level(*BRAURONION) - 0.05, 4.0),
        circle_pad(PROMACHOS, 4.5, acropolis_level(*PROMACHOS) - 0.05, 4.0),
        rect_pad((100.0, -98.0), 0.0, 34.0, 26.0, None, 10.0, 6),
        rect_pad(THEATRE, 0.0, 14.0, 9.0, None, 6.0),
        rect_pad(ODEON, 0.0, 33.0, 36.0, None, 10.0),
        rect_pad((-315.0, 435.0), 0.0, 75.0, 95.0, None, 25.0, 10),
        rect_pad(HEPHAISTEION, 90.0, 9.5, 18.5, None, 8.0),
        rect_pad(POIKILE, 180.0, 21.0, 8.5, None, 6.0),
        rect_pad(ROYAL_STOA, 90.0, 11.0, 6.0, None, 5.0),
        rect_pad(BOULEUTERION, 0.0, 13.5, 13.5, None, 5.0),
        circle_pad(THOLOS, 11.0, None, 5.0),
        rect_pad(FOUNTAIN, 0.0, 10.0, 5.0, None, 4.0),
        rect_pad(ELEUSINION, 0.0, 16.0, 20.0, None, 6.0),
        circle_pad(PNYX, 48.0, None, 14.0, 8),
        rect_pad(OLYMPIEION, 90.0, 23.0, 57.0, None, 8.0),
    ]


def segment_distance(point, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = max(0.0, min(1.0, ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / max(dx * dx + dy * dy, 1e-9)))
    return math.hypot(point[0] - a[0] - t * dx, point[1] - a[1] - t * dy)


def ground(scene, point):
    return scene.ground(point[0], point[1])


def wedge(builder, x0, x1, y0, y1, z0, z1, material, depth=1.5):
    low = min(z0, z1) - depth
    piece = MeshBuilder()
    piece.prism([(y0, low), (y1, low), (y1, z1), (y0, z0)] if y1 > y0 else [(y1, low), (y0, low), (y0, z0), (y1, z1)],
                x0, x1, material)
    builder.merge(piece, Matrix(((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1))))


def hip_house(builder, x0, x1, y0, y1, height, wall=LIMESTONE, roof=TERRACOTTA, pitch=0.32, base=-1.5, tint=None,
              door=None):
    first = len(builder.polygons)
    builder.box((x0, y0, base), (x1, y1, height), wall, bottom=False, top=False)
    if tint is not None:
        builder.tint(first, tint)
    hx, hy = (x1 - x0) / 2, (y1 - y0) / 2
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    eave = 0.35
    top = height + min(hx, hy) * pitch
    if hx >= hy:
        ridge = [(cx - hx + hy, cy, top), (cx + hx - hy, cy, top)]
    else:
        ridge = [(cx, cy - hy + hx, top), (cx, cy + hy - hx, top)]
    a = (x0 - eave, y0 - eave, height)
    b = (x1 + eave, y0 - eave, height)
    c = (x1 + eave, y1 + eave, height)
    d = (x0 - eave, y1 + eave, height)
    r0, r1 = ridge
    if hx >= hy:
        faces = [([a, b, r1, r0], (0, -1, 1)), ([c, d, r0, r1], (0, 1, 1)), ([d, a, r0], (-1, 0, 1)),
                 ([b, c, r1], (1, 0, 1))]
    else:
        faces = [([a, b, r0], (0, -1, 1)), ([c, d, r1], (0, 1, 1)), ([d, a, r0, r1], (-1, 0, 1)),
                 ([b, c, r1, r0], (1, 0, 1))]
    for corners, normal in faces:
        builder.oriented(corners, normal, roof)
    builder.oriented([a, b, c, d], (0, 0, -1), WOOD)
    if door is not None:
        side, position, width, tall = door
        y = (y0 if side < 0 else y1) + side * 0.02
        builder.oriented([(position - width / 2, y, 0.0), (position + width / 2, y, 0.0),
                          (position + width / 2, y, tall), (position - width / 2, y, tall)], (0, side, 0),
                         "shadow_void")


def altar(builder, width, depth, height, material=MARBLE, steps=1):
    hw, hd = width / 2, depth / 2
    builder.box((-hw - 0.4 * steps, -hd - 0.4 * steps, -0.8), (hw + 0.4 * steps, hd + 0.4 * steps, 0.25), LIMESTONE,
                bottom=False)
    builder.box((-hw, -hd, 0.25), (hw, hd, height), material, bottom=False)
    builder.box((-hw - 0.12, -hd - 0.12, height), (hw + 0.12, hd + 0.12, height + 0.22), material, bottom=False)
    first = len(builder.polygons)
    builder.box((-hw + 0.25, -hd + 0.25, height + 0.22), (hw - 0.25, hd - 0.25, height + 0.3), LIMESTONE, bottom=False)
    builder.tint(first, (0.25, 0.22, 0.2))


def enclosure(builder, half_u, half_v, height, material=LIMESTONE, gap=2.5, thickness=0.5):
    builder.box((-half_u, -half_v, -0.6), (half_u, -half_v + thickness, height), material, bottom=False)
    builder.box((-half_u, half_v - thickness, -0.6), (-gap / 2, half_v, height), material, bottom=False)
    builder.box((gap / 2, half_v - thickness, -0.6), (half_u, half_v, height), material, bottom=False)
    builder.box((-half_u, -half_v + thickness, -0.6), (-half_u + thickness, half_v - thickness, height), material,
                bottom=False)
    builder.box((half_u - thickness, -half_v + thickness, -0.6), (half_u, half_v - thickness, height), material,
                bottom=False)


def cyclopean(builder, path, height, depth, rng, material=LIMESTONE, sink=2.0):
    for (x0, y0, z0), (x1, y1, z1) in zip(path[:-1], path[1:]):
        length = math.hypot(x1 - x0, y1 - y0)
        tangent = Vector(((x1 - x0) / length, (y1 - y0) / length, 0.0))
        normal = Vector((tangent.y, -tangent.x, 0.0))
        along = 0.0
        while along < length:
            size = rng.uniform(1.0, 2.3)
            z = min(z0, z1) - sink
            top_course = max(z0, z1) + height
            t = along / length
            base = Vector((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t, 0.0))
            while z < top_course:
                tall = rng.uniform(0.7, 1.4)
                out = rng.uniform(-0.12, 0.12)
                corner = base + normal * out
                rotation = Matrix((tangent, normal, Vector((0.0, 0.0, 1.0)))).transposed().to_4x4()
                rotation.translation = (corner.x, corner.y, z)
                first = len(builder.polygons)
                builder.box((0.0, -depth, 0.0), (min(size, length - along), 0.0, min(tall, top_course - z)), material,
                            matrix=rotation, bottom=False)
                shade = rng.uniform(0.82, 1.02)
                builder.tint(first, (shade, shade * 0.98, shade * 0.95))
                z += tall
            along += size


def wall_run(scene, points, profile, material, tint=(1.0, 1.0, 1.0)):
    path = [(x, y, acropolis_level(x, y)) for x, y in points]
    dense = []
    for (x0, y0, _), (x1, y1, _) in zip(path[:-1], path[1:]):
        count = max(int(math.hypot(x1 - x0, y1 - y0) / 6.0), 1)
        for k in range(count):
            x = x0 + (x1 - x0) * k / count
            y = y0 + (y1 - y0) * k / count
            dense.append((x, y, acropolis_level(x, y)))
    dense.append(path[-1])
    builder = MeshBuilder()
    builder.sweep(dense, profile, material)
    builder.tint(0, tint)
    return builder, dense


def point_along(dense, distance):
    for a, b in zip(dense[:-1], dense[1:]):
        length = math.hypot(b[0] - a[0], b[1] - a[1])
        if distance <= length:
            t = distance / length
            tangent = Vector(((b[0] - a[0]) / length, (b[1] - a[1]) / length, 0.0))
            return Vector((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t)), tangent
        distance -= length
    return None, None


def projection(dense, x):
    best = None
    walked = 0.0
    for a, b in zip(dense[:-1], dense[1:]):
        length = math.hypot(b[0] - a[0], b[1] - a[1])
        if min(a[0], b[0]) <= x <= max(a[0], b[0]) and abs(b[0] - a[0]) > 1e-6:
            best = walked + length * (x - a[0]) / (b[0] - a[0])
        walked += length
    return best


def memorial(dense):
    builder = MeshBuilder()
    start, end = sorted((projection(dense, 70.0), projection(dense, -8.0)))
    count = 26
    for k in range(count):
        point, tangent = point_along(dense, start + (end - start) * (k + 0.5) / count)
        normal = Vector((tangent.y, -tangent.x, 0.0))
        centre = point + normal * 2.1 + Vector((0.0, 0.0, -2.2))
        rotation = Vector((0.0, 0.0, 1.0)).rotation_difference(tangent).to_matrix().to_4x4()
        builder.lathe([(0.0, -0.7), (0.92, -0.7), (0.92, 0.7), (0.0, 0.7)], 16, MARBLE, smooth=False,
                      matrix=Matrix.Translation(centre) @ rotation)
    start, end = sorted((projection(dense, -14.0), projection(dense, -58.0)))
    length = end - start
    pieces = int(length / 1.3)
    for k in range(pieces):
        point, tangent = point_along(dense, start + (k + 0.5) * length / pieces)
        normal = Vector((tangent.y, -tangent.x, 0.0))
        rotation = Matrix((tangent, normal, Vector((0.0, 0.0, 1.0)))).transposed().to_4x4()
        rotation.translation = point + normal * 1.9 + Vector((0.0, 0.0, -4.0))
        builder.box((-0.65, -0.4, 0.0), (0.65, 0.25, 0.9), POROS, matrix=rotation, bottom=False)
        first = len(builder.polygons)
        if k % 2 == 0:
            builder.box((-0.35, 0.25, 0.95), (0.35, 0.33, 1.9), PAINT, matrix=rotation, bottom=False)
            builder.tint(first, greek.PALETTE["triglyph"])
        else:
            builder.box((-0.6, 0.18, 0.95), (0.6, 0.26, 1.9), POROS, matrix=rotation, bottom=False)
        builder.box((-0.65, -0.4, 1.95), (0.65, 0.5, 2.4), POROS, matrix=rotation, bottom=False)
    return builder


def acropolis_walls(scene):
    outline = plan.ACROPOLIS_OUTLINE
    east = outline.index((156.0, 8.0))
    north_end = outline.index((-128.0, 48.0))
    profile = [(2.0, -16.0), (2.0, 1.3), (1.2, 1.3), (1.2, 0.06), (-1.5, 0.06)]
    south, _ = wall_run(scene, plan.wobbly(outline[1:east + 1], False), profile, ASHLAR)
    north, dense = wall_run(scene, plan.wobbly(outline[east:north_end + 1], False), profile, LIMESTONE,
                            (0.92, 0.88, 0.8))
    scene.unique("acropole", south)
    scene.unique("acropole", north)
    scene.unique("acropole", memorial(dense))
    rng = random.Random(5)
    builder = MeshBuilder()
    fragment = [(-121.0, -12.0), (-116.0, -21.0), (-108.0, -27.0)]
    cyclopean(builder, [(x, y, scene.ground(x, y)) for x, y in fragment], 3.2, 3.0, rng)
    pelargikon = [(-170.0, -52.0), (-196.0, -30.0), (-214.0, 5.0), (-212.0, 42.0), (-196.0, 72.0), (-170.0, 92.0)]
    cyclopean(builder, [(x, y, scene.ground(x, y)) for x, y in pelargikon], 0.9, 1.8, rng, LIMESTONE, 1.2)
    scene.unique("acropole", builder)
    return {"north_wall_points": len(dense)}


def parthenon(scene):
    temple = greek.temple(PARTHENON_SPEC, True, "high", "parthenon")
    matrix = frame(PARTHENON, PARTHENON_LEVEL, plan.PARTHENON_AZIMUTH)
    greek.place_building(temple, scene.library, scene.collection, scene.tiles, scene.root("acropole"), matrix)
    sekos = temple.info["sekos"]
    spec = PARTHENON_SPEC["sekos"]
    floor = temple.info["stylobate_top"] + spec["raised"]
    front_wall = sekos["front_wall"]
    naos_front = sekos["naos"][1]
    statue_y = naos_front - 19.05
    interior = MeshBuilder()
    interior.merge(statues.parthenos_group(), Matrix.Translation((0.0, statue_y, floor)))
    pool_y0 = statue_y + statues.PARTHENOS_BASE[1] / 2 + 0.3
    pool_y1 = pool_y0 + 9.4
    half = 4.8
    for x0, x1, y0, y1 in ((-half - 0.3, half + 0.3, pool_y0 - 0.3, pool_y0), (-half - 0.3, half + 0.3, pool_y1,
                                                                                 pool_y1 + 0.3),
                           (-half - 0.3, -half, pool_y0, pool_y1), (half, half + 0.3, pool_y0, pool_y1)):
        first = len(interior.polygons)
        interior.box((x0, y0, floor - 0.05), (x1, y1, floor + 0.14), LIMESTONE, bottom=False)
        interior.tint(first, (0.32, 0.32, 0.34))
    interior.polygon([(-half, pool_y0, floor + 0.07), (half, pool_y0, floor + 0.07), (half, pool_y1, floor + 0.07),
                      (-half, pool_y1, floor + 0.07)], "bassin")
    dp = spec["porch_diameter"]
    axis_x = spec["width"] / 2 - 0.46 * dp
    xs = [-axis_x + 2 * axis_x * k / (spec["porch_columns"] - 1) for k in range(spec["porch_columns"])]
    y = sekos["front_axis"]
    for bay, (a, b) in enumerate(zip(xs[:-1], xs[1:])):
        if bay not in (0, len(xs) - 2):
            continue
        left, right = a + dp / 2, b - dp / 2
        interior.box((left, y - 0.06, floor), (right, y + 0.06, floor + 0.25), BRONZE_DARK)
        interior.box((left, y - 0.06, floor + 6.2), (right, y + 0.06, floor + 6.4), BRONZE_DARK)
        bars = int((right - left) / 0.32)
        for k in range(1, bars):
            x = left + (right - left) * k / bars
            interior.box((x - 0.03, y - 0.03, floor + 0.25), (x + 0.03, y + 0.03, floor + 6.2), BRONZE_DARK,
                         bottom=False, top=False)
        interior.box((left, y - 0.05, floor + 3.1), (right, y + 0.05, floor + 3.22), BRONZE_DARK)
    half_width = spec["width"] / 2
    ceiling_z = temple.info["ceiling"]
    first = len(interior.polygons)
    interior.oriented([(-half_width, sekos["back_axis"], ceiling_z - 0.02), (half_width, sekos["back_axis"], ceiling_z - 0.02),
                       (half_width, sekos["front_axis"], ceiling_z - 0.02), (-half_width, sekos["front_axis"], ceiling_z - 0.02)],
                      (0, 0, -1), PAINT)
    interior.tint(first, (0.10, 0.16, 0.36))
    first = len(interior.polygons)
    for k in range(int(2 * half_width / 1.9) + 1):
        x = -half_width + k * 1.9
        interior.box((x - 0.14, sekos["back_axis"], ceiling_z - 0.42), (x + 0.14, sekos["front_axis"], ceiling_z - 0.02),
                     PAINT, top=False)
    length = sekos["front_axis"] - sekos["back_axis"]
    for k in range(int(length / 1.9) + 1):
        y = sekos["back_axis"] + k * 1.9
        interior.box((-half_width, y - 0.12, ceiling_z - 0.36), (half_width, y + 0.12, ceiling_z - 0.02), PAINT, top=False)
    interior.tint(first, (0.42, 0.13, 0.08))
    scene.unique("athena", interior, matrix)
    world = lambda local: matrix @ Vector(local)
    door_centre = world((0.0, front_wall + spec["wall"] / 2, floor + spec["door"][1] / 2))
    return {"info": {k: v for k, v in temple.info.items() if k != "sekos"},
            "matrix": [list(row) for row in matrix],
            "floor": round(matrix.translation.z + floor, 3),
            "door_centre": list(door_centre),
            "door_inside": list(world((0.0, front_wall - 0.2, floor))),
            "statue": list(world((0.0, statue_y, floor))),
            "statue_face": list(world((0.0, statue_y + 0.3, floor + statues.PARTHENOS_BASE[2] + 9.2))),
            "pool_front": list(world((0.0, pool_y1 + 0.6, floor))),
            "pool_centre": list(world((0.0, (pool_y0 + pool_y1) / 2, floor + 0.1))),
            "windows": [list(world((x, front_wall + spec["wall"] / 2, floor + 4.1))) for x in (-5.7, 5.7)],
            "naos": [list(world((0.0, sekos["naos"][0], floor))), list(world((0.0, sekos["naos"][1], floor)))],
            "east_front": list(world((0.0, temple.info["flank_axes"][-1], temple.info["stylobate_top"]))),
            "pediment": list(world((0.0, temple.info["flank_axes"][-1], temple.info["eave"] + 2.0)))}


def bosses(points):
    return [Matrix.Translation(p) for p in points]


def boss():
    builder = MeshBuilder()
    builder.box((-0.17, 0.0, -0.11), (0.17, 0.22, 0.11), MARBLE, bottom=True)
    return builder


def block(size=(1.4, 0.7, 0.62)):
    builder = MeshBuilder()
    x, y, z = size
    builder.box((-x / 2, -y / 2, 0.0), (x / 2, y / 2, z), MARBLE, bottom=False)
    builder.box((-0.15, y / 2, z * 0.35), (0.15, y / 2 + 0.18, z * 0.65), MARBLE)
    builder.box((-0.15, -y / 2 - 0.18, z * 0.35), (0.15, -y / 2, z * 0.65), MARBLE)
    return builder


def scaffold(builder, x0, x1, height, decks, dismantled, rng, matrix):
    piece = MeshBuilder()
    bays = max(int((x1 - x0) / 2.2), 1)
    for k in range(bays + 1):
        x = x0 + (x1 - x0) * k / bays
        if rng.random() < dismantled:
            continue
        for y in (0.6, 1.9):
            piece.box((x - 0.07, y - 0.07, -0.6), (x + 0.07, y + 0.07, height), WOOD, bottom=False)
    for level in decks:
        if rng.random() < dismantled * 0.6:
            continue
        piece.box((x0, 0.4, level - 0.06), (x1, 2.1, level), WOOD)
        for y in (0.6, 1.9):
            piece.box((x0, y - 0.05, level + 0.9), (x1, y + 0.05, level + 1.0), WOOD)
    builder.merge(piece, matrix)


def propylaea(scene):
    azimuth = plan.PROPYLAEA_AZIMUTH
    z = PROPYLAEA_LEVEL
    matrix = frame(PROPYLAEA, z, azimuth)
    from .acropole_life import away_from_eyes
    gate = greek.propylon(polychromy=True, detail="high", name="propylees", acroteria=False)
    greek.place_building(gate, scene.library, scene.collection, scene.tiles, scene.root("acropole"), matrix)
    top = gate.info["stylobate_top"]
    ramps = MeshBuilder()
    wedge(ramps, -1.9, 1.9, 17.5, 12.4, 0.0, top, MARBLE)
    wedge(ramps, -1.9, 1.9, -17.5, -12.4, 0.0, top, MARBLE)
    scene.unique("propylees_rampe", ramps, matrix)
    wings = MeshBuilder()
    pinakotheke = greek.stoa(length=11.0, depth=5.4, column_height=5.85, diameter=1.04, steps=3, step_rise=0.33,
                             step_tread=0.45, inner_columns=False, roof=MARBLE, polychromy=True, detail="medium",
                             name="pinacotheque", acroteria=False)
    north_wing = matrix @ Matrix.Translation((14.6, 13.0, 0.0)) @ Matrix.Rotation(math.pi / 2, 4, "Z")
    greek.place_building(pinakotheke, scene.library, scene.collection, scene.tiles, scene.root("acropole"), north_wing)
    hip_house(wings, 20.4, 29.5, 5.2, 20.6, 7.2, MARBLE, MARBLE, 0.28, -2.0, door=(-1, 12.9, 2.2, 4.0))
    wings.box((20.2, 6.0, 2.6), (20.45, 8.0, 4.4), "shadow_void")
    south = greek.stoa(length=7.6, depth=4.2, column_height=5.85, diameter=1.04, steps=3, step_rise=0.33,
                       step_tread=0.45, inner_columns=False, roof=MARBLE, polychromy=True, detail="medium",
                       name="aile_sud", acroteria=False)
    south_wing = matrix @ Matrix.Translation((-14.6, 11.5, 0.0)) @ Matrix.Rotation(-math.pi / 2, 4, "Z")
    greek.place_building(south, scene.library, scene.collection, scene.tiles, scene.root("acropole"), south_wing)
    rng = random.Random(11)
    for side, dismantled, decks in ((-1, 0.25, (3.0, 6.0, 9.0)), (1, 0.5, (3.0, 6.0))):
        scaffold(wings, -9.0, -1.5, 9.5, decks, dismantled, rng,
                 Matrix.Translation((side * 10.34, 0.0, 0.0)) @ Matrix.Rotation(-side * math.pi / 2, 4, "Z"))
    for k in range(9):
        wings.box((-14.0 + k * 0.18, -21.0, 0.0 + 0.16 * (k % 3)), (-13.88 + k * 0.18, -13.0, 0.16 + 0.16 * (k % 3)),
                  WOOD, bottom=False)
    eleusis = "eleusis"
    for side in (-1, 1):
        x0, x1 = sorted((side * 10.34, side * 10.38))
        wings.box((x0, -9.25, top - 0.02), (x1, 9.25, top + 0.52), eleusis, bottom=False)
    wings.box((-10.78, 11.92, top - 0.37), (10.78, 12.44, top + 0.005), eleusis, bottom=False)
    for x0, x1, y0, y1 in ((20.36, 29.54, 5.16, 5.2), (20.36, 29.54, 20.6, 20.64), (20.36, 20.4, 5.2, 20.6),
                           (29.5, 29.54, 5.2, 20.6)):
        wings.box((x0, y0, -0.3), (x1, y1, 0.55), eleusis, bottom=False)
    scene.unique("acropole", wings, matrix)
    boss_points = []
    for side in (-1, 1):
        x = side * 10.38
        for row in range(9):
            for column in range(7):
                y = -8.8 + column * 1.2 + (0.6 if row % 2 else 0.0)
                if y > -1.5:
                    continue
                boss_points.append(matrix @ Matrix.Translation((x, y, 0.9 + row * 0.92))
                                   @ Matrix.Rotation(-side * math.pi / 2, 4, "Z"))
    for row in range(5):
        for column in range(6):
            boss_points.append(matrix @ Matrix.Translation((29.5 + 0.0, 6.4 + column * 2.3, 0.9 + row * 1.2))
                               @ Matrix.Rotation(-math.pi / 2, 4, "Z"))
    scene.instances("acropole", "tenon", boss, boss_points, cast_shadow=False)
    blocks = []
    for k in range(16):
        u = rng.uniform(-16.0, 16.0)
        v = rng.uniform(-30.0, -19.0)
        x, y = plan.to_world(PROPYLAEA, azimuth, u, v)
        if abs(u) < 4.0 or not away_from_eyes(x, y, 1.0):
            continue
        blocks.append(frame((x, y), scene.ground.surface(x, y) - 0.02, azimuth + rng.uniform(-20, 20)))
    scene.instances("acropole", "bloc_marbre", block, blocks)
    cx, cy = plan.to_world(PROPYLAEA, azimuth, 9.5, -24.0)
    scene.instances("acropole", "chariot_boeufs", ox_cart, [frame((cx, cy), scene.ground(cx, cy), azimuth + 200.0)])
    east = plan.to_world(PROPYLAEA, azimuth, 0.0, -12.4)
    west = plan.to_world(PROPYLAEA, azimuth, 0.0, 12.4)
    porch = plan.to_world(PROPYLAEA, azimuth, -4.0, -8.0)
    return {"info": {k: v for k, v in gate.info.items() if k != "doors"}, "matrix": [list(r) for r in matrix],
            "east": [*east, z + top], "west": [*west, z + top], "porch": [*porch, z + top]}


def promachos(scene):
    z = ground(scene, PROMACHOS)
    scene.unique("bronze", statues.promachos(8.0), frame(PROMACHOS, z, plan.PROPYLAEA_AZIMUTH))
    return {"base": [*PROMACHOS, z], "head": [PROMACHOS[0], PROMACHOS[1], z + 1.85 + 8.0 * 0.92]}


def old_temple(scene):
    builder = MeshBuilder()
    builder.box((-10.7, -21.7, -1.2), (10.7, 21.7, 0.45), POROS, bottom=False)
    for x0, x1, y0, y1 in ((-10.7, 10.7, -21.7, -19.5), (-10.7, 10.7, 19.5, 21.7), (-10.7, -8.5, -19.5, 19.5),
                           (8.5, 10.7, -19.5, 19.5)):
        first = len(builder.polygons)
        builder.box((x0, y0, 0.45), (x1, y1, 0.75), POROS, bottom=False)
        builder.tint(first, (0.86, 0.84, 0.8))
    builder.box((-6.7, -17.0, 0.0), (6.7, 17.0, 7.6), LIMESTONE, bottom=False, top=False)
    builder.tint(len(builder.polygons) - 4, (0.95, 0.9, 0.82))
    gable_roof(builder, -17.6, 17.6, 7.3, 7.5, 9.6, TERRACOTTA, "y", True, 0.6)
    for y, side in ((-17.0, -1), (17.0, 1)):
        builder.oriented([(-6.7, y, 7.6), (6.7, y, 7.6), (0.0, y, 9.55)], (0, side, 0), LIMESTONE)
    builder.oriented([(-7.3, -17.6, 7.5), (7.3, -17.6, 7.5), (7.3, 17.6, 7.5), (-7.3, 17.6, 7.5)], (0, 0, -1), WOOD)
    for y, side in ((17.02, 1), (-17.02, -1)):
        builder.oriented([(-1.6, y, 0.0), (1.6, y, 0.0), (1.6, y, 5.0), (-1.6, y, 5.0)], (0, side, 0), "shadow_void")
    rng = random.Random(23)
    for k in range(10):
        x = rng.choice((-9.6, 9.6))
        y = rng.uniform(-18.0, 18.0)
        builder.lathe([(0.0, 0.45), (0.8, 0.45), (0.8, 0.45 + rng.uniform(0.5, 1.0)), (0.0, 0.45 + 0.8)], 10, POROS,
                      smooth=False, matrix=Matrix.Translation((x, y, 0.0)))
    z = ground(scene, OLD_TEMPLE)
    scene.unique("acropole", builder, frame(OLD_TEMPLE, z, plan.PARTHENON_AZIMUTH))
    return {"level": z}


def north_sanctuaries(scene):
    pandroseion = MeshBuilder()
    enclosure(pandroseion, 9.0, 7.0, 1.5)
    altar(pandroseion, 1.6, 1.2, 0.9, MARBLE)
    pandroseion.box((4.5, -5.5, -0.5), (7.0, -3.0, 0.8), LIMESTONE, bottom=False)
    scene.unique("acropole", pandroseion, frame(PANDROSEION, ground(scene, PANDROSEION), plan.PARTHENON_AZIMUTH))
    great = MeshBuilder()
    great.box((-7.0, -4.5, -1.0), (7.0, 4.5, 0.3), LIMESTONE, bottom=False)
    great.merge(altar_builder(8.0, 3.6, 1.5), Matrix.Translation((0.0, 0.0, 0.3)))
    scene.unique("acropole", great, frame(GREAT_ALTAR, ground(scene, GREAT_ALTAR), plan.PARTHENON_AZIMUTH))
    zeus = MeshBuilder()
    enclosure(zeus, 10.0, 7.0, 1.3, gap=3.0)
    zeus.merge(altar_builder(3.0, 2.0, 1.1), Matrix.Translation((0.0, 0.0, 0.0)))
    hip_house(zeus, -9.0, -4.0, -5.5, -2.0, 3.0, LIMESTONE, TERRACOTTA, 0.3, -0.8)
    scene.unique("acropole", zeus, frame(ZEUS_POLIEUS, ground(scene, ZEUS_POLIEUS), plan.PARTHENON_AZIMUTH))
    house = MeshBuilder()
    hip_house(house, -6.0, 6.0, -5.5, 5.5, 4.8, PLASTER, TERRACOTTA, 0.3, -1.5, door=(-1, 0.0, 1.4, 2.4))
    enclosure(house, 7.5, 8.5, 1.8, PLASTER)
    scene.unique("acropole", house, frame(ARREPHORION, ground(scene, ARREPHORION), plan.PARTHENON_AZIMUTH + 8.0))
    z = ground(scene, OLIVE)
    from .acropole_city import ancient_olive
    scene.instances("acropole", "olivier_sacre", lambda: ancient_olive(6.5, 4), [frame(OLIVE, z - 0.15, 30.0)])
    return {"altar": [*GREAT_ALTAR, ground(scene, GREAT_ALTAR) + 2.5],
            "zeus_altar": [*ZEUS_POLIEUS, ground(scene, ZEUS_POLIEUS) + 2.0], "olive": [*OLIVE, z + 3.0]}


def altar_builder(width, depth, height):
    builder = MeshBuilder()
    altar(builder, width, depth, height)
    return builder


def brauronion(scene):
    z = ground(scene, BRAURONION)
    stoa = greek.stoa(length=36.0, depth=6.8, column_height=4.2, diameter=0.62, steps=2, step_rise=0.25,
                      step_tread=0.4, inner_columns=False, roof=TERRACOTTA, polychromy=False, detail="medium",
                      name="brauronion")
    matrix = frame(BRAURONION, z, BRAURONION_AZIMUTH)
    greek.place_building(stoa, scene.library, scene.collection, scene.tiles, scene.root("acropole"), matrix)
    wings = MeshBuilder()
    for side in (-1, 1):
        x0, x1 = sorted((side * 18.6, side * 24.8))
        hip_house(wings, x0, x1, -6.8, 2.5, 4.9, LIMESTONE, TERRACOTTA, 0.3, -1.5)
    scene.unique("acropole", wings, matrix)
    return {"level": z}


def nike_bastion(scene):
    centre = plan.to_world(PROPYLAEA, plan.PROPYLAEA_AZIMUTH, -21.0, 23.0)
    top = PROPYLAEA_LEVEL + 0.4
    rng = random.Random(41)
    builder = MeshBuilder()
    half_u, half_v = 7.5, 9.5
    corners = [(-half_u, -half_v), (half_u, -half_v), (half_u, half_v), (-half_u, half_v)]
    world = [plan.to_world(centre, plan.PROPYLAEA_AZIMUTH + 8.0, u, v) for u, v in corners]
    base = min(scene.ground(x, y) for x, y in world) - 2.0
    ring = [(x, y, base) for x, y in world] + [(world[0][0], world[0][1], base)]
    cyclopean(builder, ring[::-1], top - base, 2.6, rng, LIMESTONE, 0.0)
    lid = [(x, y, top) for x, y in world]
    builder.polygon(lid if sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(lid, lid[1:] + lid[:1])) > 0 else lid[::-1],
                    LIMESTONE, color=(0.86, 0.82, 0.74))
    scene.unique("acropole", builder)
    shrine = MeshBuilder()
    hip_house(shrine, -1.8, 1.8, -2.2, 2.2, 3.4, POROS, TERRACOTTA, 0.35, -0.3, door=(1, 0.0, 1.1, 2.2))
    shrine.merge(altar_builder(1.8, 1.2, 1.0), Matrix.Translation((0.0, 5.2, 0.0)))
    scene.unique("acropole", shrine, frame(centre, top, plan.PROPYLAEA_AZIMUTH - 180.0 + 8.0))
    return {"top": [*centre, top]}


def workshop(scene):
    builder = MeshBuilder()
    for x in (-6.0, 0.0, 6.0):
        for y in (-3.5, 3.5):
            builder.box((x - 0.12, y - 0.12, -0.3), (x + 0.12, y + 0.12, 3.6), WOOD, bottom=False)
    for side in (-1, 1):
        builder.oriented([(-6.6, 0.0, 4.3), (6.6, 0.0, 4.3), (6.6, side * 4.3, 3.3), (-6.6, side * 4.3, 3.3)],
                         (0, side, 1), WOOD)
        builder.oriented([(-6.6, 0.0, 4.25), (6.6, 0.0, 4.25), (6.6, side * 4.3, 3.25), (-6.6, side * 4.3, 3.25)],
                         (0, -side, -1), WOOD)
    builder.box((-1.0, -0.8, 0.0), (1.0, 0.8, 0.9), MARBLE, bottom=False)
    builder.merge(monochrome(statues.athena("promachos"), MARBLE,
                             Matrix.Translation((0.0, 0.0, 0.9)) @ Matrix.Scale(0.9, 4)))
    z = ground(scene, WORKSHOP)
    scene.unique("acropole", builder, frame(WORKSHOP, z, plan.PARTHENON_AZIMUTH))
    rng = random.Random(17)
    blocks = []
    for k in range(10):
        x, y = WORKSHOP[0] + rng.uniform(-12.0, 12.0), WORKSHOP[1] + rng.uniform(-9.0, 9.0)
        if abs(x - WORKSHOP[0]) < 7.5 and abs(y - WORKSHOP[1]) < 5.0:
            continue
        blocks.append(frame((x, y), scene.ground.surface(x, y) - 0.02, rng.uniform(0, 360)))
    scene.instances("acropole", "bloc_marbre", block, blocks)
    return {"centre": [*WORKSHOP, z]}


def stele(height=1.9):
    builder = MeshBuilder()
    builder.box((-0.42, -0.3, -0.4), (0.42, 0.3, 0.25), LIMESTONE, bottom=False)
    builder.box((-0.3, -0.09, 0.25), (0.3, 0.09, height), MARBLE, bottom=False)
    for line in range(7):
        z = height - 0.25 - line * 0.13
        first = len(builder.polygons)
        builder.polygon([(-0.24, -0.095, z), (0.24, -0.095, z), (0.24, -0.095, z + 0.05), (-0.24, -0.095, z + 0.05)],
                        PAINT)
        builder.tint(first, (0.62, 0.12, 0.08))
    return builder


def monochrome(source, material, matrix):
    builder = MeshBuilder()
    copy = MeshBuilder()
    copy.points(source.positions)
    for indices, smooth in zip(source.polygons, source.polygon_smooth):
        copy.face(list(indices), material, smooth)
    builder.merge(copy, matrix)
    return builder


def votive():
    builder = MeshBuilder()
    builder.box((-0.35, -0.35, -0.3), (0.35, 0.35, 1.25), LIMESTONE, bottom=False)
    builder.merge(monochrome(statues.athena("promachos"), "bronze_statue",
                             Matrix.Translation((0.0, 0.0, 1.25)) @ Matrix.Scale(0.72, 4)))
    return builder


def offerings(scene, avoid):
    rng = random.Random(29)
    clusters = [((-100.0, 2.0), 9.0, 14), ((-66.0, -24.0), 11.0, 18), ((-52.0, 14.0), 8.0, 10), ((-6.0, 30.0), 7.0, 8),
                ((40.0, 28.0), 8.0, 10), ((75.0, 14.0), 9.0, 8), ((-110.0, 32.0), 7.0, 6)]
    steles, votives = [], []
    for (cx, cy), radius, count in clusters:
        placed = 0
        attempts = 0
        while placed < count and attempts < count * 30:
            attempts += 1
            x, y = cx + rng.uniform(-radius, radius), cy + rng.uniform(-radius, radius)
            if not avoid(x, y, 1.6):
                continue
            z = scene.ground.surface(x, y)
            turn = rng.uniform(-25.0, 25.0) + 257.0
            if rng.random() < 0.75:
                steles.append(frame((x, y), z, turn, 1.0) @ Matrix.Diagonal((1.0, 1.0, rng.uniform(0.75, 1.35), 1.0)))
            else:
                votives.append(frame((x, y), z, turn + 180.0))
            placed += 1
    x, y = -44.0, 16.0
    steles.append(frame((x, y), scene.ground(x, y), 257.0) @ Matrix.Diagonal((1.4, 1.2, 1.95, 1.0)))
    scene.instances("acropole", "stele", stele, steles, cast_shadow=False)
    scene.instances("acropole", "offrande_bronze", votive, votives, cast_shadow=False)
    return {"steles": len(steles), "votives": len(votives)}


def build_acropolis(scene):
    from .acropole_life import clear_of_routes
    info = {"parthenon": parthenon(scene), "propylees": propylaea(scene), "murs": acropolis_walls(scene),
            "promachos": promachos(scene), "vieux_temple": old_temple(scene), "nord": north_sanctuaries(scene),
            "brauronion": brauronion(scene), "nike": nike_bastion(scene), "atelier": workshop(scene)}
    info["offrandes"] = offerings(scene, clear_of_routes)
    return info


def ikria():
    builder = MeshBuilder()
    builder.box((-2.0, -0.2, 0.32), (2.0, 0.2, 0.42), WOOD)
    builder.box((-2.0, 0.55, -0.05), (2.0, 0.95, 0.03), WOOD)
    for x in (-1.8, 0.0, 1.8):
        for y in (0.0, 0.75):
            builder.box((x - 0.07, y - 0.07, -3.5), (x + 0.07, y + 0.07, 0.32), WOOD, bottom=False, top=False)
    return builder


def theatre(scene):
    level = ground(scene, THEATRE)
    benches = []
    previous = level + 0.2
    for row in range(16):
        y = THEATRE[1] + 10.0 + row * 2.0
        half = 16.0 + row * 0.9
        count = int(2 * half / 4.0)
        z = max(scene.ground(THEATRE[0], y) + 0.05, previous + 0.3)
        previous = z
        for k in range(count):
            x = THEATRE[0] - half + 2.0 + k * 4.0
            if abs(x - THEATRE[0]) < 1.2:
                continue
            zx = max(z, scene.ground(x, y) + 0.05)
            benches.append(placement(x, y, zx, math.pi))
    scene.instances("pente_sud", "ikria", ikria, benches)
    builder = MeshBuilder()
    skene_y = THEATRE[1] - 11.0
    builder.box((-12.0, -2.5, -1.0), (12.0, 2.5, 5.2), WOOD, bottom=False)
    builder.oriented([(-12.4, -2.9, 5.2), (12.4, -2.9, 5.2), (12.4, 2.9, 5.2), (-12.4, 2.9, 5.2)], (0, 0, 1), WOOD)
    for x in (-6.0, 0.0, 6.0):
        builder.oriented([(x - 0.9, 2.52, 0.0), (x + 0.9, 2.52, 0.0), (x + 0.9, 2.52, 2.8), (x - 0.9, 2.52, 2.8)],
                         (0, 1, 0), "shadow_void")
    scene.unique("pente_sud", builder, placement(THEATRE[0], skene_y, scene.ground(THEATRE[0], skene_y)))
    temple_point = (THEATRE[0] - 6.0, THEATRE[1] - 34.0)
    shrine = MeshBuilder()
    hip_house(shrine, -4.0, 4.0, -6.5, 6.5, 5.0, POROS, TERRACOTTA, 0.35, -1.5, door=(1, 0.0, 1.6, 3.0))
    shrine.merge(altar_builder(2.4, 1.6, 1.0), Matrix.Translation((0.0, 12.0, 0.0)))
    scene.unique("pente_sud", shrine, placement(*temple_point, scene.ground(*temple_point), 0.0))
    return {"orchestra": [*THEATRE, level], "rows": 16, "benches": len(benches)}


def odeon(scene):
    z = ground(scene, ODEON)
    half_x, half_y = 31.2, 34.3
    builder = MeshBuilder()
    builder.box((-half_x, -half_y, -3.0), (half_x, half_y, 7.5), POROS, bottom=False, top=False)
    builder.tint(0, (0.95, 0.9, 0.82))
    eave = 7.2
    apex = (0.0, 0.0, 7.2 + 0.36 * half_x)
    corners = [(-half_x - 0.8, -half_y - 0.8, eave), (half_x + 0.8, -half_y - 0.8, eave),
               (half_x + 0.8, half_y + 0.8, eave), (-half_x - 0.8, half_y + 0.8, eave)]
    for a, b in zip(corners, corners[1:] + corners[:1]):
        normal = Vector(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 30.0))
        builder.oriented([a, b, apex], normal, TERRACOTTA)
    builder.oriented(corners, (0, 0, -1), WOOD)
    for x in range(-24, 25, 8):
        builder.oriented([(x - 1.2, -half_y - 0.02, 0.0), (x + 1.2, -half_y - 0.02, 0.0),
                          (x + 1.2, -half_y - 0.02, 4.0), (x - 1.2, -half_y - 0.02, 4.0)], (0, -1, 0), "shadow_void")
    scene.unique("pente_sud", builder, placement(*ODEON, z))
    return {"centre": [*ODEON, z], "apex": [ODEON[0], ODEON[1], z + apex[2]]}


def build_south_slope(scene):
    return {"theatre": theatre(scene), "odeon": odeon(scene)}


def hephaisteion(scene):
    z = ground(scene, HEPHAISTEION)
    temple = greek.temple(HEPHAISTEION_SPEC, True, "medium", "hephaisteion")
    matrix = frame(HEPHAISTEION, z, 90.0)
    greek.place_building(temple, scene.library, scene.collection, scene.tiles, scene.root("agora"), matrix)
    builder = MeshBuilder()
    half_x = 13.71 / 2
    half_y = 31.78 / 2
    eave = temple.info["eave"]
    for side in (-1, 1):
        scaffold(builder, -half_y + 1.0, half_y - 1.0, eave + 1.0, (2.0, 4.0, eave - 0.6), 0.2,
                 random.Random(7 + side),
                 Matrix.Translation((side * (half_x + 1.6), 0.0, 0.0)) @ Matrix.Rotation(-side * math.pi / 2, 4, "Z"))
    builder.box((-0.12, half_y + 3.4, -0.5), (0.12, half_y + 3.64, eave + 5.0), WOOD, bottom=False)
    scene.unique("agora", builder, matrix)
    return {"centre": [*HEPHAISTEION, z], "top": [HEPHAISTEION[0], HEPHAISTEION[1], z + eave]}


def build_agora(scene):
    info = {"hephaisteion": hephaisteion(scene)}
    for name, point, azimuth, length, depth, height, diameter in (
            ("stoa_poikile", POIKILE, 180.0, 36.0, 12.5, 5.0, 0.82), ("stoa_royale", ROYAL_STOA, 90.0, 18.0, 7.5,
                                                                      4.2, 0.62)):
        z = ground(scene, point)
        stoa = greek.stoa(length=length, depth=depth, column_height=height, diameter=diameter, roof=TERRACOTTA,
                          polychromy=True, detail="medium", name=name, inner_columns=name == "stoa_poikile")
        greek.place_building(stoa, scene.library, scene.collection, scene.tiles, scene.root("agora"),
                             frame(point, z, azimuth))
        info[name] = [*point, z]
    builder = MeshBuilder()
    hip_house(builder, -11.5, 11.5, -11.5, 11.5, 7.5, POROS, TERRACOTTA, 0.3, -1.5, door=(1, 0.0, 2.2, 3.6))
    scene.unique("agora", builder, frame(BOULEUTERION, ground(scene, BOULEUTERION), 90.0))
    tholos = MeshBuilder()
    tholos.lathe([(9.15, -1.5), (9.15, 5.6)], 28, POROS, smooth=True, caps=False)
    tholos.lathe([(9.8, 5.5), (0.0, 9.0)], 28, TERRACOTTA, smooth=False, caps=False)
    tholos.lathe([(0.0, 5.45), (9.8, 5.45)], 28, WOOD, smooth=False, caps=False)
    tholos.oriented([(-1.1, 9.17, 0.0), (1.1, 9.17, 0.0), (1.1, 9.17, 3.2), (-1.1, 9.17, 3.2)], (0, 1, 0),
                    "shadow_void")
    scene.unique("agora", tholos, frame(THOLOS, ground(scene, THOLOS), 70.0))
    fountain = MeshBuilder()
    hip_house(fountain, -9.0, 9.0, -3.5, 3.5, 5.0, POROS, TERRACOTTA, 0.3, -1.5)
    for x in (-4.0, 0.0, 4.0):
        fountain.oriented([(x - 1.0, 3.52, 0.0), (x + 1.0, 3.52, 0.0), (x + 1.0, 3.52, 2.8), (x - 1.0, 3.52, 2.8)],
                          (0, 1, 0), "shadow_void")
    scene.unique("agora", fountain, frame(FOUNTAIN, ground(scene, FOUNTAIN), 0.0))
    gods = MeshBuilder()
    enclosure(gods, 4.75, 4.75, 1.0, MARBLE, 1.6, 0.35)
    gods.merge(altar_builder(1.6, 1.2, 0.9), Matrix.Identity(4))
    scene.unique("agora", gods, frame(TWELVE_GODS, ground(scene, TWELVE_GODS), 0.0))
    group = MeshBuilder()
    group.box((-1.5, -0.8, -0.5), (1.5, 0.8, 1.6), MARBLE, bottom=False)
    for side, lean in ((-1, 0.15), (1, -0.1)):
        group.merge(monochrome(statues.athena("promachos"), "bronze_statue",
                               Matrix.Translation((side * 0.6, 0.0, 1.6)) @ Matrix.Rotation(lean, 4, "Z")
                               @ Matrix.Scale(1.05, 4)))
    scene.unique("agora", group, frame(TYRANNICIDES, ground(scene, TYRANNICIDES), 200.0))
    eleusinion = MeshBuilder()
    enclosure(eleusinion, 15.0, 19.0, 2.4, LIMESTONE, 3.0, 0.6)
    hip_house(eleusinion, -4.5, 4.5, -2.0, 13.0, 6.0, MARBLE, TERRACOTTA, 0.3, -1.5, door=(-1, 0.0, 1.8, 3.2))
    scene.unique("agora", eleusinion, frame(ELEUSINION, ground(scene, ELEUSINION), 160.0))
    rng = random.Random(61)
    trees = []
    for k in range(18):
        x = rng.uniform(-385.0, -255.0)
        y = rng.choice((rng.uniform(345.0, 365.0), rng.uniform(505.0, 520.0), rng.uniform(345.0, 520.0)))
        if segment_distance((x, y), (-400.0, 560.0), (-245.0, 340.0)) < 12.0:
            continue
        trees.append(placement(x, y, scene.ground(x, y) - 0.2, rng.uniform(0, 6.28), rng.uniform(0.85, 1.1)))
    scene.instances("agora", "platane", lambda: plane_tree(15.0, 3), trees)
    info["platanes"] = len(trees)
    info["pnyx"] = pnyx(scene)
    info["olympieion"] = olympieion(scene)
    return info


def pnyx(scene):
    builder = MeshBuilder()
    bema = MeshBuilder()
    bema.box((-2.0, -1.5, -1.0), (2.0, 1.5, 1.2), LIMESTONE, bottom=False)
    bema.box((-2.6, -2.4, -1.0), (2.6, -1.5, 0.45), LIMESTONE, bottom=False)
    builder.merge(bema, frame(BEMA, ground(scene, BEMA), 225.0))
    arc = [(x, y, scene.ground(x, y)) for x, y in ((-676.0, -16.0), (-660.0, -14.0), (-644.0, -10.0), (-630.0, -3.0))]
    rng = random.Random(77)
    cyclopean(builder, arc, 0.7, 1.2, rng, LIMESTONE, 0.6)
    gnomon = MeshBuilder()
    gnomon.box((-1.3, -1.3, -0.3), (1.3, 1.3, 0.3), MARBLE, bottom=False)
    for k in range(9):
        first = len(gnomon.polygons)
        gnomon.box((-1.1 + k * 0.27, -1.2, 0.3), (-1.08 + k * 0.27, 1.2, 0.31), PAINT)
        gnomon.tint(first, (0.15, 0.12, 0.1))
    gnomon.box((-0.07, -0.07, 0.3), (0.07, 0.07, 2.1), BRONZE_DARK, bottom=False)
    z = ground(scene, HELIOTROPION)
    builder.merge(gnomon, frame(HELIOTROPION, z, 0.0))
    scene.unique("agora", builder)
    return {"bema": [*BEMA, ground(scene, BEMA)], "heliotropion": [*HELIOTROPION, z]}


def olympieion(scene):
    z = ground(scene, OLYMPIEION)
    builder = MeshBuilder()
    builder.box((-20.5, -54.0, -2.0), (20.5, 54.0, 1.2), POROS, bottom=False)
    rng = random.Random(83)
    for k in range(18):
        u = rng.uniform(-24.0, 24.0)
        v = rng.uniform(-60.0, 60.0)
        if abs(u) < 20.0 and abs(v) < 53.0:
            builder.lathe([(0.0, 1.2), (1.2, 1.2), (1.2, 2.5), (0.0, 2.5)], 12, POROS, smooth=False,
                          matrix=Matrix.Translation((u, v, 0.0)))
        else:
            builder.lathe([(0.0, -0.7), (1.2, -0.7), (1.2, 0.7), (0.0, 0.7)], 12, POROS, smooth=False,
                          matrix=Matrix.Translation((u, v, 1.1)) @ Matrix.Rotation(math.pi / 2, 4, "X"))
    scene.unique("agora", builder, frame(OLYMPIEION, z, 90.0))
    return {"centre": [*OLYMPIEION, z]}


def walkable(scene):
    names = ("propylees_body",)
    objects = [bpy.data.objects[name] for name in names if name in bpy.data.objects]
    if "propylees_rampe" in scene.statics:
        objects.append(scene.statics["propylees_rampe"])
    return objects
