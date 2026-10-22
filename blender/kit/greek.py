import math
import random

from mathutils import Matrix, Vector

from . import figures as people
from .geometry import UP, MeshBuilder, new_empty, unique_object
from .greek_materials import DORIC_FLUTED, IONIC_FLUTED, MARBLE, PAINT, POROS, TERRACOTTA
from .orders import fluting, ridge_cap, tile_roof

TAU = 2 * math.pi
WOOD = "dark_wood"
SEGMENTS = {"high": 20, "medium": 16, "low": 10}
RINGS = {"high": 8, "medium": 5, "low": 3}
DORIC_CAPITAL = 0.41
IONIC_BASE = 0.36
IONIC_CAPITAL = 0.35
ROOF_TINT = (0.9, 0.88, 0.84)
SWAP_YZ = Matrix(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)))
UVW_TO_YZX = Matrix(((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1)))

PALETTE = {
    "triglyph": (0.08, 0.11, 0.22),
    "mutule": (0.14, 0.25, 0.50),
    "regula": (0.68, 0.16, 0.10),
    "taenia": (0.68, 0.16, 0.10),
    "metope": (0.20, 0.36, 0.64),
    "tympanum": (0.20, 0.36, 0.64),
    "frieze": (0.20, 0.36, 0.64),
    "coffer": (0.26, 0.41, 0.70),
    "blue": (0.17, 0.31, 0.60),
    "red": (0.68, 0.16, 0.10),
}

PARTHENON = {
    "status": "approximate measurements, to be checked and overridden by the scene script",
    "stylobate": (30.88, 69.50),
    "columns": (8, 17),
    "steps": 3,
    "step_rise": 0.55,
    "step_tread": 0.70,
    "column_height": 10.43,
    "diameter": 1.905,
    "corner_diameter": 1.948,
    "top_ratio": 0.78,
    "spacing": 4.296,
    "corner_spacing": 3.681,
    "flank_spacing": None,
    "slope_degrees": 13.5,
    "roof": MARBLE,
    "tile_pitch": 0.66,
    "sekos": {
        "width": 21.72, "wall": 1.15, "front_porch": 4.4, "back_porch": 4.4, "naos": 29.9, "back_room": 13.4,
        "raised": 0.7, "raised_steps": 2, "porch_columns": 6, "porch_diameter": 1.715, "architrave": 1.05,
        "frieze": 1.0, "door": (4.9, 9.8), "back_door": (4.2, 8.6),
    },
    "inner_colonnade": {"sides": 10, "back": 5, "diameter": 1.1, "aisle": 2.9, "front_gap": 3.5},
    "back_room_columns": {"count": 4, "diameter": 1.25},
    "metope_reliefs": True,
    "pediment_figures": True,
    "acroteria": True,
    "antefixes": True,
}


class Building:
    def __init__(self, name):
        self.name = name
        self.body = MeshBuilder()
        self.columns = {}
        self.info = {}

    def add_columns(self, template, matrices):
        key, build = template
        self.columns.setdefault(key, (build, []))[1].extend(matrices)


def place_building(building, library, collection, tile_sizes, parent=None, matrix=None):
    root = new_empty(building.name, collection, parent, matrix)
    unique_object(f"{building.name}_body", building.body, collection, root, tile_sizes)
    for key, (build, matrices) in building.columns.items():
        library.place(key, build, collection, root, matrices)
    return root


def painted(builder, polychromy, role, build):
    first = len(builder.polygons)
    build(PAINT if polychromy else MARBLE)
    if polychromy:
        builder.tint(first, PALETTE[role])


def bezier(start, control, end, steps):
    points = []
    for step in range(1, steps + 1):
        t = step / steps
        points.append(tuple((1 - t) ** 2 * a + 2 * (1 - t) * t * b + t * t * c for a, b, c in zip(start, control, end)))
    return points


def counter_clockwise(outline):
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(outline, outline[1:] + outline[:1]))
    return outline if area > 0 else list(reversed(outline))


def facade_prism(builder, outline, y0, y1, material, matrix=None, back=False):
    piece = MeshBuilder()
    piece.prism(counter_clockwise(outline), y0, y1, material, bottom=back)
    builder.merge(piece, (matrix if matrix is not None else Matrix.Identity(4)) @ SWAP_YZ)


def rect(builder, x0, x1, z0, z1, y, color, material=PAINT):
    builder.polygon([(x0, y, z0), (x0, y, z1), (x1, y, z1), (x1, y, z0)], material, color=color)


def entasis_radius(radius, top_ratio, swell, t):
    return radius * (1.0 - (1.0 - top_ratio) * t) + swell * math.sin(math.pi * t ** 0.7565)


def ring_heights(bottom, top, detail):
    count = RINGS[detail]
    return [bottom + (top - bottom) * k / (count - 1) for k in range(count)]


def fluted_shaft(builder, heights, radii, flutes, steps, depth, material):
    for flute in range(flutes):
        start = TAU * flute / flutes
        rows = []
        for z, radius in zip(heights, radii):
            row = []
            for step in range(steps + 1):
                p = step / steps
                local = radius * (1.0 - depth * math.sin(math.pi * p))
                angle = start + TAU / flutes * p
                row.append((local * math.cos(angle), local * math.sin(angle), z))
            rows.append(row)
        builder.surface(rows, material, smooth=True)


def ring_shaft(builder, heights, radii, segments, material, smooth=True, mapped=False):
    rings = [[builder.point((r * math.cos(TAU * s / segments), r * math.sin(TAU * s / segments), z))
              for s in range(segments)] for z, r in zip(heights, radii)]
    for lower in range(len(rings) - 1):
        for s in range(segments):
            following = (s + 1) % segments
            uvs = None
            if mapped:
                u0, u1 = s / segments, (s + 1) / segments
                v0, v1 = heights[lower] / 3.0, heights[lower + 1] / 3.0
                uvs = [(u0, v0), (u1, v0), (u1, v1), (u0, v1)]
            builder.face([rings[lower][s], rings[lower][following], rings[lower + 1][following], rings[lower + 1][s]],
                         material, smooth, uvs)


def doric_shaft(builder, diameter, top, top_ratio, swell, flutes, detail, material):
    heights = ring_heights(0.0, top, detail)
    radii = [entasis_radius(diameter / 2, top_ratio, swell * diameter, z / top) for z in heights]
    if detail == "high":
        fluted_shaft(builder, heights, radii, flutes, 4, 0.05, material)
    elif detail == "medium":
        ring_shaft(builder, heights, radii, flutes * 2, DORIC_FLUTED if material == MARBLE else material, mapped=True)
    else:
        ring_shaft(builder, heights, radii, flutes, material, smooth=False)


