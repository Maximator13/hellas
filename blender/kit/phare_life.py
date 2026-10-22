import math
import random

from mathutils import Matrix, Vector

from . import figures as f
from . import phare_plan as plan
from . import phare_ships as ships
from .geometry import MeshBuilder, new_empty, new_object, placement
from .phare_city import palace_sites
from .life import pack_animal

LINEN_WHITE = (0.93, 0.92, 0.86)


def kausia(builder, color=(0.55, 0.47, 0.36), center=(0.0, 0.01, 1.6)):
    x, y, z = center
    frame = Matrix.Translation((x, y, 0.0))
    f.lathe(builder, [(0.0, z + 0.2), (0.15, z + 0.19), (0.16, z + 0.12), (0.11, z + 0.07)], color, 8, frame)


def macedonian(stride=0.0, soldier=False):
    builder = MeshBuilder()
    f.legs(builder, f.SKIN, stride, lower=f.LEATHER)
    f.skirt(builder, f.WOOL_WHITE if not soldier else f.CRIMSON, 1.0, 0.64, 0.18, 0.22)
    f.torso(builder, f.WOOL_WHITE if not soldier else f.CRIMSON)
    f.arms(builder, (0.29, 0.06, 0.88), (-0.25, 0.1, 0.9), f.WOOL_WHITE, f.SKIN)
    f.lathe(builder, [(0.21, 1.45), (0.25, 1.15), (0.27, 0.78)], f.MADDER if not soldier else f.PURPLE, 5,
            Matrix.Diagonal((1.0, 0.75, 1.0, 1.0)), start=math.radians(120), sweep=math.radians(230), both_sides=True)
    f.head(builder, f.SKIN, f.HAIR)
    kausia(builder)
    if soldier:
        f.aspis(builder, (-0.3, 0.12, 1.05), 0.66, f.BRONZE)
        f.spear(builder, (0.29, 0.06, 0.05), (0.29, 0.06, 2.6), 0.018, f.WOOD, 0.22, f.IRON)
    return builder


def egyptian(stride=0.0, priest=False):
    builder = MeshBuilder()
    skin = f.SKIN_SUN
    if priest:
        f.feet_only(builder, stride)
        f.skirt(builder, LINEN_WHITE, 1.0, 0.04, 0.17, 0.22, 8)
        f.torso(builder, LINEN_WHITE)
        f.arms(builder, (0.26, 0.1, 0.9), (-0.26, 0.1, 0.9), LINEN_WHITE, skin)
        f.head(builder, skin)
    else:
        f.legs(builder, skin, stride)
        f.skirt(builder, LINEN_WHITE, 1.0, 0.6, 0.17, 0.21)
        f.torso(builder, skin)
        f.arms(builder, (0.27, 0.08, 0.9), (-0.27, 0.06, 0.9), skin, skin)
        f.head(builder, skin, f.HAIR)
    return builder


def sailor(stride=0.0, tunic=f.UNDYED, torch=False):
    builder = MeshBuilder()
    f.legs(builder, f.SKIN_SUN, stride)
    f.skirt(builder, tunic, 1.0, 0.56, 0.18, 0.23)
    f.torso(builder, f.SKIN_SUN)
    f.sash(builder, tunic, depth=0.36)
    if torch:
        f.arms(builder, (0.24, 0.16, 1.5), (-0.26, 0.08, 0.88), f.SKIN_SUN, f.SKIN_SUN)
        f.tube(builder, [(0.24, 0.16, 1.2), (0.24, 0.18, 1.95)], [0.025, 0.03], f.WOOD, 5)
        builder.lathe([(0.07, 0.0), (0.06, 0.12), (0.025, 0.26), (0.0, 0.33)], 5, "flame", smooth=True,
                      matrix=Matrix.Translation((0.24, 0.18, 1.95)))
    else:
        f.arms(builder, (0.28, 0.08, 0.9), (-0.26, 0.08, 0.88), f.SKIN_SUN, f.SKIN_SUN)
    f.head(builder, f.SKIN_SUN, f.HAIR, f.HAIR)
    return builder


def grounded(builder):
    lowest = min(p[2] for p in builder.positions)
    result = MeshBuilder()
    result.merge(builder, Matrix.Translation((0.0, 0.0, -lowest)))
    return result


