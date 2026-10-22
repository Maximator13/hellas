import math
import random

from mathutils import Matrix, Vector

from . import figures as f
from . import olympie_plan as plan
from . import olympie_zeus as zeus
from .buildings import lathe_tree, lobe, olive_tree, plane_tree, scrub, trunk, umbrella_pine
from .geometry import MeshBuilder, new_empty, new_object, placement
from .life import animal, pack_animal
from .stage import sun_vector

BRONZE = "bronze_statue"


def grounded(builder):
    lowest = min(p[2] for p in builder.positions)
    result = MeshBuilder()
    result.merge(builder, Matrix.Translation((0.0, 0.0, -lowest)))
    return result


def scaled(builder, factor):
    result = MeshBuilder()
    result.merge(builder, Matrix.Scale(factor, 4))
    return result


def athlete(stride=0.0, skin=f.SKIN_SUN):
    builder = MeshBuilder()
    f.legs(builder, skin, stride, feet=skin)
    f.torso(builder, skin)
    f.arms(builder, (0.3, 0.1, 0.9), (-0.3, 0.04, 0.92), skin, skin)
    f.head(builder, skin, f.HAIR)
    return builder


def trainer(stride=0.0):
    builder = f.man_himation(f.UNDYED, f.SKIN_SUN, f.HAIR_GREY, f.HAIR_GREY, stride, right_hand=(0.3, 0.2, 1.0))
    f.tube(builder, [(0.3, 0.22, 0.05), (0.3, 0.24, 1.6), (0.25, 0.24, 1.75)], [0.015, 0.015, 0.01], f.WOOD, 4)
    f.tube(builder, [(0.3, 0.24, 1.6), (0.35, 0.24, 1.75)], [0.012, 0.01], f.WOOD, 4)
    return builder


def judge(stride=0.0):
    builder = f.man_himation(f.PURPLE, f.SKIN, f.HAIR_GREY, f.HAIR_GREY, stride, right_hand=(0.3, 0.2, 1.0))
    f.tube(builder, [(0.3, 0.22, 0.4), (0.3, 0.24, 1.7)], [0.014, 0.014], f.WOOD, 4)
    f.wreath(builder)
    return builder


def traveller(stride=0.0, mantle=f.MADDER):
    builder = f.man_himation(mantle, f.SKIN_SUN, f.HAIR, f.HAIR, stride)
    f.petasos(builder, (0.66, 0.54, 0.34))
    return builder


def elean_guard(stride=0.0):
    builder = MeshBuilder()
    f.legs(builder, f.SKIN_SUN, stride, lower=f.BRONZE, feet=f.LEATHER)
    f.skirt(builder, f.WOAD, 0.98, 0.66, 0.18, 0.23)
    f.skirt(builder, f.LINEN, 1.0, 0.8, 0.178, 0.215)
    f.torso(builder, f.LINEN)
    f.arms(builder, (0.27, 0.12, 0.98), (-0.2, 0.25, 1.05), f.LINEN, f.SKIN_SUN)
    f.head(builder, f.SKIN_SUN, f.HAIR, f.HAIR)
    f.pilos(builder, f.BRONZE, (0.0, 0.01, 1.62))
    f.aspis(builder, (-0.26, 0.3, 1.05), 0.9, (0.70, 0.30, 0.18))
    f.spear(builder, (0.27, 0.12, 0.03), (0.27, 0.16, 2.55), 0.016)
    return builder


def girl(stride=0.0):
    return scaled(f.woman_peplos(f.LINEN, f.SAFFRON, stride=stride), 0.86)


def merchant(stride=0.0):
    return f.worker(f.SAFFRON, f.SKIN_SUN, f.HAIR, stride, carry="amphora")


def horse():
    builder = MeshBuilder()
    f.horse(builder, (0.46, 0.32, 0.20))
    return builder


WALKERS = {
    "walker_citoyen": lambda: f.man_himation(stride=0.16),
    "walker_voyageur-petase": lambda: traveller(0.16),
    "walker_ouvrier": lambda: f.worker(f.OLIVE, stride=0.2),
    "walker_esclave-porteur": lambda: f.worker(f.UNDYED, f.SKIN_SUN, stride=0.18, carry="amphora"),
    "walker_athlete": lambda: athlete(0.22),
    "walker_entraineur": lambda: trainer(0.14),
    "walker_juge": lambda: judge(0.12),
    "walker_pretre": lambda: f.priest(),
    "walker_hoplite-eleen": lambda: elean_guard(0.16),
    "walker_jeune-fille": lambda: girl(0.12),
    "walker_marchand": lambda: merchant(0.16),
    "walker_boeuf": lambda: animal("ox"),
    "walker_cheval": horse,
    "walker_mulet": lambda: pack_animal("mule"),
}

