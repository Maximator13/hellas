import math
import random

from mathutils import Matrix, Vector

from . import figures as people
from . import greek
from . import olympie_plan as plan
from . import olympie_zeus as zeus
from .acropole_monuments import hip_house
from .acropole_statues import ellipsoid, tube, winged_victory
from .geometry import MeshBuilder
from .greek_materials import DORIC_FLUTED, MARBLE, PAINT, POROS, TERRACOTTA

LIMESTONE = "limestone"
PLASTER = "plaster"
WOOD = "dark_wood"
GILT = "bronze_gilt"
BRONZE = "bronze_statue"
ASH = "ash"
OIL = "dallage_huile"
MUDBRICK = "mudbrick"

ZEUS_SPEC = {
    "status": "420 BC state, approximate dimensions from docs/scenes/olympie.md",
    "stylobate": (27.68, 64.12), "columns": (6, 13), "steps": 3, "step_rise": 0.5, "step_tread": 0.6,
    "column_height": 10.43, "diameter": 2.21, "corner_diameter": 2.25, "top_ratio": 0.78, "spacing": 5.22,
    "corner_spacing": 4.8, "flank_spacing": None, "slope_degrees": 14.0, "roof": MARBLE, "tile_pitch": 0.7,
    "sekos": {"width": 16.39, "wall": 1.0, "front_porch": 8.0, "back_porch": 8.0, "naos": 28.74, "back_room": 0.0,
              "raised": 0.25, "raised_steps": 1, "porch_columns": 4, "porch_diameter": 1.9, "architrave": 1.5,
              "frieze": 1.55, "door": (5.0, 9.6), "back_door": (4.2, 8.0)},
    "inner_colonnade": None, "back_room_columns": None, "metope_reliefs": False, "pediment_figures": True,
    "acroteria": False, "antefixes": True,
}

HERAION_SPEC = {
    "status": "420 BC state, approximate dimensions from docs/scenes/olympie.md",
    "stylobate": (18.75, 50.01), "columns": (6, 16), "steps": 2, "step_rise": 0.3, "step_tread": 0.45,
    "column_height": 5.22, "diameter": 1.25, "corner_diameter": 1.3, "top_ratio": 0.74, "spacing": 3.56,
    "corner_spacing": 3.26, "flank_spacing": None, "slope_degrees": 13.0, "roof": TERRACOTTA, "tile_pitch": 0.6,
    "sekos": {"width": 10.7, "wall": 1.0, "front_porch": 4.2, "back_porch": 3.6, "naos": 26.0, "back_room": 0.0,
              "raised": 0.2, "raised_steps": 1, "porch_columns": 4, "porch_diameter": 1.0, "architrave": 0.8,
              "frieze": 0.75, "door": (3.0, 5.4), "back_door": (2.4, 4.4)},
    "inner_colonnade": None, "back_room_columns": None, "metope_reliefs": False, "pediment_figures": False,
    "acroteria": False, "antefixes": True,
}

TEMPLE_LIFT = 1.4
STATUE_FROM_DOOR = 17.0
POOL = (6.4, 7.0)


def recoloured(builder, swaps, tint=None):
    copy = MeshBuilder()
    copy.points(builder.positions)
    copy.heights = list(builder.heights)
    for indices, material, smooth, uvs, colour in zip(builder.polygons, builder.polygon_materials,
                                                      builder.polygon_smooth, builder.polygon_uvs,
                                                      builder.polygon_colors):
        name = builder.materials[material]
        target = swaps.get(name, name)
        if target != name and tint is not None:
            colour = tint if colour is None else tuple(a * b for a, b in zip(colour, tint))
        copy.face(list(indices), target, smooth, uvs, colour, raw=True)
    return copy


def place(scene, group, building, matrix):
    return greek.place_building(building, scene.library, scene.collection, scene.tiles, scene.root(group), matrix)


def column_pair(builder, x0, x1, y, z0, height, diameter, material=MARBLE):
    for x in (x0, x1):
        builder.merge(greek.doric_column(diameter, height, "low", 0.78, material=material),
                      Matrix.Translation((x, y, z0)))