WALKERS = {
    "walker_grec": lambda: f.man_himation(stride=0.16),
    "walker_grecque": lambda: f.woman_peplos(f.LINEN, f.WOAD, stride=0.12, veil=f.MADDER),
    "walker_macedonien": lambda: macedonian(0.18),
    "walker_soldat": lambda: macedonian(0.18, True),
    "walker_egyptien": lambda: egyptian(0.18),
    "walker_pretre-egyptien": lambda: egyptian(0.12, True),
    "walker_marin": lambda: sailor(0.2),
    "walker_porteur": lambda: f.worker(f.MADDER, stride=0.18, carry="amphora"),
    "walker_porte-torche": lambda: sailor(0.16, f.SAFFRON, True),
    "walker_ane": lambda: pack_animal("donkey"),
}

STANDING = {
    "fig_grec": lambda: f.man_himation(),
    "fig_grec_couleur": lambda: f.man_himation(f.WOAD, f.SKIN_SUN, f.HAIR_GREY, f.HAIR_GREY,
                                               right_hand=(0.3, 0.3, 1.32)),
    "fig_grecque": lambda: f.woman_peplos(f.LINEN, f.WOAD, veil=f.MADDER),
    "fig_macedonien": lambda: macedonian(),
    "fig_soldat": lambda: macedonian(0.0, True),
    "fig_egyptien": lambda: egyptian(),
    "fig_pretre": lambda: egyptian(0.0, True),
    "fig_marin": lambda: sailor(),
    "fig_porteur": lambda: f.worker(f.MADDER, carry="amphora"),
    "fig_torche": lambda: sailor(0.0, f.SAFFRON, True),
}


def build_walkers(scene):
    root = scene.root("vie")
    report = {}
    for index, (key, build) in enumerate(WALKERS.items()):
        mesh = scene.library.mesh(key, lambda build=build: grounded(build()), ground_occlusion=False)
        lowest = min(v.co.z for v in mesh.vertices)
        assert abs(lowest) < 1e-4, (key, lowest)
        created = new_object(key, mesh, scene.collection, root, placement(9000.0 + index * 3.0, 9000.0, 0.0))
        created["cast_shadow"] = True
        report[key] = scene.library.builders[key].triangle_count()
    return report


def resample(points, spacing=2.8):
    out = [points[0]]
    for a, b in zip(points[:-1], points[1:]):
        count = max(int(math.ceil((Vector(b) - Vector(a)).length / spacing)), 1)
        for k in range(1, count + 1):
            out.append(tuple(Vector(a).lerp(Vector(b), k / count)))
    return out


def offset_line(points, distance, ground):
    out = []
    for k, p in enumerate(points):
        a = Vector(points[max(k - 1, 0)])
        b = Vector(points[min(k + 1, len(points) - 1)])
        tangent = (b - a).normalized()
        normal = Vector((tangent.y, -tangent.x))
        candidate = Vector(p) + normal * distance
        other = Vector(p) - normal * distance
        out.append(tuple(candidate if ground.shore(*candidate) > ground.shore(*other) else other))
    return out


def routes(scene, hepta, tower_frame):
    ground = scene.ground
    frame, length = hepta
    quay = plan.MAINLAND_SEA[16:24]
    result = {"quai": offset_line(resample(quay, 20.0), 7.0, ground)}
    result["heptastade"] = [tuple((frame @ Vector((-3.0, y, 0.0))).to_2d()) for y in (40.0, length * 0.36 - 30.0,
                                                                                         length * 0.36 + 30.0,
                                                                                         length * 0.7 - 30.0,
                                                                                         length * 0.7 + 30.0,
                                                                                         length - 40.0)]
    canopic = [tuple(plan.grid_point(t, plan.CANOPIC_N + 6.0)) for t in (-200.0, 0.0, 200.0, 420.0)]
    result["canopique"] = canopic
    r = plan.RHAKOTIS
    result["rhakotis"] = [tuple(plan.grid_point(r["t"] + 30.0 * math.cos(a), r["n"] - 40.0 + 30.0 * math.sin(a)))
                          for a in [k * math.pi / 5 for k in range(11)]]
    palace = plan.grid_point(1180.0, 1080.0)
    result["palais"] = [tuple(palace + plan.D * u + plan.N * v) for u, v in ((-24.0, -24.0), (24.0, -24.0),
                                                                           (24.0, 24.0), (-24.0, 24.0),
                                                                           (-24.0, -20.0))]
    result["phare"] = [tuple((tower_frame @ Vector((x, y, 0.0))).to_2d()) for x, y in
                       ((-36.0, -36.0), (-36.0, 0.0), (-30.0, 30.0), (0.0, 38.0), (30.0, 30.0), (36.0, 0.0),
                        (36.0, -36.0))]
    return result


