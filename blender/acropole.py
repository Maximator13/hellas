import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bpy
from mathutils import Matrix, Vector

from kit import acropole_city as city
from kit import acropole_life as life
from kit import acropole_materials as scene_materials
from kit import acropole_monuments as monuments
from kit import acropole_plan as plan
from kit import acropole_terrain as terrain
from kit.geometry import MeshBuilder, TemplateLibrary, ensure_collection, new_empty, new_object, unique_object
from kit.greek_materials import build_library
from kit.stage import camera, configure_render, export_glb, group_statistics, haze_volume, render_still, sun_lamp

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(PROJECT, ".cache", "scenes", "acropole")
PREVIEWS = os.path.join(PROJECT, ".cache", "previews", "acropole")
BLEND = os.path.join(CACHE, "work", "acropole.blend")
PARTS = ("acropole", "pente_sud", "agora", "ville", "vie")


def arguments():
    values = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    options = {"previews": "vue-d-ensemble", "samples": "24", "parts": ",".join(PARTS), "export": "1"}
    for item in values:
        key, _, value = item.partition("=")
        options[key.lstrip("-")] = value
    options["samples"] = int(options["samples"])
    options["parts"] = [part for part in options["parts"].split(",") if part]
    return options


class Scene:
    def __init__(self, tiles):
        self.tiles = tiles
        self.library = TemplateLibrary(tiles)
        self.collection = ensure_collection("Acropole")
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


def build_sea(scene):
    water = MeshBuilder()
    reach = 70000.0
    water.polygon([(-reach, -reach, 0.0), (reach, -reach, 0.0), (reach, reach, 0.0), (-reach, reach, 0.0)], "sea")
    sea = unique_object("sea", water, scene.collection, scene.root("terrain"), scene.tiles, cast_shadow=False,
                        ground_occlusion=False)
    return sea


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


def interior_rig(stage, rig):
    lights = []
    if not rig:
        return lights
    axis = (Vector(rig["naos"][1]) - Vector(rig["naos"][0])).normalized()

    def area(name, location, direction, size, energy, colour):
        data = bpy.data.lights.new(name, type="AREA")
        data.shape = "RECTANGLE"
        data.size, data.size_y = size
        data.energy = energy
        data.color = colour
        light = new_object(name, data, stage)
        light.location = location
        light.rotation_euler = Vector(direction).to_track_quat("-Z", "Y").to_euler()
        lights.append(light)
    door = Vector(rig["door_centre"])
    area("door_sky", door + axis * 0.8, -axis, (4.6, 9.4), float(rig.get("door_power", 2600.0)), (0.82, 0.9, 1.0))
    for index, window in enumerate(rig["windows"]):
        area(f"window_{index}", Vector(window) + axis * 0.7, -axis + Vector((0, 0, -0.3)), (2.4, 2.7), 380.0,
             (0.85, 0.9, 1.0))
    area("pool_bounce", Vector(rig["pool_centre"]) + Vector((0, 0, 0.05)), (0, 0, 1), (9.4, 9.2), 520.0,
         (1.0, 0.9, 0.74))
    for index, side in enumerate((-1, 1)):
        data = bpy.data.lights.new(f"lamp_{index}", type="POINT")
        data.energy = 40.0
        data.color = (1.0, 0.66, 0.36)
        data.shadow_soft_size = 0.05
        light = new_object(f"lamp_{index}", data, stage)
        light.location = Vector(rig["statue"]) + axis * 9.0 + Vector((axis.y, -axis.x, 0.0)) * side * 6.5 + Vector(
            (0, 0, 1.6))
        lights.append(light)
    return lights


