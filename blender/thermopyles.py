import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bpy
import numpy as np
from mathutils import Matrix, Vector

from kit import figures
from kit import thermopyles_props as props
from kit.geometry import TemplateLibrary, ensure_collection, new_empty, new_object, placement, unique_object
from kit.materials import principled_material
from kit.stage import (configure_render, evening_world, export_glb, group_statistics, render_still, sun_lamp,
                       triangles_of)
from kit.terrain import point_in_polygon
from kit.thermopyles_terrain import (ANOPAIA, CORE, DEM_LICENCE, EXTENT, FOOT, PERSIAN_CAMP, ROAD, SHORE, SPRINGS,
                                     Ground, Relief, chaikin, densify, far_ground, far_material, ground_materials,
                                     polyline_distance, scatter, water_surfaces)

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(PROJECT, ".cache", "scenes", "thermopyles")
GEO_CACHE = os.path.join(PROJECT, ".cache", "geo", "copernicus")
PREVIEWS = os.path.join(PROJECT, ".cache", "previews", "thermopyles")
TEXTURE_SIZES = ((2048, 2048), (4096, 1596), (4096, 1332))
TEMPLATE_DEPTH = -1000.0
ANTHELA = (-2324.0, 236.0)
TRACHIS = (-7780.0, -410.0)
ALPENOI = (3380.0, 785.0)
XERXES_SEAT = (-2840.0, 160.0)
PAVILION = (-6480.0, 230.0)
MELAMPYGOS = (2771.0, 872.0)
ALTAR = (-848.0, -208.0)
CAMP_UNITS = [((-5600, 900), 300, 200), ((-6000, 1200), 250, 120), ((-6600, 600), 300, 200),
              ((-7000, 1300), 300, 200), ((-6300, 1800), 400, 300), ((-6900, 300), 50, 40)]
GREEK_UNITS = [((300, 60), 12, 30), ((450, 150), 20, 60), ((650, 200), 18, 50), ((850, 250), 13, 40),
               ((1150, 350), 30, 80), ((1450, 450), 18, 45), ((1750, 550), 24, 50)]
PERSIAN_TENTS = [props.LINEN, props.SAFFRON, props.HIDE, (0.80, 0.46, 0.34)]
GREEK_TENTS = [props.LEATHER, props.HIDE]
SUN = {"attente": (124.0, 54.0), "assaut": (109.0, 44.0), "kolonos": (180.0, 66.0)}
FOV = 40.0
TACTICAL_TILT = 52.0


def arguments():
    values = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    options = {"previews": "", "samples": "24"}
    for item in values:
        key, _, value = item.partition("=")
        options[key.lstrip("-")] = value
    return options


def near_rect(x, y, rects, margin):
    for (cx, cy), along, across in rects:
        if abs(x - cx) < along / 2 + margin and abs(y - cy) < across / 2 + margin:
            return True
    return False


def road_distance(x, y):
    distance, _ = polyline_distance(densify(chaikin(ROAD), 20.0), x, y)
    return distance


def persian_tents(relief, ground, generator):
    spacing = 26.0
    xs = np.arange(-8700, -4400, spacing)
    ys = np.arange(-400, 2800, spacing)
    grid_x, grid_y = np.meshgrid(xs, ys)
    x = (grid_x + generator.uniform(-6, 6, grid_x.shape)).ravel()
    y = (grid_y + generator.uniform(-6, 6, grid_y.shape)).ravel()
    inside = np.array([point_in_polygon(px, py, PERSIAN_CAMP) for px, py in zip(x, y)])
    shore = np.interp(x, SHORE[:, 0], SHORE[:, 1])
    keep = inside & (y < shore - 120)
    x, y = x[keep], y[keep]
    blocks = (np.floor(x / 160) + np.floor(y / 130)) % 3 != 0
    lanes = road_distance(x, y) > 45
    free = np.array([not near_rect(px, py, CAMP_UNITS, 35) for px, py in zip(x, y)])
    keep = blocks & lanes & free & (generator.random(len(x)) < 0.24)
    x, y = x[keep], y[keep]
    return np.column_stack([x, y, ground.sample(x, y), generator.uniform(-0.2, 0.2, len(x)) + 0.35])


