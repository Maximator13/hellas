import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bpy
from mathutils import Matrix, Vector

from kit import acropole_materials as scene_materials
from kit import phare_city as city
from kit import phare_life as life
from kit import phare_plan as plan
from kit import phare_terrain as terrain
from kit import phare_tower as tower
from kit.geometry import MeshBuilder, TemplateLibrary, ensure_collection, new_empty, new_object, unique_object
from kit.greek_materials import build_library
from kit.materials import generated_image, linear_color, principled_material, smooth_stone_pixels
from kit.stage import camera, configure_render, evening_world, export_glb, group_statistics, render_still, sun_lamp

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(PROJECT, ".cache", "scenes", "phare")
PREVIEWS = os.path.join(PROJECT, ".cache", "previews", "phare")
BLEND = os.path.join(CACHE, "work", "phare.blend")


def arguments():
    values = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    options = {"previews": "vue-d-ensemble", "samples": "16", "export": "1", "light": "night"}
    for item in values:
        key, _, value = item.partition("=")
        options[key.lstrip("-")] = value
    options["samples"] = int(options["samples"])
    return options


class Scene:
    def __init__(self, tiles):
        self.tiles = tiles
        self.library = TemplateLibrary(tiles)
        self.collection = ensure_collection("Phare")
        self.roots = {}
        self.pending = {}
        self.pending_instances = {}
        self.shadowless = set()
        self.palace_wings = []
        self.ground = None

    def root(self, name):
        if name not in self.roots:
            self.roots[name] = new_empty(name, self.collection)
        return self.roots[name]

    def unique(self, group, builder, matrix=None, occlusion=True):
        if not occlusion:
            builder.heights = [10.0] * len(builder.positions)
        self.pending.setdefault(group, []).append((builder, matrix if matrix is not None else Matrix.Identity(4)))
        self.root(group)

    def flush(self):
        statics = {}
        for group, items in self.pending.items():
            merged = MeshBuilder()
            for builder, matrix in items:
                merged.merge(builder, matrix, keep_local=True)
            statics[group] = unique_object(f"{group}_static", merged, self.collection, self.root(group), self.tiles,
                                           cast_shadow=group not in self.shadowless)
        self.pending = {}
        return statics

    def add_instances(self, group, key, build, matrices, cast_shadow=True, occlusion=True):
        entry = self.pending_instances.setdefault(key, [group, build, [], cast_shadow, occlusion])
        entry[2].extend(matrices)

    def flush_instances(self):
        counts = {}
        for key, (group, build, matrices, cast_shadow, occlusion) in self.pending_instances.items():
            if matrices:
                self.library.place(key, build, self.collection, self.root(group), matrices, cast_shadow, occlusion)
            counts[key] = len(matrices)
        self.pending_instances = {}
        return counts


def emissive(name, colour, strength):
    material = principled_material(name, linear_color(colour), 0.7, vertex_color=False)
    shader = next(node for node in material.node_tree.nodes if node.type == "BSDF_PRINCIPLED")
    shader.inputs["Emission Color"].default_value = (*linear_color(colour), 1.0)
    shader.inputs["Emission Strength"].default_value = strength
    material.use_backface_culling = False
    return material


def materials(tiles):
    texture_dir = os.path.join(CACHE, "kit", "textures")
    for name in ("terrain_plaine", "terrain_ile", "terrain_far", "ground_rue"):
        principled_material(name, (1.0, 1.0, 1.0), 0.95)
        tiles[name] = 6.0
    quay = generated_image("quay_grain", os.path.join(texture_dir, "quay_grain_v1.jpg"),
                           lambda: smooth_stone_pixels((0.86, 0.82, 0.74), size=256, seed=41))
    principled_material("ground_quai", linear_color((0.86, 0.82, 0.74)), 0.85, 0.0, quay)
    tiles["ground_quai"] = 3.0
    emissive("lamp_glow", (1.0, 0.52, 0.22), 10.0)
    emissive("flame", (1.0, 0.3, 0.06), 2.2)
    return tiles