def cella_colonnade(scene, temple, matrix, floor, ceiling):
    sekos = temple.info["sekos"]
    inner = ZEUS_SPEC["sekos"]["width"] / 2 - ZEUS_SPEC["sekos"]["wall"]
    x = inner - 2.6
    y0, y1 = sekos["naos"][0] + 2.0, sekos["naos"][1] - 3.2
    ys = [y0 + (y1 - y0) * k / 6 for k in range(7)]
    height = ceiling - floor
    lower = 0.52 * height
    beam = 0.85
    upper = height - lower - beam - 0.7
    building = greek.Building("cella")
    building.add_columns(greek.doric_template(1.25, lower, "medium"), greek.placements([(s * x, y) for s in (-1, 1)
                                                                                         for y in ys], floor))
    building.add_columns(greek.doric_template(0.92, upper, "medium"),
                         greek.placements([(s * x, y) for s in (-1, 1) for y in ys], floor + lower + beam))
    b = building.body
    for side in (-1, 1):
        greek.beam(b, (side * x, y0 - 0.8), (side * x, y1 + 0.8), 1.3, floor + lower, floor + lower + beam)
        greek.beam(b, (side * x, y0 - 0.8), (side * x, y1 + 0.8), 0.98, ceiling - 0.7, ceiling)
        lo, hi = sorted((side * (x + 0.6), side * inner))
        b.box((lo, sekos["naos"][0], floor + lower + beam - 0.28), (hi, sekos["naos"][1], floor + lower + beam), WOOD)
        b.box((side * x - 0.04, y0 - 0.8, floor + lower + beam), (side * x + 0.04, y1 + 0.8, floor + lower + beam + 1.0),
              WOOD, bottom=False)
    place(scene, "temple_zeus", building, matrix)
    return {"columns_x": x, "rows": [round(y, 2) for y in ys]}


def nike_acroterion(builder, at, height):
    winged_victory(builder, at, height, GILT)


def cauldron(builder, at, radius):
    x, y, z = at
    builder.lathe([(0.0, 0.0), (radius * 0.55, 0.05 * radius), (radius, 0.6 * radius), (radius * 0.92, 1.0 * radius),
                   (0.0, 1.0 * radius)], 14, GILT, smooth=True, matrix=Matrix.Translation((x, y, z + 0.5 * radius)))
    for k in range(3):
        a = 2 * math.pi * k / 3
        tube(builder, [(x + 0.5 * radius * math.cos(a), y + 0.5 * radius * math.sin(a), z + 0.6 * radius),
                       (x + 0.8 * radius * math.cos(a), y + 0.8 * radius * math.sin(a), z)], [0.06 * radius] * 2, GILT, 5)


