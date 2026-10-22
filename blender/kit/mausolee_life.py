import math
import random

from mathutils import Matrix, Vector

from . import figures
from . import mausolee_plan as plan
from .acropole_life import clearance, grounded, resample
from .colosse_life import FAR, STANDING, child, labourer, lifted, on_land
from .geometry import MeshBuilder, new_empty, new_object, placement
from .life import animal, pack_animal

ENGINE_LENS = 24.4
SAILOR = (0.62, 0.52, 0.38)
WALKERS = ("walker_citoyen", "walker_femme-chiton", "walker_femme-voilee", "walker_ouvrier", "walker_marin",
           "walker_porteur", "walker_mercenaire", "walker_perse", "walker_enfant", "walker_ane", "walker_mulet-bate",
           "walker_boeuf", "walker_chien")


def mercenary(stride=0.0):
    builder = labourer(figures.WOOL_WHITE, figures.SKIN_SUN, stride, cap=figures.BRONZE)
    figures.sash(builder, figures.OLIVE, depth=0.4)
    figures.spear(builder, (0.28, 0.12, 0.05), (0.28, 0.14, 2.45), 0.016)
    return builder


def persian(stride=0.0):
    builder = MeshBuilder()
    figures.persian_body(builder, figures.MADDER, figures.WOAD, figures.SAFFRON, figures.MADDER, figures.UNDYED,
                         (0.26, 0.1, 0.9), (-0.26, 0.08, 0.9), 0.5)
    return builder


VARIANTS = {
    "walker_citoyen": lambda: figures.man_himation(stride=0.16),
    "walker_femme-chiton": lambda: figures.woman_peplos(figures.MADDER, figures.LINEN, stride=0.12),
    "walker_femme-voilee": lambda: figures.woman_peplos(figures.SAFFRON, figures.MADDER, stride=0.12,
                                                        veil=figures.WOOL_WHITE),
    "walker_ouvrier": lambda: labourer(figures.UNDYED, stride=0.18, tool=True, cap=(0.6, 0.5, 0.34)),
    "walker_marin": lambda: labourer(SAILOR, stride=0.18, cap=(0.5, 0.4, 0.3)),
    "walker_porteur": lambda: figures.worker(figures.UNDYED, stride=0.18, carry="amphora"),
    "walker_mercenaire": lambda: mercenary(0.16),
    "walker_perse": lambda: persian(),
    "walker_enfant": child,
    "walker_ane": lambda: animal("donkey"),
    "walker_mulet-bate": lambda: pack_animal("mule"),
    "walker_boeuf": lambda: animal("ox"),
    "walker_chien": lambda: animal("dog"),
}

EXTRA = {
    "fig_mercenaire": lambda: mercenary(),
    "fig_perse": persian,
    "fig_ouvrier": lambda: labourer(figures.UNDYED, tool=True, cap=(0.6, 0.5, 0.34)),
    "fig_tailleur": lambda: labourer(figures.UNDYED, sack=True),
    "fig_puiseuse": lambda: figures.woman_peplos(figures.OLIVE, figures.LINEN, carry="hydria"),
    "fig_boeuf": lambda: animal("ox"),
    "fig_chevre": lambda: animal("goat"),
}


def ground_eye(scene, x, y, height):
    return Vector((x, y, scene.ground.surface(x, y) + height))


def sea_point(scene, start, toward, step=4.0, reach=400.0):
    x, y = start
    dx, dy = toward[0] - x, toward[1] - y
    length = math.hypot(dx, dy)
    for k in range(int(reach / step)):
        px, py = x - dx / length * k * step, y - dy / length * k * step
        if all(scene.ground(px + ox, py + oy) < -1.0 for ox, oy in ((0, 0), (6, 0), (-6, 0), (0, 6), (0, -6))):
            return px, py
    return x, y


