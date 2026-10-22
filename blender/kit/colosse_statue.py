import math

import bpy
from mathutils import Matrix, Quaternion, Vector

from .geometry import MeshBuilder

TAU = 2 * math.pi
BRONZE = "bronze_colosse"
GOLD = "or_rayons"
EYE = "oeil_incruste"
IRIS = "iris_incruste"
HUMAN = 1.85
HEIGHT = 33.0
SCALE = HEIGHT / HUMAN


def ellipsoid(builder, centre, radii, rotation=None, segments=18, rings=10, material=BRONZE):
    turn = rotation.to_matrix().to_4x4() if rotation is not None else Matrix.Identity(4)
    matrix = Matrix.Translation(centre) @ turn @ Matrix.Diagonal((*radii, 1.0))
    profile = [(math.sin(math.pi * k / rings), -math.cos(math.pi * k / rings)) for k in range(rings + 1)]
    builder.lathe(profile, segments, material, smooth=True, matrix=matrix)


def frame_of(axis, hint):
    axis = Vector(axis).normalized()
    u = Vector(hint) - axis * Vector(hint).dot(axis)
    if u.length < 1e-6:
        u = axis.orthogonal()
    u.normalize()
    return axis, u, axis.cross(u).normalized()


def tube(builder, path, radii, sides=18, flatten=1.0, hint=(0.0, 0.0, 1.0), material=BRONZE, caps=True):
    path = [Vector(p) for p in path]
    rings = []
    previous = Vector(hint)
    for index, (point, radius) in enumerate(zip(path, radii)):
        axis = (path[min(index + 1, len(path) - 1)] - path[max(index - 1, 0)]).normalized()
        if abs(previous.normalized().dot(axis)) > 0.95:
            previous = Vector((0.0, 1.0, 0.0)) if abs(axis.y) < 0.9 else Vector((1.0, 0.0, 0.0))
        _, u, v = frame_of(axis, previous)
        previous = u
        rings.append([builder.point(point + (u * math.cos(TAU * k / sides) * flatten + v * math.sin(TAU * k / sides))
                                    * radius) for k in range(sides)])
    for lower, upper in zip(rings[:-1], rings[1:]):
        for k in range(sides):
            j = (k + 1) % sides
            builder.face([lower[k], lower[j], upper[j], upper[k]], material, True)
    if not caps:
        return
    builder.face(list(reversed(rings[0])), material)
    builder.face(list(rings[-1]), material)
    for point, radius in ((path[0], radii[0]), (path[-1], radii[-1])):
        ellipsoid(builder, point, (radius, radius, radius), segments=12, rings=6, material=material)


def limb(builder, start, end, radii, bow=(0.0, 0.0, 0.0), sides=18):
    start, end = Vector(start), Vector(end)
    count = len(radii)
    path = []
    for k in range(count):
        t = k / (count - 1)
        path.append(start.lerp(end, t) + Vector(bow) * math.sin(math.pi * t))
    tube(builder, path, radii, sides)


def superellipse(angle, power=2.6):
    c, s = math.cos(angle), math.sin(angle)
    return (math.copysign(abs(c) ** (2.0 / power), c), math.copysign(abs(s) ** (2.0 / power), s))


def loft(builder, sections, sides=36, ring=None, material=BRONZE):
    rings = []
    for section in sections:
        z, cx, cy, half_w, half_d = section[:5]
        front = section[5] if len(section) > 5 else 1.0
        points = []
        for k in range(sides):
            angle = TAU * k / sides
            if ring is not None:
                x, y = ring(angle, section)
            else:
                ux, uy = superellipse(angle)
                x = cx + half_w * ux
                y = cy + half_d * uy * (front if uy > 0 else 1.0)
            points.append(builder.point((x, y, z)))
        rings.append(points)
    for lower, upper in zip(rings[:-1], rings[1:]):
        for k in range(sides):
            j = (k + 1) % sides
            builder.face([lower[k], lower[j], upper[j], upper[k]], material, True)
    builder.face(list(reversed(rings[0])), material)
    builder.face(list(rings[-1]), material)