def greek_tents(relief, ground, generator):
    candidates = []
    for x in np.arange(160, 1960, 13.0):
        foot = np.interp(x, FOOT[:, 0], FOOT[:, 1])
        for y in np.arange(foot + 14, foot + 80, 11.0):
            px, py = x + generator.uniform(-3, 3), y + generator.uniform(-2, 2)
            if math.hypot(px, py) < 95 or near_rect(px, py, [((c[0], c[1]), b, a) for c, a, b in GREEK_UNITS], 14):
                continue
            if generator.random() < 0.45:
                candidates.append((px, py))
    x = np.array([c[0] for c in candidates])
    y = np.array([c[1] for c in candidates])
    keep = road_distance(x, y) > 12
    x, y = x[keep], y[keep]
    return np.column_stack([x, y, ground.sample(x, y), generator.uniform(-0.3, 0.3, len(x))])


def place_set(library, collection, parent, key, build, points, scale_range, generator, sink=0.0, shadow=True):
    matrices = [placement(px, py, pz - sink, generator.uniform(0, math.tau), generator.uniform(*scale_range))
                for px, py, pz in points]
    if matrices:
        library.place(key, build, collection, parent, matrices, cast_shadow=shadow, ground_occlusion=False)
    return len(matrices)


def vegetation(relief, ground, library, collection, root):
    generator = np.random.default_rng(31)
    group = new_empty("vegetation", collection, root)
    counts = {}

    def strip(x, y):
        shore = np.interp(x, SHORE[:, 0], SHORE[:, 1])
        foot = np.interp(x, FOOT[:, 0], FOOT[:, 1])
        return (x > -4400) & (y > foot - 25) & (y < shore)

    def oaks(x, y, f):
        return (f["h"] > 600) & (f["slope"] < 0.75) & (f["noise"] > 0.45) & (f["random"] < 0.2)

    def shrubs(x, y, f):
        camp = np.array([point_in_polygon(px, py, PERSIAN_CAMP) for px, py in zip(x, y)])
        return (f["land"] & (f["h"] > 8) & (f["h"] < 640) & (f["slope"] < 1.0) & (f["noise"] > 0.4)
                & (f["random"] < 0.28) & ~strip(x, y) & ~camp)

    def off_road(mask, x, y, margin):
        mask[mask] &= road_distance(x[mask], y[mask]) > margin
        return mask

    def reeds(x, y, f):
        return off_road(f["land"] & (f["h"] < 1.6) & ((f["shore"] < 45) | (f["river"] < 18)) & (f["random"] < 0.6)
                        & ~((x > -1300) & (x < 2000)), x, y, 14)

    def boulders(x, y, f):
        return off_road(f["land"] & (f["slope"] > 0.45) & (f["slope"] < 0.85) & (f["h"] < 160) & (f["foot"] < 90)
                        & (f["random"] < 0.5),
                        x, y, 16)

    rules = [("oak", lambda: props.oak(), oaks, EXTENT, 52.0, (0.8, 1.25), 1.2),
             ("shrub", lambda: props.shrub(), shrubs, EXTENT, 70.0, (0.7, 1.4), 0.2),
             ("shrub_dry", lambda: props.shrub(True), shrubs, CORE, 46.0, (0.6, 1.2), 0.2),
             ("reeds", lambda: props.reeds(), reeds, EXTENT, 22.0, (0.8, 1.3), 0.1),
             ("boulder", lambda: props.boulder(), boulders, CORE, 26.0, (0.7, 1.6), 0.9)]
    for index, (key, build, rule, bounds, spacing, scale_range, sink) in enumerate(rules):
        points = scatter(relief, ground, bounds, spacing, 100 + index, rule)
        counts[key] = place_set(library, collection, group, key, build, points, scale_range, generator, sink,
                                shadow=key == "oak")
    return counts