def render_previews(options, views):
    wanted = options["previews"]
    if wanted == "none":
        return {}
    names = list(views) if wanted == "all" else wanted.split(",")
    stage = ensure_collection("Stage")
    world = sky_world(float(options.get("sky", 0.08)))
    rig = json.loads(bpy.context.scene.get("interior_rig", "{}"))
    lights = interior_rig(stage, rig)
    sun_lamp(stage, plan.SUN[0], plan.SUN[1], float(options.get("sun", 6.5)), (1.0, 0.95, 0.88), 0.53)
    haze = haze_volume(stage, 40000.0, 1500.0, float(options.get("haze", 0.000012)), (0.78, 0.86, 0.98), 0.4)
    configure_render(1280, 720, options["samples"], exposure=float(options.get("exposure", 0.0)),
                     volumetric_end=30000.0)
    bpy.context.scene.eevee.use_volumetric_shadows = False
    bpy.context.scene.view_settings.view_transform = "Khronos PBR Neutral"
    bpy.context.scene.view_settings.look = "None"
    timings = {}
    for name in names:
        eye, target, lens = views[name]
        rig = camera(stage, f"cam_{name}", eye, target, lens=lens)
        inside = name == "athena-parthenos"
        haze.hide_render = name in options.get("clear", "athena-de-bronze").split(",")
        boost = float(options.get("inside_exposure", 0.0)) if inside else 0.0
        bpy.context.scene.eevee.use_raytracing = inside
        world.node_tree.nodes["Background"].inputs["Strength"].default_value = (
            0.004 if inside else float(options.get("sky", 0.08)))
        for light in lights:
            light.hide_render = not inside
        bpy.context.scene.view_settings.exposure = float(options.get("exposure", -0.2)) + boost
        rig.data.clip_start = 0.1 if eye[2] - target[2] < 30 else rig.data.clip_start
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
    started = time.perf_counter()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    tiles = build_library(os.path.join(CACHE, "kit"))
    scene_materials.build(tiles, os.path.join(CACHE, "kit"))
    scene = Scene(tiles)
    report = {"parts": options["parts"]}
    report["roads"] = city.road_lines()
    scene.ground = terrain.build(scene.collection, scene.root("terrain"), CACHE, monuments.pads(),
                                 monuments.RAMP, monuments.AGORA_POLYGON, new_object, report,
                                 options.get("textures") == "keep")
    del report["roads"]
    build_sea(scene)
    print("TERRAIN", round(time.perf_counter() - started, 1), json.dumps(report.get("triangles")), flush=True)
    info = {}
    if "acropole" in options["parts"]:
        info["acropole"] = monuments.build_acropolis(scene)
        print("ACROPOLE", round(time.perf_counter() - started, 1), flush=True)
    if "pente_sud" in options["parts"]:
        info["pente_sud"] = monuments.build_south_slope(scene)
    if "agora" in options["parts"]:
        info["agora"] = monuments.build_agora(scene)
    if "ville" in options["parts"]:
        info["ville"] = city.build(scene)
        print("VILLE", round(time.perf_counter() - started, 1), flush=True)
    scene.flush()
    scene.ground.add_surface(monuments.walkable(scene))
    points = life.points_of_interest(scene, info)
    life.place_markers(scene, points)
    if "vie" in options["parts"]:
        info["vie"] = life.build(scene, info)
    report["info"] = info
    report["clearance"] = life.clearance(points)
    print("CLEARANCE", json.dumps(report["clearance"]), flush=True)
    roots = list(scene.roots.values())
    statistics = group_statistics(roots)
    for key, value in statistics.items():
        print("GROUP", key, json.dumps(value), flush=True)
    report["statistics"] = statistics
    if options["export"] == "1":
        glb = os.path.join(CACHE, "acropole.glb")
        report["export_seconds"] = round(export_glb(glb, roots), 1)
        report["glb_bytes"] = os.path.getsize(glb)
        print("GLB", glb, report["glb_bytes"], flush=True)
    report["elevation_source"] = [terrain.DEM_URL.format(name) for name in terrain.DEM_TILES.values()]
    report["elevation_licence"] = terrain.DEM_LICENCE
    report["markers"] = {key: [[round(v, 2) for v in eye], [round(v, 2) for v in target]]
                         for key, (eye, target, _) in points.items()}
    views = life.preview_views(points)
    bpy.context.scene["interior_rig"] = json.dumps(info.get("acropole", {}).get("parthenon", {}), default=list)
    bpy.context.scene["preview_views"] = json.dumps({key: [list(eye), list(target), lens]
                                                     for key, (eye, target, lens) in views.items()})
    os.makedirs(os.path.dirname(BLEND), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=BLEND)
    report["build_seconds"] = round(time.perf_counter() - started, 1)
    report["previews"] = render_previews(options, views)
    with open(os.path.join(CACHE, "build_report.json"), "w", encoding="utf8") as handle:
        json.dump(report, handle, indent=1, default=str)
    print("TOTAL", round(time.perf_counter() - started, 1), flush=True)


if __name__ == "__main__":
    main()