def points_of_interest(scene, info):
    g = scene.ground
    level = info["mausolee"]["level"]
    tops = info["mausolee"]["heights"]
    points = {}
    points["vue-d-ensemble"] = (Vector((250.0, -1500.0, 220.0)), Vector((-100.0, 150.0, level + 20.0)), ENGINE_LENS)
    px, py = sea_point(scene, (-60.0, -430.0), (60.0, -120.0))
    points["port-et-agora"] = (Vector((px, py, 4.0)), Vector((15.0, -40.0, level + 16.0)), ENGINE_LENS)
    belvedere = info["palais"]["belvedere"]
    points["palais-de-mausole"] = (Vector((belvedere[0], belvedere[1], belvedere[2] + 5.0)),
                                   Vector((-120.0, -330.0, 8.0)), ENGINE_LENS)
    basin = info["salmakis"]["basin"]
    sx, sy = sea_point(scene, (basin[0] + 55.0, basin[1] + 30.0), (basin[0], basin[1]))
    points["salmakis"] = (Vector((sx, sy, 5.0)), Vector((basin[0] - 4.0, basin[1] - 2.0, basin[2] + 3.0)), ENGINE_LENS)
    points["mausolee"] = (ground_eye(scene, 132.0, 8.0, 1.7), Vector((0.0, 0.0, level + 21.0)), ENGINE_LENS)
    points["sculpteurs"] = (Vector((28.0, -26.0, level + 20.0)), Vector((15.0, -12.5, level + 17.0)), ENGINE_LENS)
    points["quadrige"] = (Vector((22.0, 22.0, level + 50.0)), Vector((0.0, 0.0, tops["base_top"] + 1.5)),
                          ENGINE_LENS)
    ares = info["ares"]
    aim = Vector((-50.0, -90.0, level + 8.0))
    start = Vector((ares["altar"][0], ares["altar"][1], 0.0))
    heading = Vector((aim.x - start.x, aim.y - start.y, 0.0)).normalized()
    brow = start + heading * 110.0
    points["temple-d-ares"] = (ground_eye(scene, brow.x, brow.y, 4.0), aim, ENGINE_LENS)
    gate = info["murs"]["gate"]
    ox, oy = info["murs"]["outward"]
    angle = info["murs"]["gate_angle"]
    ax, ay = math.cos(angle), math.sin(angle)
    ex, ey = gate[0] + ox * 95.0 - ax * 25.0, gate[1] + oy * 95.0 - ay * 25.0
    points["porte-de-myndos"] = (ground_eye(scene, ex, ey, 3.0), Vector((gate[0] + ax * 8.0, gate[1] + ay * 8.0,
                                                                        gate[2] + 7.0)), ENGINE_LENS)
    return points


def place_markers(scene, points):
    root = scene.root("markers")
    for key, (eye, target, _) in points.items():
        new_empty(f"poi_{key}", scene.collection, root, Matrix.Translation(eye))
        new_empty(f"poi_{key}_target", scene.collection, root, Matrix.Translation(target))


def ring(centre, rx, ry, count):
    return [(centre[0] + rx * math.cos(math.tau * k / count), centre[1] + ry * math.sin(math.tau * k / count))
            for k in range(count + 1)]


def routes(info):
    ax, ay = plan.AGORA
    quay = info["quai"]
    gate = info["murs"]["gate"]
    ox, oy = info["murs"]["outward"]
    px, py = plan.PROPYLON
    palace = plan.PALACE
    basin = info["salmakis"]["basin"]
    temple = info["salmakis"]["temple"]
    return {
        "quais": [(x, y + 1.5) for x, y in quay[2:-2:3]],
        "agora": ring((ax, ay - 6.0), 30.0, 16.0, 24),
        "grande-rue": [(ax, ay + 20.0), (ax, 48.0)] + [p for p in plan.AVENUE[1:] if p[0] > gate[0] - 1.0]
        + [(gate[0], gate[1])],
        "propylon": [(px + 30.0, py + 2.0), (px + 12.0, py), (px + 4.0, py), (px - 10.0, py - 4.0)],
        "palais": [(palace[0] + 60.0, palace[1] + 120.0), (palace[0] + 40.0, palace[1] + 60.0),
                   (palace[0] + 10.0, palace[1] + 30.0), (palace[0], palace[1] - 10.0)],
        "salmakis": [(temple[0] - 30.0, temple[1] + 40.0), (temple[0] - 12.0, temple[1] + 14.0),
                     (temple[0] + 4.0, temple[1] + 4.0), (basin[0] + 3.0, basin[1] + 2.0)],
        "myndos": [(gate[0] + ox * 400.0, gate[1] + oy * 400.0 + 120.0), (gate[0] + ox * 200.0, gate[1] + oy * 200.0 + 50.0),
                   (gate[0] + ox * 60.0, gate[1] + oy * 60.0), (gate[0], gate[1])],
    }


def place_routes(scene, info):
    root = scene.root("life")
    counts = {}
    for name, points in routes(info).items():
        snapped = points
        for _ in range(3):
            snapped = resample([on_land(scene, x, y) for x, y in snapped], 2.5)
        snapped = [(x, y) for x, y in snapped if lifted(scene, x, y) >= 0.8]
        refined = [Vector((x, y, lifted(scene, x, y))) for x, y in snapped]
        for index, point in enumerate(refined):
            new_empty(f"walk_{name}_{index:02d}", scene.collection, root, Matrix.Translation(point))
        counts[name] = len(refined)
        counts[f"{name}_max_step"] = round(max((b - a).length for a, b in zip(refined[:-1], refined[1:])), 2)
    return counts


