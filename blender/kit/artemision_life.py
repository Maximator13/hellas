import math
import random

import numpy as np
from mathutils import Matrix, Vector

from . import artemision_plan as plan
from . import figures as f
from . import phare_ships as ships
from .buildings import cypress, olive_tree, plane_tree, umbrella_pine
from .geometry import MeshBuilder, new_empty, new_object, placement
from .greek_materials import MARBLE, POROS, TERRACOTTA
from .life import animal, pack_animal
from .olympie_life import aleppo_pine, oleander
from .phare_life import kausia, sailor
from .stage import sun_vector
from .terrain import point_in_polygon, polyline_distance

PLASTER = "plaster"
ASHLAR = "ashlar"
WOOD = "dark_wood"
REED = "matte"


def grounded(builder):
    lowest = min(p[2] for p in builder.positions)
    result = MeshBuilder()
    result.merge(builder, Matrix.Translation((0.0, 0.0, -lowest)))
    return result


def scaled(builder, factor):
    result = MeshBuilder()
    result.merge(builder, Matrix.Scale(factor, 4))
    return result


def branch(builder, hand):
    x, y, z = hand
    f.tube(builder, [(x, y, z - 0.1), (x, y + 0.08, z + 0.7)], [0.012, 0.008], f.WOOD, 4)
    for k in range(4):
        f.ellipsoid(builder, (x + 0.04 * (k % 2 * 2 - 1), y + 0.04 + k * 0.02, z + 0.3 + k * 0.12), (0.05, 0.03, 0.08),
                    f.LAUREL, 4, 2)
    f.ellipsoid(builder, (x, y + 0.03, z + 0.18), (0.05, 0.05, 0.05), f.WOOL_WHITE, 5, 3)


def pilgrim(stride=0.0, mantle=f.MADDER):
    builder = f.man_himation(mantle, f.SKIN_SUN, f.HAIR, f.HAIR, stride)
    f.petasos(builder, (0.62, 0.52, 0.34))
    return builder


def pilgrim_woman(stride=0.0):
    return f.woman_peplos(f.WOAD, f.LINEN, stride=stride, veil=f.UNDYED)


def megabyzos(stride=0.0):
    builder = MeshBuilder()
    f.feet_only(builder, stride)
    f.skirt(builder, f.WOOL_WHITE, 1.0, 0.04, 0.19, 0.27, 8)
    f.torso(builder, f.WOOL_WHITE)
    f.tube(builder, [(0.0, 0.0, 1.32), (0.0, 0.0, 0.95), (0.0, 0.0, 0.2)], [0.21, 0.22, 0.28], [f.PURPLE, f.PURPLE],
           7, cap=False, squash=0.74)
    f.arms(builder, (0.24, 0.3, 1.0), (-0.24, 0.12, 0.98), f.WOOL_WHITE, f.SKIN)
    f.head(builder, f.SKIN, f.HAIR)
    f.lathe(builder, [(0.12, 1.66), (0.13, 1.92), (0.1, 2.02), (0.0, 2.04)], f.SAFFRON, 8)
    f.tube(builder, [(0.24, 0.3, 0.1), (0.24, 0.32, 1.7)], [0.014, 0.014], f.GOLD, 4)
    return builder


def neokoros(stride=0.0):
    builder = f.man_himation(f.LINEN, f.SKIN, f.HAIR_GREY, f.HAIR_GREY, stride, right_hand=(0.3, 0.2, 1.0))
    f.tube(builder, [(0.3, 0.22, 0.05), (0.3, 0.24, 1.6)], [0.015, 0.015], f.WOOD, 4)
    f.wreath(builder)
    return builder


def parthenos(stride=0.0):
    return scaled(f.woman_peplos(f.WOOL_WHITE, f.WOOL_WHITE, stride=stride), 0.9)


def suppliant(stride=0.0):
    builder = f.man_himation(f.UNDYED, f.SKIN_SUN, f.HAIR_GREY, f.HAIR_GREY, stride, right_hand=(0.3, 0.12, 1.0))
    branch(builder, (0.3, 0.12, 1.0))
    return builder


def seated(builder):
    result = MeshBuilder()
    moved = []
    for x, y, z in builder.positions:
        if z >= 0.95:
            moved.append((x, y, z - 0.5))
        else:
            t = (0.95 - z) / 0.95
            moved.append((x, y + 0.5 * min(t * 2.0, 1.0), 0.45 - 0.45 * max(t * 2.0 - 1.0, 0.0)))
    copy = MeshBuilder()
    copy.points(moved)
    copy.heights = list(builder.heights)
    for indices, material, smooth, uvs, colour in zip(builder.polygons, builder.polygon_materials,
                                                      builder.polygon_smooth, builder.polygon_uvs,
                                                      builder.polygon_colors):
        copy.face(list(indices), builder.materials[material], smooth, uvs, colour, raw=True)
    result.merge(copy)
    return result


def seated_suppliant(seed):
    builder = f.man_himation(f.UNDYED if seed % 2 else f.WOAD, f.SKIN_SUN, f.HAIR, f.HAIR, 0.0,
                             right_hand=(0.26, 0.2, 1.05))
    branch(builder, (0.26, 0.2, 1.05))
    return seated(builder)


def seated_woman(seed):
    builder = f.woman_peplos(f.MADDER if seed % 2 else f.OLIVE, f.LINEN, veil=f.UNDYED)
    branch(builder, (0.25, 0.08, 0.88))
    return seated(builder)