STANDING = {
    "fig_citoyen": lambda: f.man_himation(),
    "fig_citoyen_couleur": lambda: f.man_himation(f.WOAD, f.SKIN_SUN, f.HAIR_GREY, f.HAIR_GREY,
                                                  right_hand=(0.3, 0.3, 1.32)),
    "fig_voyageur": lambda: traveller(0.0, f.SAFFRON),
    "fig_athlete": lambda: athlete(),
    "fig_entraineur": lambda: trainer(),
    "fig_juge": lambda: judge(),
    "fig_pretre": lambda: f.priest(),
    "fig_hoplite": lambda: elean_guard(),
    "fig_argien": lambda: f.hoplite(),
    "fig_porteur": lambda: f.worker(f.MADDER, carry="amphora"),
    "fig_jeune_fille": lambda: girl(),
    "fig_marchand": lambda: merchant(),
    "fig_boeuf": lambda: animal("ox"),
    "fig_cheval": horse,
    "fig_mulet": lambda: animal("mule"),
}

FAR = {
    "fig_loin_a": lambda: f.far_infantry(f.WOOL_WHITE, f.WOOL_WHITE, f.HAIR, None, spear_color=None),
    "fig_loin_b": lambda: f.far_infantry(f.MADDER, f.SAFFRON, f.HAIR, None, spear_color=None),
    "fig_loin_c": lambda: f.far_infantry(f.UNDYED, f.SKIN_SUN, f.HAIR, None, spear_color=None),
    "fig_loin_d": lambda: f.far_infantry(f.WOAD, f.LINEN, f.HAIR, None, spear_color=None),
}


def tent(length=4.0, width=2.6, height=1.9, colour=(0.90, 0.85, 0.72)):
    builder = MeshBuilder()
    for side in (-1, 1):
        builder.oriented([(side * width / 2, -length / 2, 0.0), (side * width / 2, length / 2, 0.0),
                          (0.0, length / 2, height), (0.0, -length / 2, height)], (side, 0, 0.6), "velum_linen")
    builder.oriented([(-width / 2, -length / 2, 0.0), (width / 2, -length / 2, 0.0), (0.0, -length / 2, height)],
                     (0, -1, 0), "velum_linen")
    builder.tint(0, colour)
    first = len(builder.polygons)
    builder.oriented([(-width / 2, length / 2, 0.0), (0.0, length / 2, height), (-width / 4, length / 2, 0.0)],
                     (0, 1, 0), "velum_linen")
    builder.tint(first, colour)
    for y in (-length / 2 - 0.05, length / 2 + 0.05):
        builder.box((-0.03, y - 0.03, 0.0), (0.03, y + 0.03, height + 0.15), "dark_wood", bottom=False)
    return builder


def hide_tent():
    return tent(3.2, 2.4, 1.6, (0.56, 0.42, 0.28))


def embassy_tent():
    builder = MeshBuilder()
    w, d, h = 6.0, 8.0, 2.6
    for x in (-w / 2, w / 2):
        for y in (-d / 2, d / 2):
            builder.box((x - 0.06, y - 0.06, 0.0), (x + 0.06, y + 0.06, h), "dark_wood", bottom=False)
    first = len(builder.polygons)
    builder.box((-w / 2 - 0.2, -d / 2 - 0.2, h), (w / 2 + 0.2, d / 2 + 0.2, h + 0.08), "velum_linen")
    builder.tint(first, (0.92, 0.88, 0.78))
    for k in range(4):
        first = len(builder.polygons)
        x = -w / 2 + 0.2 + k * (w - 0.4) / 3
        builder.box((x - 0.35, -d / 2 - 0.22, h - 0.4), (x + 0.35, -d / 2 - 0.21, h + 0.08), "velum_linen")
        builder.tint(first, (0.62, 0.20, 0.14) if k % 2 else (0.20, 0.30, 0.52))
    for side in (-1, 1):
        first = len(builder.polygons)
        builder.box((side * w / 2 - 0.02, -d / 2, 0.0), (side * w / 2 + 0.02, d / 2, h), "velum_linen", bottom=False,
                    top=False)
        builder.tint(first, (0.84, 0.78, 0.64))
    first = len(builder.polygons)
    builder.box((-w / 2, d / 2 - 0.02, 0.0), (w / 2, d / 2 + 0.02, h), "velum_linen", bottom=False, top=False)
    builder.tint(first, (0.84, 0.78, 0.64))
    first = len(builder.polygons)
    builder.box((-1.6, -2.5, 0.0), (1.6, 1.5, 0.03), "velum_linen", bottom=False)
    builder.tint(first, (0.58, 0.22, 0.16))
    return builder