def rotation_between(a, b):
    return Vector(a).rotation_difference(Vector(b))


def finger(builder, root, direction, down, length, radius, curl):
    direction = Vector(direction).normalized()
    down = Vector(down).normalized()
    points = [Vector(root)]
    current = direction.copy()
    segment = length / 3
    for _ in range(3):
        points.append(points[-1] + current * segment)
        current = (current + down * curl).normalized()
    tube(builder, points, [radius, radius * 0.95, radius * 0.88, radius * 0.78], sides=10)


def hand(builder, wrist, forward, across, normal, length=0.19, width=0.085, curl=0.25, thumb_side=1.0):
    forward = Vector(forward).normalized()
    across = Vector(across).normalized()
    normal = Vector(normal).normalized()
    wrist = Vector(wrist)
    palm_length = length * 0.48
    centre = wrist + forward * palm_length * 0.55
    basis = Matrix((across, forward, normal)).transposed()
    ellipsoid(builder, centre, (width * 0.52, palm_length * 0.6, width * 0.17), basis.to_quaternion(), 16, 8)
    lengths = (0.92, 1.0, 0.95, 0.78)
    for k, scale in enumerate(lengths):
        offset = (k - 1.5) / 1.5 * width * 0.36
        root = wrist + forward * palm_length * 0.98 + across * offset
        finger(builder, root, forward + across * offset * 1.2, -normal, length * 0.52 * scale, width * 0.105, curl)
    thumb_root = wrist + forward * palm_length * 0.3 + across * thumb_side * width * 0.42
    finger(builder, thumb_root, forward * 0.7 + across * thumb_side * 0.7 - normal * 0.2, -normal, length * 0.38,
           width * 0.12, curl * 0.6)


def foot(builder, ankle, toward, width=0.05, length=0.255, ground=0.0):
    toward = Vector((toward[0], toward[1], 0.0)).normalized()
    side = Vector((toward.y, -toward.x, 0.0))
    ankle = Vector(ankle)
    heel = Vector((ankle.x, ankle.y, ground)) - toward * 0.045
    ellipsoid(builder, heel + Vector((0.0, 0.0, 0.035)) + toward * 0.01, (width * 0.75, 0.045, 0.04),
              rotation_between((0.0, 1.0, 0.0), toward))
    middle = heel + toward * length * 0.42 + Vector((0.0, 0.0, 0.034))
    ellipsoid(builder, middle, (width, length * 0.36, 0.036), rotation_between((0.0, 1.0, 0.0), toward))
    limb(builder, ankle, middle + Vector((0.0, 0.0, 0.01)), [0.034, 0.036, 0.04], sides=14)
    ball = heel + toward * length * 0.72 + Vector((0.0, 0.0, 0.022))
    ellipsoid(builder, ball, (width * 1.05, 0.04, 0.022), rotation_between((0.0, 1.0, 0.0), toward))
    for k in range(5):
        offset = (k - 1.6) * width * 0.4
        scale = 1.0 if k == 0 else 0.86 - 0.08 * k
        root = ball + side * offset + toward * 0.025
        tip = root + toward * (0.05 * scale + 0.012) + Vector((0.0, 0.0, -0.006))
        limb(builder, root, tip, [0.0125 * (1.25 if k == 0 else 0.95 - 0.06 * k)] * 3, sides=10)


