import os

import numpy as np

from .materials import (PLAIN, fluting_pixels, generated_image, height_to_normal, linear_color, principled_material,
                        smooth_stone_pixels)

MARBLE = "marble"
DORIC_FLUTED = "marble_fluted_doric"
IONIC_FLUTED = "marble_fluted_ionic"
PAINT = "greek_paint"
POROS = "poros"
TERRACOTTA = "roof_tiles"
MATTE = "matte"

PENTELIC = (0.95, 0.925, 0.87)
POROS_STONE = (0.83, 0.76, 0.62)
PAINT_GROUND = (1.0, 1.0, 1.0)
VERSION = "v1"


def doric_fluting_pixels(flutes=20, width=640, height=64):
    phase = (np.linspace(0, 1, width, endpoint=False) * flutes) % 1.0
    depth = np.sin(np.pi * phase)
    return height_to_normal(np.tile(-depth[None, :], (height, 1)), 7.0)


def grain(texture_dir, name, color, seed):
    return generated_image(name, os.path.join(texture_dir, f"{name}_{VERSION}.jpg"),
                           lambda: smooth_stone_pixels(color, seed=seed))


def normal_image(texture_dir, name, build):
    return generated_image(name, os.path.join(texture_dir, f"{name}_{VERSION}.jpg"), build, colorspace="Non-Color",
                           quality=95)


def build_library(cache_dir):
    texture_dir = os.path.join(cache_dir, "textures")
    os.makedirs(texture_dir, exist_ok=True)
    tiles = {}
    for name, spec in PLAIN.items():
        color = spec["color"] if spec.get("linear") else linear_color(spec["color"])
        principled_material(name, color, spec["roughness"], spec.get("metallic", 0.0))
        tiles[name] = 2.0
    marble = grain(texture_dir, "pentelic_grain", PENTELIC, 7)
    principled_material(MARBLE, linear_color(PENTELIC), 0.42, 0.0, marble)
    tiles[MARBLE] = 3.0
    doric = normal_image(texture_dir, "doric_fluting_normal", doric_fluting_pixels)
    principled_material(DORIC_FLUTED, linear_color(PENTELIC), 0.42, 0.0, marble, doric, 1.0)
    tiles[DORIC_FLUTED] = 1.0
    ionic = normal_image(texture_dir, "ionic_fluting_normal", fluting_pixels)
    principled_material(IONIC_FLUTED, linear_color(PENTELIC), 0.42, 0.0, marble, ionic, 1.0)
    tiles[IONIC_FLUTED] = 1.0
    principled_material(PAINT, linear_color(PAINT_GROUND), 0.62, 0.0, grain(texture_dir, "paint_grain", PAINT_GROUND, 11))
    tiles[PAINT] = 2.0
    principled_material(POROS, linear_color(POROS_STONE), 0.85, 0.0, grain(texture_dir, "poros_grain", POROS_STONE, 5))
    tiles[POROS] = 2.5
    return tiles