def shelter():
    builder = MeshBuilder()
    builder.oriented([(-1.8, -1.0, 0.0), (1.8, -1.0, 0.0), (1.8, 1.0, 1.6), (-1.8, 1.0, 1.6)], (0, -1, 1), "matte")
    builder.tint(0, (0.48, 0.44, 0.26))
    for x in (-1.6, 1.6):
        builder.box((x - 0.05, 0.95, 0.0), (x + 0.05, 1.05, 1.65), "dark_wood", bottom=False)
    return builder


def bronze_statue(seed):
    rng = random.Random(seed)
    builder = MeshBuilder()
    height = rng.uniform(1.0, 1.6)
    builder.box((-0.55, -0.55, -0.4), (0.55, 0.55, height), "limestone", bottom=False)
    builder.box((-0.62, -0.62, height - 0.12), (0.62, 0.62, height), "limestone", bottom=False)
    figure = athlete(0.0 if seed % 2 else 0.18, f.BRONZE) if seed % 3 else f.man_himation(stride=0.1)
    builder.merge(zeus.mono(figure, BRONZE), Matrix.Translation((0.0, 0.0, height)) @ Matrix.Scale(1.1, 4))
    return builder


def tripod():
    builder = MeshBuilder()
    builder.box((-0.5, -0.5, -0.3), (0.5, 0.5, 0.5), "limestone", bottom=False)
    for k in range(3):
        a = 2 * math.pi * k / 3
        f.tube(builder, [(0.42 * math.cos(a), 0.42 * math.sin(a), 0.5), (0.25 * math.cos(a), 0.25 * math.sin(a), 2.1)],
               [0.035, 0.03], f.BRONZE, 4)
    builder.lathe([(0.0, 1.85), (0.32, 1.9), (0.45, 2.15), (0.42, 2.35)], 10, BRONZE, smooth=True)
    for k in range(2):
        a = math.pi * k
        builder.lathe([(0.12, 0.0), (0.1, 0.02)], 8, BRONZE, smooth=True,
                      matrix=Matrix.Translation((0.42 * math.cos(a), 0.42 * math.sin(a), 2.45)) @ Matrix.Rotation(
                          math.pi / 2, 4, "X"))
    return builder


def stele():
    builder = MeshBuilder()
    builder.box((-0.45, -0.25, -0.3), (0.45, 0.25, 0.25), "limestone", bottom=False)
    builder.box((-0.32, -0.08, 0.25), (0.32, 0.08, 1.9), "marble", bottom=False)
    builder.box((-0.4, -0.12, 1.9), (0.4, 0.12, 2.05), "marble", bottom=False)
    return builder


def small_altar():
    builder = MeshBuilder()
    builder.box((-0.8, -0.6, -0.3), (0.8, 0.6, 1.0), "limestone", bottom=False)
    builder.box((-0.9, -0.7, 1.0), (0.9, 0.7, 1.12), "limestone", bottom=False)
    return builder


def poplar(height=17.0, seed=0):
    builder = MeshBuilder()
    trunk(builder, height * 0.3, 0.25, (0.1, 0.0), "plaster_grey")
    r = height * 0.13
    crown = [(0.0, height * 0.18), (r * 0.8, height * 0.3), (r, height * 0.5), (r * 0.8, height * 0.75),
             (r * 0.35, height * 0.93), (0.0, height)]
    builder.merge(lathe_tree(0.0, 0.0, crown, "foliage_plane", 8, seed))
    return builder


def aleppo_pine(height=11.0, seed=0):
    builder = MeshBuilder()
    trunk(builder, height * 0.6, 0.2, (0.6, 0.2))
    lobe(builder, (0.6, 0.2, height * 0.72), height * 0.26, height * 0.36, "foliage_dark", 7, seed, 0.2)
    lobe(builder, (-0.7, 0.4, height * 0.55), height * 0.18, height * 0.26, "foliage_dark", 6, seed + 1, 0.2)
    return builder


def oleander(seed=0):
    builder = scrub(2.2, seed)
    first = len(builder.polygons)
    for k in range(5):
        a = k * 1.3
        builder.centered_box((0.6 * math.cos(a), 0.6 * math.sin(a), 1.2 + 0.2 * (k % 2)), (0.25, 0.25, 0.2), "matte")
    builder.tint(first, (0.86, 0.42, 0.52))
    return builder


