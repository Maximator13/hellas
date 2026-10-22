import math
import random

from mathutils import Matrix, Vector

from . import colosse_plan as plan
from . import figures
from .acropole_life import clearance, grounded, resample, scaled
from .geometry import MeshBuilder, new_empty, new_object, placement
from .life import amphora_stack, animal

ENGINE_LENS = 24.4
QUAY_EYE = (600.0, -262.0)
SAILOR = (0.62, 0.52, 0.38)
WALKERS = ("walker_citoyen", "walker_femme-himation", "walker_porteur", "walker_marin", "walker_charpentier",
           "walker_marchand-etranger", "walker_pretre-helios", "walker_enfant", "walker_ane", "walker_mulet",
           "walker_chien")


def labourer(tunic=figures.UNDYED, skin=figures.SKIN_SUN, stride=0.0, cap=None, tool=False, sack=False):
    builder = MeshBuilder()
    figures.legs(builder, skin, stride)
    figures.skirt(builder, tunic, 1.0, 0.6, 0.18, 0.23)
    figures.torso(builder, skin)
    figures.sash(builder, tunic, depth=0.36)
    if sack:
        figures.arms(builder, (0.2, -0.02, 1.62), (-0.24, 0.1, 0.9), skin, skin)
        figures.box(builder, (0.12, -0.04, 1.6), (0.42, 0.3, 0.22), figures.LINEN)
    elif tool:
        figures.arms(builder, (0.26, 0.3, 1.1), (-0.2, 0.3, 1.02), skin, skin)
        figures.spear(builder, (0.26, 0.22, 1.0), (0.26, 0.5, 1.2), 0.02, figures.WOOD, 0.1, figures.IRON)
    else:
        figures.arms(builder, (0.28, 0.1, 0.9), (-0.26, 0.08, 0.88), skin, skin)
    figures.head(builder, skin, figures.HAIR, figures.HAIR)
    if cap is not None:
        figures.pilos(builder, cap)
    return builder


def foreign_merchant():
    builder = figures.man_himation(figures.PURPLE, figures.SKIN_SUN, figures.HAIR, figures.HAIR,
                                   right_hand=(0.3, 0.3, 1.2))
    figures.lathe(builder, [(0.11, 1.62), (0.1, 1.74), (0.05, 1.86), (0.0, 1.88)], figures.SAFFRON, 7)
    return builder


def priest_of_helios():
    builder = figures.priest(figures.WOOL_WHITE, figures.PURPLE)
    figures.wreath(builder, figures.GOLD)
    return builder


def child(stride=0.14):
    return scaled(labourer(figures.WOOL_WHITE, figures.SKIN, stride), 0.62)


VARIANTS = {
    "walker_citoyen": lambda: figures.man_himation(stride=0.16),
    "walker_femme-himation": lambda: figures.woman_peplos(figures.MADDER, figures.LINEN, stride=0.12,
                                                          veil=figures.WOOL_WHITE),
    "walker_porteur": lambda: figures.worker(figures.UNDYED, stride=0.18, carry="amphora"),
    "walker_marin": lambda: labourer(SAILOR, stride=0.18, cap=(0.5, 0.4, 0.3)),
    "walker_charpentier": lambda: labourer(figures.OLIVE, stride=0.16, tool=True),
    "walker_marchand-etranger": foreign_merchant,
    "walker_pretre-helios": priest_of_helios,
    "walker_enfant": child,
    "walker_ane": lambda: animal("donkey"),
    "walker_mulet": lambda: animal("mule"),
    "walker_chien": lambda: animal("dog"),
}

STANDING = {
    "fig_citoyen": lambda: figures.man_himation(),
    "fig_citoyen_couleur": lambda: figures.man_himation(figures.WOAD, figures.SKIN_SUN, figures.HAIR_GREY,
                                                        figures.HAIR_GREY, right_hand=(0.3, 0.3, 1.32)),
    "fig_femme": lambda: figures.woman_peplos(figures.SAFFRON, figures.MADDER, veil=figures.WOOL_WHITE),
    "fig_femme_offrande": lambda: figures.woman_peplos(figures.OLIVE, figures.LINEN, carry="hydria"),
    "fig_pretre": priest_of_helios,
    "fig_porteur": lambda: figures.worker(figures.MADDER, carry="amphora"),
    "fig_porteur_sac": lambda: labourer(figures.UNDYED, sack=True),
    "fig_marin": lambda: labourer(SAILOR, cap=(0.5, 0.4, 0.3)),
    "fig_charpentier": lambda: labourer(figures.OLIVE, tool=True),
    "fig_marchand": foreign_merchant,
    "fig_enfant": lambda: child(0.0),
    "fig_ane": lambda: animal("donkey"),
    "fig_mulet": lambda: animal("mule"),
    "fig_mouton": lambda: animal("sheep"),
    "fig_chien": lambda: animal("dog"),
    "fig_amphores": amphora_stack,
}