def child(stride=0.0):
    builder = MeshBuilder()
    f.legs(builder, f.SKIN, stride)
    f.skirt(builder, f.SAFFRON, 1.0, 0.6, 0.18, 0.22)
    f.torso(builder, f.SAFFRON)
    f.arms(builder, (0.27, 0.08, 0.9), (-0.26, 0.08, 0.88), f.SKIN, f.SKIN)
    f.head(builder, f.SKIN, f.HAIR)
    return scaled(builder, 0.66)


def banker():
    builder = f.man_himation(f.SAFFRON, f.SKIN, f.HAIR_GREY, f.HAIR_GREY, right_hand=(0.26, 0.3, 1.0))
    f.box(builder, (0.0, 0.42, 0.95), (0.6, 0.35, 0.3), (0.42, 0.3, 0.2))
    return builder


def macedonian_hat(stride=0.0):
    builder = f.man_himation(f.WOOL_WHITE, f.SKIN, f.HAIR, f.HAIR, stride)
    kausia(builder)
    return builder


WALKERS = {
    "walker_pelerin": lambda: pilgrim(0.16),
    "walker_pelerine": lambda: pilgrim_woman(0.12),
    "walker_megabyze": lambda: megabyzos(0.1),
    "walker_pretre": lambda: neokoros(0.12),
    "walker_parthenos": lambda: parthenos(0.12),
    "walker_suppliant": lambda: suppliant(0.1),
    "walker_marin": lambda: sailor(0.18),
    "walker_porteur": lambda: f.worker(f.UNDYED, f.SKIN_SUN, stride=0.18, carry="amphora"),
    "walker_enfant": lambda: child(0.18),
    "walker_boeuf": lambda: animal("ox"),
    "walker_chevre": lambda: animal("goat"),
    "walker_ane": lambda: pack_animal("donkey"),
}

STANDING = {
    "fig_pelerin": lambda: pilgrim(0.0, f.MADDER),
    "fig_pelerin_b": lambda: pilgrim(0.0, f.OLIVE),
    "fig_citoyen": lambda: f.man_himation(),
    "fig_citoyen_couleur": lambda: f.man_himation(f.WOAD, f.SKIN_SUN, f.HAIR_GREY, f.HAIR_GREY,
                                                  right_hand=(0.3, 0.3, 1.32)),
    "fig_macedonien": lambda: macedonian_hat(),
    "fig_pelerine": lambda: pilgrim_woman(),
    "fig_femme": lambda: f.woman_peplos(),
    "fig_femme_voilee": lambda: f.woman_peplos(f.WOOL_WHITE, f.MADDER, veil=f.MADDER),
    "fig_megabyze": lambda: megabyzos(),
    "fig_pretre": lambda: neokoros(),
    "fig_essene": lambda: f.priest(),
    "fig_parthenos": lambda: parthenos(),
    "fig_porteur": lambda: f.worker(f.MADDER, carry="amphora"),
    "fig_marin": lambda: sailor(),
    "fig_enfant": lambda: child(),
    "fig_banquier": banker,
    "fig_suppliant_assis": lambda: seated_suppliant(1),
    "fig_suppliant_assis_b": lambda: seated_suppliant(2),
    "fig_suppliante_assise": lambda: seated_woman(1),
    "fig_boeuf": lambda: animal("ox"),
    "fig_chevre": lambda: animal("goat"),
    "fig_ane": lambda: pack_animal("donkey"),
    "fig_mouton": lambda: animal("sheep"),
}

FAR = {
    "fig_loin_a": lambda: f.far_infantry(f.WOOL_WHITE, f.WOOL_WHITE, f.HAIR, None, spear_color=None),
    "fig_loin_b": lambda: f.far_infantry(f.MADDER, f.SAFFRON, f.HAIR, None, spear_color=None),
    "fig_loin_c": lambda: f.far_infantry(f.UNDYED, f.SKIN_SUN, f.HAIR, None, spear_color=None),
}


def house(width, depth, height, wall=(0.97, 0.94, 0.88), roof_tint=(1.0, 1.0, 1.0), sock=True):
    builder = MeshBuilder()
    first = len(builder.polygons)
    builder.box((-width / 2, -depth / 2, -1.0), (width / 2, depth / 2, height), PLASTER, bottom=False, top=False)
    builder.tint(first, wall)
    if sock:
        first = len(builder.polygons)
        builder.box((-width / 2 - 0.03, -depth / 2 - 0.03, -1.0), (width / 2 + 0.03, depth / 2 + 0.03, 0.6), PLASTER,
                    bottom=False, top=False)
        builder.tint(first, (0.72, 0.36, 0.26))
    rise = depth / 2 * 0.3
    first = len(builder.polygons)
    outline = [(-depth / 2 - 0.3, height), (depth / 2 + 0.3, height), (0.0, height + rise)]
    piece = MeshBuilder()
    piece.prism(outline, -width / 2 - 0.3, width / 2 + 0.3, TERRACOTTA)
    builder.merge(piece, Matrix(((0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1))))
    builder.tint(first, roof_tint)
    first = len(builder.polygons)
    builder.polygon([(-0.6, -depth / 2 - 0.02, 0.0), (0.6, -depth / 2 - 0.02, 0.0), (0.6, -depth / 2 - 0.02, 2.1),
                     (-0.6, -depth / 2 - 0.02, 2.1)], "shadow_void")
    return builder


