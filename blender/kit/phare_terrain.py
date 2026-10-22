import math

import bpy
import numpy as np
from mathutils.bvhtree import BVHTree

from . import phare_plan as plan
from .acropole_terrain import smoothstep, world_noise
from .geometry import MeshBuilder
from .terrain import polygon_mask

NEAR = dict(x0=-3400.0, y0=-5000.0, x1=5400.0, y1=900.0, spacing=20.0)
FAR = dict(half=24000.0, spacing=400.0)
SEA_DEPTH = -7.0
REACH = 600.0


def segments(polylines, closed):
    starts, ends = [], []
    for points, close in zip(polylines, closed):
        array = np.asarray(points, dtype=np.float64)
        if close:
            array = np.vstack([array, array[:1]])
        starts.append(array[:-1])
        ends.append(array[1:])
    return np.vstack(starts), np.vstack(ends)


def segment_distance(gx, gy, starts, ends, reach):
    distance = np.full(gx.shape, float(reach))
    lo_x, hi_x, lo_y, hi_y = gx.min(), gx.max(), gy.min(), gy.max()
    for (x0, y0), (x1, y1) in zip(starts, ends):
        if max(x0, x1) < lo_x - reach or min(x0, x1) > hi_x + reach:
            continue
        if max(y0, y1) < lo_y - reach or min(y0, y1) > hi_y + reach:
            continue
        dx, dy = x1 - x0, y1 - y0
        t = np.clip(((gx - x0) * dx + (gy - y0) * dy) / max(dx * dx + dy * dy, 1e-9), 0.0, 1.0)
        np.minimum(distance, np.hypot(gx - (x0 + t * dx), gy - (y0 + t * dy)), out=distance)
    return distance


def land_mask(gx, gy):
    land = np.zeros(gx.shape, dtype=bool)
    for polygon in plan.land_polygons():
        land |= polygon_mask(polygon, gx, gy)
    for polygon in plan.water_cuts():
        land &= ~polygon_mask(polygon, gx, gy)
    return land


def island_mask(gx, gy):
    return polygon_mask(plan.PHAROS_ISLAND, gx, gy) | polygon_mask(plan.islet(), gx, gy)


def signed_distance(gx, gy, reach):
    polygons = plan.land_polygons() + plan.water_cuts()
    starts, ends = segments(polygons, [True] * len(polygons))
    distance = segment_distance(gx, gy, starts, ends, reach)
    return np.where(land_mask(gx, gy), distance, -distance)


def grid_coords(gx, gy):
    dx, dy = gx - plan.C0.x, gy - plan.C0.y
    return dx * plan.D.x + dy * plan.D.y, dx * plan.N.x + dy * plan.N.y


def hills(gx, gy):
    t, n = grid_coords(gx, gy)
    r = plan.RHAKOTIS
    rhakotis = r["height"] * np.exp(-((t - r["t"]) ** 2 + (n - r["n"]) ** 2) / (2 * (r["radius"] * 0.65) ** 2))
    ridge = 1.4 * np.exp(-((n - 250.0) / 600.0) ** 2) * smoothstep((t + 3200.0) / 800.0) * smoothstep(
        (3200.0 - t) / 800.0)
    lochias = 2.0 * np.exp(-((gx - 2330.0) ** 2 + (gy + 160.0) ** 2) / (2 * 140.0 ** 2))
    return rhakotis + ridge + lochias


def heights_of(gx, gy, sd, quay):
    noise = world_noise(gx, gy, 700.0, 7, 4) - 0.5
    land = plan.PLAIN + 0.8 * smoothstep(sd / 500.0) + 1.0 * noise + hills(gx, gy)
    land = np.where(island_mask(gx, gy), 1.6 + 1.2 * smoothstep(sd / 120.0) + 0.6 * noise, land)
    land = np.maximum(land, 0.9)
    slope = 0.12 + 0.5 * (quay < 30.0)
    rising = np.minimum(land, slope * sd)
    sea = np.maximum(slope * sd, SEA_DEPTH + 2.0 * noise)
    return np.where(sd >= 0, rising, sea)