def temple_of_zeus(scene):
    temple = greek.temple(ZEUS_SPEC, True, "high", "temple_zeus_body")
    base = scene.ground(*plan.TEMPLE)
    z = base + TEMPLE_LIFT
    matrix = plan.frame(plan.TEMPLE[0], plan.TEMPLE[1], z, plan.TEMPLE_AZIMUTH)
    width, length = ZEUS_SPEC["stylobate"]
    margin = ZEUS_SPEC["steps"] * ZEUS_SPEC["step_tread"] + 0.15
    terrace = MeshBuilder()
    terrace.box((-width / 2 - margin - 0.4, -length / 2 - margin - 0.4, -TEMPLE_LIFT - 1.5),
                (width / 2 + margin + 0.4, length / 2 + margin + 0.4, 0.0), POROS, bottom=False)
    ramp = MeshBuilder()
    ramp.prism([(length / 2 + margin + 0.4, 0.0), (length / 2 + margin + 0.4 + 14.0, -TEMPLE_LIFT - 0.3),
                (length / 2 + margin + 0.4, -TEMPLE_LIFT - 0.3)], -3.2, 3.2, POROS)
    terrace.merge(ramp, Matrix(((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1))))
    terrace.tint(0, (0.96, 0.93, 0.86))
    scene.unique("temple_zeus", terrace, matrix)
    place(scene, "temple_zeus", temple, matrix)
    info = temple.info
    sekos = info["sekos"]
    spec = ZEUS_SPEC["sekos"]
    floor = info["stylobate_top"] + spec["raised"]
    ceiling = info["ceiling"]
    naos_front = sekos["naos"][1]
    base_depth = zeus.BASE[1]
    statue_y = naos_front - STATUE_FROM_DOOR - base_depth / 2
    interior = MeshBuilder()
    interior.merge(zeus.statue(), Matrix.Translation((0.0, statue_y, floor)))
    pool_w, pool_l = POOL
    pool_y0 = statue_y + base_depth / 2 + 0.15
    pool_y1 = pool_y0 + pool_l
    half = pool_w / 2
    for x0, x1, y0, y1 in ((-half - 0.35, half + 0.35, pool_y1, pool_y1 + 0.35), (-half - 0.35, -half, pool_y0, pool_y1),
                           (half, half + 0.35, pool_y0, pool_y1)):
        interior.box((x0, y0, floor - 0.05), (x1, y1, floor + 0.16), MARBLE, bottom=False)
    interior.polygon([(-half, pool_y0, floor + 0.08), (half, pool_y0, floor + 0.08), (half, pool_y1, floor + 0.08),
                      (-half, pool_y1, floor + 0.08)], OIL)
    inner = spec["width"] / 2 - spec["wall"]
    first = len(interior.polygons)
    interior.oriented([(-inner, sekos["naos"][0], ceiling - 0.02), (inner, sekos["naos"][0], ceiling - 0.02),
                       (inner, sekos["naos"][1], ceiling - 0.02), (-inner, sekos["naos"][1], ceiling - 0.02)],
                      (0, 0, -1), PAINT)
    interior.tint(first, (0.10, 0.15, 0.34))
    first = len(interior.polygons)
    for k in range(int(2 * inner / 2.0) + 1):
        xk = -inner + k * 2.0
        interior.box((xk - 0.15, sekos["naos"][0], ceiling - 0.45), (xk + 0.15, sekos["naos"][1], ceiling - 0.02), PAINT,
                     top=False)
    interior.tint(first, (0.40, 0.14, 0.08))
    first = len(interior.polygons)
    interior.box((-inner, sekos["naos"][0], floor - 0.02), (inner, pool_y0 - 0.1, floor + 0.02), LIMESTONE, bottom=False)
    interior.tint(first, (0.62, 0.58, 0.52))
    door_y = sekos["front_wall"]
    door_w, door_h = spec["door"]
    for side in (-1, 1):
        leaf = MeshBuilder()
        leaf.box((0.0, -0.08, 0.0), (door_w / 2, 0.08, door_h), "bronze", bottom=False)
        for k in range(5):
            leaf.box((0.15, 0.08, 0.6 + k * 1.8), (door_w / 2 - 0.15, 0.12, 0.7 + k * 1.8), GILT, bottom=False)
        hinge = Matrix.Translation((side * door_w / 2, door_y - 0.1, floor)) @ Matrix.Rotation(
            math.pi if side > 0 else 0.0, 4, "Z") @ Matrix.Rotation(side * math.radians(80.0), 4, "Z")
        interior.merge(leaf, hinge)
    iphitos = MeshBuilder()
    iphitos.box((-0.6, -0.6, 0.0), (0.6, 0.6, 1.3), MARBLE, bottom=False)
    iphitos.merge(zeus.mono(people.man_himation(), BRONZE), Matrix.Translation((-0.25, 0.0, 1.3)) @ Matrix.Scale(1.15, 4))
    iphitos.merge(zeus.mono(people.woman_peplos(), BRONZE), Matrix.Translation((0.35, 0.0, 1.3)) @ Matrix.Scale(1.15, 4))
    interior.merge(iphitos, Matrix.Translation((inner - 1.6, naos_front + 2.4, floor)) @ Matrix.Rotation(math.pi / 2, 4, "Z"))
    hydria = MeshBuilder()
    hydria.lathe([(0.0, 0.0), (0.22, 0.02), (0.34, 0.35), (0.3, 0.6), (0.14, 0.72), (0.12, 0.85), (0.0, 0.86)], 14,
                 "bronze", smooth=True)
    interior.merge(hydria, Matrix.Translation((half + 1.2, pool_y1 - 1.0, floor)))
    scene.unique("zeus", interior, matrix)
    scene.zeus_frame = matrix
    roof = MeshBuilder()
    xs = info["front_axes"]
    ys = info["flank_axes"]
    ridge = info["ridge"]
    eave = info["eave"]
    for end in (-1, 1):
        y = end * (ys[-1] + 2.2)
        nike_acroterion(roof, (0.0, y, ridge + 0.1), 2.6)
        for side in (-1, 1):
            cauldron(roof, (side * (xs[-1] + 0.6), y, eave + 0.2), 0.9)
    shield = MeshBuilder()
    shield.lathe([(0.0, 0.08), (0.7, 0.05), (0.95, 0.0), (0.0, 0.0)], 20, GILT, smooth=True)
    ellipsoid(shield, (0.0, 0.0, 0.1), (0.2, 0.2, 0.08), GILT, 10, 4)
    roof.merge(shield, Matrix.Translation((0.0, ys[-1] + 2.1, ridge - 1.4)) @ Matrix.Rotation(-math.pi / 2, 4, "X"))
    scene.unique("temple_zeus", roof, matrix)
    world = lambda local: matrix @ Vector(local)
    colonnade = cella_colonnade(scene, temple, matrix, floor, ceiling)
    face = zeus.face_height()
    return {"info": {k: v for k, v in info.items() if k != "sekos"}, "colonnade": colonnade,
            "floor": round(z + floor, 3), "ceiling": round(z + ceiling, 3),
            "statue_top": round(z + floor + zeus.statue_height(), 3),
            "door_centre": list(world((0.0, sekos["front_wall"] + spec["wall"] / 2, floor + door_h / 2))),
            "statue": list(world((0.0, statue_y, floor))),
            "statue_face": list(world((0.0, statue_y + zeus.face_offset(), floor + face))),
            "pool_centre": list(world((0.0, (pool_y0 + pool_y1) / 2, floor + 0.1))),
            "pool_front": list(world((0.0, pool_y1 + 0.6, floor))),
            "naos": [list(world((0.0, sekos["naos"][0], floor))), list(world((0.0, sekos["naos"][1], floor)))],
            "east_front": list(world((0.0, ys[-1], info["stylobate_top"]))),
            "pediment": list(world((0.0, ys[-1], eave + 2.6)))}