def court_house(seed):
    rng = random.Random(seed)
    builder = MeshBuilder()
    w, d = rng.uniform(12.0, 16.0), rng.uniform(11.0, 15.0)
    walls = (0.97, 0.94, 0.88) if seed % 3 else (0.93, 0.8, 0.62)
    builder.merge(house(w, 4.5, rng.uniform(4.0, 5.5), walls), Matrix.Translation((0.0, d / 2 - 2.25, 0.0)))
    builder.merge(house(4.0, d - 4.5, 3.6, walls), Matrix.Translation((-w / 2 + 2.0, -2.25, 0.0)))
    first = len(builder.polygons)
    builder.box((-w / 2 + 4.0, -d / 2, -1.0), (w / 2, -d / 2 + 0.5, 2.4), PLASTER, bottom=False)
    builder.box((w / 2 - 0.5, -d / 2, -1.0), (w / 2, d / 2 - 4.5, 2.4), PLASTER, bottom=False)
    builder.tint(first, walls)
    return builder


def far_house(seed):
    rng = random.Random(seed)
    builder = MeshBuilder()
    w, d, h = rng.uniform(9.0, 14.0), rng.uniform(8.0, 12.0), rng.uniform(4.0, 6.5)
    first = len(builder.polygons)
    builder.box((-w / 2, -d / 2, -2.0), (w / 2, d / 2, h), PLASTER, bottom=False)
    builder.tint(first, (0.95, 0.9, 0.82) if seed % 2 else (0.9, 0.8, 0.66))
    first = len(builder.polygons)
    builder.box((-w / 2 - 0.2, -d / 2 - 0.2, h), (w / 2 + 0.2, d / 2 + 0.2, h + 0.4), TERRACOTTA, bottom=False)
    builder.box((-w / 4, -d / 2 - 0.2, h + 0.4), (w / 4, d / 2 + 0.2, h + 1.2), TERRACOTTA, bottom=False)
    builder.tint(first, (0.95, 0.82, 0.72))
    return builder


def stall(seed):
    rng = random.Random(seed)
    builder = MeshBuilder()
    w, d = 4.0, 3.0
    first = len(builder.polygons)
    builder.box((-w / 2, -d / 2, -0.5), (w / 2, d / 2 - 1.0, 2.6), PLASTER, bottom=False)
    builder.tint(first, (0.93, 0.86, 0.72))
    builder.box((-w / 2, d / 2 - 1.0, 0.0), (w / 2, d / 2 - 0.4, 0.9), WOOD, bottom=False)
    for x in (-w / 2 + 0.1, w / 2 - 0.1):
        builder.box((x - 0.06, d / 2 + 0.8, 0.0), (x + 0.06, d / 2 + 0.92, 2.3), WOOD, bottom=False)
    first = len(builder.polygons)
    builder.polygon([(-w / 2 - 0.2, d / 2 - 1.0, 2.6), (w / 2 + 0.2, d / 2 - 1.0, 2.6), (w / 2 + 0.2, d / 2 + 1.0, 2.2),
                     (-w / 2 - 0.2, d / 2 + 1.0, 2.2)], "velum_linen")
    builder.tint(first, rng.choice(((0.86, 0.78, 0.6), (0.78, 0.46, 0.32), (0.62, 0.66, 0.74))))
    for k in range(5):
        first = len(builder.polygons)
        builder.lathe([(0.0, 0.0), (0.12, 0.05), (0.14, 0.2), (0.05, 0.3), (0.0, 0.32)], 6, "matte",
                      matrix=Matrix.Translation((-1.4 + k * 0.7, d / 2 - 0.7, 0.9)))
        builder.tint(first, (0.72, 0.44, 0.28) if k % 2 else (0.9, 0.86, 0.78))
    return builder


def horos():
    builder = MeshBuilder()
    first = len(builder.polygons)
    builder.box((-0.28, -0.14, -0.4), (0.28, 0.14, 1.5), MARBLE, bottom=False)
    builder.lathe([(0.2, 1.5), (0.0, 1.62)], 4, MARBLE)
    builder.tint(first, (0.94, 0.93, 0.9))
    return builder


def reeds(seed):
    rng = random.Random(seed)
    builder = MeshBuilder()
    for k in range(9):
        a = rng.uniform(0, math.tau)
        r = rng.uniform(0.0, 0.8)
        x, y = r * math.cos(a), r * math.sin(a)
        h = rng.uniform(1.6, 2.8)
        lean = rng.uniform(-0.25, 0.25)
        first = len(builder.polygons)
        builder.prism([(x - 0.03, y - 0.03), (x + 0.03, y - 0.03), (x, y + 0.04)], 0.0, h, REED, bottom=False)
        builder.tint(first, (0.42, 0.48, 0.22) if k % 3 else (0.56, 0.54, 0.32))
        if k % 3 == 0:
            first = len(builder.polygons)
            f.ellipsoid(builder, (x + lean * 0.1, y, h + 0.12), (0.06, 0.06, 0.18), (0.55, 0.46, 0.34), 4, 2)
    return builder


TREES = {
    "olivier": lambda: olive_tree(5.0, 3),
    "platane": lambda: plane_tree(16.0, 5),
    "cypres": lambda: cypress(12.0, 6),
    "pin": lambda: aleppo_pine(11.0, 9),
    "pin_parasol": lambda: umbrella_pine(12.0, 11),
    "tamaris": lambda: oleander(13),
}


def resample(points, spacing=2.6):
    out = [points[0]]
    for a, b in zip(points[:-1], points[1:]):
        count = max(int(math.ceil((Vector(b) - Vector(a)).length / spacing)), 1)
        for k in range(1, count + 1):
            out.append(tuple(Vector(a).lerp(Vector(b), k / count)))
    return out