def place_routes(scene, paths):
    root = scene.root("vie")
    counts = {}
    for name, points in paths.items():
        dense = resample(points, 2.8)
        lifted = [Vector((x, y, scene.ground.surface(x, y))) for x, y in dense]
        for index, point in enumerate(lifted):
            new_empty(f"walk_{name}_{index:02d}", scene.collection, root, Matrix.Translation(point))
        counts[name] = len(lifted)
        counts[f"{name}_max_step"] = round(max((b - a).length for a, b in zip(lifted[:-1], lifted[1:])), 2)
        counts[f"{name}_z"] = [round(min(p.z for p in lifted), 2), round(max(p.z for p in lifted), 2)]
    return counts


def crowd(scene, rng, placed, key, count, centre, radius, eyes, z_of=None, face=None):
    done = 0
    attempts = 0
    while done < count and attempts < count * 40:
        attempts += 1
        x = centre[0] + rng.uniform(-radius, radius)
        y = centre[1] + rng.uniform(-radius, radius)
        if any(math.hypot(x - px, y - py) < 0.9 for px, py in placed):
            continue
        if any(math.hypot(x - ex, y - ey) < 4.0 for ex, ey in eyes):
            continue
        z = z_of(x, y) if z_of else scene.ground.surface(x, y)
        if z < 0.5:
            continue
        heading = face(x, y) if face else rng.uniform(0, 2 * math.pi)
        placed.append((x, y))
        scene.figure_placements.setdefault(key, []).append(placement(x, y, z, heading + rng.uniform(-0.4, 0.4)))
        done += 1
    return done


def build_figures(scene, paths, eyes):
    rng = random.Random(281)
    placed = []
    scene.figure_placements = {}
    counts = {}
    harbour = list(STANDING)
    quay_points = paths["quai"]
    total = 0
    for k, (x, y) in enumerate(quay_points[::2]):
        mix = ("fig_porteur", "fig_marin", "fig_grec", "fig_egyptien", "fig_porteur", "fig_grec_couleur",
               "fig_grecque", "fig_torche")
        for key in mix[k % 3:k % 3 + 5]:
            total += crowd(scene, rng, placed, key, 1, (x, y), 7.0, eyes)
    counts["quais"] = total
    frame, length = scene.hepta
    total = 0
    for k in range(30):
        y = rng.uniform(30.0, length - 30.0)
        if any(abs(y - length * fraction) < 14.0 for fraction in plan.HEPTASTADION_BRIDGES):
            continue
        p = frame @ Vector((rng.uniform(-8.0, 8.0), y, 0.0))
        total += crowd(scene, rng, placed, harbour[k % len(harbour)], 1, (p.x, p.y), 1.0, eyes)
    counts["heptastade"] = total
    total = 0
    for t in range(-700, 900, 14):
        for side in (-1, 1):
            if rng.random() < 0.45:
                p = plan.grid_point(t + rng.uniform(-6, 6), plan.CANOPIC_N + side * rng.uniform(3.0, 12.0))
                total += crowd(scene, rng, placed, harbour[rng.randrange(len(harbour))], 1, (p.x, p.y), 1.0, eyes)
    counts["canopique"] = total
    r = plan.RHAKOTIS
    centre = plan.grid_point(r["t"], r["n"])
    total = crowd(scene, rng, placed, "fig_pretre", 3, (centre.x, centre.y), 9.0, eyes)
    total += crowd(scene, rng, placed, "fig_egyptien", 30, (centre.x, centre.y), 140.0, eyes)
    counts["rhakotis"] = total
    total = 0
    for site in palace_sites()[:2]:
        palace = plan.grid_point(site["t"], site["n"])
        total += crowd(scene, rng, placed, "fig_soldat", 6, (palace.x, palace.y), 26.0, eyes)
        total += crowd(scene, rng, placed, "fig_torche", 5, (palace.x, palace.y), 24.0, eyes)
        total += crowd(scene, rng, placed, "fig_grec_couleur", 8, (palace.x, palace.y), 24.0, eyes)
    counts["palais"] = total
    tower = scene.tower_frame
    total = 0
    for x, y, key in ((-20.0, -30.0, "fig_soldat"), (22.0, -28.0, "fig_marin"), (-8.0, -36.0, "fig_porteur"),
                      (30.0, 10.0, "fig_torche"), (-30.0, 12.0, "fig_marin")):
        p = tower @ Vector((x, y, 0.0))
        total += crowd(scene, rng, placed, key, 2, (p.x, p.y), 4.0, eyes)
    counts["phare"] = total
    for key, matrices in scene.figure_placements.items():
        scene.add_instances("figurants", key, lambda key=key: grounded(STANDING[key]()), matrices, occlusion=False)
    return counts