def mix(colour, other, weight):
    weight = np.clip(weight, 0.0, 1.0)[..., None]
    return colour * (1 - weight) + np.asarray(other) * weight


def filled(shape, rgb):
    colour = np.empty(shape + (3,))
    colour[...] = rgb
    return colour


def colours_of(gx, gy, sd, quay, heights):
    noise = world_noise(gx, gy, 90.0, 13, 3)
    broad = world_noise(gx, gy, 900.0, 17, 3)
    colour = mix(filled(gx.shape, (0.40, 0.44, 0.26)), (0.58, 0.55, 0.38), broad * 1.4 - 0.2)
    wall = polygon_mask(plan.city_wall(), gx, gy)
    colour = np.where(wall[..., None], mix(filled(gx.shape, (0.68, 0.62, 0.5)), (0.6, 0.55, 0.45), noise), colour)
    island = island_mask(gx, gy)
    colour = np.where(island[..., None], mix(filled(gx.shape, (0.76, 0.72, 0.62)), (0.62, 0.6, 0.55), noise), colour)
    lake = segment_distance(gx, gy, *segments([plan.lake_shore()], [False]), 400.0)
    colour = mix(colour, (0.28, 0.36, 0.2), smoothstep(1.0 - (lake - 30.0) / 160.0) * (~wall))
    colour = mix(colour, (0.86, 0.8, 0.66), smoothstep(1.0 - sd / 45.0) * (quay > 40.0))
    colour = mix(colour, (0.55, 0.5, 0.42), smoothstep(-heights / 2.0))
    return colour * (0.92 + 0.16 * noise[..., None])


def quay_distance(gx, gy):
    lines = plan.quay_lines()
    starts, ends = segments(lines, [False] * len(lines))
    return segment_distance(gx, gy, starts, ends, 200.0)


class Sampler:
    def __init__(self, x0, y0, spacing, values):
        self.x0, self.y0, self.spacing, self.values = x0, y0, spacing, values
        self.rows, self.columns = values.shape

    def __call__(self, x, y):
        column = np.clip((np.asarray(x, dtype=np.float64) - self.x0) / self.spacing, 0, self.columns - 1.001)
        row = np.clip((np.asarray(y, dtype=np.float64) - self.y0) / self.spacing, 0, self.rows - 1.001)
        c0, r0 = np.floor(column).astype(int), np.floor(row).astype(int)
        fx, fy = column - c0, row - r0
        v = self.values
        lower = v[r0, c0] * (1 - fx) + v[r0, c0 + 1] * fx
        upper = v[r0 + 1, c0] * (1 - fx) + v[r0 + 1, c0 + 1] * fx
        result = lower * (1 - fy) + upper * fy
        return float(result) if np.ndim(result) == 0 else result


class Ground:
    def __init__(self):
        spec = NEAR
        xs = np.arange(spec["x0"], spec["x1"] + 1e-6, spec["spacing"])
        ys = np.arange(spec["y0"], spec["y1"] + 1e-6, spec["spacing"])
        self.gx, self.gy = np.meshgrid(xs, ys)
        self.sd = signed_distance(self.gx, self.gy, REACH)
        self.quay = quay_distance(self.gx, self.gy)
        self.heights = heights_of(self.gx, self.gy, self.sd, self.quay)
        self.height = Sampler(spec["x0"], spec["y0"], spec["spacing"], self.heights)
        self.shore = Sampler(spec["x0"], spec["y0"], spec["spacing"], self.sd)
        self.trees = []

    def __call__(self, x, y):
        return self.height(x, y)

    def inside(self, x, y, margin=0.0):
        return (NEAR["x0"] + margin <= x <= NEAR["x1"] - margin) and (NEAR["y0"] + margin <= y <= NEAR["y1"] - margin)

    def add_surface(self, objects):
        for obj in objects:
            mesh = obj.data
            matrix = obj.matrix_world
            vertices = [matrix @ v.co for v in mesh.vertices]
            self.trees.append(BVHTree.FromPolygons(vertices, [p.vertices[:] for p in mesh.polygons]))

    def surface(self, x, y, lift=4.0):
        start = max(self(x, y), 0.0) + lift
        best = None
        for tree in self.trees:
            hit = tree.ray_cast((x, y, start), (0.0, 0.0, -1.0), start + 40.0)
            if hit[0] is not None and (best is None or hit[0].z > best):
                best = hit[0].z
        return best if best is not None else self(x, y)