def doric_capital(builder, diameter, bottom, top_ratio, detail, material):
    d = diameter
    neck = d / 2 * top_ratio
    if detail == "low":
        profile = [(neck, 0.0), (0.45 * d, 0.06 * d), (0.51 * d, 0.16 * d), (0.525 * d, 0.24 * d)]
    else:
        profile = [(neck, 0.0)]
        for ring in range(3):
            out = neck + 0.011 * d * (ring + 1)
            profile += [(out, 0.004 * d + 0.016 * d * ring), (out, 0.014 * d + 0.016 * d * ring)]
        profile += bezier(profile[-1], (0.52 * d, 0.15 * d), (0.525 * d, 0.24 * d), 6 if detail == "high" else 4)
    builder.lathe([(r, bottom + z) for r, z in profile], SEGMENTS[detail], material, smooth=True)
    half = 0.535 * d
    builder.box((-half, -half, bottom + 0.24 * d), (half, half, bottom + DORIC_CAPITAL * d), material)


def doric_column(diameter, height, detail="high", top_ratio=0.78, swell=0.009, flutes=20, material=MARBLE):
    builder = MeshBuilder()
    shaft_top = height - DORIC_CAPITAL * diameter
    doric_shaft(builder, diameter, shaft_top, top_ratio, swell, flutes, detail, material)
    doric_capital(builder, diameter, shaft_top, top_ratio, detail, material)
    return builder


def attic_ionic_base(builder, d, detail, material):
    profile = [(0.66, 0.0), (0.675, 0.04), (0.67, 0.09), (0.63, 0.13), (0.58, 0.145), (0.565, 0.155), (0.52, 0.19),
               (0.52, 0.215), (0.555, 0.24), (0.565, 0.25), (0.585, 0.275), (0.585, 0.31), (0.555, 0.34),
               (0.515, 0.355), (0.5, 0.36)]
    if detail == "low":
        profile = [profile[0], profile[2], profile[6], profile[11], profile[-1]]
    builder.lathe([(r * d, z * d) for r, z in profile], SEGMENTS[detail] + 4, material, smooth=True, caps=False)


def volute_spiral(builder, centre, radius, side, face, turns, steps, ridge, material):
    count = int(turns * steps)
    path = []
    for k in range(count + 1):
        theta = turns * TAU * k / count
        r = radius * (0.95 - 0.75 * k / count)
        angle = math.pi / 2 - side * theta
        path.append((centre[0] + r * math.cos(angle), centre[1], centre[2] + r * math.sin(angle)))
    builder.sweep(path, [(0.0, -ridge), (ridge, -ridge), (ridge, ridge), (0.0, ridge)], material,
                  facade_normal=(0, face, 0), caps=False)


def ionic_capital(builder, diameter, bottom, top_ratio, detail, material):
    d = diameter
    neck = d / 2 * top_ratio
    builder.lathe([(neck, bottom), (neck + 0.05 * d, bottom + 0.04 * d), (neck + 0.065 * d, bottom + 0.085 * d),
                   (neck + 0.04 * d, bottom + 0.12 * d)], SEGMENTS[detail], material, smooth=True)
    volute_x = 0.6 * d
    volute_z = bottom + 0.07 * d
    radius = 0.2 * d
    depth = 0.38 * d
    builder.box((-volute_x, -depth + 0.02 * d, bottom + 0.1 * d), (volute_x, depth - 0.02 * d, bottom + 0.27 * d),
                material)
    pulvinus = [(0.0, -depth), (radius, -depth), (0.19 * d, -0.2 * d), (0.15 * d, 0.0), (0.19 * d, 0.2 * d),
                (radius, depth), (0.0, depth)]
    for side in (-1, 1):
        frame = Matrix.Translation((side * volute_x, 0.0, volute_z)) @ Matrix.Rotation(math.pi / 2, 4, "X")
        builder.lathe(pulvinus, {"high": 14, "medium": 10, "low": 8}[detail], material, smooth=True, matrix=frame)
        if detail == "low":
            continue
        for face in (-1, 1):
            volute_spiral(builder, (side * volute_x, face * (depth + 0.001), volute_z), radius, side, face, 2.0,
                          14 if detail == "high" else 8, 0.012 * d, material)
    builder.box((-0.5 * d, -0.44 * d, bottom + 0.27 * d), (0.5 * d, 0.44 * d, bottom + IONIC_CAPITAL * d), material)


def ionic_column(diameter, height, detail="high", top_ratio=0.84, swell=0.006, material=MARBLE):
    d = diameter
    builder = MeshBuilder()
    attic_ionic_base(builder, d, detail, material)
    bottom = IONIC_BASE * d
    top = height - IONIC_CAPITAL * d
    heights = ring_heights(bottom, top, detail)
    radii = [entasis_radius(d / 2, top_ratio, swell * d, (z - bottom) / (top - bottom)) for z in heights]
    if detail == "high":
        builder.lathe(list(zip(radii, heights)), 96, material, smooth=True, radius_scale=fluting(24, 0.1), caps=False)
    elif detail == "medium":
        ring_shaft(builder, heights, radii, 32, IONIC_FLUTED if material == MARBLE else material, mapped=True)
    else:
        ring_shaft(builder, heights, radii, 12, material)
    ionic_capital(builder, d, top, top_ratio, detail, material)
    return builder


def doric_template(diameter, height, detail, top_ratio=0.78):
    return (f"doric_{diameter:.3f}_{height:.3f}_{detail}",
            lambda: doric_column(diameter, height, detail, top_ratio))


def ionic_template(diameter, height, detail):
    return f"ionic_{diameter:.3f}_{height:.3f}_{detail}", lambda: ionic_column(diameter, height, detail)


def doric_dimensions(diameter, spacing, slope_degrees=13.5, metopes_per_bay=2, **overrides):
    d = diameter
    triglyph = spacing / (2.5 * metopes_per_bay)
    dims = dict(diameter=d, spacing=spacing, pitch=spacing / metopes_per_bay, triglyph=triglyph, face=0.46 * d,
                inner=0.56 * d, architrave=1.58 * triglyph, taenia=0.05 * d, taenia_projection=0.035 * d,
                regula=0.035 * d, guttae=0.035 * d, frieze=1.58 * triglyph, frieze_crown=0.065 * d,
                recess=triglyph / 12 + 0.02 * d, projection=0.38 * d, corona=0.24 * d, crown=0.08 * d,
                sima=0.2 * d, slope=math.radians(slope_degrees))
    dims.update(overrides)
    return dims


def entablature_levels(dims, geison=True):
    frieze_top = dims["architrave"] + dims["frieze"]
    if not geison:
        return {"frieze_top": frieze_top, "top": frieze_top}
    drip = frieze_top - dims["projection"] * math.tan(dims["slope"])
    corona_top = drip + dims["corona"]
    return {"frieze_top": frieze_top, "drip": drip, "corona_top": corona_top, "top": corona_top + dims["crown"]}


def frieze_back(dims, frieze):
    return dims["face"] - dims["recess"] if frieze == "doric" else dims["face"] - 0.01 * dims["diameter"]