def heraion(scene):
    temple = greek.temple(HERAION_SPEC, True, "low", "heraion_body")
    swaps = {MARBLE: POROS}
    temple.body = recoloured(temple.body, swaps, (0.9, 0.88, 0.84))
    columns = {}
    for key, (build, matrices) in temple.columns.items():
        columns[f"{key}_poros"] = (lambda build=build: recoloured(build(), {MARBLE: POROS, DORIC_FLUTED: POROS},
                                                                   (0.9, 0.88, 0.84)), matrices)
    temple.columns = columns
    base = scene.ground(*plan.HERAION)
    matrix = plan.frame(plan.HERAION[0], plan.HERAION[1], base + 0.3, 90.0)
    place(scene, "altis", temple, matrix)
    info = temple.info
    disc = MeshBuilder()
    for end in (-1, 1):
        y = end * (info["flank_axes"][-1] + 1.6)
        frame = Matrix.Translation((0.0, y, info["ridge"] + 1.1)) @ Matrix.Rotation(math.pi / 2, 4, "X")
        first = len(disc.polygons)
        disc.lathe([(0.0, 0.12), (1.15, 0.12), (1.15, -0.12), (0.0, -0.12)], 24, PAINT, matrix=frame)
        disc.tint(first, (0.72, 0.36, 0.22))
        first = len(disc.polygons)
        disc.lathe([(0.0, 0.14), (0.75, 0.14), (0.75, 0.13), (0.0, 0.13)], 20, PAINT, matrix=frame)
        disc.tint(first, (0.16, 0.12, 0.10))
    scene.unique("altis", disc, matrix)
    return {"top": [plan.HERAION[0], plan.HERAION[1], base + info["ridge"]]}


def pelopion(scene):
    builder = MeshBuilder()
    radius = 16.0
    corners = [(radius * math.sin(math.radians(a)), radius * math.cos(math.radians(a))) for a in
               (0.0, 72.0, 144.0, 216.0, 288.0)]
    gx, gy = radius * 0.8 * math.sin(math.radians(270.0)), radius * 0.8 * math.cos(math.radians(270.0))
    base = scene.ground(*plan.PELOPION)
    for (x0, y0), (x1, y1) in zip(corners, corners[1:] + corners[:1]):
        length = math.hypot(x1 - x0, y1 - y0)
        count = max(int(length / 2.0), 1)
        for k in range(count):
            t0, t1 = k / count, (k + 1) / count
            ax, ay = x0 + (x1 - x0) * t0, y0 + (y1 - y0) * t0
            bx, by = x0 + (x1 - x0) * t1, y0 + (y1 - y0) * t1
            if math.hypot((ax + bx) / 2 - gx, (ay + by) / 2 - gy) < 2.5:
                continue
            path = [(ax, ay, 0.0), (bx, by, 0.0)]
            builder.sweep(path, [(-0.3, -0.6), (-0.3, 1.25), (0.3, 1.25), (0.3, -0.6)], POROS, caps=True)
    builder.tint(0, (0.92, 0.88, 0.8))
    first = len(builder.polygons)
    builder.lathe([(0.0, 1.6), (6.0, 1.3), (11.0, 0.5), (13.0, 0.0), (13.0, -0.6)], 20, "matte", smooth=True)
    builder.tint(first, (0.55, 0.52, 0.36))
    builder.merge(altar(1.6, 1.2, 1.0), Matrix.Translation((-6.0, -2.0, 0.6)))
    scene.unique("altis", builder, Matrix.Translation((plan.PELOPION[0], plan.PELOPION[1], base)))
    return {"centre": [plan.PELOPION[0], plan.PELOPION[1], base]}