def ship_spots(scene, rng, eyes):
    ground = scene.ground
    spots = {key: [] for key in ships.KINDS}

    def water(x, y, margin):
        return ground.shore(x, y) < -margin and not plan.is_land(x, y)

    def clear(x, y, radius):
        if any(math.hypot(x - ex, y - ey) < radius + 12.0 for ex, ey in eyes):
            return False
        return all(math.hypot(x - m[0][3], y - m[1][3]) > radius for ms in spots.values() for m in ms)

    for k in range(9):
        for attempt in range(40):
            x, y = rng.uniform(300.0, 2600.0), rng.uniform(150.0, 2200.0)
            if water(x, y, 60.0) and clear(x, y, 60.0):
                spots["navire_voile"].append(ships.heading_matrix(x, y, rng.uniform(170.0, 200.0)))
                break
    quay = plan.MAINLAND_SEA[18:36]
    for a, b in zip(quay[:-1], quay[1:]):
        a, b = Vector(a), Vector(b)
        direction = (b - a).normalized()
        normal = Vector((direction.y, -direction.x))
        if ground.shore(*(a.lerp(b, 0.5) + normal * 20.0)) > 0:
            normal = -normal
        for s in range(12, int((b - a).length) - 12, 34):
            p = a + direction * s + normal * rng.uniform(9.0, 12.0)
            if not water(p.x, p.y, 5.0) or not clear(p.x, p.y, 16.0) or rng.random() < 0.3:
                continue
            bearing = math.degrees(math.atan2(direction.x, direction.y)) + rng.choice((0.0, 180.0))
            key = rng.choice(("navire_amarre", "navire_amarre", "allege", "barque"))
            if Vector((p.x, p.y)).length > 1800.0 and rng.random() < 0.5:
                key = "navire_guerre"
            spots[key].append(ships.heading_matrix(p.x, p.y, bearing))
    for k in range(70):
        x, y = rng.uniform(-2600.0, 2400.0), rng.uniform(-2400.0, 700.0)
        if water(x, y, 30.0) and clear(x, y, 30.0):
            key = rng.choice(("barque", "barque", "allege", "navire_amarre"))
            spots[key].append(ships.heading_matrix(x, y, rng.uniform(0.0, 360.0)))
    for k in range(10):
        t = plan.LAKE_PORT["t"] + rng.uniform(-400.0, 400.0)
        n = plan.lake_n(t) - rng.uniform(40.0, 400.0)
        p = plan.grid_point(t, n)
        spots["barge_nil"].append(ships.heading_matrix(p.x, p.y, rng.uniform(0.0, 360.0), 0.35))
    return spots


def build_ships(scene, eyes):
    rng = random.Random(53)
    spots = ship_spots(scene, rng, eyes)
    for key, matrices in spots.items():
        scene.add_instances("navires", key, ships.KINDS[key], matrices, cast_shadow=key == "navire_voile")
    return {key: len(m) for key, m in spots.items()}


def quay_point(ground, target, inland):
    best, best_distance = None, float("inf")
    line = plan.MAINLAND_SEA[plan.QUAY_RANGE[0]:plan.QUAY_RANGE[1]]
    for a, b in zip(line[:-1], line[1:]):
        a, b = Vector(a), Vector(b)
        t = max(0.0, min(1.0, (target - a).dot(b - a) / max((b - a).length_squared, 1e-9)))
        p = a.lerp(b, t)
        if (p - target).length < best_distance:
            direction = (b - a).normalized()
            normal = Vector((direction.y, -direction.x))
            if ground.shore(*(p + normal * 10.0)) < ground.shore(*(p - normal * 10.0)):
                normal = -normal
            best, best_distance = p + normal * inland, (p - target).length
    return best