def build_walkers(scene):
    root = scene.root("life")
    report = {}
    for index, key in enumerate(WALKERS):
        build = VARIANTS[key]
        mesh = scene.library.mesh(key, lambda build=build: grounded(build()), ground_occlusion=False)
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
    rng = random.Random(345)
    placed = []
    scene.placements = {}
    counts = {}
    eyes = [(p[0].x, p[0].y) for p in info["points"].values()]
    avoid = [(e, 4.0) for e in eyes]
    ax, ay, _ = info["agora"]["centre"]
    total = 0
    for key, count in (("fig_citoyen", 30), ("fig_femme", 22), ("fig_citoyen_couleur", 16), ("fig_marchand", 12),
                       ("fig_porteur", 10), ("fig_enfant", 8), ("fig_ane", 6), ("fig_mulet", 3),
                       ("fig_amphores", 8), ("fig_perse", 2), ("fig_mercenaire", 3)):
        total += crowd(scene, rng, placed, key, count, (ax, ay), 46.0, avoid=avoid)
    counts["agora"] = total
    total = 0
    quay = info["quai"]
    for key, count in (("fig_porteur", 22), ("fig_porteur_sac", 18), ("fig_marin", 22), ("fig_marchand", 8),
                       ("fig_citoyen", 10), ("fig_ane", 6), ("fig_chien", 2), ("fig_amphores", 16)):
        for _ in range(count):
            x, y = quay[rng.randrange(len(quay))]
            total += crowd(scene, rng, placed, key, 1, (x, y + 4.0), 4.0, land=1.0, avoid=avoid)
    counts["port"] = total
    total = 0
    level = info["mausolee"]["level"]
    for key, count in (("fig_citoyen", 10), ("fig_citoyen_couleur", 6), ("fig_femme", 6), ("fig_enfant", 2)):
        total += crowd(scene, rng, placed, key, count, (-60.0, -20.0), 40.0, face=facing((0.0, 0.0)),
                       avoid=avoid + [((0.0, 0.0), 22.0)])
    for key, count in (("fig_citoyen", 14), ("fig_femme", 10), ("fig_ane", 4), ("fig_porteur", 6)):
        total += crowd(scene, rng, placed, key, count, (-200.0, 80.0), 120.0, avoid=avoid)
    counts["grande_rue"] = total
    gate = info["propylon"]["gate"]
    altar = info["propylon"]["altar"]
    total = crowd(scene, rng, placed, "fig_ouvrier", 8, (gate[0] + 6.0, gate[1]), 8.0, avoid=avoid)
    total += crowd(scene, rng, placed, "fig_tailleur", 6, (gate[0] + 16.0, gate[1]), 8.0, avoid=avoid)
    total += crowd(scene, rng, placed, "fig_boeuf", 2, (gate[0] + 22.0, gate[1] + 6.0), 4.0, avoid=avoid)
    total += crowd(scene, rng, placed, "fig_mercenaire", 1, (gate[0] + 4.0, gate[1] + 6.0), 1.0, avoid=avoid)
    total += crowd(scene, rng, placed, "fig_pretre", 1, (altar[0] - 3.0, altar[1]), 1.0, face=facing(altar))
    total += crowd(scene, rng, placed, "fig_femme_offrande", 2, (altar[0] - 4.0, altar[1] - 2.0), 2.0,
                   face=facing(altar))
    counts["propylon"] = total
    px, py = plan.PALACE
    upper = info["palais"]["upper"]
    total = 0
    for key, count in (("fig_mercenaire", 12), ("fig_citoyen_couleur", 6), ("fig_perse", 2), ("fig_citoyen", 6),
                       ("fig_femme", 4)):
        total += crowd(scene, rng, placed, key, count, (px, py - 10.0), 18.0, land=upper - 6.0, avoid=avoid)
    counts["palais"] = total
    basin = info["salmakis"]["basin"]
    total = crowd(scene, rng, placed, "fig_puiseuse", 4, (basin[0] + 3.5, basin[1]), 2.5,
                  face=facing(basin), avoid=avoid)
    total += crowd(scene, rng, placed, "fig_femme", 2, (basin[0] + 4.0, basin[1] - 7.0), 2.5, avoid=avoid)
    total += crowd(scene, rng, placed, "fig_marchand", 1, (basin[0] + 5.0, basin[1] + 8.0), 2.0, avoid=avoid)
    counts["salmakis"] = total
    ares = info["ares"]
    total = crowd(scene, rng, placed, "fig_pretre", 1, (ares["altar"][0], ares["altar"][1] - 3.0), 1.0,
                  face=facing(ares["altar"]))
    total += crowd(scene, rng, placed, "fig_mouton", 2, (ares["altar"][0] + 3.0, ares["altar"][1] - 4.0), 2.0)
    total += crowd(scene, rng, placed, "fig_chevre", 6, (ares["altar"][0] - 60.0, ares["altar"][1] - 40.0), 30.0)
    counts["goktepe"] = total
    murs = info["murs"]
    gx, gy, _ = murs["gate"]
    total = crowd(scene, rng, placed, "fig_mercenaire", 3, (gx, gy), 10.0, avoid=avoid)
    counts["porte"] = total
    far = list(FAR)
    city = 0
    for k in range(1600):
        if city >= 260:
            break
        x, y = rng.uniform(-1100.0, 1100.0), rng.uniform(-150.0, 1100.0)
        if not scene.ground(x, y) > 2.0 or math.hypot(x, y) < 120.0:
            continue
        scene.placements.setdefault(far[k % 3], []).append(placement(x, y, scene.ground.surface(x, y),
                                                                     rng.uniform(0, 6.28)))
        city += 1
    counts["ville"] = city
    builds = {**STANDING, **FAR, **EXTRA}
    for key, matrices in scene.placements.items():
        shadow = key not in FAR and key != "fig_amphores"
        scene.instances("figurants", key, lambda key=key: grounded(builds[key]()), matrices, cast_shadow=shadow,
                        occlusion=False)
    return counts