def grid_object(name, gx, gy, heights, colours, materials, keep, collection, parent, tile=6.0):
    rows, columns = heights.shape
    index = np.arange(rows * columns).reshape(rows, columns)
    quads = np.stack([index[:-1, :-1], index[:-1, 1:], index[1:, 1:], index[1:, :-1]], axis=-1)
    keep = keep[:-1, :-1] if keep.shape == heights.shape else keep
    quads = quads[keep]
    used = np.unique(quads)
    remap = np.full(rows * columns, -1, dtype=np.int64)
    remap[used] = np.arange(len(used))
    faces = remap[quads]
    vertices = np.column_stack([gx.ravel()[used], gy.ravel()[used], heights.ravel()[used]])
    mesh = bpy.data.meshes.new(name)
    mesh.vertices.add(len(vertices))
    mesh.vertices.foreach_set("co", vertices.astype(np.float32).ravel())
    mesh.loops.add(faces.size)
    mesh.loops.foreach_set("vertex_index", faces.astype(np.int32).ravel())
    mesh.polygons.add(len(faces))
    mesh.polygons.foreach_set("loop_start", (np.arange(len(faces)) * 4).astype(np.int32))
    mesh.polygons.foreach_set("loop_total", np.full(len(faces), 4, dtype=np.int32))
    names, slots = materials
    for material in names:
        mesh.materials.append(bpy.data.materials[material])
    mesh.polygons.foreach_set("material_index", slots[keep].astype(np.int32))
    mesh.polygons.foreach_set("use_smooth", np.ones(len(faces), dtype=bool))
    loop_vertices = faces.ravel()
    uv = mesh.uv_layers.new(name="UVMap")
    uv.data.foreach_set("uv", (vertices[loop_vertices, :2] / tile).astype(np.float32).ravel())
    rgba = np.ones((len(loop_vertices), 4), dtype=np.float32)
    rgba[:, :3] = np.clip(colours.reshape(-1, 3)[used][loop_vertices], 0.0, 1.0)
    attribute = mesh.color_attributes.new("Col", "BYTE_COLOR", "CORNER")
    attribute.data.foreach_set("color_srgb", rgba.ravel())
    mesh.color_attributes.active_color = attribute
    mesh.validate()
    mesh.update()
    created = bpy.data.objects.new(name, mesh)
    collection.objects.link(created)
    created.parent = parent
    created["cast_shadow"] = False
    return created


def near_terrain(ground, collection, parent):
    gx, gy, h = ground.gx, ground.gy, ground.heights
    colours = colours_of(gx, gy, ground.sd, ground.quay, h)
    corners = np.stack([h[:-1, :-1], h[:-1, 1:], h[1:, 1:], h[1:, :-1]])
    keep = corners.max(axis=0) > -0.8
    centre_x = (gx[:-1, :-1] + gx[1:, 1:]) / 2
    centre_y = (gy[:-1, :-1] + gy[1:, 1:]) / 2
    island = island_mask(centre_x, centre_y)
    slots = np.where(island, 1, 0)
    obj = grid_object("terrain_near", gx, gy, h, colours, (["terrain_plaine", "terrain_ile"], slots), keep,
                      collection, parent)
    return obj, int(keep.sum()) * 2