def routes(info):
    ys = info["temple"]["flank_axes"]
    xs = info["temple"]["front_axes"]
    west, east = (ys[0] + ys[1]) / 2, (ys[-1] + ys[-2]) / 2
    north = (xs[-1] + xs[-2]) / 2
    return {
        "quai": [(-232.0, 60.0), (-215.0, 50.0), (-195.0, 36.0), (-175.0, 28.0), (-150.0, 26.0), (-110.0, 22.0),
                 (-70.0, 14.0)],
        "parvis": [(-200.0, -48.0), (-182.0, -30.0), (-166.0, -26.0), (-125.0, -27.0), (-100.0, -14.0),
                   (-70.0, -6.0)],
        "peristyle": [(west, north), (east, north), (east, -north), (west, -north)],
        "voie": [(-150.0, -90.0), (-260.0, -250.0), (-420.0, -520.0), (-600.0, -800.0), (-760.0, -1000.0),
                 (-950.0, -1360.0), (-1120.0, -1640.0)],
    }


def refine(scene, a, b, depth=0):
    if (b - a).length <= 2.8 or depth > 7:
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
        if name == "peristyle":
            refined = [Vector((x, y, floor)) for x, y in dense]
        else:
            lifted = [Vector((x, y, scene.ground.surface(x, y))) for x, y in dense]
            refined = [lifted[0]]
            for a, b in zip(lifted[:-1], lifted[1:]):
                refined.extend(refine(scene, a, b))
        for index, point in enumerate(refined):
            new_empty(f"walk_{name}_{index:03d}", scene.collection, root, Matrix.Translation(point))
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
        return not any(math.hypot(x - px, y - py) < gap for px, py in self.placed[-4000:])

    def add(self, key, x, y, heading, z=None, scale=1.0):
        z = self.scene.ground.surface(x, y) if z is None else z
        self.placed.append((x, y))
        self.items.setdefault(key, []).append(placement(x, y, z, heading, scale))

    def crowd(self, key, count, centre, radius, face=None, gap=0.9, z=None, test=None):
        done = 0
        for attempt in range(count * 40):
            if done >= count:
                break
            x = centre[0] + self.rng.uniform(-radius, radius)
            y = centre[1] + self.rng.uniform(-radius, radius)
            if math.hypot(x - centre[0], y - centre[1]) > radius or not self.free(x, y, gap):
                continue
            if test is not None and not test(x, y):
                continue
            heading = face(x, y) if face else self.rng.uniform(0, 2 * math.pi)
            self.add(key, x, y, heading + self.rng.uniform(-0.35, 0.35), z)
            done += 1
        return done


def on_land(scene, x, y, margin=0.4):
    return scene.ground(x, y) > margin


