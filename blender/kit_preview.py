import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bpy
from mathutils import Matrix

from kit import figures, greek
from kit.geometry import TemplateLibrary, ensure_collection, new_object, placement
from kit.greek_materials import build_library
from kit.materials import linear_color, principled_material
from kit.stage import camera, configure_render, evening_world, export_glb, render_still, sun_lamp, triangles_of

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(PROJECT, ".cache", "previews", "kit")
SUN = (35.0, 48.0)
VIEWS = {
    "temple": ((-46.0, 82.0, 17.0), (0.0, 8.0, 8.0), 35.0),
    "corner": ((-24.0, 47.0, 2.4), (-13.5, 33.5, 11.5), 32.0),
    "figures": ((0.0, 60.0, 2.6), (0.0, 46.5, 0.9), 32.0),
    "stoa": ((22.0, 40.0, 7.0), (46.0, 10.0, 4.0), 30.0),
    "propylon": ((-21.0, 27.0, 6.0), (-46.0, 0.0, 7.0), 30.0),
    "pteroma": ((-11.8, 25.0, 3.0), (-14.0, 33.0, 12.8), 24.0),
}


def arguments():
    values = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    options = {"previews": "temple,corner,figures,stoa,propylon", "samples": "32", "detail": "high", "polychromy": "1"}
    for item in values:
        key, _, value = item.partition("=")
        options[key.lstrip("-")] = value
    return options


def ground(collection):
    principled_material("ground", linear_color((0.66, 0.58, 0.45)), 0.95, vertex_color=False)
    mesh = bpy.data.meshes.new("ground")
    half = 300.0
    mesh.from_pydata([(-half, -half, 0.0), (half, -half, 0.0), (half, half, 0.0), (-half, half, 0.0)], [],
                     [(0, 1, 2, 3)])
    mesh.materials.append(bpy.data.materials["ground"])
    return new_object("ground", mesh, collection)


def check_frieze(building):
    metopes = building.info["metopes_per_side"]
    assert metopes == [14, 32, 14, 32], metopes
    assert sum(metopes) == 92


def place_figures(library, collection, root, templates, row_y, spacing, depth=1):
    report = {}
    names = list(templates)
    start = -spacing * (len(names) - 1) / 2
    for index, name in enumerate(names):
        mesh = library.mesh(name, templates[name], ground_occlusion=False)
        lowest = min(vertex.co.z for vertex in mesh.vertices)
        assert abs(lowest) < 1e-5, (name, lowest)
        new_object(name, mesh, collection, root, placement(start + index * spacing, row_y, 0.0))
        for rank in range(1, depth):
            new_object(f"row_{name}.{rank}", mesh, collection, root,
                       placement(start + index * spacing, row_y - rank * 1.1, 0.0))
        report[name] = triangles_of(mesh)
    return report


def troop_templates(index):
    return {f"troop_{kind}" + ("_far" if index else ""): builds[index] for kind, builds in figures.TROOPS.items()}


def render_previews(options, stage):
    timings = {}
    for name in [item for item in options["previews"].split(",") if item]:
        eye, target, lens = VIEWS[name]
        rig = camera(stage, f"cam_{name}", eye, target, lens=lens)
        rig.data.clip_start = 0.1
        path = os.path.join(CACHE, f"{name}{options.get('tag', '')}.png")
        timings[name] = round(render_still(rig, path), 1)
        print(f"PREVIEW {path} {timings[name]} s", flush=True)
    return timings


def main():
    options = arguments()
    started = time.perf_counter()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    tiles = build_library(CACHE)
    library = TemplateLibrary(tiles)
    scene = ensure_collection("Kit")
    stage = ensure_collection("Stage")
    ground(stage)
    polychromy = options["polychromy"] == "1"
    detail = options["detail"]
    temple = greek.temple(greek.PARTHENON, polychromy, detail, "parthenon")
    check_frieze(temple)
    hall = greek.stoa(polychromy=polychromy, detail=detail)
    gate = greek.propylon(polychromy=polychromy, detail=detail)
    roots = [greek.place_building(temple, library, scene, tiles),
             greek.place_building(hall, library, scene, tiles, matrix=placement(48.0, 12.0, 0.0, math.pi / 2)),
             greek.place_building(gate, library, scene, tiles, matrix=placement(-46.0, 0.0, 0.0, -math.pi / 2))]
    people = new_object("figures", None, scene)
    roots.append(people)
    counts = {"civilians": place_figures(library, scene, people, {**figures.CIVILIANS, **figures.WALKERS}, 45.0, 1.1),
              "troops": place_figures(library, scene, people, troop_templates(0), 50.0, 1.7, 3),
              "far": place_figures(library, scene, people, troop_templates(1), 42.0, 1.7)}
    for root in roots[:3]:
        for child in root.children_recursive:
            if child.type == "MESH" and child.name.endswith("_body"):
                counts.setdefault("bodies", {})[child.name] = triangles_of(child.data)
    counts["columns"] = {key: triangles_of(mesh) for key, mesh in library.meshes.items()
                         if key.startswith(("doric", "ionic"))}
    for group, values in counts.items():
        for key, value in values.items():
            print(f"TRIANGLES {group} {key} {value}", flush=True)
    print("INFO parthenon", json.dumps({k: v for k, v in temple.info.items() if k != "sekos"}), flush=True)
    print("INFO stoa", json.dumps(hall.info), flush=True)
    print("INFO propylon", json.dumps(gate.info, default=str), flush=True)
    glb = os.path.join(CACHE, "kit.glb")
    export_seconds = export_glb(glb, roots)
    print(f"GLB {glb} {os.path.getsize(glb)} bytes {export_seconds:.1f} s", flush=True)
    evening_world(SUN[0], SUN[1], float(options.get("sky", 0.1)), 0.6)
    sun_lamp(stage, SUN[0], SUN[1], float(options.get("sun", 5.0)), (1.0, 0.97, 0.92), 0.53)
    configure_render(1280, 720, int(options["samples"]), exposure=float(options.get("exposure", 0.0)))
    bpy.context.scene.view_settings.view_transform = options.get("view", "Khronos PBR Neutral")
    bpy.context.scene.view_settings.look = "None"
    render_previews(options, stage)
    print(f"TOTAL {time.perf_counter() - started:.1f} s", flush=True)


if __name__ == "__main__":
    main()