def altar(width, depth, height, material=LIMESTONE):
    builder = MeshBuilder()
    builder.box((-width / 2, -depth / 2, -0.6), (width / 2, depth / 2, height), material, bottom=False)
    builder.box((-width / 2 - 0.1, -depth / 2 - 0.1, height - 0.15), (width / 2 + 0.1, depth / 2 + 0.1, height),
                material, bottom=False)
    return builder


def great_altar(scene):
    base = scene.ground(*plan.ALTAR)
    builder = MeshBuilder()
    builder.lathe([(0.0, 1.3), (6.4, 1.3), (6.4, -0.8)], 28, LIMESTONE, smooth=False)
    for k in range(3):
        first = len(builder.polygons)
        builder.box((-1.6, 6.3 + k * 0.45, -0.6), (1.6, 6.8 + k * 0.45, 1.3 - (k + 1) * 0.43), LIMESTONE, bottom=False)
        builder.tint(first, (0.95, 0.93, 0.88))
    first = len(builder.polygons)
    builder.lathe([(4.6, 1.3), (3.3, 2.8), (2.2, 4.3), (1.65, 5.5), (0.0, 5.65)], 24, ASH, smooth=True)
    builder.tint(first, (0.9, 0.88, 0.86))
    for k in range(6):
        a = math.radians(-20.0 + k * 8.0)
        r = 4.4 - k * 0.43
        builder.centered_box((r * math.sin(a), r * math.cos(a), 1.5 + k * 0.7), (0.9, 0.5, 0.25), ASH)
    builder.lathe([(1.3, 5.55), (1.1, 5.95), (0.0, 6.05)], 10, "flame", smooth=True)
    scene.unique("altis", builder, Matrix.Translation((plan.ALTAR[0], plan.ALTAR[1], base)) @ Matrix.Rotation(
        math.radians(-135.0), 4, "Z"))
    return {"top": [plan.ALTAR[0], plan.ALTAR[1], base + 6.0], "base": base}


def treasury(width, depth, height, seed):
    rng = random.Random(seed)
    builder = MeshBuilder()
    builder.box((-width / 2 - 0.5, -depth / 2 - 0.5, -1.0), (width / 2 + 0.5, depth / 2 + 0.5, 0.35), POROS,
                bottom=False)
    wall = 0.6
    porch = 2.6
    builder.box((-width / 2, -depth / 2, 0.35), (width / 2, depth / 2 - porch, height), POROS, bottom=False, top=False)
    for side in (-1, 1):
        builder.box((min(side * width / 2, side * (width / 2 - wall)), depth / 2 - porch, 0.35),
                    (max(side * width / 2, side * (width / 2 - wall)), depth / 2 - 0.3, height), POROS, bottom=False,
                    top=False)
    builder.box((-width / 2 + 0.2, depth / 2 - porch - 0.02, 0.35), (width / 2 - 0.2, depth / 2 - porch, 0.35 + 3.0),
                "shadow_void", bottom=False, top=False)
    d = width / 7.0
    column_pair(builder, -width / 6, width / 6, depth / 2 - 0.7, 0.35, height - 0.35, d, POROS)
    first = len(builder.polygons)
    builder.box((-width / 2 - 0.1, -depth / 2 - 0.1, height), (width / 2 + 0.1, depth / 2 + 0.1, height + 0.55), POROS)
    builder.tint(first, (0.95, 0.9, 0.82))
    first = len(builder.polygons)
    builder.box((-width / 2 - 0.12, -depth / 2 - 0.12, height + 0.55), (width / 2 + 0.12, depth / 2 + 0.12,
                                                                          height + 1.15), PAINT)
    builder.tint(first, greek.PALETTE["triglyph"] if rng.random() < 0.5 else (0.62, 0.22, 0.14))
    pitch = 0.27
    rise = (width / 2 + 0.3) * pitch
    roof_z = height + 1.15
    greek.facade_prism(builder, [(-width / 2 - 0.3, roof_z), (width / 2 + 0.3, roof_z), (0.0, roof_z + rise)],
                       -depth / 2 - 0.3, depth / 2 + 0.3, TERRACOTTA, back=True)
    for end in (-1, 1):
        first = len(builder.polygons)
        y = end * (depth / 2 + 0.31)
        tri = [(-width / 2 - 0.1, y, roof_z + 0.05), (width / 2 + 0.1, y, roof_z + 0.05), (0.0, y, roof_z + rise - 0.1)]
        builder.polygon(tri if end > 0 else list(reversed(tri)), PAINT)
        builder.tint(first, (0.18, 0.30, 0.56) if end > 0 else (0.6, 0.24, 0.16))
    return builder