def build_figures(scene, info):
    placer = Placer(scene, 200)
    for key, (x, y) in plan.EYES.items():
        placer.block(x, y, 4.0)
    for path in routes(info).values():
        for x, y in resample(path, 4.0):
            placer.block(x, y, 1.2)
    counts = {}
    altar = info["altar"]["top"]
    court = info["altar"]["court"]
    in_court = lambda x, y: abs(x - court[0]) < 13.0 and abs(y - court[1]) < 15.0 and x < altar[0] - 3.4
    mix = ("fig_pelerin", "fig_pelerine", "fig_citoyen", "fig_femme", "fig_citoyen_couleur", "fig_femme_voilee",
           "fig_pelerin_b", "fig_macedonien", "fig_enfant")
    total = 0
    for k in range(70):
        x, y = court[0] + placer.rng.uniform(-13.0, 6.0), court[1] + placer.rng.uniform(-14.0, 14.0)
        if in_court(x, y) and placer.free(x, y, 0.95):
            placer.add(mix[k % len(mix)], x, y, facing(altar[:2])(x, y) + placer.rng.uniform(-0.4, 0.4),
                       court[2])
            total += 1
    total += placer.crowd("fig_megabyze", 1, (altar[0] - 3.8, altar[1]), 0.5, facing(altar[:2]), z=court[2])
    total += placer.crowd("fig_essene", 3, (altar[0] - 4.5, altar[1] - 3.0), 1.6, facing(altar[:2]), z=court[2])
    total += placer.crowd("fig_parthenos", 5, (altar[0] - 5.0, altar[1] + 3.5), 2.0, facing(altar[:2]), z=court[2])
    total += placer.crowd("fig_boeuf", 1, (altar[0] - 6.0, altar[1] - 6.5), 0.8, gap=2.0, z=court[2])
    total += placer.crowd("fig_chevre", 4, (altar[0] - 8.0, altar[1] + 8.0), 2.0, gap=1.0, z=court[2])
    counts["autel"] = total
    parvis = ("fig_pelerin", "fig_pelerine", "fig_citoyen", "fig_femme", "fig_citoyen_couleur", "fig_porteur",
              "fig_pelerin_b", "fig_enfant", "fig_femme_voilee", "fig_macedonien")
    total = 0
    x0, x1, y0, y1 = plan.PARVIS
    for k in range(260):
        x, y = placer.rng.uniform(x0 - 30.0, x1 - 2.0), placer.rng.uniform(y0 - 10.0, y1 + 10.0)
        if abs(x - court[0]) < 19.0 and abs(y - court[1]) < 23.0:
            continue
        if not on_land(scene, x, y, 1.0) or not placer.free(x, y, 1.1):
            continue
        placer.add(parvis[k % len(parvis)], x, y, placer.rng.uniform(0, 2 * math.pi))
        total += 1
        if total >= 75:
            break
    total += placer.crowd("fig_boeuf", 3, (-175.0, -40.0), 6.0, gap=2.4)
    total += placer.crowd("fig_ane", 3, (-200.0, 20.0), 6.0, gap=2.0)
    total += placer.crowd("fig_mouton", 6, (-178.0, 46.0), 5.0, gap=1.2)
    counts["parvis"] = total
    total = 0
    edge = -plan.PLATFORM[0] / 2
    north = plan.PLATFORM[1] / 2
    floor = info["temple"]["floor"]
    keys = ("fig_suppliant_assis", "fig_suppliante_assise", "fig_suppliant_assis_b")
    for k in range(60):
        step = placer.rng.randint(2, 9)
        x = edge + step * 0.55 + 0.25
        y = placer.rng.uniform(-30.0, 31.0)
        if abs(y) < 5.5 or not placer.free(x, y, 1.1):
            continue
        placer.add(keys[k % 3], x, y, math.pi / 2 + placer.rng.uniform(-0.3, 0.3))
        total += 1
        if total >= 12:
            break
    for k in range(60):
        step = placer.rng.randint(2, 9)
        x = placer.rng.uniform(edge + 6.0, -38.0)
        y = north - step * 0.55 - 0.25
        if not placer.free(x, y, 1.1):
            continue
        placer.add(keys[(k + 1) % 3], x, y, placer.rng.uniform(-0.3, 0.3))
        total += 1
        if total >= 22:
            break
    look = (-84.0, 52.0)
    total += placer.crowd("fig_megabyze", 1, (-70.0, 41.0), 0.5, facing(look))
    total += placer.crowd("fig_parthenos", 5, (-68.5, 38.5), 3.0, facing(look), gap=1.0)
    total += placer.crowd("fig_essene", 1, (-72.5, 39.0), 0.8, facing((-70.0, 41.0)))
    total += placer.crowd("fig_pretre", 2, (-47.0, 21.0), 3.0, z=floor)
    total += placer.crowd("fig_banquier", 1, (-46.0, -9.0), 1.0, facing((-60.0, -9.0)), z=floor)
    peristyle = ("fig_pelerin", "fig_pelerine", "fig_citoyen", "fig_femme_voilee")
    for k in range(12):
        x = placer.rng.uniform(-52.0, 50.0)
        y = (1 if k % 2 else -1) * placer.rng.uniform(19.5, 22.5)
        if placer.free(x, y, 1.2):
            placer.add(peristyle[k % 4], x, y, placer.rng.uniform(0, 2 * math.pi), floor)
            total += 1
    counts["temple"] = total
    total = 0
    for key, n in (("fig_marin", 10), ("fig_porteur", 8), ("fig_pelerin", 5), ("fig_pelerine", 3)):
        total += placer.crowd(key, n, (-222.0, 30.0), 22.0, test=lambda x, y: scene.ground(x, y) > 0.6)
    total += placer.crowd("fig_ane", 3, (-215.0, 70.0), 8.0, gap=2.0, test=lambda x, y: scene.ground(x, y) > 0.6)
    counts["port"] = total
    naos = [Vector(p) for p in info["temple"]["naos"]]
    statue = Vector(info["temple"]["statue_front"])
    for key, x, y in (("fig_megabyze", 18.5, 1.6), ("fig_parthenos", 17.5, -2.2), ("fig_parthenos", 16.8, -3.4),
                      ("fig_pelerine", 12.0, 3.0)):
        heading = math.atan2(-(statue.x - x), statue.y - y)
        placer.items.setdefault(key, []).append(placement(x, y, naos[0].z, heading))
    counts["sekos"] = 4
    total = 0
    for k in range(400):
        x, y = placer.rng.uniform(-2600.0, -1000.0), placer.rng.uniform(-2300.0, -500.0)
        if not plan.in_city(x, y) or not on_land(scene, x, y, 2.0):
            continue
        placer.add(("fig_loin_a", "fig_loin_b", "fig_loin_c")[k % 3], x, y, placer.rng.uniform(0, 6.28))
        total += 1
    counts["ville"] = total
    builds = {**STANDING, **FAR}
    for key, matrices in placer.items.items():
        scene.add_instances("figurants", key, lambda key=key: grounded(builds[key]()), matrices,
                            cast_shadow=key not in FAR, occlusion=False)
    scene.placer = placer
    return counts