def entablature_profile(dims, frieze="doric", geison=True):
    d = dims["diameter"]
    f = dims["face"]
    a = dims["architrave"]
    levels = entablature_levels(dims, geison)
    top = levels["frieze_top"]
    crown_bottom = top - dims["frieze_crown"]
    back = frieze_back(dims, frieze)
    tp = dims["taenia_projection"]
    points = [(-dims["inner"], 0.0), (f, 0.0), (f, a - dims["taenia"]), (f + tp, a - dims["taenia"]), (f + tp, a),
              (back, a), (back, crown_bottom), (f + 0.012 * d, crown_bottom), (f + 0.012 * d, top)]
    if geison:
        p = f + dims["projection"]
        points += [(p, levels["drip"]), (p, levels["corona_top"]), (p + 0.03 * d, levels["corona_top"]),
                   (p + 0.03 * d, levels["top"])]
    points.append((-dims["inner"], levels["top"]))
    return points


def triglyph_centres(length, face, width, pitch, axes=()):
    start = -face + width / 2
    end = length + face - width / 2
    anchors = [start] + sorted(a for a in axes if 1e-6 < a < length - 1e-6) + [end]
    centres = [start]
    for a, b in zip(anchors, anchors[1:]):
        count = max(int(round((b - a) / pitch)), 1)
        centres.extend(a + (b - a) * k / count for k in range(1, count + 1))
    return centres


def mutule_centres(centres):
    middles = [(a + b) / 2 for a, b in zip(centres, centres[1:])]
    return sorted(centres + middles)


def run_frame(start, end, z):
    start = Vector((start[0], start[1], 0.0))
    end = Vector((end[0], end[1], 0.0))
    tangent = (end - start).normalized()
    outward = Vector((tangent.y, -tangent.x, 0.0))
    frame = Matrix((tangent, outward, UP)).transposed().to_4x4()
    frame.translation = (start.x, start.y, z)
    return frame, (end - start).length


def guttae(builder, centres_x, y, top, radius, length, detail, material=MARBLE, matrix=None):
    transform = matrix if matrix is not None else Matrix.Identity(4)
    if detail == "low":
        return
    if detail == "medium":
        span = (min(centres_x) - radius, max(centres_x) + radius)
        builder.box((span[0], y - radius, top - length * 0.8), (span[1], y + radius, top), material, matrix=transform,
                    top=False)
        return
    for x in centres_x:
        builder.lathe([(radius * 0.8, 0.0), (radius, -length), (0.0, -length)], 5, material, smooth=True,
                      matrix=transform @ Matrix.Translation((x, y, top)), caps=False)


def triglyph(run, centre, dims, polychromy, detail, sides):
    t = dims["triglyph"]
    u = t / 12
    f = dims["face"]
    back = f - dims["recess"]
    z0 = dims["architrave"]
    z1 = z0 + dims["frieze"] - dims["frieze_crown"]
    left = centre - t / 2
    if detail == "low":
        xs, depths = [0, 12], [0, 0]
    else:
        xs, depths = [0, 1, 3, 4, 5, 7, 8, 9, 11, 12], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    rows = [[(left + x * u, f - depth * u, z) for x, depth in zip(xs, depths)] for z in (z0, z1)]
    edge = f - depths[0] * u

    def build(material):
        run.surface(rows, material, facing=(0, 1, 0))
        for side, x in ((sides[0], left), (sides[1], left + t)):
            if side:
                run.oriented([(x, back, z0), (x, edge, z0), (x, edge, z1), (x, back, z1)],
                             (-1 if x == left else 1, 0, 0), material)
    painted(run, polychromy, "triglyph", build)


def regula(run, centre, dims, polychromy, detail, extend=(0.0, 0.0)):
    t = dims["triglyph"]
    f = dims["face"]
    tp = dims["taenia_projection"]
    top = dims["architrave"] - dims["taenia"]
    bottom = top - dims["regula"]
    painted(run, polychromy, "regula",
            lambda m: run.box((centre - t / 2 - extend[0], f, bottom), (centre + t / 2 + extend[1], f + tp, top), m,
                              top=False))
    xs = [centre - t / 2 + t / 12 + k * t / 6 for k in range(6)]
    guttae(run, xs, f + tp / 2, bottom, min(t / 26, tp * 0.45), dims["guttae"], detail)


def mutule(run, centre, dims, polychromy, detail):
    d = dims["diameter"]
    t = dims["triglyph"]
    f = dims["face"]
    top = dims["architrave"] + dims["frieze"]
    start = f + 0.012 * d
    length = (f + dims["projection"] - start) / math.cos(dims["slope"])
    tilt = Matrix.Translation((0.0, start, top)) @ Matrix.Rotation(-dims["slope"], 4, "X")
    thickness = 0.02 * d
    y0, y1 = 0.04 * d, length - 0.05 * d
    painted(run, polychromy, "mutule",
            lambda m: run.box((centre - t / 2, y0, -thickness), (centre + t / 2, y1, 0.0), m, matrix=tilt, top=False))
    xs = [centre - t / 2 + t / 12 + k * t / 6 for k in range(6)]
    for row in range(3):
        y = y0 + (y1 - y0) * (row + 0.5) / 3
        guttae(run, xs, y, -thickness, t / 26, dims["guttae"], detail, matrix=tilt)


def slab(builder, frame, centre, size, angle=0.0):
    builder.centered_box((0.0, 0.0, 0.0), size, MARBLE,
                         matrix=frame @ Matrix.Translation(centre) @ Matrix.Rotation(angle, 4, "Y"), bottom=False)


def relief_human(builder, x, y, z, h, depth, lean=0.0, arm=-0.9):
    frame = Matrix.Translation((x, y, z)) @ Matrix.Rotation(lean, 4, "Y")
    half = depth / 2
    slab(builder, frame, (-0.08 * h, half, 0.24 * h), (0.09 * h, depth, 0.5 * h), 0.25)
    slab(builder, frame, (0.08 * h, half, 0.24 * h), (0.09 * h, depth, 0.5 * h), -0.25)
    slab(builder, frame, (0.0, half, 0.63 * h), (0.22 * h, depth, 0.32 * h))
    slab(builder, frame, (0.0, half, 0.87 * h), (0.11 * h, depth * 0.9, 0.13 * h))
    slab(builder, frame, (0.17 * h, half, 0.7 * h), (0.07 * h, depth * 0.8, 0.3 * h), arm)


def relief_horse(builder, x, y, z, h, depth, facing=1, rider=True):
    frame = Matrix.Translation((x, y, z)) @ Matrix.Diagonal((facing, 1.0, 1.0, 1.0))
    half = depth / 2
    piece = MeshBuilder()
    identity = Matrix.Identity(4)
    slab(piece, identity, (0.0, half, 0.42 * h), (0.6 * h, depth, 0.22 * h))
    slab(piece, identity, (-0.24 * h, half, 0.18 * h), (0.07 * h, depth, 0.38 * h), 0.25)
    slab(piece, identity, (0.24 * h, half, 0.18 * h), (0.07 * h, depth, 0.38 * h), -0.2)
    slab(piece, identity, (0.33 * h, half, 0.6 * h), (0.1 * h, depth * 0.9, 0.3 * h), 0.5)
    if rider:
        slab(piece, identity, (0.02 * h, half, 0.68 * h), (0.16 * h, depth * 0.9, 0.3 * h), -0.15)
        slab(piece, identity, (0.06 * h, half, 0.88 * h), (0.1 * h, depth * 0.8, 0.12 * h))
    builder.merge(piece, frame)