def settlements(relief, ground, library, collection, root):
    generator = np.random.default_rng(7)
    group = new_empty("settlements", collection, root)
    height_at = lambda x, y: float(ground.sample(np.array([x]), np.array([y]))[0])

    def gentle(x, y):
        fields = relief.evaluate(np.array([x, x + 8.0, x]), np.array([y, y, y + 8.0]), fields=True)
        h = fields["h"]
        return bool(fields["land"][0]) and math.hypot(h[1] - h[0], h[2] - h[0]) / 8.0 < 0.3 and h[0] > 1.5 and (
            road_distance(np.array([x]), np.array([y]))[0] > 10)

    houses = []
    for centre, radius, count, seed in ((TRACHIS, 200.0, 26, 1), (ALPENOI, 110.0, 14, 2), ((-2250.0, 170.0), 110.0, 9, 3)):
        houses += props.village(centre, radius, count, height_at, gentle, seed)
    for variant in range(4):
        matrices = [placement(x, y, z, turn) for x, y, z, turn in houses[variant::4]]
        library.place(f"house_{variant}", lambda variant=variant: props.house(variant + 1), collection, group,
                      matrices, cast_shadow=True, ground_occlusion=False)
    for name, centre, length, width, columns in (("demeter_anthela", ANTHELA, 18.0, 9.0, 6),
                                                 ("amphictyon_anthela", (-2390.0, 175.0), 12.0, 7.0, 4)):
        x, y = centre
        unique_object(name, props.shrine(length, width, columns), collection, group, {},
                      matrix=placement(x, y, height_at(x, y), 0.0), ground_occlusion=False)
    unique_object("xerxes_seat", props.throne(XERXES_SEAT, height_at, 90.0), collection, group, {},
                  ground_occlusion=False)
    x, y = PAVILION
    unique_object("xerxes_pavilion", props.pavilion(), collection, group, {},
                  matrix=placement(x, y, height_at(x, y), 0.3), ground_occlusion=False)
    unique_object("phocian_wall", props.rough_wall(props.WALL, height_at), collection, group, {},
                  ground_occlusion=False)
    unique_object("phocian_wall_north", props.rough_wall(props.WALL_NORTH, height_at, seed=6), collection, group, {},
                  ground_occlusion=False)
    unique_object("phocian_gate", props.gate_posts(height_at), collection, group, {}, ground_occlusion=False)
    unique_object("altar_heracles", props.altar(ALTAR, height_at), collection, group, {}, ground_occlusion=False)
    unique_object("hot_springs", props.pools(SPRINGS, height_at), collection, group, {}, cast_shadow=False,
                  ground_occlusion=False)
    unique_object("melampygos", props.rock(MELAMPYGOS, height_at, 4.5), collection, group, {},
                  ground_occlusion=False)
    tents = {}
    points = persian_tents(relief, ground, generator)
    for variant, colour in enumerate(PERSIAN_TENTS):
        chosen = points[variant::len(PERSIAN_TENTS)]
        matrices = [placement(x, y, z - 0.3, turn) for x, y, z, turn in chosen]
        library.place(f"tent_persian_{variant}", lambda colour=colour: props.persian_tent(colour), collection, group,
                      matrices, cast_shadow=False, ground_occlusion=False)
        tents[f"persian_{variant}"] = len(matrices)
    points = greek_tents(relief, ground, generator)
    for variant, colour in enumerate(GREEK_TENTS):
        chosen = points[variant::len(GREEK_TENTS)]
        matrices = [placement(x, y, z, turn) for x, y, z, turn in chosen]
        library.place(f"tent_greek_{variant}", lambda colour=colour: props.greek_tent(colour), collection, group,
                      matrices, cast_shadow=False, ground_occlusion=False)
        tents[f"greek_{variant}"] = len(matrices)
    return {"houses": len(houses), **tents}