def far_terrain(collection, parent):
    half, spacing = FAR["half"], FAR["spacing"]
    axis = np.arange(-half, half + 1e-6, spacing)
    gx, gy = np.meshgrid(axis, axis)
    sd = signed_distance(gx, gy, 3000.0)
    noise = world_noise(gx, gy, 3000.0, 21, 3) - 0.5
    land = 2.0 + 3.0 * noise + 4.0 * smoothstep(sd / 4000.0)
    h = np.where(sd >= 0, np.minimum(land, 0.004 * sd), np.maximum(0.004 * sd, -12.0)) - 0.4
    colours = mix(filled(gx.shape, (0.42, 0.44, 0.28)), (0.62, 0.58, 0.42),
                  world_noise(gx, gy, 2500.0, 23, 3) * 1.5 - 0.3)
    colours = mix(colours, (0.84, 0.78, 0.62), smoothstep(1.0 - sd / 500.0))
    corners = np.stack([h[:-1, :-1], h[:-1, 1:], h[1:, 1:], h[1:, :-1]])
    cx0, cx1 = gx[:-1, :-1], gx[1:, 1:]
    cy0, cy1 = gy[:-1, :-1], gy[1:, 1:]
    inside = ((cx0 >= NEAR["x0"]) & (cx1 <= NEAR["x1"]) & (cy0 >= NEAR["y0"]) & (cy1 <= NEAR["y1"]))
    keep = (corners.max(axis=0) > -1.0) & ~inside
    obj = grid_object("terrain_far", gx, gy, h, colours, (["terrain_far"], np.zeros(keep.shape, dtype=int)), keep,
                      collection, parent, tile=60.0)
    return obj, int(keep.sum()) * 2


def flat_polygon(builder, points, z, material, colour=None):
    builder.polygon([(x, y, z) for x, y in points], material, color=colour)


def water(scene):
    sea = MeshBuilder()
    reach = 70000.0
    sea.polygon([(-reach, -reach, 0.0), (reach, -reach, 0.0), (reach, reach, 0.0), (-reach, reach, 0.0)], "sea")
    scene.unique("mer", sea, occlusion=False)
    lake = MeshBuilder()
    flat_polygon(lake, plan.lake_polygon(), 0.35, "water", (0.55, 0.62, 0.62))
    flat_polygon(lake, plan.canal_polygon(), 0.2, "water", (0.55, 0.62, 0.62))
    scene.unique("lac", lake, occlusion=False)
    scene.shadowless.update({"mer", "lac"})


def outward_sign(points, ground):
    a, b = points[0], points[1]
    tx, ty = b[0] - a[0], b[1] - a[1]
    length = math.hypot(tx, ty)
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    ox, oy = ty / length, -tx / length
    return 1.0 if ground.shore(mx + ox * 12.0, my + oy * 12.0) > ground.shore(mx - ox * 12.0, my - oy * 12.0) else -1.0


def quays(scene, ground):
    builder = MeshBuilder()
    total = 0.0
    for points in plan.quay_lines():
        sign = outward_sign(points, ground)
        top = plan.QUAY_TOP
        path = [(x, y, 0.0) for x, y in points]
        first = len(builder.polygons)
        builder.sweep(path, [(0.0, -3.5), (0.0, top), (sign * 1.2, top)], "ashlar", caps=False)
        builder.tint(first, (0.92, 0.86, 0.74))
        first = len(builder.polygons)
        builder.sweep(path, [(sign * 1.2, top), (sign * 16.0, top - 0.02)], "ground_quai", caps=False)
        builder.tint(first, (0.95, 0.9, 0.8))
        total += sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(points[:-1], points[1:]))
    scene.unique("quais", builder)
    return round(total)


def street_strips(scene, ground):
    builder = MeshBuilder()
    count = 0
    for t0 in np.arange(plan.CITY_T[0], plan.CITY_T[1], 40.0):
        t1 = t0 + 40.0
        a, b = plan.grid_point(t0, plan.CANOPIC_N), plan.grid_point(t1, plan.CANOPIC_N)
        if not (plan.is_land(*a) and plan.is_land(*b)):
            continue
        half = plan.CANOPIC_WIDTH / 2
        n0, n1 = plan.CANOPIC_N - half, plan.CANOPIC_N + half
        corners = [plan.grid_point(t0, n0), plan.grid_point(t1, n0), plan.grid_point(t1, n1), plan.grid_point(t0, n1)]
        builder.polygon([(p.x, p.y, ground(p.x, p.y) + 0.12) for p in corners], "ground_rue",
                        color=(0.84, 0.78, 0.66))
        count += 1
    scene.unique("rues", builder, occlusion=False)
    scene.shadowless.add("rues")
    return count