def torso(builder):
    sections = [
        (0.835, 0.026, -0.004, 0.105, 0.075),
        (0.88, 0.03, -0.004, 0.155, 0.098),
        (0.94, 0.03, -0.002, 0.170, 0.106),
        (1.00, 0.026, 0.004, 0.160, 0.102),
        (1.06, 0.018, 0.008, 0.140, 0.098),
        (1.11, 0.01, 0.008, 0.134, 0.099),
        (1.17, 0.0, 0.008, 0.141, 0.102),
        (1.24, -0.008, 0.006, 0.152, 0.108),
        (1.31, -0.012, 0.002, 0.168, 0.114),
        (1.38, -0.012, -0.004, 0.176, 0.112),
        (1.44, -0.01, -0.010, 0.172, 0.098),
        (1.49, -0.006, -0.016, 0.140, 0.080),
        (1.525, -0.002, -0.018, 0.092, 0.064),
        (1.55, 0.0, -0.016, 0.062, 0.056),
    ]
    loft(builder, sections)
    for side, lift in ((1, 0.012), (-1, 0.0)):
        ellipsoid(builder, (side * 0.072, 0.074, 1.372 + lift), (0.088, 0.03, 0.05),
                  Quaternion((0.0, 1.0, 0.0), side * 0.3))
        limb(builder, (side * 0.02, 0.052, 1.5), (side * 0.14, 0.022, 1.495 + lift), [0.013, 0.012, 0.011], sides=10)
        ellipsoid(builder, (0.024 + side * 0.074, -0.068, 0.905 + (0.018 if side > 0 else 0.0)), (0.086, 0.066, 0.098))
        ellipsoid(builder, (side * 0.085, -0.078, 1.39), (0.07, 0.024, 0.09), Quaternion((0.0, 1.0, 0.0),
                                                                                         side * 0.25))
        ellipsoid(builder, (0.02 + side * 0.118, 0.025, 1.02 + (0.012 if side > 0 else 0.0)), (0.034, 0.07, 0.06))
        limb(builder, (0.0, -0.035, 1.6), (side * 0.155, -0.02, 1.495 + lift), [0.05, 0.047, 0.038], sides=14)
        for z in (1.245, 1.18, 1.115):
            ellipsoid(builder, (side * 0.034, 0.085, z), (0.036, 0.018, 0.031), segments=14, rings=8)
    ellipsoid(builder, (0.016, 0.074, 1.035), (0.078, 0.04, 0.062))
    ellipsoid(builder, (0.026, 0.08, 0.86), (0.024, 0.026, 0.03), segments=12, rings=6)
    ellipsoid(builder, (0.026, 0.068, 0.83), (0.03, 0.028, 0.032), segments=12, rings=6)


def head(builder, eyes):
    ellipsoid(builder, (0.0, 0.0, 1.745), (0.077, 0.094, 0.104), segments=24, rings=14)
    ellipsoid(builder, (0.0, 0.045, 1.70), (0.062, 0.06, 0.075), segments=22, rings=12)
    ellipsoid(builder, (0.0, 0.05, 1.655), (0.055, 0.05, 0.036))
    ellipsoid(builder, (0.0, 0.088, 1.641), (0.022, 0.018, 0.02), segments=12, rings=6)
    limb(builder, (0.0, 0.102, 1.737), (0.0, 0.121, 1.699), [0.009, 0.012, 0.014], sides=12)
    ellipsoid(builder, (0.0, 0.112, 1.695), (0.017, 0.012, 0.009), segments=12, rings=6)
    ellipsoid(builder, (0.0, 0.086, 1.749), (0.064, 0.02, 0.014), segments=18, rings=8)
    ellipsoid(builder, (0.0, 0.1, 1.674), (0.022, 0.01, 0.007), segments=12, rings=6)
    ellipsoid(builder, (0.0, 0.097, 1.664), (0.019, 0.01, 0.007), segments=12, rings=6)
    for side in (-1, 1):
        ellipsoid(builder, (side * 0.042, 0.073, 1.712), (0.025, 0.02, 0.018), segments=12, rings=6)
        ellipsoid(builder, (side * 0.077, 0.0, 1.72), (0.012, 0.022, 0.03), segments=12, rings=6)
        ellipsoid(eyes, (side * 0.03, 0.089, 1.727), (0.014, 0.0075, 0.0082), segments=16, rings=8, material=EYE)
        ellipsoid(eyes, (side * 0.029, 0.0952, 1.7265), (0.0048, 0.0018, 0.0048), segments=12, rings=6,
                  material=IRIS)
    limb(builder, (0.0, -0.016, 1.5), (0.0, 0.0, 1.665), [0.066, 0.062, 0.058, 0.054], sides=18)