def metope_relief(builder, rng, x0, x1, y, z, height, depth):
    width = x1 - x0
    facing = rng.choice((-1, 1))
    relief_human(builder, x0 + width * (0.5 - 0.22 * facing), y, z, height, depth, rng.uniform(-0.25, 0.25) * facing,
                 -0.9 * facing)
    relief_horse(builder, x0 + width * (0.5 + 0.18 * facing), y, z, height * 0.95, depth, -facing)


def procession(builder, rng, x0, x1, y, z, height, depth):
    x = x0 + 0.2
    while x < x1 - 0.6:
        if rng.random() < 0.4:
            relief_horse(builder, x + 0.32 * height, y, z, height, depth)
            x += 0.65 * height + rng.uniform(0.05, 0.2)
        else:
            relief_human(builder, x + 0.12 * height, y, z, height * rng.uniform(0.85, 0.97), depth, 0.0, -0.2)
            x += 0.3 * height + rng.uniform(0.05, 0.25)


def statue(builder, source, matrix):
    copy = MeshBuilder()
    copy.points(source.positions)
    for indices, smooth in zip(source.polygons, source.polygon_smooth):
        copy.face(list(indices), MARBLE, smooth)
    builder.merge(copy, matrix)


STATUE_MODELS = (people.man_himation, people.woman_peplos, people.ephebe,
                 lambda: people.woman_peplos(veil=people.WOOL_WHITE), people.priest)


def pediment_statues(builder, rng, half_span, slope, clip, ceiling, y):
    models = [build() for build in STATUE_MODELS]
    reach = half_span - clip - 0.3

    def room(x):
        return (half_span - abs(x)) * math.tan(slope) - ceiling

    x = -reach
    while x < reach - 0.6:
        scale = min(room(x) * 0.86 / 1.8, room(x + 0.6) * 0.86 / 1.8, 1.7)
        model = rng.choice(models)
        if scale > 0.75:
            builder_matrix = Matrix.Translation((x + 0.3 * scale, y + 0.3 * scale, 0.0)) @ Matrix.Scale(scale, 4)
            statue(builder, model, builder_matrix @ Matrix.Rotation(rng.uniform(-0.4, 0.4), 4, "Z"))
            x += 0.62 * scale + rng.uniform(0.05, 0.3)
            continue
        lying = min(max(room(x) * 0.8 / 0.62, room(x + 1.2) * 0.8 / 0.62), 1.6)
        if lying < 0.35:
            x += 0.5
            continue
        length = 1.8 * lying
        if x < 0:
            matrix = Matrix.Translation((x, y + 0.3 * lying, 0.3 * lying)) @ Matrix.Rotation(math.pi / 2, 4, "Y")
        else:
            matrix = Matrix.Translation((x + length, y + 0.3 * lying, 0.3 * lying)) @ Matrix.Rotation(-math.pi / 2, 4,
                                                                                                    "Y")
        statue(builder, model, matrix @ Matrix.Scale(lying, 4))
        x += length + rng.uniform(0.1, 0.4)


def band(builder, x0, x1, y, z0, z1, pattern, detail):
    if detail == "low" or x1 <= x0:
        return
    height = z1 - z0
    if pattern == "plain":
        rect(builder, x0, x1, z0, z1, y, PALETTE["taenia"])
        return
    if pattern == "meander" and detail == "high":
        meander(builder, x0, x1, y, z0, z1)
        return
    cell = height * (1.1 if detail == "high" else 2.2)
    count = max(int((x1 - x0) / cell), 1)
    cell = (x1 - x0) / count
    for k in range(count):
        left = x0 + k * cell
        rect(builder, left, left + 0.62 * cell, z0, z1, y, PALETTE["blue"])
        rect(builder, left + 0.62 * cell, left + cell, z0, z1, y, PALETTE["red"])


MEANDER_KEY = [(0.0, 0.0, 1.0, 0.13), (0.0, 0.0, 0.13, 1.0), (0.0, 0.87, 0.78, 1.0), (0.65, 0.35, 0.78, 1.0),
               (0.38, 0.35, 0.78, 0.48), (0.38, 0.35, 0.51, 0.7)]


def meander(builder, x0, x1, y, z0, z1):
    height = z1 - z0
    count = max(int((x1 - x0) / height), 1)
    period = (x1 - x0) / count
    for k in range(count):
        left = x0 + k * period
        for a, b, c, e in MEANDER_KEY:
            rect(builder, left + a * period, left + c * period, z0 + b * height, z0 + e * height, y, PALETTE["blue"])


def slope_frame(origin, side, slope):
    direction = Vector((-side * math.cos(slope), 0.0, math.sin(slope)))
    across = Vector((side * math.sin(slope), 0.0, math.cos(slope)))
    frame = Matrix((direction, Vector((0.0, 1.0, 0.0)), across)).transposed().to_4x4()
    frame.translation = origin
    return frame


def entablature_run(builder, start, end, z, dims, axes, closed, frieze, geison, regulae, decorated, polychromy, detail,
                    reliefs, seed):
    frame, length = run_frame(start, end, z)
    run = MeshBuilder()
    d = dims["diameter"]
    f = dims["face"]
    t = dims["triglyph"]
    centres = triglyph_centres(length, f, t, dims["pitch"], axes)
    back = frieze_back(dims, frieze)
    a = dims["architrave"]
    crown_bottom = a + dims["frieze"] - dims["frieze_crown"]
    rng = random.Random(seed)

    def reach(plane):
        return plane if closed else f

    if decorated and frieze == "doric":
        for index, centre in enumerate(centres):
            first = index == 0
            last = index == len(centres) - 1
            triglyph(run, centre, dims, polychromy, detail, (not (first and closed), not (last and closed)))
        for left, right in zip(centres, centres[1:]):
            x0, x1 = left + t / 2, right - t / 2
            if polychromy and reliefs and detail != "low":
                rect(run, x0, x1, a, crown_bottom, back + 0.004, PALETTE["metope"])
            if reliefs and detail == "high":
                metope_relief(run, rng, x0, x1, back + 0.004, a + 0.05, crown_bottom - a - 0.12, 0.14 * d)
    if frieze == "ionic":
        lo, hi = -reach(back), length + reach(back)
        if polychromy and reliefs and detail != "low":
            rect(run, lo, hi, a, crown_bottom, back + 0.004, PALETTE["frieze"])
        if reliefs and detail == "high":
            procession(run, rng, lo, hi, back + 0.004, a + 0.04, crown_bottom - a - 0.1, 0.07)
    if decorated and (regulae or frieze == "doric") and detail != "low":
        tp = dims["taenia_projection"]
        for index, centre in enumerate(centres):
            extend = (tp if index == 0 and closed else 0.0, tp if index == len(centres) - 1 and closed else 0.0)
            regula(run, centre, dims, polychromy, detail, extend)
    if decorated and geison and frieze == "doric" and detail != "low":
        for centre in mutule_centres(centres):
            mutule(run, centre, dims, polychromy, detail)
    if polychromy:
        plane = f + dims["taenia_projection"]
        band(run, -reach(plane), length + reach(plane), plane + 0.003, a - dims["taenia"], a, "plain", detail)
        if geison:
            levels = entablature_levels(dims)
            crown = f + dims["projection"] + 0.03 * d
            band(run, -reach(crown), length + reach(crown), crown + 0.003, levels["corona_top"] + 0.005,
                 levels["top"] - 0.005, "kymation", detail)
    builder.merge(run, frame)
    return len(centres)