def build_tower(scene):
    frame = plan.tower_frame()
    scene.tower_frame = frame
    scene.unique("phare", tower.tower(), frame)
    scene.unique("phare", tower.dedication(), frame)
    scene.unique("phare", tower.tritons(), frame)
    scene.unique("phare_feu", tower.flames(), frame, occlusion=False)
    scene.shadowless.add("phare_feu")
    foot = scene.ground(*(frame @ Vector((0.0, -tower.SQUARE_BASE_HALF - plan.RAMP_LENGTH, 0.0))).to_2d())
    scene.unique("phare", tower.ramp(plan.RAMP_LENGTH, max(foot, 1.8) - plan.TOWER_GROUND + 0.1), frame)
    scene.unique("phare_cour", tower.enclosure(), frame)
    outline = [(x, y) for x, y in plan.islet(70.0)]
    scene.unique("phare_cour", tower.rock_base(outline), frame @ Matrix.Rotation(-plan.TOWER_TURN, 4, "Z"))
    return frame @ tower.beacon_position()


def build(options):
    started = time.perf_counter()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    tiles = build_library(os.path.join(CACHE, "kit"))
    scene_materials.build(tiles, os.path.join(CACHE, "kit"))
    materials(tiles)
    scene = Scene(tiles)
    report = {}
    scene.ground = terrain.Ground()
    print("GROUND", round(time.perf_counter() - started, 1), flush=True)
    near, near_triangles = terrain.near_terrain(scene.ground, scene.collection, scene.root("terrain"))
    far, far_triangles = terrain.far_terrain(scene.collection, scene.root("terrain"))
    report["terrain_triangles"] = {"near": near_triangles, "far": far_triangles}
    terrain.water(scene)
    report["quais_m"] = terrain.quays(scene, scene.ground)
    report["rues"] = terrain.street_strips(scene, scene.ground)
    print("TERRAIN", round(time.perf_counter() - started, 1), flush=True)
    eyes = life.eye_points()
    beacon = build_tower(scene)
    hepta_frame, hepta_length, hepta_lamps = city.heptastadion(scene)
    scene.hepta = (hepta_frame, hepta_length)
    royal, palace_lamps, palace_palms = city.royal_quarter(scene, scene.ground, eyes)
    report["royal"] = royal
    report["villes"] = city.houses(scene, scene.ground, eyes)
    report["murs"] = city.city_walls(scene, scene.ground)
    altar, rhakotis_palms, _ = city.rhakotis(scene, scene.ground)
    antirhodos_palms = city.antirhodos(scene, scene.ground)
    report["tombes"] = city.necropolis(scene, scene.ground)
    report["entrepots"] = city.lake_port(scene, scene.ground)
    report["arsenaux"] = city.arsenals(scene, scene.ground)
    palms, broads = city.countryside_trees(scene, scene.ground, eyes)
    scene.add_instances("vegetation", "palmier", lambda: city.palm(12.0, 3), palms + palace_palms + rhakotis_palms + antirhodos_palms,
                        occlusion=False)
    scene.add_instances("vegetation", "sycomore", lambda: city.broad_tree(8.0, 4), broads, occlusion=False)
    lamps = hepta_lamps + palace_lamps + quay_lamps(scene)
    scene.add_instances("vie", "lampe", city.lamp_post, lamps, cast_shadow=False, occlusion=False)
    report["arbres"] = {"palmiers": len(palms) + len(palace_palms) + len(rhakotis_palms), "sycomores": len(broads)}
    report["lampes"] = len(lamps)
    print("CITY", round(time.perf_counter() - started, 1), flush=True)
    report["navires"] = life.build_ships(scene, eyes)
    statics = scene.flush()
    walkable = [near] + [statics[key] for key in ("quais", "heptastade", "phare_cour", "rhakotis", "palais", "phare")
                         if key in statics]
    scene.ground.add_surface(walkable)
    paths = life.routes(scene, (hepta_frame, hepta_length), scene.tower_frame)
    report["routes"] = life.place_routes(scene, paths)
    report["walkers"] = life.build_walkers(scene)
    report["figures"] = life.build_figures(scene, paths, eyes)
    points = life.points_of_interest(scene)
    life.place_markers(scene, points)
    report["effects"] = life.effects(scene, altar, beacon)
    report["instances"] = scene.flush_instances()
    report["clearance"] = life.clearance(points)
    print("CLEARANCE", json.dumps(report["clearance"]), flush=True)
    roots = list(scene.roots.values())
    statistics = group_statistics(roots)
    for key, value in statistics.items():
        print("GROUP", key, json.dumps(value), flush=True)
    report["statistics"] = statistics
    if options["export"] == "1":
        glb = os.path.join(CACHE, "phare.glb")
        report["export_seconds"] = round(export_glb(glb, roots), 1)
        report["glb_bytes"] = os.path.getsize(glb)
        print("GLB", glb, report["glb_bytes"], flush=True)
    report["markers"] = {key: [[round(v, 2) for v in eye], [round(v, 2) for v in target]]
                         for key, (eye, target, _) in points.items()}
    report["tower_height"] = tower.total_height()
    report["beacon"] = [round(v, 2) for v in beacon]
    views = dict(points)
    views["phare-proche"] = (Vector((160.0, -190.0, 40.0)), Vector((0.0, 0.0, 55.0)), plan.LENS)
    views["port-haut"] = (Vector((1500.0, 300.0, 400.0)), Vector((800.0, -900.0, 0.0)), plan.LENS)
    bpy.context.scene["preview_views"] = json.dumps({key: [list(eye), list(target), lens]
                                                     for key, (eye, target, lens) in views.items()})
    bpy.context.scene["beacon"] = list(beacon)
    os.makedirs(os.path.dirname(BLEND), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=BLEND)
    report["build_seconds"] = round(time.perf_counter() - started, 1)
    return report, views