def temenos(scene, info):
    rng = random.Random(31)
    houses = {k: [] for k in range(4)}
    stalls = {k: [] for k in range(3)}
    placer = scene.placer
    for x, y in ((-150.0, 58.0), (-136.0, 58.0), (-122.0, 58.0), (-108.0, 58.0), (-150.0, -58.0), (-136.0, -58.0),
                 (-122.0, -58.0), (-108.0, -58.0), (-94.0, -58.0), (-190.0, -64.0), (-176.0, -64.0)):
        heading = 0.0 if y < 0 else math.pi
        if placer.free(x, y, 3.0):
            stalls[len(placer.placed) % 3].append(placement(x, y, scene.ground(x, y), heading))
            placer.block(x, y, 3.0)
    sites = []
    for k in range(70):
        x, y = rng.uniform(-200.0, 200.0), rng.uniform(-190.0, 190.0)
        if abs(x) < 85.0 and abs(y) < 50.0:
            continue
        if x < -45.0 and abs(y) < 75.0:
            continue
        if math.hypot(x - plan.AYASOLUK[0], y - plan.AYASOLUK[1]) < 330.0 or not on_land(scene, x, y, 1.2):
            continue
        if any(math.hypot(x - sx, y - sy) < 24.0 for sx, sy in sites) or not placer.free(x, y, 10.0):
            continue
        sites.append((x, y))
        placer.block(x, y, 10.0)
        houses[k % 4].append(placement(x, y, scene.ground(x, y), rng.choice((0.0, math.pi / 2, math.pi, -math.pi / 2))))
    for k, matrices in houses.items():
        scene.add_instances("temenos", f"maison_pretre_{k}", lambda k=k: court_house(70 + k), matrices)
    for k, matrices in stalls.items():
        scene.add_instances("temenos", f"echoppe_{k}", lambda k=k: stall(k), matrices, cast_shadow=False)
    horoi = []
    for k in range(48):
        a = math.tau * k / 48
        x, y = 210.0 * math.cos(a), 190.0 * math.sin(a)
        if on_land(scene, x, y, 1.0) and math.hypot(x - plan.AYASOLUK[0], y - plan.AYASOLUK[1]) > 280.0:
            horoi.append(placement(x, y, scene.ground(x, y), a))
    scene.add_instances("temenos", "borne_asile", horos, horoi, cast_shadow=False)
    return {"houses": len(sites), "stalls": sum(len(v) for v in stalls.values()), "horoi": len(horoi),
            "stall_sites": [list(m.translation) for v in stalls.values() for m in v][:3]}


def harbour(scene):
    builder = MeshBuilder()
    points = [(x, y, 0.0) for x, y in plan.QUAY]
    top = max(scene.ground(x + 8.0, y) for x, y in plan.QUAY)
    top = max(min(top, 1.6), plan.QUAY_TOP)
    first = len(builder.polygons)
    builder.sweep(points, [(0.0, -2.5), (0.0, top), (6.0, top), (6.0, -2.5)], ASHLAR, caps=True)
    builder.tint(first, (0.9, 0.84, 0.72))
    for k in range(10):
        x, y = plan.QUAY[1][0] + 0.5, -40.0 + k * 17.0
        builder.lathe([(0.18, top), (0.2, top + 0.7), (0.0, top + 0.75)], 6, POROS,
                      matrix=Matrix.Translation((x, y, 0.0)))
    for k in range(3):
        y = -30.0 + k * 50.0
        x = plan.QUAY[1][0] + 18.0
        first = len(builder.polygons)
        builder.merge(house(12.0, 7.0, 4.2, (0.92, 0.86, 0.74)), Matrix.Translation((x, y, scene.ground(x, y)))
                      @ Matrix.Rotation(math.pi / 2, 4, "Z"))
    scene.unique("port", builder)
    boats = {"barque": [], "navire_amarre": [], "navire_voile": [], "allege": []}
    for k, (x, y, bearing) in enumerate(((-251.0, -20.0, 10.0), (-252.0, 4.0, 170.0), (-262.0, 40.0, 30.0),
                                         (-250.0, 100.0, 200.0), (-330.0, 120.0, 250.0), (-300.0, -10.0, 300.0),
                                         (-360.0, 40.0, 80.0))):
        boats["barque"].append(ships.heading_matrix(x, y, bearing))
    boats["navire_amarre"].append(ships.heading_matrix(-262.0, 118.0, 5.0))
    boats["allege"].append(ships.heading_matrix(-256.0, -45.0, 175.0))
    boats["navire_amarre"].append(ships.heading_matrix(plan.CITY_HARBOUR[0] - 60.0, plan.CITY_HARBOUR[1] + 30.0, 80.0))
    boats["navire_amarre"].append(ships.heading_matrix(plan.CITY_HARBOUR[0] - 30.0, plan.CITY_HARBOUR[1] - 40.0,
                                                       260.0))
    for x, y, bearing in ((-900.0, 300.0, 70.0), (-2200.0, 900.0, 110.0), (-3600.0, -300.0, 60.0)):
        boats["navire_voile"].append(ships.heading_matrix(x, y, bearing))
    builds = {"barque": lambda: ships.fishing_boat(4), "navire_amarre": lambda: ships.merchant(2, False, 20.0, 6.6),
              "navire_voile": lambda: ships.merchant(1, True), "allege": lambda: ships.lighter(5)}
    for key, matrices in boats.items():
        far = key == "navire_voile"
        scene.add_instances("port", key, builds[key], matrices, cast_shadow=not far, occlusion=False)
    return {"quay_top": round(top, 2), "boats": {k: len(v) for k, v in boats.items()}}


def wall_runs(scene, points, step=12.0):
    closed = points + points[:1]
    runs, current = [], []
    for a, b in zip(closed[:-1], closed[1:]):
        length = math.hypot(b[0] - a[0], b[1] - a[1])
        n = max(int(length / step), 1)
        for k in range(n):
            x = a[0] + (b[0] - a[0]) * k / n
            y = a[1] + (b[1] - a[1]) * k / n
            z = scene.ground(x, y)
            if z > 1.0:
                current.append((x, y, z))
            elif len(current) > 1:
                runs.append(current)
                current = []
            else:
                current = []
    if len(current) > 1:
        runs.append(current)
    return runs