def treasuries(scene):
    azimuth = plan.treasury_azimuth()
    sites = plan.treasury_sites()
    level = scene.ground.levels["terrace"]
    sizes = ((12.0, 7.0, 5.2), (10.8, 12.5, 5.6), (6.6, 9.0, 4.6), (7.0, 8.0, 4.6), (6.5, 10.0, 4.8), (7.0, 9.0, 4.7),
             (8.0, 11.0, 5.0), (6.6, 10.0, 4.6), (6.4, 13.0, 5.0), (8.0, 10.0, 5.0), (13.0, 11.0, 6.2))
    builder = MeshBuilder()
    for k, ((x, y), (w, d, h)) in enumerate(zip(sites, sizes)):
        local = plan.frame(x, y, level, azimuth)
        offset = Matrix.Translation((0.0, -d / 2 + 4.0, 0.0))
        builder.merge(treasury(w, d, h, k), local @ offset)
    (x0, y0), (x1, y1) = plan.TREASURY_LINE
    length = math.hypot(x1 - x0, y1 - y0)
    mid = ((x0 + x1) / 2, (y0 + y1) / 2)
    wall = MeshBuilder()
    first = len(wall.polygons)
    wall.box((-length / 2 - 12.0, 4.0, -5.0), (length / 2 + 12.0, 5.2, 0.3), POROS, bottom=False)
    wall.tint(first, (0.9, 0.85, 0.76))
    for k in range(4):
        wall.box((-6.0 + k * 3.0 - 1.4, 5.2 + k * 0.5, -5.0), (-6.0 + k * 3.0 + 1.4, 5.7 + k * 0.5, -0.8 * k), POROS)
    builder.merge(wall, plan.frame(mid[0], mid[1], level, azimuth))
    scene.unique("altis", builder)
    return {"count": len(sites), "level": round(level, 2)}


def prytaneion(scene):
    builder = MeshBuilder()
    hip_house(builder, -10.0, 10.0, -10.0, 10.0, 5.2, POROS, TERRACOTTA, 0.3, -1.2, (0.96, 0.92, 0.84),
              door=(-1, 0.0, 2.2, 3.0))
    base = scene.ground(*plan.PRYTANEION)
    scene.unique("altis", builder, Matrix.Translation((plan.PRYTANEION[0], plan.PRYTANEION[1], base)))
    return {"base": base}


def apsidal_hall(builder, x0, x1, half, height):
    builder.box((x0, -half, -1.0), (x1, half, height), POROS, bottom=False, top=False)
    builder.lathe([(half, -1.0), (half, height)], 12, POROS, smooth=False, caps=False,
                  matrix=Matrix.Translation((x0, 0.0, 0.0)), start=math.pi / 2, sweep=math.pi)
    rise = half * 0.35
    greek.facade_prism(builder, [(-half - 0.4, height), (half + 0.4, height), (0.0, height + rise)], x0, x1 + 0.4,
                       TERRACOTTA, Matrix.Rotation(-math.pi / 2, 4, "Z"), back=True)
    builder.lathe([(half + 0.4, height), (0.0, height + rise)], 12, TERRACOTTA, smooth=False, caps=False,
                  matrix=Matrix.Translation((x0, 0.0, 0.0)), start=math.pi / 2, sweep=math.pi)


