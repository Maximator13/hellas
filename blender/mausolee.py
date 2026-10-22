import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bpy
from mathutils import Matrix, Vector

from kit import acropole_materials as shared_materials
from kit import mausolee_city as city
from kit import mausolee_life as life
from kit import mausolee_monument as monument
from kit import mausolee_plan as plan
from kit import mausolee_terrain as terrain
from kit.colosse_materials import build as colosse_materials
from kit.geometry import MeshBuilder, TemplateLibrary, ensure_collection, new_empty, new_object, unique_object
from kit.greek_materials import build_library
from kit.materials import generated_image, linear_color, principled_material, smooth_stone_pixels
from kit.stage import camera, configure_render, export_glb, group_statistics, haze_volume, render_still, sun_lamp

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(PROJECT, ".cache", "scenes", "mausolee")
PREVIEWS = os.path.join(PROJECT, ".cache", "previews", "mausolee")
BLEND = os.path.join(CACHE, "work", "mausolee.blend")
BLUE_LIMESTONE = (0.55, 0.60, 0.66)


def arguments():
    values = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    options = {"previews": "vue-d-ensemble", "samples": "16", "export": "1"}
    for item in values:
        key, _, value = item.partition("=")
        options[key.lstrip("-")] = value
    options["samples"] = int(options["samples"])
    return options


class Scene:
    def __init__(self, tiles):
        self.tiles = tiles
        self.library = TemplateLibrary(tiles)
        self.collection = ensure_collection("Mausolee")
        self.roots = {}
        self.pending = {}
        self.statics = {}
        self.ground = None
        self.shadowless = set()

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
        for group, items in self.pending.items():
            merged = MeshBuilder()
            for builder, matrix in items:
                merged.merge(builder, matrix, keep_local=True)
            self.statics[group] = unique_object(f"{group}_static", merged, self.collection, self.root(group),
                                                self.tiles, cast_shadow=group not in self.shadowless)
        self.pending = {}

    def instances(self, group, key, build, matrices, cast_shadow=True, occlusion=True):
        if matrices:
            return self.library.place(key, build, self.collection, self.root(group), matrices, cast_shadow, occlusion)
        return None


def materials(tiles):
    texture_dir = os.path.join(CACHE, "kit", "textures")
    stone = generated_image("blue_limestone_grain", os.path.join(texture_dir, "blue_limestone_grain_v1.jpg"),
                            lambda: smooth_stone_pixels(BLUE_LIMESTONE, size=512, seed=41))
    principled_material(monument.BLUE_STONE, linear_color(BLUE_LIMESTONE), 0.7, 0.0, stone)
    tiles[monument.BLUE_STONE] = 2.5
    principled_material(city.SOURCE, linear_color((0.12, 0.26, 0.28)), 0.05, vertex_color=False)
    tiles[city.SOURCE] = 4.0
    return tiles


def build_sea(scene):
    water = MeshBuilder()
    reach = 60000.0
    water.polygon([(-reach, -reach, 0.0), (reach, -reach, 0.0), (reach, reach, 0.0), (-reach, reach, 0.0)], "sea")
    return unique_object("sea", water, scene.collection, scene.root("terrain"), scene.tiles, cast_shadow=False,
                         ground_occlusion=False)


