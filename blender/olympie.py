import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bpy
from mathutils import Matrix, Vector

from kit import acropole_materials as scene_materials
from kit import olympie_life as life
from kit import olympie_monuments as monuments
from kit import olympie_plan as plan
from kit import olympie_terrain as terrain
from kit.geometry import MeshBuilder, TemplateLibrary, ensure_collection, new_empty, new_object, unique_object
from kit.greek_materials import build_library
from kit.materials import linear_color, principled_material
from kit.stage import camera, configure_render, export_glb, group_statistics, haze_volume, render_still, sun_lamp

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(PROJECT, ".cache", "scenes", "olympie")
PREVIEWS = os.path.join(PROJECT, ".cache", "previews", "olympie")
BLEND = os.path.join(CACHE, "work", "olympie.blend")


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
        self.collection = ensure_collection("Olympie")
        self.roots = {}
        self.pending = {}
        self.pending_instances = {}
        self.shadowless = set()
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


def glowing(name, colour, roughness, metallic, glow):
    material = principled_material(name, colour if metallic else linear_color(colour), roughness, metallic)
    shader = next(node for node in material.node_tree.nodes if node.type == "BSDF_PRINCIPLED")
    base = colour if metallic else linear_color(colour)
    shader.inputs["Emission Color"].default_value = (*[c * glow for c in base], 1.0)
    shader.inputs["Emission Strength"].default_value = 1.0
    return material


def materials(tiles):
    glowing("gold", (1.0, 0.66, 0.22), 0.32, 1.0, float(OPTIONS.get("gold_glow", 0.16)))
    glowing("ivory", (0.95, 0.87, 0.73), 0.42, 0.0, float(OPTIONS.get("ivory_glow", 0.14)))
    for name, colour, roughness in (("ebony", (0.10, 0.07, 0.055), 0.4), ("ash", (0.52, 0.50, 0.47), 0.97),
                                    ("mudbrick", (0.80, 0.70, 0.55), 0.95)):
        principled_material(name, linear_color(colour), roughness)
        tiles[name] = 2.0
    principled_material("bronze_statue", (0.20, 0.12, 0.06), 0.5, 1.0)
    principled_material("dallage_huile", linear_color((0.035, 0.032, 0.03)), 0.06, vertex_color=False)
    tiles["dallage_huile"] = 4.0
    flame = principled_material("flame", linear_color((1.0, 0.45, 0.12)), 0.7, vertex_color=False)
    shader = next(node for node in flame.node_tree.nodes if node.type == "BSDF_PRINCIPLED")
    shader.inputs["Emission Color"].default_value = (*linear_color((1.0, 0.45, 0.12)), 1.0)
    shader.inputs["Emission Strength"].default_value = 2.0
    return tiles


OPTIONS = {}


def build(options):
    started = time.perf_counter()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    tiles = build_library(os.path.join(CACHE, "kit"))
    scene_materials.build(tiles, os.path.join(CACHE, "kit"))
    materials(tiles)
    scene = Scene(tiles)
    report = {}
    scene.ground = terrain.build(scene.collection, scene.root("terrain"), CACHE, new_object, report,
                                 options.get("textures") == "keep")
    print("TERRAIN", round(time.perf_counter() - started, 1), json.dumps(report.get("levels")),
          json.dumps(report.get("heights")), flush=True)
    info = monuments.build(scene)
    life.build_rivers(scene)
    print("MONUMENTS", round(time.perf_counter() - started, 1), flush=True)
    statics = scene.flush()
    scene.ground.add_surface([statics[key] for key in monuments.walkable_groups() if key in statics])
    report["routes"] = life.place_routes(scene, info)
    report["walkers"] = life.build_walkers(scene)
    report["figures"] = life.build_figures(scene, info)
    report["camps"] = life.build_camps(scene)
    report["offerings"], altars = life.build_offerings(scene)
    report["trees"] = life.build_trees(scene, info)
    points = life.points_of_interest(scene, info)
    life.place_markers(scene, points)
    report["interior"] = life.interior(scene, info)
    report["effects"] = life.effects(scene, info, altars)
    report["instances"] = scene.flush_instances()
    report["info"] = info
    report["clearance"] = life.clearance(points)
    print("CLEARANCE", json.dumps(report["clearance"]), flush=True)
    roots = list(scene.roots.values())
    statistics = group_statistics(roots)
    for key, value in statistics.items():
        print("GROUP", key, json.dumps(value), flush=True)
    report["statistics"] = statistics
    if options["export"] == "1":
        glb = os.path.join(CACHE, "olympie.glb")
        report["export_seconds"] = round(export_glb(glb, roots), 1)
        report["glb_bytes"] = os.path.getsize(glb)
        print("GLB", glb, report["glb_bytes"], flush=True)
    report["elevation_source"] = terrain.DEM_URL.format(terrain.DEM_TILE)
    report["elevation_licence"] = terrain.DEM_LICENCE
    report["markers"] = {key: [[round(v, 2) for v in eye], [round(v, 2) for v in target]]
                         for key, (eye, target, _) in points.items()}
    views = dict(points)
    temple = info["temple"]
    face = Vector(temple["statue_face"])
    pool = Vector(temple["pool_centre"])
    views["statue-face"] = (pool + Vector((0.0, 0.0, 6.0)), face, 30.0)
    views["sanctuaire-haut"] = (Vector((260.0, -160.0, scene.ground.level + 70.0)), Vector((20.0, 50.0, scene.ground.level)),
                                30.0)
    bpy.context.scene["preview_views"] = json.dumps({key: [list(eye), list(target), lens]
                                                     for key, (eye, target, lens) in views.items()})
    bpy.context.scene["interior_rig"] = json.dumps({key: temple[key] for key in ("door_centre", "pool_centre",
                                                                                  "statue_face", "naos")})
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
    sky.aerosol_density = 0.8
    world.node_tree.links.new(sky.outputs["Color"], background.inputs["Color"])
    background.inputs["Strength"].default_value = strength
    return world