def bouleuterion(scene):
    builder = MeshBuilder()
    for offset in (-15.0, 15.0):
        hall = MeshBuilder()
        apsidal_hall(hall, -15.0, 15.0, 6.8, 6.0)
        builder.merge(hall, Matrix.Translation((0.0, offset, 0.0)))
    hip_house(builder, -6.0, 6.0, -6.5, 6.5, 5.0, POROS, TERRACOTTA, 0.3, -1.0, (0.96, 0.92, 0.84))
    base = scene.ground(*plan.BOULEUTERION)
    scene.unique("altis", builder, Matrix.Translation((plan.BOULEUTERION[0], plan.BOULEUTERION[1], base)))
    statue = MeshBuilder()
    statue.box((-0.8, -0.8, 0.0), (0.8, 0.8, 1.4), MARBLE, bottom=False)
    statue.merge(zeus.mono(people.man_himation(right_hand=(0.3, 0.3, 1.32)), BRONZE),
                 Matrix.Translation((0.0, 0.0, 1.4)) @ Matrix.Scale(1.5, 4))
    scene.unique("altis", statue, Matrix.Translation((plan.BOULEUTERION[0] + 22.0, plan.BOULEUTERION[1], base)))
    return {"base": base}


def workshop(scene):
    builder = MeshBuilder()
    w, d, h = 17.0, 34.0, 14.5
    builder.box((-w / 2 - 0.6, -d / 2 - 0.6, -1.0), (w / 2 + 0.6, d / 2 + 0.6, 0.3), POROS, bottom=False)
    first = len(builder.polygons)
    builder.box((-w / 2, -d / 2, 0.3), (w / 2, d / 2, 1.6), POROS, bottom=False, top=False)
    builder.tint(first, (0.95, 0.9, 0.82))
    first = len(builder.polygons)
    builder.box((-w / 2, -d / 2, 1.6), (w / 2, d / 2, h), MUDBRICK, bottom=False, top=False)
    builder.tint(first, (1.0, 0.97, 0.92))
    rise = (w / 2 + 0.5) * 0.3
    greek.facade_prism(builder, [(-w / 2 - 0.5, h), (w / 2 + 0.5, h), (0.0, h + rise)], -d / 2 - 0.5, d / 2 + 0.5,
                       TERRACOTTA, back=True)
    for end in (-1, 1):
        y = end * (d / 2 + 0.01)
        tri = [(-w / 2, y, h), (w / 2, y, h), (0.0, y, h + rise - 0.15)]
        builder.polygon(tri if end > 0 else list(reversed(tri)), MUDBRICK)
    builder.polygon([(-2.0, d / 2 + 0.03, 0.3), (2.0, d / 2 + 0.03, 0.3), (2.0, d / 2 + 0.03, 6.0),
                     (-2.0, d / 2 + 0.03, 6.0)], "shadow_void")
    for k in range(4):
        builder.polygon([(-w / 2 - 0.02, -12.0 + k * 8.0, 9.0), (-w / 2 - 0.02, -12.0 + k * 8.0, 11.0),
                         (-w / 2 - 0.02, -10.6 + k * 8.0, 11.0), (-w / 2 - 0.02, -10.6 + k * 8.0, 9.0)], "shadow_void")
    hip_house(builder, w / 2 + 0.5, w / 2 + 8.5, -12.0, 4.0, 4.0, MUDBRICK, TERRACOTTA, 0.3, -1.0, (0.94, 0.9, 0.84))
    yard = MeshBuilder()
    for x0, y0, x1, y1 in ((w / 2 + 0.5, 4.0, w / 2 + 14.0, 4.6), (w / 2 + 13.4, -16.0, w / 2 + 14.0, 4.0),
                           (w / 2 + 0.5, -16.6, w / 2 + 14.0, -16.0)):
        yard.box((x0, y0, -0.5), (x1, y1, 2.2), MUDBRICK, bottom=False)
    builder.merge(yard)
    stack = MeshBuilder()
    for k in range(6):
        stack.box((-0.6, -0.4, k * 0.12), (0.6, 0.4, k * 0.12 + 0.1), "bronze" if k % 2 else LIMESTONE, bottom=False)
    builder.merge(stack, Matrix.Translation((w / 2 + 6.0, -6.0, 0.0)))
    kiln = MeshBuilder()
    kiln.lathe([(1.3, -0.3), (1.3, 1.0), (0.9, 1.8), (0.35, 2.1), (0.0, 2.1)], 12, MUDBRICK, smooth=True)
    builder.merge(kiln, Matrix.Translation((w / 2 + 10.0, -12.0, 0.0)))
    base = scene.ground(*plan.WORKSHOP)
    matrix = plan.frame(plan.WORKSHOP[0], plan.WORKSHOP[1], base, 90.0)
    scene.unique("atelier", builder, matrix)
    return {"base": base, "kiln": list(matrix @ Vector((w / 2 + 10.0, -12.0, 2.2)))}