TREES = {
    "olivier": lambda: olive_tree(5.0, 3),
    "platane": lambda: plane_tree(15.0, 5),
    "peuplier": lambda: poplar(17.0, 7),
    "pin": lambda: aleppo_pine(11.0, 9),
    "pin_parasol": lambda: umbrella_pine(12.0, 11),
    "laurier_rose": lambda: oleander(13),
}


def resample(points, spacing=2.6):
    out = [points[0]]
    for a, b in zip(points[:-1], points[1:]):
        count = max(int(math.ceil((Vector(b) - Vector(a)).length / spacing)), 1)
        for k in range(1, count + 1):
            out.append(tuple(Vector(a).lerp(Vector(b), k / count)))
    return out


def routes(info):
    temple = info["temple"]
    naos = [Vector(p) for p in temple["naos"]]
    axis = (naos[1] - naos[0]).normalized()
    pool = Vector(temple["pool_front"])
    cella = [tuple((naos[1] + axis * 6.0).to_2d()), tuple((naos[1] - axis * 1.0).to_2d()),
             tuple((pool + axis * 2.0 + Vector((0.0, 2.6, 0.0))).to_2d())]
    return {
        "procession": [(-70.0, 112.0), (-50.0, 90.0), (-30.0, 76.0), (-12.0, 82.0), (8.0, 80.0), (16.0, 78.0)],
        "altis": [(36.0, 64.0), (42.0, 40.0), (40.0, 20.0), (46.0, 0.0), (40.0, -22.0), (10.0, -30.0), (-25.0, -30.0)],
        "tresors": [(40.0, 66.0), (60.0, 96.0), (95.0, 112.0), (130.0, 118.0), (165.0, 122.0), (190.0, 130.0)],
        "stade": [plan.stadium_point(u, v) for u, v in ((8.0, -6.0), (100.0, -6.0), (190.0, -6.0), (190.0, 6.0),
                                                         (100.0, 6.0), (8.0, 6.0))],
        "campement": [(80.0, -140.0), (120.0, -200.0), (180.0, -235.0), (260.0, -270.0), (360.0, -290.0),
                      (460.0, -300.0), (560.0, -280.0)],
        "kladeos": [(-140.0, -60.0), (-170.0, 0.0), (-175.0, 80.0), (-160.0, 140.0)],
        "cella": cella,
    }


def refine(scene, a, b, depth=0):
    if (b - a).length <= 2.8 or depth > 6:
        return [b]
    middle = (a + b) / 2
    middle.z = scene.ground.surface(middle.x, middle.y, hint=middle.z)
    return refine(scene, a, middle, depth + 1) + refine(scene, middle, b, depth + 1)


def place_routes(scene, info):
    root = scene.root("vie")
    counts = {}
    floor = info["temple"]["floor"]
    for name, points in routes(info).items():
        dense = resample(points)
        if name == "cella":
            lifted = [Vector((x, y, floor)) for x, y in dense]
            refined = lifted
        else:
            lifted = [Vector((x, y, scene.ground.surface(x, y))) for x, y in dense]
            refined = [lifted[0]]
            for a, b in zip(lifted[:-1], lifted[1:]):
                refined.extend(refine(scene, a, b))
        for index, point in enumerate(refined):
            new_empty(f"walk_{name}_{index:02d}", scene.collection, root, Matrix.Translation(point))
        counts[name] = len(refined)
        counts[f"{name}_max_step"] = round(max((b - a).length for a, b in zip(refined[:-1], refined[1:])), 2)
    return counts


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


def facing(point):
    return lambda x, y: math.atan2(-(point[0] - x), point[1] - y)


class Placer:
    def __init__(self, scene, seed):
        self.scene = scene
        self.rng = random.Random(seed)
        self.placed = []
        self.items = {}
        self.blocked = []

    def block(self, x, y, radius):
        self.blocked.append((x, y, radius))

    def free(self, x, y, gap):
        if any(math.hypot(x - bx, y - by) < r for bx, by, r in self.blocked):
            return False
        return not any(math.hypot(x - px, y - py) < gap for px, py in self.placed)

    def add(self, key, x, y, heading, z=None, scale=1.0):
        z = self.scene.ground.surface(x, y) if z is None else z
        self.placed.append((x, y))
        self.items.setdefault(key, []).append(placement(x, y, z, heading, scale))

    def crowd(self, key, count, centre, radius, face=None, gap=0.9, z=None):
        done = 0
        for attempt in range(count * 40):
            if done >= count:
                break
            x = centre[0] + self.rng.uniform(-radius, radius)
            y = centre[1] + self.rng.uniform(-radius, radius)
            if math.hypot(x - centre[0], y - centre[1]) > radius or not self.free(x, y, gap):
                continue
            heading = face(x, y) if face else self.rng.uniform(0, 2 * math.pi)
            self.add(key, x, y, heading + self.rng.uniform(-0.35, 0.35), z)
            done += 1
        return done