def build_troops(collection, parent):
    group = new_empty("troops", collection, parent)
    report = {}
    for kind, (near, far) in figures.TROOPS.items():
        for suffix, build in (("", near), ("_far", far)):
            name = f"troop_{kind}{suffix}"
            created = unique_object(name, build(), collection, group, {}, ground_occlusion=False)
            created.location.z = TEMPLATE_DEPTH
            report[name] = triangles_of(created.data)
    return report


def seeded(index):
    value = math.sin(index * 127.1 + 311.7) * 43758.5453
    return value - math.floor(value)


def slots(count, width, depth, seed):
    columns = max(1, min(count, round(math.sqrt(count * width / depth))))
    rows = math.ceil(count / columns)
    result = []
    for index in range(count):
        key = seed * 7919 + index * 13
        result.append(((index % columns + 0.5 + (seeded(key) - 0.5) * 0.22) / columns,
                       (index // columns + 0.5 + (seeded(key + 1) - 0.5) * 0.22) / rows,
                       (index + 0.5) / count, (seeded(key + 2) - 0.5) * 1.2, (seeded(key + 3) - 0.5) * 1.2))
    return result


def trail_point(points, distance):
    travelled = 0.0
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        length = math.hypot(x1 - x0, y1 - y0)
        if travelled + length >= distance or (x1, y1) == tuple(points[-1]):
            local = min(1.0, max(0.0, (distance - travelled) / max(length, 1e-6)))
            return x0 + (x1 - x0) * local, y0 + (y1 - y0) * local, math.degrees(math.atan2(x1 - x0, y1 - y0))
        travelled += length
    return points[-1][0], points[-1][1], 0.0


def preview_units():
    road = [(-5000, 700), (-4300, 905), (-3950, 930), (-3750, 917), (-3550, 892), (-3300, 843), (-3000, 720),
            (-2750, 615), (-2500, 450), (-2350, 300), (-2000, 120), (-1600, 0), (-1300, -90), (-1100, -170),
            (-900, -192), (-700, -195), (-430, -191)]
    return {
        "assaut": [("hoplite-spartiate", 60, ("rect", (-420, -190), 270, 25, 12)),
                   ("hoplite", 140, ("rect", (-330, -188), 270, 25, 28)),
                   ("psilos", 180, ("rect", (-120, -130), 270, 40, 20)),
                   ("perse-sparabara", 2000, ("column", road, 22, 600)),
                   ("perse-archer", 1000, ("column", road[:12] + [(-1320, -84)], 30, 800))],
        "kolonos": [("hoplite-spartiate", 60, ("rect", (-25, 0), 270, 30, 20)),
                    ("hoplite", 140, ("rect", (15, 5), 90, 40, 25)),
                    ("psilos", 180, ("rect", (0, -25), 180, 40, 10)),
                    ("hoplite", 80, ("rect", (-720, -194), 270, 30, 13)),
                    ("immortel", 2000, ("rect", (90, 10), 270, 150, 40)),
                    ("perse-sparabara", 4000, ("column", [(-1480, -40), (-1100, -170), (-900, -192), (-450, -192),
                                                          (-300, -180), (-150, -165), (-90, -112)], 40, 700))],
    }


def place_preview_figures(ground, collection, units, scale):
    meshes = {kind: figures.TROOPS[kind][0]().to_mesh(f"preview_{kind}", {}, False) for kind in figures.TROOPS}
    group = new_empty("preview_figures", collection)
    positions = []
    for seed, (kind, count, formation) in enumerate(units, start=1):
        for u, v, rank, jx, jy in slots(count, formation[3] if formation[0] == "rect" else formation[2],
                                        formation[4] if formation[0] == "rect" else formation[3], seed):
            if formation[0] == "rect":
                _, (cx, cy), facing, width, depth = formation
                angle = math.radians(facing)
                along = (u - 0.5) * width
                ahead = depth * (0.5 - v)
                x = cx + math.cos(angle) * along + math.sin(angle) * ahead + jx
                y = cy - math.sin(angle) * along + math.cos(angle) * ahead + jy
                heading = facing
            else:
                _, points, width, depth = formation
                total = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(points[:-1], points[1:]))
                px, py, heading = trail_point(points, total - rank * depth)
                turn = math.radians(heading)
                lateral = (u - 0.5) * width
                x = px + math.cos(turn) * lateral + jx
                y = py - math.sin(turn) * lateral + jy
            positions.append((kind, x, y, heading))
    xs = np.array([p[1] for p in positions])
    ys = np.array([p[2] for p in positions])
    zs = ground.engine_height(xs, ys)
    for (kind, x, y, heading), z in zip(positions, zs):
        matrix = Matrix.Translation((x, y, float(z))) @ Matrix.Rotation(math.radians(-heading), 4, "Z") @ Matrix.Scale(
            scale, 4)
        new_object(f"preview_{kind}", meshes[kind], collection, group, matrix)
    return group