def entablature(builder, path, z, dims, axes=None, closed=True, frieze="doric", geison=True, regulae=True,
                plain_runs=(), polychromy=True, detail="high", reliefs=False, seed=0):
    path = [Vector((p[0], p[1], z)) for p in path]
    sweep_path = list(path)
    if not closed:
        tangent_start = (path[1] - path[0]).normalized()
        tangent_end = (path[-1] - path[-2]).normalized()
        sweep_path[0] = path[0] - tangent_start * dims["face"]
        sweep_path[-1] = path[-1] + tangent_end * dims["face"]
    builder.sweep(sweep_path, entablature_profile(dims, frieze, geison), MARBLE, closed=closed)
    count = len(path) if closed else len(path) - 1
    triglyphs = []
    for index in range(count):
        start, end = path[index], path[(index + 1) % len(path)]
        run_axes = axes[index] if axes else ()
        triglyphs.append(entablature_run(builder, start, end, z, dims, run_axes, closed, frieze, geison, regulae,
                                         index not in plain_runs, polychromy, detail, reliefs, seed + index))
    return {"triglyphs": triglyphs, "metopes": [n - 1 for n in triglyphs],
            "top": z + entablature_levels(dims, geison)["top"]}


def palmette(width, height, petals=9):
    centre = 0.42
    outline = [(-0.08, 0.0), (0.08, 0.0), (0.08, 0.2), (0.3, 0.1), (0.44, 0.2), (0.34, 0.3), (0.16, 0.3)]
    for k in range(2 * petals - 1):
        angle = math.radians(12 + 156 * k / (2 * petals - 2))
        radius = 0.58 if k % 2 == 0 else 0.3
        outline.append((radius * math.cos(angle), centre + radius * math.sin(angle)))
    outline += [(-0.16, 0.3), (-0.34, 0.3), (-0.44, 0.2), (-0.3, 0.1), (-0.08, 0.2)]
    return [(x * width / 1.1, z * height) for x, z in outline]


def acroterion(builder, x, y, z, size, depth, material=MARBLE):
    outline = [(px + x, pz + z) for px, pz in palmette(size * 0.8, size)]
    facade_prism(builder, outline, y - depth / 2, y + depth / 2, material, back=True)


def pediment(builder, half_span, dims, polychromy, detail, figures, acroteria, seed):
    d = dims["diameter"]
    slope = dims["slope"]
    f = dims["face"]
    tympanum_y = f - dims["recess"]
    face_y = f + dims["projection"] + 0.03 * d
    geison = dims["corona"] + dims["crown"]
    rise = half_span * math.tan(slope)
    clip = geison / math.sin(slope)
    soffit_apex = rise - geison / math.cos(slope)
    sima = dims["sima"] / math.cos(slope)
    painted(builder, polychromy and figures, "tympanum",
            lambda m: builder.oriented([(-(half_span - clip), tympanum_y, 0.0), (half_span - clip, tympanum_y, 0.0),
                                        (0.0, tympanum_y, soffit_apex)], (0, 1, 0), m))
    for side in (-1, 1):
        facade_prism(builder, [(side * half_span, 0.0), (side * (half_span - clip), 0.0), (0.0, soffit_apex),
                               (0.0, rise)], tympanum_y, face_y, MARBLE)
        facade_prism(builder, [(side * (half_span + 0.02), 0.0), (0.0, rise), (0.0, rise + sima),
                               (side * (half_span + 0.02), sima)], face_y - 0.5, face_y + 0.04, MARBLE)
        if polychromy and detail != "low":
            along = half_span / math.cos(slope)
            crown_band = MeshBuilder()
            band(crown_band, 0.7, along, 0.0, -dims["crown"] + 0.005, -0.005, "kymation", detail)
            builder.merge(crown_band, slope_frame((side * half_span, face_y + 0.003, 0.0), side, slope))
            sima_band = MeshBuilder()
            band(sima_band, 0.2, along, 0.0, 0.18 * dims["sima"], 0.82 * dims["sima"], "meander", detail)
            builder.merge(sima_band, slope_frame((side * (half_span + 0.02), face_y + 0.043, 0.0), side, slope))
    if figures and detail != "low":
        pediment_statues(builder, random.Random(seed), half_span, slope, clip, geison / math.cos(slope),
                         tympanum_y + 0.06)
    if acroteria:
        acroterion(builder, 0.0, face_y - 0.2, rise + sima - 0.1, 0.6 * rise, 0.3)
        for side in (-1, 1):
            acroterion(builder, side * (half_span - 0.4), face_y - 0.2, sima - 0.05, 0.36 * rise, 0.3)


def antefix(builder, x, y, z, side, size, detail, material):
    if detail == "low":
        return
    outline = palmette(size * 0.75, size) if detail == "high" else [(-0.3 * size, 0.0), (0.3 * size, 0.0),
                                                                     (0.2 * size, size), (-0.2 * size, size)]
    piece = MeshBuilder()
    piece.prism(counter_clockwise(outline), -0.025, 0.025, material)
    builder.merge(piece, Matrix.Translation((x - side * 0.03, y, z)) @ UVW_TO_YZX)


def rafters(builder, half_span, half_length, ridge, slope, spacing=1.6, size=0.24):
    builder.box((-size / 2, -half_length, ridge - size), (size / 2, half_length, ridge), WOOD)
    length = half_span / math.cos(slope)
    count = max(int(2 * half_length / spacing), 1)
    for k in range(count + 1):
        y = -half_length + 2 * half_length * k / count
        for side in (-1, 1):
            frame = Matrix.Translation((0.0, y, ridge)) @ Matrix.Rotation(side * slope, 4, "Y")
            span = (0.0, length) if side > 0 else (-length, 0.0)
            builder.box((span[0], -size / 2, -size), (span[1], size / 2, 0.0), WOOD, matrix=frame)