def build(options):
    started = time.perf_counter()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    tiles = build_library(os.path.join(CACHE, "kit"))
    shared_materials.build(tiles, os.path.join(CACHE, "kit"))
    colosse_materials(tiles)
    materials(tiles)
    scene = Scene(tiles)
    report = {}
    scene.ground = terrain.build(scene.collection, scene.root("terrain"), CACHE, city.pads(), city.shaping(),
                                 new_object, report, options.get("textures") == "keep")
    build_sea(scene)
    print("TERRAIN", round(time.perf_counter() - started, 1), json.dumps(report.get("heights")),
          json.dumps(report.get("levels")), json.dumps(report.get("triangles")), flush=True)
    info = {}
    level = city.level(scene, "terrasse")
    info["mausolee"] = monument.build(scene, plan.MAUSOLEUM, level)
    monument.terrace_walls(scene, scene.ground, level)
    info["propylon"] = monument.propylon_site(scene, scene.ground, level)
    info["agora"] = city.agora(scene)
    info["palais"] = city.palace(scene)
    info["salmakis"] = city.salmakis(scene)
    info["ares"] = city.ares(scene)
    info["theatre"] = city.theatre(scene)
    info["murs"] = city.walls(scene)
    info["quai"] = city.quays(scene)
    print("MONUMENTS", round(time.perf_counter() - started, 1), json.dumps(info["mausolee"]), flush=True)
    scene.flush()
    scene.ground.add_surface(city.walkable(scene))
    points = life.points_of_interest(scene, info)
    info["points"] = points
    eyes = [(eye.x, eye.y) for eye, _, _ in points.values()]
    info["maisons"] = city.houses(scene, eyes)
    info["arbres"] = city.trees(scene, eyes)
    info["navires"] = city.ships(scene, info["quai"])
    life.place_markers(scene, points)
    report["life"] = life.build(scene, info)
    scene.flush()
    report["info"] = {key: value for key, value in info.items() if key not in ("points", "quai")}
    report["clearance"] = life.clearance(points)
    print("CLEARANCE", json.dumps(report["clearance"]), flush=True)
    roots = list(scene.roots.values())
    statistics = group_statistics(roots)
    for key, value in statistics.items():
        print("GROUP", key, json.dumps(value), flush=True)
    report["statistics"] = statistics
    if options["export"] == "1":
        glb = os.path.join(CACHE, "mausolee.glb")
        report["export_seconds"] = round(export_glb(glb, roots), 1)
        report["glb_bytes"] = os.path.getsize(glb)
        print("GLB", glb, report["glb_bytes"], flush=True)
    report["elevation_source"] = [terrain.DEM_URL.format(name) for name in terrain.DEM_TILES.values()]
    report["elevation_licence"] = terrain.DEM_LICENCE
    report["markers"] = {key: [[round(v, 2) for v in eye], [round(v, 2) for v in target]]
                         for key, (eye, target, _) in points.items()}
    views = life.preview_views(points, info)
    bpy.context.scene["preview_views"] = json.dumps({key: [list(eye), list(target), lens]
                                                     for key, (eye, target, lens) in views.items()})
    os.makedirs(os.path.dirname(BLEND), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=BLEND)
    report["build_seconds"] = round(time.perf_counter() - started, 1)
    return report, views


def sky_world(strength):
    world = bpy.data.worlds.new("MorningSky")
    bpy.context.scene.world = world
    world.use_nodes = True
    nodes = world.node_tree.nodes
    background = nodes["Background"]
    sky = nodes.new("ShaderNodeTexSky")
    sky.sky_type = "MULTIPLE_SCATTERING"
    sky.sun_elevation = math.radians(plan.SUN[1])
    sky.sun_rotation = math.radians(plan.SUN[0]) % math.tau
    sky.sun_disc = False
    sky.altitude = 100.0
    sky.aerosol_density = 0.6
    world.node_tree.links.new(sky.outputs["Color"], background.inputs["Color"])
    background.inputs["Strength"].default_value = strength
    return world


def render_previews(options, views):
    wanted = options["previews"]
    if wanted == "none":
        return {}
    names = list(views) if wanted == "all" else wanted.split(",")
    stage = ensure_collection("Stage")
    sky_world(float(options.get("sky", 0.08)))
    sun_lamp(stage, plan.SUN[0], plan.SUN[1], float(options.get("sun", 6.0)), (1.0, 0.94, 0.84), 0.53)
    haze_volume(stage, 40000.0, 1500.0, float(options.get("haze", 0.000012)), (0.8, 0.86, 0.96), 0.4)
    configure_render(int(options.get("width", 1280)), int(options.get("height", 720)), options["samples"],
                     volumetric_end=30000.0)
    bpy.context.scene.eevee.use_volumetric_shadows = False
    bpy.context.scene.view_settings.view_transform = "Khronos PBR Neutral"
    bpy.context.scene.view_settings.look = "None"
    bpy.context.scene.view_settings.exposure = float(options.get("exposure", -0.2))
    timings = {}
    for name in names:
        eye, target, lens = views[name]
        rig = camera(stage, f"cam_{name}", Vector(eye), Vector(target), lens=lens)
        rig.data.clip_start = 0.1 if Vector(eye).z - Vector(target).z < 30 else rig.data.clip_start
        path = os.path.join(PREVIEWS, f"{name}{options.get('tag', '')}.png")
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