def obstacles(placer, info):
    for x, y, r in ((0.0, 0.0, 36.0), (-23.0, 118.0, 28.0), (25.0, 75.0, 8.5), (-115.0, 20.0, 22.0),
                    (-70.0, 130.0, 13.0), (20.0, -72.0, 26.0), (45.0, -10.0, 3.0), (-10.0, 60.0, 17.0)):
        placer.block(x, y, r)
    for x, y in plan.treasury_sites():
        placer.block(x, y + 2.0, 9.0)
    for key, (x, y) in plan.EYES.items():
        placer.block(x, y, 7.0)
    for path in routes(info).values():
        for x, y in resample(path, 4.0):
            placer.block(x, y, 1.4)


def build_figures(scene, info):
    placer = Placer(scene, 420)
    obstacles(placer, info)
    counts = {}
    altar = plan.ALTAR
    ring = []
    for k in range(70):
        a = 2 * math.pi * k / 70
        r = placer.rng.uniform(10.0, 22.0)
        ring.append((altar[0] + r * math.cos(a), altar[1] + r * math.sin(a)))
    total = 0
    mix = ("fig_citoyen", "fig_citoyen", "fig_citoyen_couleur", "fig_voyageur", "fig_athlete", "fig_jeune_fille",
           "fig_citoyen", "fig_marchand")
    for k, (x, y) in enumerate(ring * 3):
        x += placer.rng.uniform(-3.0, 3.0)
        y += placer.rng.uniform(-3.0, 3.0)
        if placer.free(x, y, 0.9):
            placer.add(mix[k % len(mix)], x, y, facing(altar)(x, y) + placer.rng.uniform(-0.4, 0.4))
            total += 1
    total += placer.crowd("fig_pretre", 6, (altar[0] - 3.0, altar[1] - 9.0), 3.0, facing(altar))
    total += placer.crowd("fig_juge", 2, (altar[0] + 6.0, altar[1] - 10.0), 1.5, facing(altar))
    total += placer.crowd("fig_boeuf", 10, (altar[0] + 12.0, altar[1] + 14.0), 7.0, gap=2.4)
    total += placer.crowd("fig_porteur", 8, (altar[0] - 12.0, altar[1] - 10.0), 6.0)
    counts["autel"] = total
    altis = ("fig_citoyen", "fig_citoyen_couleur", "fig_voyageur", "fig_athlete", "fig_entraineur", "fig_citoyen",
             "fig_marchand", "fig_jeune_fille", "fig_porteur")
    total = 0
    for k in range(380):
        x, y = placer.rng.uniform(-60.0, 190.0), placer.rng.uniform(-40.0, 150.0)
        if not point_in(plan.ALTIS, x, y) or not placer.free(x, y, 1.0):
            continue
        placer.add(altis[k % len(altis)], x, y, placer.rng.uniform(0, 2 * math.pi))
        total += 1
    counts["altis"] = total
    total = 0
    for k in range(90):
        side = 1 if k % 2 else -1
        u = placer.rng.uniform(10.0, 200.0)
        v = side * placer.rng.uniform(19.0, 30.0)
        x, y = plan.stadium_point(u, v)
        if placer.free(x, y, 1.0):
            placer.add(("fig_citoyen", "fig_voyageur", "fig_citoyen_couleur")[k % 3], x, y,
                       math.atan2(-(plan.stadium_point(u, 0.0)[0] - x), plan.stadium_point(u, 0.0)[1] - y))
            total += 1
    track = plan.stadium_point
    total += placer.crowd("fig_athlete", 12, track(60.0, 0.0), 12.0)
    total += placer.crowd("fig_entraineur", 4, track(60.0, 6.0), 10.0)
    counts["stade"] = total
    total = 0
    for (cx, cy), radius in plan.CAMPS:
        total += placer.crowd("fig_citoyen", int(radius * 0.12), (cx, cy), radius * 0.8)
        total += placer.crowd("fig_voyageur", int(radius * 0.1), (cx, cy), radius * 0.8)
        total += placer.crowd("fig_marchand", int(radius * 0.05), (cx, cy), radius * 0.8)
        total += placer.crowd("fig_porteur", int(radius * 0.05), (cx, cy), radius * 0.8)
        total += placer.crowd("fig_mulet", int(radius * 0.04), (cx, cy), radius * 0.8, gap=2.0)
        total += placer.crowd("fig_cheval", int(radius * 0.03), (cx, cy), radius * 0.8, gap=2.0)
        for key in FAR:
            total += placer.crowd(key, int(radius * 0.25), (cx, cy), radius, gap=1.2)
    (ax, ay), radius = plan.ARGIVE_CAMP
    total += placer.crowd("fig_argien", 50, (ax, ay), radius)
    counts["campements"] = total
    guards = 0
    for x, y, n in ((210.0, -232.0, 4), (95.0, -60.0, 5), (240.0, 40.0, 4), (-150.0, 110.0, 3), (150.0, 175.0, 3)):
        guards += placer.crowd("fig_hoplite", n, (x, y), 4.0, facing((x, y - 30.0)))
    counts["garde"] = guards
    workshop = plan.WORKSHOP
    counts["atelier"] = placer.crowd("fig_citoyen", 3, (workshop[0] + 4.0, workshop[1] - 16.0), 5.0)
    temple = info["temple"]
    naos = [Vector(p) for p in temple["naos"]]
    axis = (naos[1] - naos[0]).normalized()
    side = Vector((axis.y, -axis.x, 0.0))
    statue = Vector(temple["statue"])
    floor = temple["floor"]
    for key, along, across in (("fig_pretre", 13.5, 2.8), ("fig_citoyen", 10.5, -3.5), ("fig_citoyen_couleur", 7.5,
                                                                                      3.9), ("fig_voyageur", 5.0, -2.2)):
        p = naos[1] - axis * along + side * across
        heading = math.atan2(-(statue.x - p.x), statue.y - p.y)
        placer.items.setdefault(key, []).append(placement(p.x, p.y, floor, heading))
    counts["cella"] = 4
    builds = {**STANDING, **FAR}
    for key, matrices in placer.items.items():
        scene.add_instances("figurants", key, lambda key=key: grounded(builds[key]()), matrices,
                            cast_shadow=key not in FAR, occlusion=False)
    scene.placer = placer
    return counts