def gable(builder, frame, half_span, length, dims, polychromy, detail, roof=MARBLE, tile_pitch=0.66, figures=False,
          acroteria=True, antefixes=True, seed=0):
    g = MeshBuilder()
    for end in (-1, 1):
        piece = MeshBuilder()
        pediment(piece, half_span, dims, polychromy, detail, figures, acroteria, seed + end)
        g.merge(piece, Matrix.Translation((0.0, end * length / 2, 0.0)) @ Matrix.Rotation(0 if end > 0 else math.pi,
                                                                                            4, "Z"))
    rise = half_span * math.tan(dims["slope"])
    face_y = dims["face"] + dims["projection"] + 0.03 * dims["diameter"]
    half_roof = length / 2 + face_y - 0.5
    lift = 0.03
    first = len(g.polygons)
    if roof is None:
        rafters(g, half_span, half_roof, rise + lift, dims["slope"])
    else:
        for side in (-1, 1):
            tile_roof(g, (0.0, -half_roof, rise + lift), (0.0, half_roof, rise + lift),
                      (side * half_span, 0.0, -rise), roof, tile_pitch, imbrex=detail != "low")
        ridge_cap(g, (0.0, -half_roof, rise + lift + 0.05), (0.0, half_roof, rise + lift + 0.05), 0.14, roof)
    if roof == MARBLE:
        g.tint(first, ROOF_TINT)
    if antefixes and roof is not None:
        channels = max(int(round(2 * half_roof / tile_pitch)), 1)
        actual = 2 * half_roof / channels
        for side in (-1, 1):
            for k in range(channels):
                antefix(g, side * half_span, -half_roof + (k + 0.8) * actual, lift + 0.02, side, 0.42, detail, roof)
    builder.merge(g, frame)
    return rise


def crepidoma(builder, x0, x1, y0, y1, steps, rise, tread, material=MARBLE, foundation=1.0):
    margin = steps * tread + 0.15
    builder.box((x0 - margin, y0 - margin, -foundation), (x1 + margin, y1 + margin, 0.0), POROS, bottom=False,
                top=False)
    for k in range(steps):
        grow = (steps - 1 - k) * tread
        builder.box((x0 - grow, y0 - grow, k * rise), (x1 + grow, y1 + grow, (k + 1) * rise), material, bottom=False)
    return steps * rise


