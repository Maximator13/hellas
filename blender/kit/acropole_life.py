import math
import random

from mathutils import Matrix, Vector

from . import acropole_monuments as monuments
from . import acropole_plan as plan
from . import figures
from .geometry import MeshBuilder, new_empty, new_object, placement
from .life import animal
from .stage import sun_vector

EYES = {
    "vue-d-ensemble": (700.0, 300.0),
    "agora": (-250.0, 250.0),
    "propylees": (-60.0, 5.0),
    "parthenon": (51.9, 51.0),
    "athena-de-bronze": (-103.5, 21.0),
    "vieux-temple-et-olivier": (14.0, 68.0),
    "pente-sud": (90.0, -55.0),
    "pnyx-et-meton": (-660.0, -30.0),
}


ENGINE_LENS = 24.4


def eye_points():
    return list(EYES.values())


def propylaea_point(u, v):
    return plan.to_world(monuments.PROPYLAEA, plan.PROPYLAEA_AZIMUTH, u, v)


def parthenon_point(u, v):
    return plan.to_world(monuments.PARTHENON, plan.PARTHENON_AZIMUTH, u, v)


def routes():
    ramp_foot = (monuments.RAMP[0], monuments.RAMP[1])
    hx, hy = monuments.HELIOTROPION
    return {
        "rampe": [(-146.0, 194.0), (-180.0, 125.0), (-222.0, 62.0), (-240.0, 22.0), ramp_foot, propylaea_point(0.0, 60.0),
                  propylaea_point(0.0, 21.0), propylaea_point(0.0, 17.5), propylaea_point(0.0, 12.0),
                  propylaea_point(0.0, 0.0), propylaea_point(0.0, -4.5), propylaea_point(0.0, -12.0),
                  propylaea_point(0.0, -17.5), propylaea_point(0.0, -24.0)],
        "plateau": [propylaea_point(0.0, -24.0), (-95.0, 19.0), (-81.0, 22.0), parthenon_point(-21.5, -38.0),
                    parthenon_point(-21.5, 30.0), (16.0, 37.0)],
        "agora": [(-520.0, 640.0), (-450.0, 600.0), (-400.0, 560.0), (-320.0, 470.0), (-262.0, 368.0)],
        "pnyx": [(hx + 5.0 * math.cos(a), hy + 5.0 * math.sin(a)) for a in [k * math.pi / 5 for k in range(11)]],
        "chantier": [propylaea_point(3.0, -24.0), (-70.0, -4.0), parthenon_point(21.5, -40.0),
                     parthenon_point(21.5, 40.0), (112.0, -6.0)],
    }


def resample(points, spacing=2.6):
    out = [points[0]]
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        count = max(int(math.ceil(math.hypot(x1 - x0, y1 - y0) / spacing - 1e-6)), 1)
        for k in range(1, count + 1):
            out.append((x0 + (x1 - x0) * k / count, y0 + (y1 - y0) * k / count))
    return out