def square_tower():
    builder = MeshBuilder()
    first = len(builder.polygons)
    builder.box((-3.5, -3.5, -4.0), (3.5, 3.5, 11.0), ASHLAR, bottom=False)
    builder.tint(first, (0.9, 0.84, 0.74))
    for k in range(4):
        rotation = Matrix.Rotation(k * math.pi / 2, 4, "Z")
        for j in range(3):
            builder.box((-3.3 + j * 2.6, 3.45, 11.0), (-2.5 + j * 2.6, 3.6, 12.0), ASHLAR, matrix=rotation,
                        bottom=False)
    return builder


def city(scene):
    total = 0.0
    towers = []
    for run in wall_runs(scene, plan.CITY_WALL):
        builder = MeshBuilder()
        builder.sweep(run, [(1.6, -5.0), (1.6, 7.5), (-1.6, 7.5), (-1.6, -5.0)], ASHLAR)
        builder.tint(0, (0.92, 0.86, 0.76))
        scene.unique("ville", builder)
        walked, next_tower = 0.0, 40.0
        for a, b in zip(run[:-1], run[1:]):
            length = math.hypot(b[0] - a[0], b[1] - a[1])
            while walked + length >= next_tower:
                t = (next_tower - walked) / length
                x, y = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
                towers.append(placement(x, y, scene.ground(x, y), math.atan2(b[1] - a[1], b[0] - a[0])))
                next_tower += 85.0
            walked += length
        total += walked
    scene.add_instances("ville", "tour", square_tower, towers, cast_shadow=False)
    rng = random.Random(5)
    matrices = {k: [] for k in range(6)}
    cell = 21.0
    agora = (-2028.0, -1080.0)
    for y in np.arange(-2400.0, -350.0, cell):
        for x in np.arange(-3300.0, -700.0, cell):
            x += rng.uniform(-3.0, 3.0)
            y2 = y + rng.uniform(-3.0, 3.0)
            if not plan.in_city(x, y2) or math.hypot(x - agora[0], y2 - agora[1]) < 55.0:
                continue
            if math.hypot(x - plan.THEATRE[0], y2 - plan.THEATRE[1]) < 60.0:
                continue
            corners = [scene.ground(x + 6.0 * c, y2 + 6.0 * s) for c, s in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
            if min(corners) < 1.5 or max(corners) - min(corners) > 4.0 or max(corners) > 115.0:
                continue
            if rng.random() < 0.3:
                continue
            matrices[rng.randrange(6)].append(placement(x, y2, min(corners), rng.choice((0.0, math.pi / 2)) + 0.25))
    for k, items in matrices.items():
        scene.add_instances("ville", f"maison_ville_{k}", lambda k=k: far_house(500 + k), items, cast_shadow=False,
                            occlusion=False)
    scene.shadowless.add("ville")
    return {"wall_length": round(total), "towers": len(towers), "houses": sum(len(v) for v in matrices.values())}


def rivers(scene):
    builder = MeshBuilder()
    for path, width in ((plan.SELINOUS, 6.0), (plan.MARNAS, 7.0)):
        dense = resample(path, 12.0)
        run = []
        for x, y in dense:
            low = min(scene.ground(x + dx, y + dy) for dx in (-6.0, 0.0, 6.0) for dy in (-6.0, 0.0, 6.0))
            if low < 0.2:
                break
            run.append((x, y, max(low + 0.12, 0.05)))
        if len(run) > 1:
            builder.sweep(run, [(-width / 2, 0.0), (width / 2, 0.0)], "river", caps=False)
    scene.unique("rivieres", builder, occlusion=False)
    scene.shadowless.add("rivieres")


def eye_clear(x, y, gap=14.0):
    if math.hypot(x - plan.AYASOLUK[0], y - plan.AYASOLUK[1]) < 140.0:
        return False
    return all(math.hypot(x - ex, y - ey) > gap for ex, ey in plan.EYES.values())


def build_trees(scene, info):
    rng = random.Random(91)
    placer = scene.placer
    items = {key: [] for key in TREES}
    reed_items = {k: [] for k in range(3)}

    def put(key, x, y, gap=3.0, scale=None):
        if not eye_clear(x, y) or not placer.free(x, y, gap):
            return False
        z = scene.ground(x, y)
        placer.placed.append((x, y))
        s = scale if scale is not None else rng.uniform(0.8, 1.2)
        items[key].append(placement(x, y, z - 0.2, rng.uniform(0, 2 * math.pi), s))
        return True

    ax, ay = plan.AYASOLUK
    for k in range(700):
        a = rng.uniform(0, math.tau)
        r = math.sqrt(rng.random()) * 420.0
        x, y = ax + r * math.cos(a), ay + r * math.sin(a)
        z = scene.ground(x, y)
        if z < 4.0 or z > 70.0 or math.hypot(x, y) < 230.0:
            continue
        put("olivier" if rng.random() < 0.8 else "cypres", x, y, 7.0)
    for k in range(1600):
        x, y = rng.uniform(-2200.0, -600.0), rng.uniform(-1800.0, -350.0)
        z = scene.ground(x, y)
        if z < 12.0 or plan.in_city(x, y) and z < 90.0:
            continue
        if rng.random() < 0.5:
            put("pin" if z > 60.0 else "olivier", x, y, 8.0)
    for k in range(900):
        x, y = rng.uniform(-1000.0, 800.0), rng.uniform(-1800.0, 300.0)
        d = float(polyline_distance(plan.SELINOUS, np.array([x]), np.array([y]))[0])
        dm = float(polyline_distance(plan.MARNAS, np.array([x]), np.array([y]))[0])
        if 5.0 < min(d, dm) < 30.0 and scene.ground(x, y) > 0.8 and math.hypot(x + 60, y) > 140.0:
            put(("platane", "tamaris", "tamaris", "platane")[k % 4], x, y, 6.0)
    for k in range(500):
        x, y = rng.uniform(100.0, 800.0), rng.uniform(-1500.0, 200.0)
        if scene.ground(x, y) > 1.5 and rng.random() < 0.5:
            put("olivier", x, y, 8.0)
    for x, y in ((-30.0, 70.0), (20.0, 72.0), (-30.0, -70.0), (25.0, -72.0), (95.0, 40.0), (95.0, -35.0),
                 (-200.0, 70.0), (-205.0, -75.0), (120.0, 10.0)):
        put("cypres", x, y, 2.0, 1.1)
    count = 0
    for k in range(9000):
        x, y = rng.uniform(-700.0, 800.0), rng.uniform(-200.0, 1200.0)
        z = scene.ground(x, y)
        if not (-0.1 < z < 1.2) or not eye_clear(x, y, 25.0) or plan.in_sea_zone(x, y):
            continue
        if math.hypot(x + 40, y) < 230.0:
            continue
        reed_items[k % 3].append(placement(x, y, z - 0.1, rng.uniform(0, 6.28), rng.uniform(0.8, 1.3)))
        count += 1
        if count > 1300:
            break
    for key, matrices in items.items():
        scene.add_instances("vegetation", key, TREES[key], matrices, cast_shadow=key in ("platane", "cypres"),
                            occlusion=False)
    for k, matrices in reed_items.items():
        scene.add_instances("vegetation", f"roseaux_{k}", lambda k=k: reeds(k), matrices, cast_shadow=False,
                            occlusion=False)
    report = {key: len(m) for key, m in items.items()}
    report["roseaux"] = count
    return report


def points_of_interest(scene, info):
    g = scene.ground
    lens = plan.LENS
    temple = info["temple"]
    level = temple["level"]

    def at(x, y, height):
        return Vector((x, y, g.surface(x, y) + height))

    points = {}
    points["vue-d-ensemble"] = (Vector((-1100.0, 1100.0, 380.0)), Vector((-80.0, -120.0, 0.0)), lens)
    points["port-sacre"] = (Vector((-300.0, 60.0, 2.0)), Vector((-63.0, 0.0, level + 15.0)), lens)
    points["autel"] = (at(-180.0, 20.0, 1.7), Vector((-130.0, 0.0, level + 3.5)), lens)
    points["facade-ouest"] = (at(-110.0, -20.0, 1.7), Vector((-63.0, 0.0, level + 15.0)), lens)
    xs = temple["front_axes"]
    column_x = temple["flank_axes"][0]
    points["colonnes-sculptees"] = (at(column_x - 5.6, xs[4] + 6.4, 1.7),
                                    Vector((column_x, xs[4], temple["floor"] + 1.5)), lens)
    points["megabyze-et-asile"] = (at(-84.0, 52.0, 2.4), Vector((-60.0, 31.0, level + 2.0)), lens)
    points["statue-de-culte"] = (Vector((-5.0, 0.0, temple["floor"] + 1.7)), Vector(temple["statue_face"]), lens)
    summit = g(*plan.AYASOLUK)
    target = Vector((-1500.0, -1250.0, g(-1500.0, -1250.0) - 20.0))
    heading = (target.to_2d() - Vector(plan.AYASOLUK)).normalized()
    brow = Vector(plan.AYASOLUK)
    for k in range(1, 60):
        candidate = Vector(plan.AYASOLUK) + heading * (5.0 * k)
        brow = candidate
        if g(candidate.x, candidate.y) < summit - 7.0:
            break
    points["ville-de-lysimaque"] = (at(brow.x, brow.y, 1.7), target, lens)
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
    entry = Vector((door.x, door.y, floor + 6.5))
    distance = (entry.z - floor) / sun.z
    target = entry - sun * distance
    oculus = entry + sun * 16.0
    new_empty("oculus", scene.collection, root, Matrix.Translation(oculus))
    new_empty("sunbeam_target", scene.collection, root, Matrix.Translation(target))
    naos = [Vector(p) for p in temple["naos"]]
    centre = (naos[0] + naos[1]) / 2
    marker = new_empty("interior", scene.collection, root, Matrix.Translation(centre))
    marker["radius"] = 24.0
    marker["height"] = 19.0
    marker["ambientScale"] = 0.25
    return {"oculus": [round(v, 2) for v in oculus], "sunbeam_target": [round(v, 2) for v in target],
            "interior_centre": [round(v, 2) for v in centre], "beam_length": round((target - entry).length, 2)}


def effects(scene, info, temenos_info):
    root = scene.root("vie")
    g = scene.ground
    smokes = [Vector(info["altar"]["top"]) + Vector((0.0, 0.0, 0.4))]
    for x, y, z in temenos_info["stall_sites"][:2]:
        smokes.append(Vector((x, y, z + 0.4)))
    for x, y in ((-1700.0, -1200.0), (-2200.0, -1500.0), (-1450.0, -1700.0)):
        smokes.append(Vector((x, y, g(x, y) + 7.0)))
    smokes.append(Vector((-330.0, 120.0, 1.2)))
    for index, point in enumerate(smokes, start=1):
        new_empty(f"smoke_{index}", scene.collection, root, Matrix.Translation(point))
    level = info["temple"]["level"]
    birds = [(0.0, 0.0, level + 42.0), (150.0, 950.0, 14.0), (700.0, 2100.0, 60.0), (-330.0, 50.0, 22.0)]
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
