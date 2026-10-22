import os

import numpy as np

from .materials import generated_image, linear_color, principled_material, smooth_stone_pixels

LIMESTONE = (0.80, 0.77, 0.70)
ASHLAR = (0.86, 0.80, 0.68)
PLASTER = (0.96, 0.93, 0.86)
ELEUSIS = (0.27, 0.28, 0.30)


def ashlar_pixels(color, size=1024, courses=6, seed=19):
    generator = np.random.default_rng(seed)
    rows = np.arange(size)
    course = rows * courses // size
    tone = np.ones((size, size))
    for index in range(courses):
        band = course == index
        offset = generator.integers(0, size)
        widths = generator.integers(size // 5, size // 2, 8)
        edges = (offset + np.cumsum(widths)) % size
        columns = np.arange(size)
        block = np.searchsorted(np.sort(edges), columns) % len(edges)
        shades = 0.9 + 0.16 * generator.random(len(edges) + 1)
        tone[band] = shades[block][None, :]
        for edge in edges:
            tone[band, max(edge - 2, 0):edge + 1] = 0.62
    joints = (rows * courses) % size < 4
    tone[joints] = 0.6
    grain = generator.normal(0.0, 0.025, (size, size))
    return np.dstack([np.clip(color[c] * (tone + grain), 0, 1) for c in range(3)])


def build(tiles, cache_dir):
    texture_dir = os.path.join(cache_dir, "textures")
    os.makedirs(texture_dir, exist_ok=True)
    limestone = generated_image("limestone_grain", os.path.join(texture_dir, "limestone_grain_v2.jpg"),
                                lambda: smooth_stone_pixels(LIMESTONE, size=1024, seed=23))
    principled_material("limestone", linear_color(LIMESTONE), 0.9, 0.0, limestone)
    tiles["limestone"] = 3.0
    ashlar = generated_image("ashlar_courses", os.path.join(texture_dir, "ashlar_courses_v2.jpg"),
                             lambda: ashlar_pixels(ASHLAR))
    principled_material("ashlar", linear_color(ASHLAR), 0.85, 0.0, ashlar)
    tiles["ashlar"] = 4.0
    eleusis = generated_image("eleusis_grain", os.path.join(texture_dir, "eleusis_grain_v1.jpg"),
                              lambda: smooth_stone_pixels(ELEUSIS, seed=31))
    principled_material("eleusis", linear_color(ELEUSIS), 0.45, 0.0, eleusis)
    tiles["eleusis"] = 2.0
    plaster = generated_image("plaster_grain", os.path.join(texture_dir, "plaster_grain_v1.jpg"),
                              lambda: smooth_stone_pixels(PLASTER, seed=29))
    principled_material("plaster", linear_color(PLASTER), 0.92, 0.0, plaster)
    tiles["plaster"] = 3.0
    for name, colour, roughness, metallic in (("gold", (1.0, 0.62, 0.18), 0.3, 1.0),
                                              ("ivory", (0.94, 0.86, 0.72), 0.38, 0.0),
                                              ("eye_stone", (0.12, 0.09, 0.08), 0.3, 0.0),
                                              ("bronze_statue", (0.42, 0.24, 0.09), 0.48, 1.0)):
        principled_material(name, colour if metallic else linear_color(colour), roughness, metallic)
        tiles[name] = 2.0
    for name, colour, roughness in (("sea", (0.03, 0.15, 0.36), 0.22), ("river", (0.20, 0.32, 0.32), 0.1),
                                    ("bassin", (0.16, 0.20, 0.22), 0.04)):
        principled_material(name, linear_color(colour), roughness, vertex_color=False)
        tiles[name] = 4.0
    return tiles