def look_camera(collection, name, eye, target):
    data = bpy.data.cameras.new(name)
    data.sensor_fit = "VERTICAL"
    data.angle_y = math.radians(FOV)
    data.clip_start = 0.3
    data.clip_end = 80000.0
    rig = new_object(name, data, collection)
    rig.location = eye
    rig.rotation_euler = (Vector(target) - Vector(eye)).to_track_quat("-Z", "Y").to_euler()
    return rig


def tactical_view(ground, focus, span):
    fx, fy = focus
    distance = span / (2 * math.tan(math.radians(FOV / 2)) * 1.6)
    tilt = math.radians(TACTICAL_TILT)
    fz = float(ground.sample(np.array([fx]), np.array([fy]))[0])
    return (fx, fy - math.cos(tilt) * distance, fz + math.sin(tilt) * distance), (fx, fy, fz)


def ground_view(ground, at, facing, along, across, look, turn=0.0):
    angle = math.radians(facing)
    fx, fy = math.sin(angle), math.cos(angle)
    ex = at[0] + fx * along + fy * across
    ey = at[1] + fy * along - fx * across
    heading = math.radians(facing + turn)
    tx, ty = ex + math.sin(heading) * look, ey + math.cos(heading) * look
    ez = float(ground.sample(np.array([ex]), np.array([ey]))[0]) + 1.7
    tz = float(ground.sample(np.array([tx]), np.array([ty]))[0]) + 1.4
    return (ex, ey, ez), (tx, ty, tz)


def render_previews(options, ground, collection):
    shots = {
        "tactique_attente": ("attente", 3.0, None, tactical_view(ground, (-3300, 450), 7200)),
        "tactique_assaut": ("assaut", 3.0, "assaut", tactical_view(ground, (-560, -188), 650)),
        "tactique_kolonos": ("kolonos", 3.0, "kolonos", tactical_view(ground, (-260, -80), 1000)),
        "rasante_assaut": ("assaut", 1.0, "assaut", ground_view(ground, (-420, -190), 270, -30, 8, 180)),
        "rasante_kolonos": ("kolonos", 1.0, "kolonos", ground_view(ground, (-25, 0), 270, 0, 0, 90)),
        "rasante_mer": ("attente", 1.0, None, ((-700.0, 300.0, 6.0), (-500.0, -250.0, 20.0))),
    }
    wanted = [name for name in options["previews"].split(",") if name]
    configure_render(1280, 720, int(options["samples"]))
    scene = bpy.context.scene
    scene.view_settings.view_transform = "Khronos PBR Neutral"
    scene.view_settings.look = "None"
    timings = {}
    for name in wanted:
        sun_key, scale, units, (eye, target) = shots[name]
        azimuth, elevation = SUN[sun_key]
        for world in list(bpy.data.worlds):
            bpy.data.worlds.remove(world)
        for lamp in [item for item in bpy.data.objects if item.type == "LIGHT"]:
            bpy.data.objects.remove(lamp)
        evening_world(azimuth, elevation, float(options.get("sky", 0.12)), 0.5)
        sun_lamp(collection, azimuth, elevation, float(options.get("sun", 3.2)), (1.0, 0.96, 0.9), 0.53)
        group = place_preview_figures(ground, collection, preview_units()[units], scale) if units else None
        rig = look_camera(collection, f"cam_{name}", eye, target)
        rig.data.clip_start = 20.0 if name.startswith("tactique") else 0.3
        timings[name] = round(render_still(rig, os.path.join(PREVIEWS, f"{name}.png")), 1)
        print(f"PREVIEW {name} {timings[name]} s", flush=True)
        if group is not None:
            for child in list(group.children):
                bpy.data.objects.remove(child)
            bpy.data.objects.remove(group)
    return timings