def points_of_interest(scene):
    g = scene.ground
    lens = plan.LENS
    tower = Vector((0.0, 0.0, plan.TOWER_GROUND))
    points = {"vue-d-ensemble": (Vector((2300.0, -2100.0, 420.0)), Vector((300.0, -800.0, 0.0)), lens)}
    quay = quay_point(g, Vector((1150.0, -1340.0)), 4.0)
    points["le-grand-port"] = (Vector((quay.x, quay.y, g.surface(quay.x, quay.y) + 4.2)),
                               Vector((0.0, 0.0, 40.0)), lens)
    frame, length = scene.hepta
    eye = frame @ Vector((-4.0, length * 0.36 - 46.0, 0.0))
    points["l-heptastade"] = (Vector((eye.x, eye.y, g.surface(eye.x, eye.y) + 1.7)), Vector((0.0, 0.0, 45.0)), lens)
    eye = plan.grid_point(260.0, plan.CANOPIC_N - 4.0)
    target = plan.grid_point(900.0, plan.CANOPIC_N - 4.0)
    points["la-voie-canopique"] = (Vector((eye.x, eye.y, g.surface(eye.x, eye.y) + 1.7)),
                                   Vector((target.x, target.y, g(target.x, target.y) + 12.0)), lens)
    r = plan.RHAKOTIS
    eye = plan.grid_point(r["t"] + 2.0, r["n"] - 30.0)
    points["rhakotis"] = (Vector((eye.x, eye.y, g.surface(eye.x, eye.y) + 7.0)), Vector((0.0, 0.0, 20.0)), lens)
    palace = plan.grid_point(1180.0, 1080.0)
    eye = palace + Vector((40.0, -24.0))
    points["le-quartier-royal"] = (Vector((eye.x, eye.y, 20.0)), Vector((0.0, 0.0, 40.0)), lens)
    points["le-phare"] = (Vector((350.0, -280.0, 3.0)), Vector((0.0, 0.0, 52.0)), lens)
    beacon = scene.tower_frame @ Vector((0.0, 0.0, 93.0))
    points["le-sommet"] = (Vector((52.0, -40.0, plan.TOWER_GROUND + 100.0)), beacon + Vector((0.0, 0.0, 3.0)), lens)
    return points


def eye_points():
    return [(2300.0, -2100.0), (1150.0, -1340.0), (350.0, -280.0), (2458.0, -342.0), (60.0, -45.0), (184.0, -1149.0),
            (1971.0, -1668.0), (1036.0, -3427.0)]


def place_markers(scene, points):
    root = scene.root("reperes")
    for key, (eye, target, _) in points.items():
        new_empty(f"poi_{key}", scene.collection, root, Matrix.Translation(eye))
        new_empty(f"poi_{key}_target", scene.collection, root, Matrix.Translation(target))


def effects(scene, altar, beacon):
    root = scene.root("vie")
    g = scene.ground
    rng = random.Random(61)
    smokes = []
    for t, n in ((-2200.0, 300.0), (-900.0, -400.0), (300.0, -700.0), (1300.0, 200.0), (2100.0, -600.0),
                 (-300.0, 600.0)):
        p = plan.grid_point(t + rng.uniform(-30, 30), n + rng.uniform(-30, 30))
        smokes.append(Vector((p.x, p.y, g(p.x, p.y) + 9.0)))
    kitchen = plan.grid_point(1240.0, 1010.0)
    smokes.append(Vector((kitchen.x, kitchen.y, g(kitchen.x, kitchen.y) + 8.0)))
    smokes.append(Vector(altar))
    for index, point in enumerate(smokes, start=1):
        new_empty(f"smoke_{index}", scene.collection, root, Matrix.Translation(point))
    reef = Vector(plan.REEFS[0][2])
    new_empty("birds_1", scene.collection, root, Matrix.Translation((reef.x, reef.y, 30.0)))
    new_empty("beacon", scene.collection, root, Matrix.Translation(beacon))
    return {"smoke": len(smokes), "birds": 1}


def clearance(points, reach=6.0, count=200):
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