FAR = {
    "fig_loin_a": lambda: figures.far_infantry(figures.WOOL_WHITE, figures.WOOL_WHITE, figures.HAIR, None,
                                               spear_color=None),
    "fig_loin_b": lambda: figures.far_infantry(figures.MADDER, figures.SAFFRON, figures.HAIR, None, spear_color=None),
    "fig_loin_c": lambda: figures.far_infantry(figures.UNDYED, figures.SKIN_SUN, figures.HAIR, None, spear_color=None),
}


def statue_level(info):
    return info["colosse"]["terrace"]


def south_tower(scene):
    towers = getattr(scene, "wall_towers", [])
    if not towers:
        return (-250.0, -1520.0, scene.ground(-250.0, -1520.0) + 12.8, 0.0)
    return min(towers, key=lambda t: math.hypot(t[0] + 300.0, t[1] + 1500.0))


def points_of_interest(scene, info):
    g = scene.ground
    z = statue_level(info)
    top = info["colosse"]["statue_top"]
    points = {}

    def at(x, y, height):
        return Vector((x, y, g.surface(x, y) + height))

    points["vue-d-ensemble"] = (Vector((470.0, 600.0, 165.0)), Vector((-100.0, -140.0, z + 6.0)), ENGINE_LENS)
    points["la-legende-du-port"] = (Vector((305.0, 742.0, 4.5)), Vector((40.0, 60.0, z + 30.0)), ENGINE_LENS)
    points["port-militaire"] = (Vector((262.0, 585.0, 6.0)), Vector((185.0, 250.0, 3.0)), ENGINE_LENS)
    px, py = on_land(scene, *QUAY_EYE, 1.0)
    points["grand-port"] = (Vector((px, py, lifted(scene, px, py) + 1.8)), Vector((60.0, 130.0, z + 16.0)),
                            ENGINE_LENS)
    points["ville-hippodamienne"] = (at(0.0, -430.0, 1.7), Vector((0.0, 0.0, top - 12.0)), ENGINE_LENS)
    eye = colossus_eye()
    points["colosse"] = (Vector((eye[0], eye[1], z + 16.0)), Vector((0.0, 0.0, z + 20.0)), ENGINE_LENS)
    ax, ay = plan.APOLLO
    points["acropole"] = (at(ax + 24.0, ay + 34.0, 4.0), Vector((0.0, 0.0, top - 14.0)), ENGINE_LENS)
    tx, ty, tz, angle = south_tower(scene)
    along = Vector((math.cos(angle), math.sin(angle), 0.0))
    outward = Vector((along.y, -along.x, 0.0))
    aim = Vector((tx, ty, 0.0)) + along * 260.0 + outward * 220.0
    eye = Vector((tx, ty, 0.0)) - outward * 35.0 - along * 60.0
    points["murailles-et-siege"] = (Vector((eye.x, eye.y, tz + 9.0)), Vector((aim.x, aim.y, g(aim.x, aim.y) + 2.0)),
                                    ENGINE_LENS)
    points["la-chute"] = (Vector((-150.0, -110.0, z + 24.0)), Vector((0.0, 0.0, z + 22.0)), ENGINE_LENS)
    return points


def colossus_eye():
    return plan.to_world(plan.STATUE, plan.STATUE_AZIMUTH + 22.0, 0.0, 108.0)


def eye_points():
    return [colossus_eye(), (305.0, 742.0), (262.0, 585.0), QUAY_EYE, (0.0, -430.0),
            (plan.APOLLO[0] + 24.0, plan.APOLLO[1] + 34.0), (-150.0, -110.0)]


def place_markers(scene, points):
    root = scene.root("markers")
    for key, (eye, target, _) in points.items():
        new_empty(f"poi_{key}", scene.collection, root, Matrix.Translation(eye))
        new_empty(f"poi_{key}_target", scene.collection, root, Matrix.Translation(target))


def ring(centre, radius, count, start=0.0):
    return [(centre[0] + radius * math.cos(start + math.tau * k / count),
             centre[1] + radius * math.sin(start + math.tau * k / count)) for k in range(count + 1)]