def point_in(polygon, x, y):
    from .terrain import point_in_polygon
    return point_in_polygon(x, y, polygon)


def build_camps(scene):
    placer = scene.placer
    rng = random.Random(77)
    counts = {"tente": 0, "tente_peau": 0, "ambassade": 0, "abri": 0}
    for (cx, cy), radius in plan.CAMPS + [plan.ARGIVE_CAMP]:
        rows = int(radius / 9.0)
        for i in range(-rows, rows + 1):
            for j in range(-rows, rows + 1):
                x = cx + i * 9.0 + rng.uniform(-2.5, 2.5)
                y = cy + j * 8.0 + rng.uniform(-2.5, 2.5)
                if math.hypot(x - cx, y - cy) > radius or rng.random() < 0.45 or not placer.free(x, y, 3.0):
                    continue
                if scene.ground.is_bed(x, y):
                    continue
                roll = rng.random()
                key = "tente" if roll < 0.5 else "tente_peau" if roll < 0.75 else "abri" if roll < 0.93 else "ambassade"
                if key == "ambassade" and not placer.free(x, y, 6.0):
                    continue
                heading = math.radians(rng.choice((0.0, 90.0, 180.0, 270.0)) + rng.uniform(-12.0, 12.0))
                placer.add(key, x, y, heading)
                counts[key] += 1
    builds = {"tente": tent, "tente_peau": hide_tent, "ambassade": embassy_tent, "abri": shelter}
    for key, build in builds.items():
        scene.add_instances("campements", key, build, placer.items.get(key, []))
    return counts