def hair(builder):
    ellipsoid(builder, (0.0, -0.012, 1.765), (0.083, 0.098, 0.094), segments=24, rings=12)
    golden = math.pi * (3.0 - math.sqrt(5.0))
    count = 70
    centre = Vector((0.0, -0.01, 1.762))
    for k in range(count):
        z = 1.0 - 1.6 * (k + 0.5) / count
        radius = math.sqrt(max(1.0 - z * z, 0.0))
        direction = Vector((math.cos(golden * k) * radius, math.sin(golden * k) * radius, z))
        if direction.y > 0.45 and direction.z < 0.55:
            continue
        if direction.z < -0.25 and direction.y > -0.3:
            continue
        point = centre + Vector((direction.x * 0.084, direction.y * 0.098, direction.z * 0.094))
        size = 0.021 + 0.006 * math.sin(k * 2.3)
        ellipsoid(builder, point, (size, size * 0.8, size * 0.75), rotation_between((0.0, 0.0, 1.0), direction), 10, 6)
    for k in range(7):
        x = (k - 3) * 0.022
        ellipsoid(builder, (x, 0.066 - abs(x) * 0.25, 1.832 - abs(x) * 0.25), (0.016, 0.022, 0.03),
                  Quaternion((1.0, 0.0, 0.0), -0.5) @ Quaternion((0.0, 1.0, 0.0), x * 6.0), 10, 6)


def crown(rays):
    band_centre = Vector((0.0, -0.006, 1.8))
    tilt = Matrix.Rotation(-0.16, 4, "X")
    band = []
    sides = 40
    for k in range(sides):
        angle = TAU * k / sides
        band.append(Vector((math.sin(angle) * 0.091, math.cos(angle) * 0.106, 0.0)))
    path = [band_centre + (tilt @ point) for point in band]
    tube(rays, path + path[:1], [0.008] * (sides + 1), sides=8, flatten=0.55, hint=(0.0, 0.0, 1.0), material=GOLD,
         caps=False)
    count = 19
    for k in range(count):
        angle = math.radians(-162.0 + 324.0 * k / (count - 1))
        radial = Vector((math.sin(angle), math.cos(angle), 0.0))
        base = band_centre + tilt @ Vector((radial.x * 0.095, radial.y * 0.11, 0.0))
        rise = math.radians(28.0)
        direction = (radial * math.cos(rise) + Vector((0.0, 0.0, math.sin(rise)))).normalized()
        across = Vector((radial.y, -radial.x, 0.0))
        length = 0.085 if k % 2 == 0 else 0.065
        thickness = 0.005
        width = 0.026
        tip = base + direction * length
        normal = direction.cross(across).normalized()
        corners = [base + across * width / 2 + normal * thickness, base - across * width / 2 + normal * thickness,
                   base - across * width / 2 - normal * thickness, base + across * width / 2 - normal * thickness]
        indices = rays.points(corners)
        apex = rays.point(tip)
        for a in range(4):
            rays.face([indices[a], indices[(a + 1) % 4], apex], GOLD)
        rays.face(list(reversed(indices)), GOLD)