def routes():
    ax, ay = plan.APOLLO
    return {
        "grand_port": [(440.0, -170.0), (470.0, -268.0), (560.0, -280.0),
                       (650.0, -270.0), (695.0, -200.0), (700.0, -100.0), (700.0, 40.0)],
        "mandraki": [(297.0, 190.0), (313.0, 300.0), (325.0, 450.0), (335.0, 600.0)],
        "rue": [(0.0, -560.0), (0.0, -420.0), (0.0, -300.0), (0.0, -180.0), (0.0, -90.0), (4.0, -62.0)],
        "colosse": ring((0.0, 0.0), 13.5, 36, math.radians(90.0 - plan.STATUE_AZIMUTH))
        + [plan.to_world(plan.STATUE, plan.STATUE_AZIMUTH, 3.0, 19.0)],
        "acropole": ring((ax, ay + 4.0), 17.0, 20),
    }


def lifted(scene, x, y):
    return scene.ground.surface(x, y, hint=max(scene.ground(x, y), 0.0))


def on_land(scene, x, y, floor=0.8):
    if lifted(scene, x, y) >= floor:
        return x, y
    for radius in range(2, 60, 2):
        for k in range(16):
            px = x + radius * math.cos(math.tau * k / 16)
            py = y + radius * math.sin(math.tau * k / 16)
            if lifted(scene, px, py) >= floor:
                return px, py
    return x, y


def place_routes(scene, info):
    root = scene.root("life")
    counts = {}
    for name, points in routes().items():
        snapped = points
        for _ in range(3):
            snapped = resample([on_land(scene, x, y) for x, y in snapped], 2.5)
        snapped = [(x, y) for x, y in snapped if lifted(scene, x, y) >= 0.8]
        refined = [Vector((x, y, lifted(scene, x, y))) for x, y in snapped]
        for index, point in enumerate(refined):
            new_empty(f"walk_{name}_{index:02d}", scene.collection, root, Matrix.Translation(point))
        counts[name] = len(refined)
        counts[f"{name}_max_step"] = round(max((b - a).length for a, b in zip(refined[:-1], refined[1:])), 2)
        counts[f"{name}_lowest"] = round(min(p.z for p in refined), 2)
        worst = max(zip(refined[:-1], refined[1:]), key=lambda pair: (pair[1] - pair[0]).length)
        counts[f"{name}_worst"] = [round(v, 1) for v in worst[0]]
    return counts


def build_walkers(scene):
    root = scene.root("life")
    report = {}
    for index, key in enumerate(WALKERS):
        build = VARIANTS[key]
        mesh = scene.library.mesh(key, lambda build=build: grounded(build()), ground_occlusion=False)
        lowest = min(v.co.z for v in mesh.vertices)
        assert abs(lowest) < 1e-4, (key, lowest)
        created = new_object(key, mesh, scene.collection, root, placement(9000.0 + index * 3.0, 9000.0, 0.0))
        created["cast_shadow"] = True
        report[key] = scene.library.builders[key].triangle_count()
    return report


def facing(point):
    return lambda x, y: math.atan2(-(point[0] - x), point[1] - y)


def crowd(scene, rng, placed, key, count, centre, radius, face=None, land=0.95, avoid=()):
    done = 0
    attempts = 0
    while done < count and attempts < count * 60:
        attempts += 1
        x = centre[0] + rng.uniform(-radius, radius)
        y = centre[1] + rng.uniform(-radius, radius)
        if any(math.hypot(x - px, y - py) < 1.0 for px, py in placed):
            continue
        if any(math.hypot(x - ax, y - ay) < r for (ax, ay), r in avoid):
            continue
        z = scene.ground.surface(x, y)
        if z < land:
            continue
        heading = face(x, y) if face else rng.uniform(0, 2 * math.pi)
        placed.append((x, y))
        scene.placements.setdefault(key, []).append(placement(x, y, z, heading + rng.uniform(-0.4, 0.4)))
        done += 1
    return done