def nike(scene):
    builder = MeshBuilder()
    side = 1.6
    triangle = [(side * math.cos(math.radians(a)), side * math.sin(math.radians(a))) for a in (90.0, 210.0, 330.0)]
    builder.prism([(x * 1.4, y * 1.4) for x, y in triangle], -0.5, 1.0, LIMESTONE)
    builder.prism(triangle, 1.0, 8.8, MARBLE, bottom=False)
    first = len(builder.polygons)
    winged_victory(builder, (0.0, 0.3, 8.8), 2.1, MARBLE)
    builder.tint(first, (1.0, 0.98, 0.95))
    for k in range(2):
        first = len(builder.polygons)
        ellipsoid(builder, (0.0, 0.25, 9.3 + k * 0.3), (0.32, 0.26, 0.2), PAINT, 8, 4)
        builder.tint(first, (0.62, 0.30, 0.20) if k == 0 else (0.30, 0.42, 0.62))
    base = scene.ground(*plan.NIKE)
    scene.unique("altis", builder, Matrix.Translation((plan.NIKE[0], plan.NIKE[1], base)) @ Matrix.Rotation(
        math.radians(-110.0), 4, "Z"))
    return {"top": [plan.NIKE[0], plan.NIKE[1], base + 10.9]}


def stadium(scene):
    builder = MeshBuilder()
    level = scene.ground.levels["track"]
    for along in (0.0, 192.0):
        x, y = plan.stadium_point(along + 10.0, 0.0)
        frame = plan.frame(x, y, level, plan.STADIUM_AZIMUTH)
        first = len(builder.polygons)
        builder.box((-plan.STADIUM_WIDTH / 2 + 1.0, -0.25, -0.3), (plan.STADIUM_WIDTH / 2 - 1.0, 0.25, 0.06), LIMESTONE,
                    matrix=frame, bottom=False)
        builder.tint(first, (0.95, 0.92, 0.84))
    jx, jy = plan.stadium_point(130.0, -22.5)
    judges = MeshBuilder()
    judges.box((-5.0, -2.5, -1.0), (5.0, 2.5, 3.0), LIMESTONE, bottom=False)
    judges.box((-5.0, -2.5, 3.0), (5.0, 2.5, 3.15), WOOD)
    for x in (-4.6, 4.6):
        for y in (-2.1, 2.1):
            judges.box((x - 0.1, y - 0.1, 3.15), (x + 0.1, y + 0.1, 5.4), WOOD, bottom=False)
    judges.box((-5.3, -2.8, 5.4), (5.3, 2.8, 5.55), "velum_linen")
    builder.merge(judges, plan.frame(jx, jy, scene.ground(jx, jy), plan.STADIUM_AZIMUTH))
    dx, dy = plan.stadium_point(130.0, 22.0)
    builder.merge(altar(1.8, 1.1, 1.1, MARBLE), plan.frame(dx, dy, scene.ground(dx, dy), plan.STADIUM_AZIMUTH))
    scene.unique("stade", builder)
    return {"level": round(level, 2), "judges": [jx, jy], "demeter": [dx, dy]}


def altis_wall(scene):
    builder = MeshBuilder()
    points = plan.ALTIS + plan.ALTIS[:1]
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        length = math.hypot(x1 - x0, y1 - y0)
        count = max(int(length / 4.0), 1)
        for k in range(count):
            if k % 9 == 4:
                continue
            ax, ay = x0 + (x1 - x0) * k / count, y0 + (y1 - y0) * k / count
            bx, by = x0 + (x1 - x0) * (k + 1) / count, y0 + (y1 - y0) * (k + 1) / count
            builder.sweep([(ax, ay, scene.ground(ax, ay)), (bx, by, scene.ground(bx, by))],
                          [(-0.3, -0.5), (-0.3, 1.0), (0.3, 1.0), (0.3, -0.5)], POROS)
    builder.tint(0, (0.93, 0.89, 0.8))
    scene.unique("altis", builder)


def build(scene):
    info = {"temple": temple_of_zeus(scene), "heraion": heraion(scene), "pelopion": pelopion(scene),
            "altar": great_altar(scene), "tresors": treasuries(scene), "prytanee": prytaneion(scene),
            "bouleuterion": bouleuterion(scene), "atelier": workshop(scene), "nike": nike(scene),
            "stade": stadium(scene)}
    altis_wall(scene)
    return info


def walkable_groups():
    return ("temple_zeus", "altis", "stade", "atelier")