def segment_distance(point, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = max(0.0, min(1.0, ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / max(dx * dx + dy * dy, 1e-9)))
    return math.hypot(point[0] - a[0] - t * dx, point[1] - a[1] - t * dy)


def clear_of_routes(x, y, radius):
    for points in routes().values():
        for a, b in zip(points[:-1], points[1:]):
            if segment_distance((x, y), a, b) < radius + 1.0:
                return False
    return away_from_eyes(x, y, radius)


def away_from_eyes(x, y, radius, clearance=8.5):
    return all(math.hypot(x - ex, y - ey) > radius + clearance for ex, ey in EYES.values())


def points_of_interest(scene, info):
    g = scene.ground
    acro = info.get("acropole", {})
    points = {}

    def at(x, y, height):
        return Vector((x, y, g.surface(x, y) + height))
    points["vue-d-ensemble"] = (Vector((700.0, 300.0, 450.0)), Vector((-400.0, -200.0, g(-400.0, -200.0))), ENGINE_LENS)
    hephaisteion = info.get("agora", {}).get("hephaisteion", {}).get("top", [-453.0, 449.0, g(-453.0, 449.0) + 9.0])
    points["agora"] = (at(-250.0, 250.0, 40.0), Vector(hephaisteion) - Vector((0.0, 0.0, 3.0)), ENGINE_LENS)
    base = monuments.PROPYLAEA_LEVEL
    east = propylaea_point(0.0, -12.0)
    points["propylees"] = (at(-60.0, 5.0, 1.7), Vector((east[0], east[1], base + 6.0)), ENGINE_LENS)
    statue_base = g(*monuments.PROMACHOS)
    points["athena-de-bronze"] = (at(*EYES["athena-de-bronze"], 1.7),
                                  Vector((*monuments.PROMACHOS, statue_base + 6.0)), ENGINE_LENS)
    temple = acro.get("parthenon")
    points["parthenon"] = (at(*EYES["parthenon"], 1.7), Vector((0.0, 0.0, monuments.PARTHENON_LEVEL + 9.0)),
                           ENGINE_LENS)
    if temple:
        naos = [Vector(p) for p in temple["naos"]]
        axis = (naos[1] - naos[0]).normalized()
        eye = naos[1] - axis * 6.0 + Vector((0.0, 0.0, 1.7))
        points["athena-parthenos"] = (eye, Vector(temple["statue_face"]) - Vector((0.0, 0.0, 2.5)), ENGINE_LENS)
    olive = acro.get("nord", {}).get("olive", [-28.0, 56.0, g(-28.0, 56.0) + 3.0])
    points["vieux-temple-et-olivier"] = (at(14.0, 68.0, 1.7), Vector(olive) + Vector((4.0, -6.0, 1.5)), ENGINE_LENS)
    wall_top = monuments.acropolis_level(90.0, -37.0) + 1.3
    points["pente-sud"] = (Vector((90.0, -55.0, wall_top + 3.0)), Vector((142.0, -127.0, g(142.0, -127.0) + 4.0)),
                          ENGINE_LENS)
    points["pnyx-et-meton"] = (at(-660.0, -30.0, 1.7), Vector((0.0, 0.0, g(0.0, 0.0) + 12.0)), ENGINE_LENS)
    return points


def clearance(points, reach=8.0, count=240):
    import bpy
    depsgraph = bpy.context.evaluated_depsgraph_get()
    report = {}
    golden = math.pi * (3.0 - math.sqrt(5.0))
    for key, (eye, _, _) in points.items():
        nearest, what = reach, None
        for k in range(count):
            z = 1.0 - 1.15 * k / (count - 1)
            radius = math.sqrt(max(1.0 - z * z, 0.0))
            direction = Vector((math.cos(golden * k) * radius, math.sin(golden * k) * radius, z))
            hit, location, _, _, obj, _ = bpy.context.scene.ray_cast(depsgraph, eye, direction, distance=reach)
            if hit and (location - eye).length < nearest:
                nearest, what = (location - eye).length, obj.name
        report[key] = {"nearest": round(nearest, 2), "object": what}
    return report


def place_markers(scene, points):
    root = scene.root("markers")
    for key, (eye, target, _) in points.items():
        new_empty(f"poi_{key}", scene.collection, root, Matrix.Translation(eye))
        new_empty(f"poi_{key}_target", scene.collection, root, Matrix.Translation(target))


def interior(scene, info):
    temple = info.get("acropole", {}).get("parthenon")
    if not temple:
        return {}
    root = scene.root("markers")
    sun = sun_vector(*plan.SUN)
    door = Vector(temple["door_centre"])
    floor = temple["floor"]
    entry = Vector((door.x, door.y, floor + 3.0))
    distance = (entry.z - floor) / sun.z
    target = entry - sun * distance
    oculus = entry + sun * 14.0
    new_empty("oculus", scene.collection, root, Matrix.Translation(oculus))
    new_empty("sunbeam_target", scene.collection, root, Matrix.Translation(target))
    naos = [Vector(p) for p in temple["naos"]]
    centre = (naos[0] + naos[1]) / 2 + Vector((0.0, 0.0, 7.0))
    marker = new_empty("interior", scene.collection, root, Matrix.Translation(centre))
    marker["radius"] = 16.0
    marker["height"] = 14.0
    marker["ambientScale"] = 0.25
    marker["lightShaftRadius"] = 2.4
    pool = Vector(temple["pool_front"])
    return {"oculus": [round(v, 2) for v in oculus], "sunbeam_target": [round(v, 2) for v in target],
            "beam_from_door": round((target - entry).length, 2),
            "target_before_pool": round((pool - target).dot((naos[1] - naos[0]).normalized()), 2),
            "interior": [round(v, 2) for v in centre]}


def refine(scene, a, b, depth=0):
    if (b - a).length <= 2.8 or depth > 6:
        return [b]
    middle = (a + b) / 2
    middle.z = scene.ground.surface(middle.x, middle.y)
    return refine(scene, a, middle, depth + 1) + refine(scene, middle, b, depth + 1)


def place_routes(scene):
    root = scene.root("life")
    counts = {}
    for name, points in routes().items():
        lifted = [Vector((x, y, scene.ground.surface(x, y))) for x, y in resample(points)]
        refined = [lifted[0]]
        for a, b in zip(lifted[:-1], lifted[1:]):
            refined.extend(refine(scene, a, b))
        for index, point in enumerate(refined):
            new_empty(f"walk_{name}_{index:02d}", scene.collection, root, Matrix.Translation(point))
        counts[name] = len(refined)
        counts[f"{name}_max_step"] = round(max((b - a).length for a, b in zip(refined[:-1], refined[1:])), 2)
    return counts


def grounded(builder):
    lowest = min(p[2] for p in builder.positions)
    shifted = MeshBuilder()
    shifted.merge(builder, Matrix.Translation((0.0, 0.0, -lowest)))
    return shifted


def scaled(builder, factor):
    result = MeshBuilder()
    result.merge(builder, Matrix.Scale(factor, 4))
    return result


def scythian_archer():
    builder = MeshBuilder()
    trousers = (0.62, 0.28, 0.20)
    figures.legs(builder, trousers, 0.16, trousers, (0.25, 0.30, 0.42), figures.LEATHER)
    figures.skirt(builder, (0.30, 0.38, 0.52), 1.0, 0.7, 0.18, 0.23)
    figures.torso(builder, (0.30, 0.38, 0.52))
    figures.arms(builder, (0.26, 0.1, 0.92), (-0.12, 0.45, 1.3), (0.62, 0.28, 0.20), figures.SKIN, True)
    figures.head(builder, figures.SKIN, figures.HAIR, figures.HAIR)
    figures.lathe(builder, [(0.11, 1.6), (0.09, 1.72), (0.03, 1.9), (0.0, 1.95)], (0.62, 0.28, 0.20), 6)
    figures.bow(builder, (-0.12, 0.5, 1.3), 0.9, 0.12)
    figures.gorytos(builder, figures.LEATHER, (-0.24, -0.05, 0.9))
    return builder


def child():
    builder = figures.worker(figures.WOOL_WHITE, figures.SKIN, figures.HAIR, 0.14)
    return scaled(builder, 0.62)


WALKERS = {
    "walker_citoyen": lambda: figures.man_himation(stride=0.16),
    "walker_femme-peplos": lambda: figures.woman_peplos(figures.SAFFRON, figures.MADDER, stride=0.12),
    "walker_femme-chiton": lambda: figures.woman_peplos((0.86, 0.84, 0.78), figures.WOAD, stride=0.12,
                                                        veil=figures.MADDER),
    "walker_ouvrier": lambda: figures.worker(figures.OLIVE, stride=0.2),
    "walker_esclave-porteur": lambda: figures.worker(figures.UNDYED, figures.SKIN_SUN, stride=0.18, carry="amphora"),
    "walker_pretresse": lambda: figures.woman_peplos(figures.WOOL_WHITE, figures.SAFFRON, stride=0.1,
                                                     veil=figures.WOOL_WHITE),
    "walker_arrhephore": lambda: scaled(figures.woman_peplos(figures.WOOL_WHITE, figures.WOOL_WHITE, stride=0.1), 0.74),
    "walker_archer-scythe": scythian_archer,
    "walker_enfant": child,
    "walker_boeuf": lambda: animal("ox"),
    "walker_brebis": lambda: animal("sheep"),
}

STANDING = {
    "fig_citoyen": lambda: figures.man_himation(),
    "fig_citoyen_couleur": lambda: figures.man_himation(figures.WOAD, figures.SKIN_SUN, figures.HAIR_GREY,
                                                        figures.HAIR_GREY, right_hand=(0.3, 0.3, 1.32)),
    "fig_femme": lambda: figures.woman_peplos(),
    "fig_femme_offrande": lambda: figures.woman_peplos(figures.OLIVE, figures.LINEN, carry="hydria"),
    "fig_pretresse": lambda: figures.woman_peplos(figures.WOOL_WHITE, figures.SAFFRON, veil=figures.WOOL_WHITE),
    "fig_pretre": lambda: figures.priest(),
    "fig_ouvrier": lambda: figures.worker(),
    "fig_ouvrier_porteur": lambda: figures.worker(figures.MADDER, carry="amphora"),
    "fig_arrhephore": lambda: scaled(figures.woman_peplos(figures.WOOL_WHITE, figures.WOOL_WHITE), 0.74),
    "fig_archer": scythian_archer,
    "fig_brebis": lambda: animal("sheep"),
    "fig_boeuf": lambda: animal("ox"),
}

FAR = {
    "fig_loin_a": lambda: figures.far_infantry(figures.WOOL_WHITE, figures.WOOL_WHITE, figures.HAIR, None,
                                               spear_color=None),
    "fig_loin_b": lambda: figures.far_infantry(figures.MADDER, figures.SAFFRON, figures.HAIR, None, spear_color=None),
    "fig_loin_c": lambda: figures.far_infantry(figures.UNDYED, figures.SKIN_SUN, figures.HAIR, None, spear_color=None),
}


def build_walkers(scene):
    root = scene.root("life")
    report = {}
    for index, (key, build) in enumerate(WALKERS.items()):
        mesh = scene.library.mesh(key, lambda build=build: grounded(build()), ground_occlusion=False)
        lowest = min(v.co.z for v in mesh.vertices)
        assert abs(lowest) < 1e-4, (key, lowest)
        created = new_object(key, mesh, scene.collection, root, placement(9000.0 + index * 3.0, 9000.0, 0.0))
        created["cast_shadow"] = True
        report[key] = scene.library.builders[key].triangle_count()
    return report


def crowd(scene, rng, placed, key, count, centre, radius, z_of=None, face=None, check=True):
    done = 0
    attempts = 0
    while done < count and attempts < count * 40:
        attempts += 1
        x = centre[0] + rng.uniform(-radius, radius)
        y = centre[1] + rng.uniform(-radius, radius)
        if check and not clear_of_routes(x, y, 0.4):
            continue
        if any(math.hypot(x - px, y - py) < 0.9 for px, py in placed):
            continue
        z = z_of(x, y) if z_of else scene.ground.surface(x, y)
        heading = face(x, y) if face else rng.uniform(0, 2 * math.pi)
        placed.append((x, y))
        scene.placements.setdefault(key, []).append(placement(x, y, z, heading + rng.uniform(-0.4, 0.4)))
        done += 1
    return done


def facing(point):
    return lambda x, y: math.atan2(-(point[0] - x), point[1] - y)


def build_figures(scene, info):
    rng = random.Random(432)
    placed = []
    scene.placements = {}
    counts = {}
    workers = ("fig_ouvrier", "fig_ouvrier_porteur")
    for k, (u, v, radius, count) in enumerate(((0.0, -22.0, 9.0, 10), (13.0, -26.0, 5.0, 5), (-14.0, -20.0, 5.0, 6),
                                               (18.0, 8.0, 5.0, 3))):
        centre = propylaea_point(u, v)
        for index in range(count):
            crowd(scene, rng, placed, workers[index % 2], 1, centre, radius)
    counts["chantier"] = 24
    workshop = monuments.WORKSHOP
    counts["atelier"] = crowd(scene, rng, placed, "fig_ouvrier", 5, workshop, 7.0, face=facing(workshop))
    altar = monuments.GREAT_ALTAR
    counts["autel"] = crowd(scene, rng, placed, "fig_pretresse", 2, (altar[0] - 3.0, altar[1] - 6.0), 2.0,
                            face=facing(altar))
    counts["autel"] += crowd(scene, rng, placed, "fig_femme_offrande", 4, (altar[0] - 6.0, altar[1] - 7.0), 4.0,
                             face=facing(altar))
    counts["autel"] += crowd(scene, rng, placed, "fig_citoyen", 5, (altar[0] - 8.0, altar[1] - 9.0), 6.0,
                             face=facing(altar))
    counts["autel"] += crowd(scene, rng, placed, "fig_brebis", 2, (altar[0] - 4.0, altar[1] - 8.0), 2.0)
    zeus = monuments.ZEUS_POLIEUS
    counts["zeus"] = crowd(scene, rng, placed, "fig_pretre", 1, (zeus[0], zeus[1] - 6.0), 1.0, face=facing(zeus))
    arrephorion = monuments.ARREPHORION
    counts["arrhephores"] = crowd(scene, rng, placed, "fig_arrhephore", 2, (arrephorion[0] + 4.0, arrephorion[1] - 9.0),
                                  2.0)
    old = monuments.OLD_TEMPLE
    west_door = plan.to_world(old, plan.PARTHENON_AZIMUTH, 0.0, -24.0)
    counts["tresoriers"] = crowd(scene, rng, placed, "fig_citoyen_couleur", 3, west_door, 3.0, face=facing(old))
    for key, count, centre, radius in (("fig_citoyen", 10, (-40.0, 20.0), 30.0), ("fig_femme", 6, (-30.0, 12.0), 30.0),
                                       ("fig_citoyen_couleur", 6, (50.0, 10.0), 14.0),
                                       ("fig_femme", 4, (52.0, 4.0), 10.0), ("fig_citoyen", 4, (-75.0, 20.0), 10.0),
                                       ("fig_archer", 2, propylaea_point(4.5, -15.0), 1.5),
                                       ("fig_citoyen", 3, propylaea_point(4.0, 16.0), 3.0)):
        counts.setdefault("plateau", 0)
        counts["plateau"] += crowd(scene, rng, placed, key, count, centre, radius)
    temple = info.get("acropole", {}).get("parthenon")
    if temple:
        naos = [Vector(p) for p in temple["naos"]]
        axis = (naos[1] - naos[0]).normalized()
        side = Vector((axis.y, -axis.x, 0.0))
        floor = temple["floor"]
        statue = Vector(temple["statue"])
        for k, (key, along, across) in enumerate((("fig_pretresse", 12.0, 3.5), ("fig_citoyen", 9.0, -4.0),
                                                   ("fig_citoyen_couleur", 16.5, 6.0))):
            point = naos[0] + axis * along + side * across
            heading = math.atan2(-(statue.x - point.x), statue.y - point.y)
            scene.placements.setdefault(key, []).append(placement(point.x, point.y, floor, heading))
        counts["cella"] = 3
    for key, count, centre, radius in (("fig_citoyen", 8, (-175.0, 140.0), 18.0), ("fig_femme", 6, (-205.0, 85.0), 16.0),
                                       ("fig_citoyen_couleur", 5, (-232.0, 40.0), 10.0),
                                       ("fig_ouvrier_porteur", 4, (-190.0, 115.0), 14.0),
                                       ("fig_boeuf", 2, (-238.0, 60.0), 8.0)):
        counts.setdefault("rampe", 0)
        counts["rampe"] += crowd(scene, rng, placed, key, count, centre, radius)
    hx, hy = monuments.HELIOTROPION
    counts["pnyx"] = crowd(scene, rng, placed, "fig_citoyen", 3, (hx + 2.0, hy + 9.0), 2.5,
                           face=facing(monuments.HELIOTROPION))
    counts["pnyx"] += crowd(scene, rng, placed, "fig_citoyen_couleur", 1, (hx - 4.0, hy + 4.0), 1.0,
                            face=facing(monuments.HELIOTROPION))
    far = list(FAR)
    agora = 0
    for k in range(220):
        x = rng.uniform(-385.0, -255.0)
        y = rng.uniform(345.0, 520.0)
        if not clear_of_routes(x, y, 0.3):
            continue
        scene.placements.setdefault(far[k % 3], []).append(placement(x, y, scene.ground.surface(x, y),
                                                                     rng.uniform(0, 6.28)))
        agora += 1
    counts["agora"] = agora
    builds = {**STANDING, **FAR}
    for key, matrices in scene.placements.items():
        shadow = key not in FAR
        scene.instances("figurants", key, lambda key=key: grounded(builds[key]()), matrices, cast_shadow=shadow,
                        occlusion=False)
    return counts


def build(scene, info):
    report = {"routes": place_routes(scene), "walkers": build_walkers(scene), "figures": build_figures(scene, info),
              "interior": interior(scene, info)}
    acro = info.get("acropole", {})
    nord = acro.get("nord", {})
    root = scene.root("life")
    g = scene.ground
    smokes = [nord.get("altar", [*monuments.GREAT_ALTAR, g(*monuments.GREAT_ALTAR) + 2.5]),
              nord.get("zeus_altar", [*monuments.ZEUS_POLIEUS, g(*monuments.ZEUS_POLIEUS) + 2.0])]
    for x, y, lift in ((-488.0, 418.0, 3.0), (-480.0, 482.0, 3.0), (-770.0, 795.0, 4.0), (310.0, 690.0, 6.0),
                       (-700.0, 300.0, 6.0), (620.0, -80.0, 6.0), (-260.0, -620.0, 6.0)):
        smokes.append([x, y, g(x, y) + lift])
    for index, point in enumerate(smokes, start=1):
        new_empty(f"smoke_{index}", scene.collection, root, Matrix.Translation(point))
    birds = [(0.0, 0.0, 192.0), (-110.0, 40.0, 178.0), (-330.0, 450.0, 112.0), (70.0, -62.0, 150.0)]
    for index, point in enumerate(birds, start=1):
        new_empty(f"birds_{index}", scene.collection, root, Matrix.Translation(point))
    report["smoke"] = len(smokes)
    report["birds"] = len(birds)
    return report


def preview_views(points):
    views = dict(points)
    views["acropole-ouest"] = (Vector((-420.0, 60.0, 190.0)), Vector((-40.0, 10.0, 150.0)), 30.0)
    return views