def build_trees(scene, info):
    placer = scene.placer
    rng = random.Random(91)
    items = {key: [] for key in TREES}

    def put(key, x, y, gap=3.0, scale=None):
        if any(math.hypot(x - ex, y - ey) < 16.0 for ex, ey in plan.EYES.values()):
            return False
        if not placer.free(x, y, gap):
            return False
        z = scene.ground(x, y)
        placer.placed.append((x, y))
        s = scale if scale is not None else rng.uniform(0.8, 1.2)
        items[key].append(placement(x, y, z - 0.2, rng.uniform(0, 2 * math.pi), s))
        return True

    for k in range(160):
        x, y = rng.uniform(-60.0, 190.0), rng.uniform(-40.0, 150.0)
        if point_in(plan.ALTIS, x, y):
            put(("olivier", "olivier", "platane")[k % 3], x, y, 5.0)
    put("olivier", -40.0, -26.0, 4.0, 1.25)
    for k in range(60):
        x, y = rng.uniform(-14.0, 6.0), rng.uniform(46.0, 74.0)
        if math.hypot(x - plan.PELOPION[0], y - plan.PELOPION[1]) < 11.0:
            put("olivier" if k % 3 else "platane", x, y, 3.5)
    kr = plan.KRONION
    for k in range(900):
        a = rng.uniform(0, 2 * math.pi)
        r = math.sqrt(rng.random()) * 330.0
        x, y = kr[0] + r * math.cos(a), kr[1] + r * math.sin(a)
        if y < 165.0 or point_in(plan.SANCTUARY, x, y):
            continue
        put("pin" if rng.random() < 0.7 else "pin_parasol", x, y, 4.0)
    for k in range(700):
        x, y = rng.uniform(-680.0, 820.0), rng.uniform(-620.0, 780.0)
        if scene.ground(x, y) < scene.ground.level + 14.0 or point_in(plan.SANCTUARY, x, y):
            continue
        if rng.random() < 0.55:
            put("pin" if rng.random() < 0.6 else "pin_parasol", x, y, 5.0)
    from .terrain import polyline_distance
    import numpy as np
    for path, half, count in ((plan.ALPHEIOS, plan.ALPHEIOS_WIDTH / 2, 500), (plan.KLADEOS, 10.0, 160)):
        for k in range(count):
            x, y = rng.uniform(-680.0, 820.0), rng.uniform(-620.0, 780.0)
            d = float(polyline_distance(path, np.array([x]), np.array([y]))[0])
            if half + 2.0 < d < half + 26.0:
                put(("peuplier", "platane", "laurier_rose", "laurier_rose")[k % 4], x, y, 4.0)
    for key, matrices in items.items():
        scene.add_instances("vegetation", key, TREES[key], matrices, cast_shadow=key not in ("laurier_rose",),
                            occlusion=False)
    return {key: len(m) for key, m in items.items()}


def build_offerings(scene):
    placer = scene.placer
    rng = random.Random(55)
    items = {"statue_bronze_a": [], "statue_bronze_b": [], "statue_bronze_c": [], "trepied": [], "stele": [],
             "autel_secondaire": []}
    lines = [((-40.0, -34.0), (50.0, -34.0)), ((48.0, -30.0), (55.0, 40.0)), ((-58.0, 30.0), (-45.0, 100.0)),
             ((75.0, 62.0), (140.0, 96.0)), ((-30.0, 30.0), (20.0, 32.0))]
    for (x0, y0), (x1, y1) in lines:
        length = math.hypot(x1 - x0, y1 - y0)
        heading = math.atan2(-(y1 - y0), -(x1 - x0))
        for k in range(int(length / 3.2)):
            t = (k + 0.5) / int(length / 3.2)
            x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            if not placer.free(x, y, 2.0):
                continue
            roll = rng.random()
            key = ("statue_bronze_a" if roll < 0.3 else "statue_bronze_b" if roll < 0.55 else "statue_bronze_c"
                   if roll < 0.7 else "trepied" if roll < 0.82 else "stele")
            placer.add(key, x, y, heading + math.pi / 2)
    altars = []
    for x, y in ((-40.0, 50.0), (60.0, 30.0), (110.0, 95.0), (-35.0, 10.0), (15.0, 110.0), (80.0, 70.0)):
        if placer.free(x, y, 2.0):
            placer.add("autel_secondaire", x, y, 0.0)
            altars.append((x, y))
    builds = {"statue_bronze_a": lambda: bronze_statue(1), "statue_bronze_b": lambda: bronze_statue(2),
              "statue_bronze_c": lambda: bronze_statue(3), "trepied": tripod, "stele": stele,
              "autel_secondaire": small_altar}
    for key in items:
        scene.add_instances("offrandes", key, builds[key], placer.items.get(key, []), cast_shadow=False)
    return {key: len(placer.items.get(key, [])) for key in items}, altars


def build_rivers(scene):
    builder = MeshBuilder()
    for path, width, step in ((plan.ALPHEIOS, 26.0, 60.0), (plan.KLADEOS, 4.0, 20.0)):
        dense = resample(path, step)
        points = []
        for x, y in dense:
            low = min(scene.ground(x + dx, y + dy) for dx in (-20.0, 0.0, 20.0) for dy in (-20.0, 0.0, 20.0))
            points.append((x, y, low + 0.25))
        builder.sweep(points, [(-width / 2, 0.0), (width / 2, 0.0)], "river", caps=False)
    scene.unique("rivieres", builder, occlusion=False)
    scene.shadowless.add("rivieres")