def arms(builder):
    right_shoulder = Vector((0.185, -0.004, 1.475))
    right_elbow = Vector((0.335, 0.17, 1.64))
    right_wrist = Vector((0.106, 0.132, 1.778))
    ellipsoid(builder, right_shoulder.lerp(right_elbow, 0.12) + Vector((0.01, 0.0, 0.0)), (0.06, 0.056, 0.085),
              rotation_between((0.0, 0.0, 1.0), right_elbow - right_shoulder))
    limb(builder, right_shoulder, right_elbow, [0.056, 0.052, 0.046, 0.04], bow=(0.0, 0.006, 0.008))
    ellipsoid(builder, right_shoulder.lerp(right_elbow, 0.55) + Vector((0.0, 0.0, -0.012)), (0.036, 0.034, 0.08),
              rotation_between((0.0, 0.0, 1.0), right_elbow - right_shoulder))
    limb(builder, right_elbow, right_wrist, [0.041, 0.04, 0.033, 0.027, 0.025], bow=(0.0, 0.008, 0.01))
    ellipsoid(builder, right_elbow.lerp(right_wrist, 0.28), (0.038, 0.034, 0.075),
              rotation_between((0.0, 0.0, 1.0), right_wrist - right_elbow))
    hand(builder, right_wrist, (-1.0, 0.16, -0.04), (0.16, 1.0, 0.0), (0.0, 0.05, 1.0), length=0.19, curl=0.12,
         thumb_side=-1.0)
    left_shoulder = Vector((-0.18, -0.01, 1.462))
    left_elbow = Vector((-0.236, -0.022, 1.188))
    left_wrist = Vector((-0.268, 0.214, 1.137))
    ellipsoid(builder, left_shoulder.lerp(left_elbow, 0.14) + Vector((-0.008, 0.0, 0.0)), (0.058, 0.055, 0.085),
              rotation_between((0.0, 0.0, 1.0), left_shoulder - left_elbow))
    limb(builder, left_shoulder, left_elbow, [0.054, 0.05, 0.045, 0.04], bow=(-0.004, 0.006, 0.0))
    limb(builder, left_elbow, left_wrist, [0.04, 0.039, 0.032, 0.027, 0.025], bow=(0.0, 0.0, 0.008))
    ellipsoid(builder, left_elbow.lerp(left_wrist, 0.28), (0.037, 0.033, 0.072),
              rotation_between((0.0, 0.0, 1.0), left_wrist - left_elbow))
    ellipsoid(builder, left_shoulder.lerp(left_elbow, 0.55) + Vector((0.0, 0.014, 0.0)), (0.034, 0.033, 0.075),
              rotation_between((0.0, 0.0, 1.0), left_elbow - left_shoulder))
    hand(builder, left_wrist, (-0.04, 1.0, -0.12), (1.0, 0.05, 0.0), (0.05, 0.1, 1.0), length=0.18, curl=0.42,
         thumb_side=1.0)
    return {"right_hand": right_wrist, "left_wrist": left_wrist, "left_elbow": left_elbow}


def legs(builder):
    right_hip = Vector((0.116, -0.004, 0.936))
    right_knee = Vector((0.094, 0.016, 0.522))
    right_ankle = Vector((0.07, -0.004, 0.086))
    left_hip = Vector((-0.07, -0.004, 0.908))
    left_knee = Vector((-0.062, 0.06, 0.508))
    left_ankle = Vector((-0.112, 0.014, 0.094))
    for hip, knee, ankle, toward in ((right_hip, right_knee, right_ankle, (0.12, 1.0)),
                                     (left_hip, left_knee, left_ankle, (-0.3, 1.0))):
        limb(builder, hip, knee, [0.09, 0.084, 0.074, 0.062, 0.052], bow=(0.0, 0.014, 0.0))
        ellipsoid(builder, hip.lerp(knee, 0.62) + Vector((0.0, 0.03, 0.0)), (0.056, 0.05, 0.11),
                  rotation_between((0.0, 0.0, 1.0), hip - knee))
        ellipsoid(builder, knee + Vector((0.0, 0.034, 0.012)), (0.03, 0.022, 0.034), segments=12, rings=6)
        limb(builder, knee, ankle, [0.05, 0.052, 0.046, 0.036, 0.031])
        ellipsoid(builder, knee.lerp(ankle, 0.3) + Vector((0.0, -0.026, 0.0)), (0.044, 0.042, 0.09),
                  rotation_between((0.0, 0.0, 1.0), knee - ankle))
        foot(builder, ankle, toward)


