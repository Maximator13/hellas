import bpy

from .greek_materials import PENTELIC
from .materials import linear_color, principled_material

BRONZE_COLOUR = (0.48, 0.3, 0.15)


def build(tiles):
    principled_material("bronze_colosse", BRONZE_COLOUR, 0.38, 1.0, vertex_color=False)
    principled_material("or_rayons", (1.0, 0.7, 0.28), 0.22, 1.0, vertex_color=False)
    principled_material("oeil_incruste", linear_color((0.66, 0.6, 0.52)), 0.35, 0.0, vertex_color=False)
    principled_material("iris_incruste", linear_color((0.1, 0.07, 0.05)), 0.25, 0.0, vertex_color=False)
    marble = bpy.data.images.get("pentelic_grain")
    principled_material("marbre_socle", linear_color(PENTELIC), 0.4, 0.0, marble)
    principled_material("lens_smooth", linear_color((0.91, 0.88, 0.81)), 0.55, 0.0, marble)
    principled_material("ground_quai", linear_color((0.84, 0.77, 0.64)), 0.9, 0.0,
                        bpy.data.images.get("ashlar_courses"))
    for name in ("bronze_colosse", "or_rayons", "oeil_incruste", "iris_incruste"):
        tiles[name] = 1.0
    tiles["marbre_socle"] = 3.0
    tiles["lens_smooth"] = 3.0
    tiles["ground_quai"] = 4.0
    return tiles