def column_axes(count, spacing, corner_spacing, central=None):
    gaps = [spacing] * (count - 1)
    if count >= 3:
        gaps[0] = gaps[-1] = corner_spacing
    if central is not None:
        gaps[(count - 1) // 2] = central
    total = sum(gaps)
    positions = [-total / 2]
    for gap in gaps:
        positions.append(positions[-1] + gap)
    return positions


def ideal_corner(dims):
    return dims["spacing"] - (dims["face"] - dims["triglyph"] / 2)


def ring_axes(xs, ys):
    x0, x1, y0, y1 = xs[0], xs[-1], ys[0], ys[-1]
    return [[x - x0 for x in xs], [y - y0 for y in ys], [x1 - x for x in xs], [y1 - y for y in ys]]


def rectangle(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def ceiling(builder, x0, x1, y0, y1, z, polychromy, role="coffer", material=MARBLE):
    corners = [(x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z)]
    if material == MARBLE:
        painted(builder, polychromy, role, lambda m: builder.oriented(corners, (0, 0, -1), m))
    else:
        builder.oriented(corners, (0, 0, -1), material)


def door_frame(builder, left, right, y0, y1, z0, height, width, material=MARBLE):
    builder.box((left - width, y0 - 0.08, z0), (left, y1 + 0.08, z0 + height + width), material, bottom=False)
    builder.box((right, y0 - 0.08, z0), (right + width, y1 + 0.08, z0 + height + width), material, bottom=False)
    builder.box((left, y0 - 0.08, z0 + height), (right, y1 + 0.08, z0 + height + width), material)


def wall_with_doors(builder, x0, x1, y0, y1, z0, z1, doors, material=MARBLE, frame=0.3):
    edge = x0
    for door in sorted(doors):
        centre, width, height = door[:3]
        sill = door[3] if len(door) > 3 else 0.0
        left, right = centre - width / 2, centre + width / 2
        builder.box((edge, y0, z0), (left, y1, z1), material, bottom=False, top=False)
        builder.box((left, y0, z0 + sill + height), (right, y1, z1), material, top=False)
        if sill > 0:
            builder.box((left, y0, z0), (right, y1, z0 + sill), material, bottom=False)
        door_frame(builder, left, right, y0, y1, z0 + sill, height, frame, material)
        edge = right
    builder.box((edge, y0, z0), (x1, y1, z1), material, bottom=False, top=False)


def beam(builder, start, end, width, z0, z1, material=MARBLE):
    x0, x1 = sorted((start[0], end[0]))
    y0, y1 = sorted((start[1], end[1]))
    builder.box((x0 - width / 2, y0 - width / 2, z0), (x1 + width / 2, y1 + width / 2, z1), material)


def placements(points, z):
    return [Matrix.Translation((x, y, z)) for x, y in points]


def flank_layout(spec, xs):
    count = spec["columns"][1]
    width, length = spec["stylobate"]
    margin = (width - (xs[-1] - xs[0])) / 2
    contraction = spec["spacing"] - spec["corner_spacing"]
    spacing = spec.get("flank_spacing") or (length - 2 * margin + 2 * contraction) / (count - 1)
    return column_axes(count, spacing, spacing - contraction), margin, spacing


def peristyle(building, spec, xs, ys, z, detail):
    corners, others = [], []
    for x in xs:
        for y in (ys[0], ys[-1]):
            (corners if x in (xs[0], xs[-1]) else others).append((x, y))
    for y in ys[1:-1]:
        others += [(xs[0], y), (xs[-1], y)]
    height = spec["column_height"]
    building.add_columns(doric_template(spec["diameter"], height, detail, spec["top_ratio"]), placements(others, z))
    building.add_columns(doric_template(spec.get("corner_diameter") or spec["diameter"], height, detail,
                                        spec["top_ratio"]), placements(corners, z))


def sekos_plan(spec):
    s = spec["sekos"]
    w = s["wall"]
    total = s["back_porch"] + s["front_porch"] + s["naos"] + s["back_room"] + w * (3 if s["back_room"] else 2)
    back_axis = -total / 2
    back_wall = back_axis + s["back_porch"]
    room = (back_wall + w, back_wall + w + s["back_room"]) if s["back_room"] else None
    naos_start = (room[1] + w) if room else back_wall + w
    naos = (naos_start, naos_start + s["naos"])
    return {"back_axis": back_axis, "front_axis": total / 2, "back_wall": back_wall, "room": room, "naos": naos,
            "front_wall": naos[1], "half": s["width"] / 2, "wall": w}


def sekos(building, spec, z_floor, z_ceiling, polychromy, detail):
    s = spec["sekos"]
    b = building.body
    plan = sekos_plan(spec)
    half, w = plan["half"], plan["wall"]
    dp = s["porch_diameter"]
    face = 0.46 * dp
    axis_x = half - face
    xs = [-axis_x + 2 * axis_x * k / (s["porch_columns"] - 1) for k in range(s["porch_columns"])]
    porch_spacing = xs[1] - xs[0]
    dims = doric_dimensions(dp, porch_spacing, face=face, inner=0.55 * dp, architrave=s["architrave"],
                            frieze=s["frieze"])
    z_beam = z_ceiling - s["architrave"] - s["frieze"]
    for k in range(s["raised_steps"]):
        grow = (s["raised_steps"] - 1 - k) * 0.5
        rise = s["raised"] / s["raised_steps"]
        b.box((-half - 0.8, plan["back_axis"] - dp - grow, z_floor - s["raised"] + k * rise),
              (half + 0.8, plan["front_axis"] + dp + grow, z_floor - s["raised"] + (k + 1) * rise), MARBLE,
              bottom=False)
    for y in (plan["back_axis"], plan["front_axis"]):
        building.add_columns(doric_template(dp, z_beam - z_floor, detail), placements([(x, y) for x in xs], z_floor))
    anta = 1.1 * dp
    for side in (-1, 1):
        b.box((min(side * half, side * (half - w)), plan["back_axis"] + anta, z_floor),
              (max(side * half, side * (half - w)), plan["front_axis"] - anta, z_beam), MARBLE, bottom=False, top=False)
    inner = half - w
    wall_with_doors(b, -inner, inner, plan["front_wall"], plan["front_wall"] + w, z_floor, z_ceiling,
                    [(0.0, *s["door"])] + list(s.get("windows", ())))
    wall_with_doors(b, -inner, inner, plan["back_wall"], plan["back_wall"] + w, z_floor, z_ceiling,
                    [(0.0, *s["back_door"])])
    if plan["room"]:
        b.box((-inner, plan["room"][1], z_floor), (inner, plan["room"][1] + w, z_ceiling), MARBLE, bottom=False,
              top=False)
    info = entablature(b, rectangle(-axis_x, axis_x, plan["back_axis"], plan["front_axis"]), z_beam, dims,
                       axes=ring_axes(xs, [plan["back_axis"], plan["front_axis"]]), frieze="ionic", geison=False,
                       regulae=True, polychromy=polychromy, detail=detail, reliefs=spec.get("metope_reliefs", False),
                       seed=31)
    inner_colonnade(building, spec, plan, z_floor, z_ceiling, detail)
    back_room_columns(building, spec, plan, z_floor, z_ceiling, detail)
    return {"plan": plan, "porch_spacing": porch_spacing, "inner_frieze": info}


def inner_colonnade(building, spec, plan, z_floor, z_ceiling, detail):
    ic = spec.get("inner_colonnade")
    if not ic:
        return
    d = ic["diameter"]
    upper_d = d * spec["top_ratio"]
    x = plan["half"] - plan["wall"] - ic["aisle"]
    y_back = plan["naos"][0] + ic["aisle"]
    y_front = plan["naos"][1] - ic["front_gap"]
    ys = [y_back + (y_front - y_back) * k / (ic["sides"] - 1) for k in range(ic["sides"])]
    xs = [-x + 2 * x * k / (ic["back"] - 1) for k in range(1, ic["back"] - 1)]
    points = [(side * x, y) for side in (-1, 1) for y in ys] + [(px, y_back) for px in xs]
    lower_beam = 0.75 * d
    upper_beam = 0.75 * upper_d
    free = z_ceiling - z_floor - lower_beam - upper_beam
    lower = free * 0.58
    upper = free - lower
    building.add_columns(doric_template(d, lower, detail), placements(points, z_floor))
    z_upper = z_floor + lower + lower_beam
    building.add_columns(doric_template(upper_d, upper, detail), placements(points, z_upper))
    for z0, z1, width in ((z_floor + lower, z_upper, 1.07 * d), (z_upper + upper, z_ceiling, 1.07 * upper_d)):
        for side in (-1, 1):
            beam(building.body, (side * x, y_back), (side * x, y_front), width, z0, z1)
        beam(building.body, (-x, y_back), (x, y_back), width, z0, z1)


def back_room_columns(building, spec, plan, z_floor, z_ceiling, detail):
    rc = spec.get("back_room_columns")
    if not rc or not plan["room"]:
        return
    d = rc["diameter"]
    x = (plan["half"] - plan["wall"]) / 2.2
    middle = sum(plan["room"]) / 2
    offset = (plan["room"][1] - plan["room"][0]) / 4
    top_beam = 0.6 * d
    points = [(sx * x, middle + sy * offset) for sx in (-1, 1) for sy in (-1, 1)]
    building.add_columns(ionic_template(d, z_ceiling - z_floor - top_beam, detail), placements(points, z_floor))
    for side in (-1, 1):
        beam(building.body, (side * x, plan["room"][0]), (side * x, plan["room"][1]), 0.9 * d, z_ceiling - top_beam,
             z_ceiling)


def temple(spec=PARTHENON, polychromy=True, detail="high", name="temple"):
    building = Building(name)
    b = building.body
    xs = column_axes(spec["columns"][0], spec["spacing"], spec["corner_spacing"])
    ys, margin, flank_spacing = flank_layout(spec, xs)
    width, length = spec["stylobate"]
    z_stylobate = crepidoma(b, -width / 2, width / 2, -length / 2, length / 2, spec["steps"], spec["step_rise"],
                            spec["step_tread"])
    peristyle(building, spec, xs, ys, z_stylobate, detail)
    z_column_top = z_stylobate + spec["column_height"]
    dims = doric_dimensions(spec["diameter"], spec["spacing"], spec["slope_degrees"])
    frieze = entablature(b, rectangle(xs[0], xs[-1], ys[0], ys[-1]), z_column_top, dims, axes=ring_axes(xs, ys),
                         polychromy=polychromy, detail=detail, reliefs=spec.get("metope_reliefs", False), seed=11)
    levels = entablature_levels(dims)
    z_ceiling = z_column_top + levels["frieze_top"]
    inner = dims["inner"]
    ceiling(b, xs[0] + inner, xs[-1] - inner, ys[0] + inner, ys[-1] - inner, z_ceiling, polychromy)
    inside = sekos(building, spec, z_stylobate + spec["sekos"]["raised"], z_ceiling, polychromy, detail) \
        if spec.get("sekos") else None
    half_span = xs[-1] + dims["face"] + dims["projection"] + 0.03 * dims["diameter"]
    z_eave = z_column_top + levels["top"]
    rise = gable(b, Matrix.Translation((0.0, 0.0, z_eave)), half_span, ys[-1] - ys[0], dims, polychromy, detail,
                 spec.get("roof", MARBLE), spec.get("tile_pitch", 0.66), spec.get("pediment_figures", False),
                 spec.get("acroteria", True), spec.get("antefixes", True), seed=5)
    building.info = {"front_axes": [round(x, 3) for x in xs], "flank_axes": [round(y, 3) for y in ys],
                     "stylobate_margin": round(margin, 3), "flank_spacing": round(flank_spacing, 3),
                     "triglyphs_per_side": frieze["triglyphs"], "metopes_per_side": frieze["metopes"],
                     "stylobate_top": z_stylobate, "column_top": z_column_top, "ceiling": z_ceiling,
                     "eave": z_eave, "ridge": z_eave + rise, "sekos": inside and inside["plan"]}
    return building


def stoa(length=46.0, depth=11.0, column_height=5.4, diameter=0.82, spacing=None, metopes_per_bay=2, steps=2,
         step_rise=0.3, step_tread=0.45, wall=0.75, inner_columns=True, slope_degrees=14.0, roof=TERRACOTTA,
         polychromy=True, detail="high", name="stoa", acroteria=True):
    building = Building(name)
    b = building.body
    spacing = spacing or 3.3 * diameter
    dims = doric_dimensions(diameter, spacing, slope_degrees, metopes_per_bay)
    count = max(int(round(length / spacing)) + 1, 3)
    xs = column_axes(count, spacing, ideal_corner(dims))
    f = dims["face"]
    depth_axis = depth - 2 * f
    x0, x1, y_back = xs[0], xs[-1], -depth_axis
    margin = 0.6 * diameter + 0.2
    z_stylobate = crepidoma(b, x0 - margin, x1 + margin, y_back - f - 0.3, margin, steps, step_rise, step_tread)
    building.add_columns(doric_template(diameter, column_height, detail), placements([(x, 0.0) for x in xs],
                                                                                     z_stylobate))
    z_top = z_stylobate + column_height
    b.box((x0 - f, y_back - f, z_stylobate), (x1 + f, y_back - f + wall, z_top), POROS, bottom=False, top=False)
    for side in (-1, 1):
        edge = (x1 if side > 0 else x0) + side * f
        b.box((min(edge, edge - side * wall), y_back - f + wall, z_stylobate),
              (max(edge, edge - side * wall), -0.9 * spacing, z_top), POROS, bottom=False, top=False)
    frieze = entablature(b, rectangle(x0, x1, y_back, 0.0), z_top, dims,
                         axes=[[], [], [x1 - x for x in xs], []], plain_runs=(0,), polychromy=polychromy,
                         detail=detail, seed=21)
    levels = entablature_levels(dims)
    z_ceiling = z_top + levels["frieze_top"]
    inner = dims["inner"]
    ceiling(b, x0 + inner, x1 - inner, y_back + inner, -inner, z_ceiling, polychromy, material=WOOD)
    if inner_columns:
        inner_xs = [x for x in xs[2:-2:2]]
        height = z_ceiling - z_stylobate - 0.5
        building.add_columns(ionic_template(height / 9.5, height, detail),
                             placements([(x, y_back / 2) for x in inner_xs], z_stylobate))
        beam(b, (x0, y_back / 2), (x1, y_back / 2), 0.5, z_ceiling - 0.5, z_ceiling, WOOD)
    half_span = depth_axis / 2 + f + dims["projection"] + 0.03 * diameter
    z_eave = z_top + levels["top"]
    frame = Matrix.Translation((0.0, y_back / 2, z_eave)) @ Matrix.Rotation(math.pi / 2, 4, "Z")
    rise = gable(b, frame, half_span, x1 - x0, dims, polychromy, detail, roof, 0.5, acroteria=acroteria, seed=23)
    building.info = {"columns": count, "spacing": spacing, "metopes_per_side": frieze["metopes"],
                     "stylobate_top": z_stylobate, "eave": z_eave, "ridge": z_eave + rise}
    return building


PROPYLAEA_DOORS = ((1.4, 3.6), (2.94, 5.5), (4.18, 7.38), (2.94, 5.5), (1.4, 3.6))


def propylon(columns=6, spacing=3.63, central_spacing=5.43, column_height=8.81, diameter=1.56, depth=24.0,
             cross_wall=0.3, doors=PROPYLAEA_DOORS, inner_ionic=True, steps=4, step_rise=0.36, step_tread=0.5,
             wall=1.0, slope_degrees=14.0, polychromy=True, detail="high", name="propylon", acroteria=True):
    building = Building(name)
    b = building.body
    dims = doric_dimensions(diameter, spacing, slope_degrees)
    xs = column_axes(columns, spacing, ideal_corner(dims), central_spacing if columns % 2 == 0 else None)
    f = dims["face"]
    half_y = depth / 2 - f
    x0, x1 = xs[0], xs[-1]
    margin = 0.6 * diameter + 0.2
    z_stylobate = crepidoma(b, x0 - margin, x1 + margin, -half_y - margin, half_y + margin, steps, step_rise,
                            step_tread)
    front = [(x, half_y) for x in xs] + [(x, -half_y) for x in xs]
    building.add_columns(doric_template(diameter, column_height, detail), placements(front, z_stylobate))
    z_top = z_stylobate + column_height
    levels = entablature_levels(dims)
    z_ceiling = z_top + levels["frieze_top"]
    anta = 1.3 * diameter
    for side in (-1, 1):
        edge = (x1 if side > 0 else x0) + side * f
        b.box((min(edge, edge - side * wall), -half_y + anta, z_stylobate),
              (max(edge, edge - side * wall), half_y - anta, z_top), MARBLE, bottom=False, top=False)
    gaps = [(a + c) / 2 for a, c in zip(xs, xs[1:])]
    first = (len(gaps) - len(doors)) // 2
    door_list = [(gaps[first + k], width, height) for k, (width, height) in enumerate(doors)]
    y_wall = -half_y + cross_wall * 2 * half_y
    inner_x = x1 + f - wall
    wall_with_doors(b, -inner_x, inner_x, y_wall - wall / 2, y_wall + wall / 2, z_stylobate, z_ceiling, door_list)
    if inner_ionic and columns % 2 == 0:
        height = z_ceiling - z_stylobate - 0.6
        middle = columns // 2
        ys = [y_wall + 3.0 + (half_y - 3.0 - y_wall - 3.0) * k / 2 for k in range(3)]
        points = [(x, y) for x in (xs[middle - 1], xs[middle]) for y in ys]
        building.add_columns(ionic_template(height / 10.0, height, detail), placements(points, z_stylobate))
        for x in (xs[middle - 1], xs[middle]):
            beam(b, (x, y_wall), (x, half_y), 0.55, z_ceiling - 0.6, z_ceiling)
    frieze = entablature(b, rectangle(x0, x1, -half_y, half_y), z_top, dims,
                         axes=ring_axes(xs, [-half_y, half_y]), polychromy=polychromy, detail=detail, seed=41)
    inner = dims["inner"]
    ceiling(b, x0 + inner, x1 - inner, -half_y + inner, half_y - inner, z_ceiling, polychromy)
    half_span = x1 + f + dims["projection"] + 0.03 * diameter
    z_eave = z_top + levels["top"]
    rise = gable(b, Matrix.Translation((0.0, 0.0, z_eave)), half_span, 2 * half_y, dims, polychromy, detail,
                 MARBLE, 0.6, acroteria=acroteria, seed=43)
    building.info = {"axes": [round(x, 3) for x in xs], "doors": door_list, "metopes_per_side": frieze["metopes"],
                     "stylobate_top": z_stylobate, "eave": z_eave, "ridge": z_eave + rise}
    return building