def build_figures(scene, info):
    rng = random.Random(432)
    placed = []
    scene.placements = {}
    counts = {}
    altar = info["sanctuaire"]["altar"]
    statue = (0.0, 0.0)
    base = [((0.0, 0.0), 9.8)]
    counts["autel"] = crowd(scene, rng, placed, "fig_pretre", 1, (altar[0] - 3.0, altar[1] - 3.0), 1.0,
                            face=facing(altar))
    counts["autel"] += crowd(scene, rng, placed, "fig_femme_offrande", 4, (altar[0] - 4.0, altar[1] - 6.0), 3.5,
                             face=facing(altar))
    counts["autel"] += crowd(scene, rng, placed, "fig_mouton", 3, (altar[0] - 2.0, altar[1] - 7.0), 2.5)
    counts["colosse"] = 0
    for key, count in (("fig_citoyen", 9), ("fig_femme", 6), ("fig_marchand", 5), ("fig_citoyen_couleur", 6),
                       ("fig_enfant", 3)):
        counts["colosse"] += crowd(scene, rng, placed, key, count, statue, 30.0, face=facing(statue), avoid=base)
    port = []
    for key, count in (("fig_porteur", 28), ("fig_porteur_sac", 22), ("fig_marchand", 14), ("fig_citoyen", 14),
                       ("fig_marin", 16), ("fig_ane", 8), ("fig_mulet", 6), ("fig_chien", 3), ("fig_amphores", 16)):
        port.append(crowd(scene, rng, placed, key, count, (520.0, -60.0), 230.0, land=0.9))
    for key, count in (("fig_porteur", 10), ("fig_amphores", 8), ("fig_porteur_sac", 8), ("fig_marchand", 4),
                       ("fig_ane", 3)):
        port.append(crowd(scene, rng, placed, key, count, (QUAY_EYE[0] - 30.0, QUAY_EYE[1] + 5.0), 30.0, land=0.9,
                          avoid=[(QUAY_EYE, 12.0)]))
    counts["grand_port"] = sum(port)
    mandraki = []
    for key, count in (("fig_charpentier", 22), ("fig_marin", 22), ("fig_citoyen", 6), ("fig_porteur_sac", 6)):
        mandraki.append(crowd(scene, rng, placed, key, count, (215.0, 380.0), 140.0, land=0.9))
    counts["mandraki"] = sum(mandraki)
    counts["agora"] = 0
    ax, ay, _ = info["agora"]["centre"]
    for key, count in (("fig_citoyen", 14), ("fig_femme", 10), ("fig_citoyen_couleur", 8), ("fig_marchand", 6),
                       ("fig_ane", 3)):
        counts["agora"] += crowd(scene, rng, placed, key, count, (ax, ay), 50.0)
    px, py = plan.APOLLO
    counts["acropole"] = 0
    for key, count in (("fig_citoyen", 6), ("fig_femme", 4), ("fig_pretre", 1), ("fig_mouton", 2)):
        counts["acropole"] += crowd(scene, rng, placed, key, count, (px, py + 10.0), 22.0)
    far = list(FAR)
    city = 0
    for k in range(900):
        if city >= 260:
            break
        x = rng.uniform(-1200.0, 900.0)
        y = rng.uniform(-1300.0, 700.0)
        if rng.random() < 0.5:
            x = 30.0 * round(x / 30.0)
        else:
            y = 30.0 * round(y / 30.0)
        if math.hypot(x, y) < 90.0 or scene.ground(x, y) < 2.0:
            continue
        scene.placements.setdefault(far[k % 3], []).append(placement(x, y, scene.ground.surface(x, y),
                                                                     rng.uniform(0, 6.28)))
        city += 1
    counts["ville"] = city
    builds = {**STANDING, **FAR}
    for key, matrices in scene.placements.items():
        shadow = key not in FAR and key != "fig_amphores"
        scene.instances("figurants", key, lambda key=key: grounded(builds[key]()), matrices, cast_shadow=shadow,
                        occlusion=False)
    return counts


def build(scene, info):
    report = {"routes": place_routes(scene, info), "walkers": build_walkers(scene),
              "figures": build_figures(scene, info)}
    root = scene.root("life")
    g = scene.ground
    altar = info["sanctuaire"]["altar"]
    smokes = [[altar[0], altar[1], altar[2] + 0.4]]
    for x, y, lift in ((-420.0, -1050.0, 4.0), (620.0, -560.0, 4.0), (240.0, 225.0, 3.0), (-520.0, -260.0, 6.0),
                       (380.0, -820.0, 6.0), (-180.0, 420.0, 6.0), (-900.0, -150.0, 6.0)):
        smokes.append([x, y, g(x, y) + lift])
    for index, point in enumerate(smokes, start=1):
        new_empty(f"smoke_{index}", scene.collection, root, Matrix.Translation(point))
    top = info["colosse"]["statue_top"]
    birds = [(520.0, 120.0, 45.0), (250.0, 520.0, 40.0), (14.0, 22.0, top + 6.0)]
    for index, point in enumerate(birds, start=1):
        new_empty(f"birds_{index}", scene.collection, root, Matrix.Translation(point))
    report["smoke"] = len(smokes)
    report["birds"] = len(birds)
    return report


def preview_views(points, info):
    views = dict(points)
    top = info["colosse"]["statue_top"]
    face = Vector(info["colosse"]["face"])
    views["visage"] = (face + Vector((10.0, 22.0, 2.0)), face, 35.0)
    views["statue-loin"] = (Vector((180.0, 260.0, 60.0)), Vector((0.0, 0.0, top - 20.0)), 30.0)
    return views