def drapery_ring(angle, section):
    z, cx, cy, half_w, half_d, phase, amplitude = section
    ux, uy = superellipse(angle, 2.4)
    y = cy + half_d * uy
    wave = math.sin((y - cy) / 0.032 * math.pi + phase)
    folds = amplitude * (wave if ux > 0 else 0.6 * wave)
    return cx + half_w * ux + folds, y


def drapery(builder, left_wrist, left_elbow):
    sections = []
    top = left_wrist.z + 0.04
    count = 20
    for k in range(count):
        t = k / (count - 1)
        z = top * (1.0 - t) ** 1.02
        cx = left_wrist.x - 0.01 - 0.035 * t
        cy = (left_elbow.y + left_wrist.y) / 2 + 0.02 + 0.03 * t
        half_d = 0.1 + 0.075 * t ** 1.2
        half_w = 0.03 + 0.008 * t
        amplitude = 0.008 + 0.024 * min(t * 2.5, 1.0)
        sections.append((z, cx, cy, half_w, half_d, 0.6 * t, amplitude))
    last = sections[-1]
    sections[-1] = (0.0, last[1], last[2], last[3] + 0.02, last[4] + 0.02, last[5], last[6])
    loft(builder, sections, sides=96, ring=drapery_ring)
    tube(builder, [left_wrist + Vector((0.01, -0.04, 0.035)), left_wrist + Vector((0.015, -0.12, 0.03)),
                   left_elbow + Vector((0.02, 0.05, 0.03))], [0.034, 0.038, 0.034], sides=14)


def remeshed(name, builder, voxel, smooth, ratio):
    mesh = bpy.data.meshes.new(f"{name}_raw")
    mesh.from_pydata(builder.positions, [], builder.polygons)
    holder = bpy.data.objects.new(f"{name}_raw", mesh)
    bpy.context.scene.collection.objects.link(holder)
    remesh = holder.modifiers.new("remesh", "REMESH")
    remesh.mode = "VOXEL"
    remesh.voxel_size = voxel
    remesh.adaptivity = 0.0
    laplacian = holder.modifiers.new("smooth", "LAPLACIANSMOOTH")
    laplacian.iterations = smooth
    laplacian.lambda_factor = 0.7
    laplacian.use_volume_preserve = True
    laplacian.use_normalized = True
    relax = holder.modifiers.new("relax", "SMOOTH")
    relax.factor = 0.8
    relax.iterations = smooth
    if ratio < 1.0:
        decimate = holder.modifiers.new("decimate", "DECIMATE")
        decimate.ratio = ratio
    bpy.context.view_layer.update()
    depsgraph = bpy.context.evaluated_depsgraph_get()
    result = bpy.data.meshes.new_from_object(holder.evaluated_get(depsgraph))
    bpy.data.objects.remove(holder)
    bpy.data.meshes.remove(mesh)
    result.name = name
    result.materials.append(bpy.data.materials[BRONZE])
    result.polygons.foreach_set("use_smooth", [True] * len(result.polygons))
    result.update()
    return result


def builder_mesh(name, builder):
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(builder.positions, [], builder.polygons)
    for material in builder.materials:
        mesh.materials.append(bpy.data.materials[material])
    mesh.polygons.foreach_set("material_index", builder.polygon_materials)
    mesh.polygons.foreach_set("use_smooth", builder.polygon_smooth)
    mesh.update()
    return mesh


def helios(voxel=0.006, smooth=14, ratio=0.6):
    body = MeshBuilder()
    eyes = MeshBuilder()
    rays = MeshBuilder()
    torso(body)
    head(body, eyes)
    hair(body)
    landmarks = arms(body)
    legs(body)
    drapery(body, landmarks["left_wrist"], landmarks["left_elbow"])
    crown(rays)
    return {"body": remeshed("colosse_corps", body, voxel, smooth, ratio),
            "rays": builder_mesh("colosse_rayons", rays),
            "eyes": builder_mesh("colosse_yeux", eyes),
            "landmarks": {key: list(value) for key, value in landmarks.items()}}