def effects(scene, info):
    root = scene.root("life")
    g = scene.ground
    ares = info["ares"]["altar"]
    salmakis = info["salmakis"]["altar"]
    gate = info["propylon"]["gate"]
    smokes = [[ares[0], ares[1], ares[2] + 0.3], [salmakis[0], salmakis[1], salmakis[2] + 0.3],
              [gate[0] + 26.0, gate[1] - 14.0, g(gate[0] + 26.0, gate[1] - 14.0) + 1.5]]
    for x, y, lift in ((-60.0, -330.0, 2.5), (-380.0, 180.0, 6.0), (300.0, 260.0, 6.0), (650.0, 120.0, 6.0),
                       (-700.0, 520.0, 6.0)):
        smokes.append([x, y, g(x, y) + lift])
    for index, point in enumerate(smokes, start=1):
        new_empty(f"smoke_{index}", scene.collection, root, Matrix.Translation(point))
    top = info["mausolee"]["heights"]["top"]
    birds = [(60.0, -320.0, 35.0), (-80.0, -500.0, 30.0), (-150.0, 220.0, 70.0),
             (plan.GOKTEPE[0], plan.GOKTEPE[1], info["ares"]["level"] + 25.0), (10.0, 10.0, top + 12.0)]
    for index, point in enumerate(birds[:4], start=1):
        new_empty(f"birds_{index}", scene.collection, root, Matrix.Translation(point))
    return {"smoke": len(smokes), "birds": 4}


def interior(scene, info):
    level = info["mausolee"]["level"]
    stylobate = info["mausolee"]["heights"]["stylobate"]
    marker = new_empty("interior", scene.collection, scene.root("markers"),
                       Matrix.Translation((0.0, 0.0, stylobate)))
    marker["radius"] = 18.0
    marker["height"] = 12.0
    return {"centre": [0.0, 0.0, round(stylobate, 2)], "level": level}


def preview_views(points, info):
    views = dict(points)
    tops = info["mausolee"]["heights"]
    views["mausolee-sud"] = (Vector((40.0, -110.0, tops["stylobate"] - 6.0)), Vector((0.0, 0.0, tops["stylobate"])),
                             30.0)
    views["colonnade"] = (Vector((0.0, -10.8, tops["stylobate"] + 1.7)), Vector((14.0, -10.0, tops["stylobate"] + 4.0)),
                          24.0)
    views["plan-port"] = (Vector((100.0, -480.0, 1100.0)), Vector((100.0, -479.0, 0.0)), 24.0)
    views["plan-ville"] = (Vector((-200.0, 300.0, 2200.0)), Vector((-200.0, 301.0, 0.0)), 24.0)
    return views


def build(scene, info):
    report = {"routes": place_routes(scene, info), "walkers": build_walkers(scene),
              "figures": build_figures(scene, info), "effects": effects(scene, info),
              "interior": interior(scene, info)}
    return report