def main():
    options = arguments()
    started = time.perf_counter()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    principled_material("matte", color=(1.0, 1.0, 1.0), roughness=0.88)
    principled_material("water", color=(0.10, 0.30, 0.32), roughness=0.1, vertex_color=False)
    relief = Relief(GEO_CACHE)
    lap = lambda label: print(f"STAGE {label} {time.perf_counter() - started:.0f} s", flush=True)
    collection = ensure_collection("Thermopyles")
    root = new_empty("thermopyles", collection)
    materials = ground_materials(relief, os.path.join(CACHE, "work"), TEXTURE_SIZES)
    ground = Ground(relief)
    terrain, vertices = ground.build(materials, collection, new_object)
    terrain.parent = root
    lap("ground")
    far = far_ground(relief, ground, collection, new_object, far_material(relief, CACHE))
    far.parent = root
    lap("far")
    for water in water_surfaces(relief, ground, collection, new_object):
        water.parent = root
    lap("water")
    library = TemplateLibrary({})
    counts = {"settlements": settlements(relief, ground, library, collection, root),
              "vegetation": vegetation(relief, ground, library, collection, root)}
    lap("props")
    troops = build_troops(collection, root)
    statistics = group_statistics([root])
    lap("statistics")
    glb = os.path.join(CACHE, "thermopyles.glb")
    export_seconds = export_glb(glb, [root])
    probes = {name: float(ground.sample(np.array([x]), np.array([y]))[0]) for name, (x, y) in {
        "kolonos": (0, 0), "narrows_road": (-600, -194), "west_gate_road": (-3750, 917),
        "east_gate_road": (2700, 840), "anthela": ANTHELA, "xerxes_seat": XERXES_SEAT,
        "phocian_post": (-3000, -3400), "persian_camp": (-6300, 1200)}.items()}
    report = {
        "extent": EXTENT,
        "relief": DEM_LICENCE,
        "ground_vertices": vertices,
        "probes": probes,
        "anopaia_metres": float(np.sum(np.hypot(*np.diff(densify(chaikin(ANOPAIA), 15.0), axis=0).T))),
        "counts": counts,
        "troop_triangles": troops,
        "statistics": statistics,
        "export_seconds": export_seconds,
        "glb_bytes": os.path.getsize(glb),
    }
    if options["previews"]:
        report["previews"] = render_previews(options, ground, collection)
    report["total_seconds"] = time.perf_counter() - started
    with open(os.path.join(CACHE, "report.json"), "w", encoding="utf8") as handle:
        json.dump(report, handle, indent=1)
    print("REPORT", json.dumps({key: report[key] for key in ("ground_vertices", "probes", "counts", "glb_bytes",
                                                             "total_seconds")}), flush=True)
    print("TROOPS", json.dumps(troops), flush=True)


if __name__ == "__main__":
    main()