def points_of_interest(scene, info):
    g = scene.ground
    lens = plan.LENS
    points = {}

    def at(x, y, height):
        return Vector((x, y, g.surface(x, y) + height))
    points["vue-d-ensemble"] = (Vector((450.0, -350.0, g.level + 180.0)), Vector((-20.0, 80.0, g.level + 6.0)), lens)
    points["campements-et-garde"] = (at(200.0, -250.0, 3.0), Vector((150.0, -60.0, g.level + 8.0)), lens)
    altar_top = Vector(info["altar"]["top"])
    points["grand-autel"] = (at(60.0, 50.0, 1.7), altar_top - Vector((0.0, 0.0, 2.0)), lens)
    heraion = info["heraion"]["top"]
    points["heraion-et-pelopion"] = (at(10.0, 85.0, 1.7), Vector((-24.0, 100.0, heraion[2] - 9.0)), lens)
    points["terrasse-des-tresors"] = (at(60.0, 100.0, 1.7), Vector((110.0, 140.0, g.levels["terrace"] + 5.0)), lens)
    eye = plan.stadium_point(95.0, -27.0)
    target = plan.stadium_point(-40.0, 0.0)
    points["stade"] = (at(eye[0], eye[1], 2.4), Vector((target[0], target[1], g.levels["track"] + 3.0)), lens)
    pediment = Vector(info["temple"]["pediment"])
    points["temple-de-zeus"] = (at(75.0, -20.0, 1.7), pediment - Vector((0.0, 0.0, 6.0)), lens)
    temple = info["temple"]
    naos = [Vector(p) for p in temple["naos"]]
    axis = (naos[1] - naos[0]).normalized()
    eye = naos[1] - axis * 6.0 + Vector((0.0, 0.0, 1.7))
    points["zeus-de-phidias"] = (eye, Vector(temple["statue_face"]) - Vector((0.0, 0.0, 3.0)), lens)
    points["atelier-de-phidias"] = (at(-50.0, -32.0, 1.7), Vector((-112.0, 18.0, g(-115.0, 20.0) + 6.0)), lens)
    return points


def place_markers(scene, points):
    root = scene.root("reperes")
    for key, (eye, target, _) in points.items():
        new_empty(f"poi_{key}", scene.collection, root, Matrix.Translation(eye))
        new_empty(f"poi_{key}_target", scene.collection, root, Matrix.Translation(target))


def interior(scene, info):
    temple = info["temple"]
    root = scene.root("reperes")
    sun = sun_vector(*plan.SUN)
    door = Vector(temple["door_centre"])
    floor = temple["floor"]
    entry = Vector((door.x, door.y, floor + 7.5))
    distance = (entry.z - floor) / sun.z
    target = entry - sun * distance
    oculus = entry + sun * 16.0
    new_empty("oculus", scene.collection, root, Matrix.Translation(oculus))
    new_empty("sunbeam_target", scene.collection, root, Matrix.Translation(target))
    naos = [Vector(p) for p in temple["naos"]]
    centre = (naos[0] + naos[1]) / 2
    marker = new_empty("interior", scene.collection, root, Matrix.Translation(centre))
    marker["radius"] = 15.0
    marker["height"] = 15.0
    marker["ambientScale"] = 0.3
    return {"oculus": [round(v, 2) for v in oculus], "sunbeam_target": [round(v, 2) for v in target],
            "interior_centre": [round(v, 2) for v in centre], "beam_length": round((target - entry).length, 2)}


def effects(scene, info, altars):
    root = scene.root("vie")
    g = scene.ground
    smokes = [Vector(info["altar"]["top"]) + Vector((0.0, 0.0, 0.3))]
    p = plan.PRYTANEION
    smokes.append(Vector((p[0] + 3.0, p[1], g(*p) + 7.5)))
    for x, y in altars[:2]:
        smokes.append(Vector((x, y, g(x, y) + 1.3)))
    for (cx, cy), radius in plan.CAMPS[:5]:
        smokes.append(Vector((cx + 10.0, cy - 6.0, g(cx + 10.0, cy - 6.0) + 0.8)))
    for index, point in enumerate(smokes, start=1):
        new_empty(f"smoke_{index}", scene.collection, root, Matrix.Translation(point))
    birds = [(40.0, 60.0, g.level + 45.0), (300.0, -350.0, g.level + 70.0), (25.0, 75.0, g.level + 25.0)]
    for index, point in enumerate(birds, start=1):
        new_empty(f"birds_{index}", scene.collection, root, Matrix.Translation(point))
    return {"smoke": len(smokes), "birds": len(birds)}


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