def interior_rig(stage, rig):
    lights = []
    if not rig:
        return lights
    naos = [Vector(p) for p in rig["naos"]]
    axis = (naos[1] - naos[0]).normalized()
    data = bpy.data.lights.new("pool_bounce", type="AREA")
    data.shape = "RECTANGLE"
    data.size, data.size_y = 6.0, 7.0
    data.energy = float(OPTIONS.get("bounce", 900.0))
    data.color = (1.0, 0.86, 0.66)
    light = new_object("pool_bounce", data, stage)
    light.location = Vector(rig["pool_centre"]) + Vector((0.0, 0.0, 0.1))
    lights.append(light)
    door = new_object("door_sky", bpy.data.lights.new("door_sky", type="AREA"), stage)
    door.data.shape = "RECTANGLE"
    door.data.size, door.data.size_y = 5.0, 9.6
    door.data.energy = float(OPTIONS.get("door", 2500.0))
    door.data.color = (0.9, 0.93, 1.0)
    door.location = Vector(rig["door_centre"]) - axis * 0.6
    door.rotation_euler = (-axis).to_track_quat("-Z", "Y").to_euler()
    lights.append(door)
    return lights


def render_previews(options, views):
    wanted = options["previews"]
    if wanted == "none":
        return {}
    names = list(views) if wanted == "all" else wanted.split(",")
    stage = ensure_collection("Stage")
    world = sky_world(float(options.get("sky", 0.08)))
    lights = interior_rig(stage, json.loads(bpy.context.scene.get("interior_rig", "{}")))
    sun_lamp(stage, plan.SUN[0], plan.SUN[1], float(options.get("sun", 6.5)), (1.0, 0.94, 0.84), 0.53)
    haze = haze_volume(stage, 30000.0, 1200.0, float(options.get("haze", 0.000015)), (0.82, 0.86, 0.94), 0.4)
    configure_render(int(options.get("width", 1280)), int(options.get("height", 720)), options["samples"],
                     exposure=float(options.get("exposure", -0.2)), volumetric_end=25000.0)
    bpy.context.scene.eevee.use_volumetric_shadows = False
    bpy.context.scene.view_settings.view_transform = "Khronos PBR Neutral"
    bpy.context.scene.view_settings.look = "None"
    timings = {}
    for name in names:
        eye, target, lens = views[name]
        rig = camera(stage, f"cam_{name}", Vector(eye), Vector(target), lens=lens)
        inside = name in ("zeus-de-phidias", "statue-face")
        world.node_tree.nodes["Background"].inputs["Strength"].default_value = (
            0.01 if inside else float(options.get("sky", 0.08)))
        haze.hide_render = inside
        for light in lights:
            light.hide_render = not inside
        bpy.context.scene.view_settings.exposure = float(options.get("exposure", -0.2)) + (
            float(options.get("inside_exposure", 0.8)) if inside else 0.0)
        rig.data.clip_start = 0.1 if Vector(eye).z - Vector(target).z < 30 else rig.data.clip_start
        path = os.path.join(PREVIEWS, f"{name}{options.get('tag', '')}.png")
        timings[name] = round(render_still(rig, path), 1)
        print(f"PREVIEW {path} {timings[name]} s", flush=True)
    return timings


def main():
    options = arguments()
    OPTIONS.update(options)
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