def quay_lamps(scene):
    lamps = []
    line = plan.MAINLAND_SEA[18:36]
    for a, b in zip(line[:-1], line[1:]):
        a, b = Vector(a), Vector(b)
        direction = (b - a).normalized()
        normal = Vector((direction.y, -direction.x))
        if scene.ground.shore(*(a.lerp(b, 0.5) + normal * 10.0)) < 0:
            normal = -normal
        for s in range(10, int((b - a).length), 45):
            p = a + direction * s + normal * 3.0
            lamps.append(Matrix.Translation((p.x, p.y, plan.QUAY_TOP)))
    return lamps


def render_previews(options, views):
    wanted = options["previews"]
    if wanted == "none":
        return {}
    names = list(views) if wanted == "all" else wanted.split(",")
    stage = ensure_collection("Stage")
    night = options["light"] == "night"
    if night:
        evening_world(plan.SKY_SUN[0], plan.SKY_SUN[1], float(options.get("sky", 1.0)), 0.6)
        sun_lamp(stage, plan.MOON[0], plan.MOON[1], float(options.get("moon", 0.25)), (0.62, 0.71, 0.86), 0.5)
        data = bpy.data.lights.new("fire", type="POINT")
        data.energy = float(options.get("fire", 4.0e6))
        data.color = (1.0, 0.65, 0.3)
        data.shadow_soft_size = 1.5
        light = new_object("fire", data, stage)
        light.location = Vector(bpy.context.scene["beacon"])
        exposure = float(options.get("exposure", 2.5))
    else:
        evening_world(288.0, 25.0, 0.08, 0.6)
        sun_lamp(stage, 250.0, 35.0, 6.5, (1.0, 0.95, 0.88), 0.5)
        exposure = -0.2
    configure_render(int(options.get("width", 1280)), int(options.get("height", 720)), options["samples"],
                     exposure=exposure)
    bpy.context.scene.view_settings.view_transform = "Khronos PBR Neutral"
    bpy.context.scene.view_settings.look = "None"
    timings = {}
    for name in names:
        eye, target, lens = views[name]
        rig = camera(stage, f"cam_{name}", Vector(eye), Vector(target), lens=lens)
        rig.data.clip_start = 0.2
        path = os.path.join(PREVIEWS, f"{name}{'' if night else '-jour'}{options.get('tag', '')}.png")
        timings[name] = round(render_still(rig, path), 1)
        print(f"PREVIEW {path} {timings[name]} s", flush=True)
    return timings


def main():
    options = arguments()
    if options.get("reuse") == "1":
        bpy.ops.wm.open_mainfile(filepath=BLEND)
        views = {key: (Vector(eye), Vector(target), lens) for key, (eye, target, lens) in
                 json.loads(bpy.context.scene["preview_views"]).items()}
        print("PREVIEWS", json.dumps(render_previews(options, views)), flush=True)
        return
    report, views = build(options)
    report["previews"] = render_previews(options, views)
    with open(os.path.join(CACHE, "build_report.json"), "w", encoding="utf8") as handle:
        json.dump(report, handle, indent=1, default=str)
    print("TOTAL", report["build_seconds"], flush=True)


if __name__ == "__main__":
    main()
