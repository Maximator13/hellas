import math

from mathutils import Matrix

from .terrain import GeoFrame

ORIGIN = (37.97156, 23.72658)
FRAME = GeoFrame(*ORIGIN)
SUN = (79.0, 26.0)
PARTHENON_AZIMUTH = 77.0
PROPYLAEA_AZIMUTH = 257.0

SITES = {
    "acropole": (37.97165, 23.72644),
    "propylees": (37.97174, 23.72510),
    "athena_bronze": (37.97182, 23.72566),
    "nike": (37.97153, 23.72489),
    "brauronion": (37.97151, 23.72544),
    "batiment_iv": (37.97150, 23.72800),
    "vieux_temple": (37.97190, 23.72628),
    "pandroseion": (37.97206, 23.72626),
    "grand_autel": (37.97195, 23.72684),
    "zeus_polieus": (37.97186, 23.72724),
    "klepsydra": (37.97219, 23.72490),
    "aglauros": (37.97139, 23.72877),
    "theatre": (37.97043, 23.72774),
    "odeon": (37.97041, 23.72868),
    "areopage": (37.97237, 23.72337),
    "pnyx": (37.97143, 23.71947),
    "mouseion": (37.96756, 23.72212),
    "agora": (37.97550, 23.72265),
    "colonos": (37.97543, 23.72121),
    "hephaisteion": (37.97560, 23.72141),
    "poikile": (37.97640, 23.72270),
    "stoa_royale": (37.97612, 23.72235),
    "bouleuterion": (37.97522, 23.72207),
    "tholos": (37.97487, 23.72194),
    "fontaine_se": (37.97398, 23.72379),
    "douze_dieux": (37.97579, 23.72276),
    "eleusinion": (37.97331, 23.72492),
    "dipylon": (37.97854, 23.71898),
    "ceramique": (37.97842, 23.71830),
    "olympieion": (37.96943, 23.73311),
    "lycabette": (37.98190, 23.74310),
    "phalere": (37.93731, 23.70625),
    "piree": (37.93722, 23.64461),
    "mounichie": (37.94060, 23.65590),
    "salamine": (37.94876, 23.53033),
    "egine": (37.75015, 23.42367),
    "hymette": (37.94149, 23.81742),
    "near_centre": (37.9729, 23.7249),
    "city_centre": (37.9581, 23.6924),
}

NEAR_HALF = 800.0
CITY_HALF = 6000.0
FAR_HALF = 30000.0


def local(name):
    return FRAME.to_local(*SITES[name])


def heading(azimuth_degrees):
    return -math.radians(azimuth_degrees)


def direction(azimuth_degrees):
    return math.sin(math.radians(azimuth_degrees)), math.cos(math.radians(azimuth_degrees))


def frame(x, y, z, azimuth_degrees=0.0, scale=1.0):
    return (Matrix.Translation((x, y, z)) @ Matrix.Rotation(heading(azimuth_degrees), 4, "Z")
            @ Matrix.Scale(scale, 4))


def to_world(origin, azimuth_degrees, u, v):
    a = heading(azimuth_degrees)
    return (origin[0] + u * math.cos(a) - v * math.sin(a), origin[1] + u * math.sin(a) + v * math.cos(a))


NEAR_CENTRE = local("near_centre")
CITY_CENTRE = local("city_centre")

ACROPOLIS_OUTLINE = [
    (-150.0, 2.0), (-136.0, -14.0), (-112.0, -28.0), (-80.0, -36.0), (-40.0, -40.0), (0.0, -42.0),
    (40.0, -40.0), (80.0, -38.0), (114.0, -35.0), (140.0, -27.0), (153.0, -11.0), (156.0, 8.0),
    (147.0, 29.0), (126.0, 48.0), (96.0, 66.0), (60.0, 78.0), (20.0, 86.0), (-14.0, 90.0), (-48.0, 88.0),
    (-80.0, 80.0), (-108.0, 64.0), (-128.0, 48.0), (-142.0, 30.0),
]

def wobble(x, y):
    return 2.6 * (0.6 * math.sin(x * 0.13 + y * 0.07) + 0.4 * math.sin(x * 0.051 - y * 0.11 + 1.3))


def wobbly(points, closed=True, step=6.0):
    pairs = list(zip(points, points[1:] + points[:1])) if closed else list(zip(points[:-1], points[1:]))
    out = []
    for (x0, y0), (x1, y1) in pairs:
        length = math.hypot(x1 - x0, y1 - y0)
        count = max(int(length / step), 1)
        nx, ny = (y1 - y0) / length, -(x1 - x0) / length
        for k in range(count):
            x, y = x0 + (x1 - x0) * k / count, y0 + (y1 - y0) * k / count
            offset = wobble(x, y) if k else 0.0
            out.append((x + nx * offset, y + ny * offset))
    if not closed:
        out.append(points[-1])
    return out


ACROPOLIS_EDGE = wobbly(ACROPOLIS_OUTLINE)

CITY_WALL = [
    (-680.0, 790.0), (-470.0, 1000.0), (-150.0, 1180.0), (250.0, 1250.0), (650.0, 1150.0), (950.0, 900.0),
    (1150.0, 520.0), (1180.0, 120.0), (1000.0, -250.0), (760.0, -520.0), (420.0, -720.0), (40.0, -860.0),
    (-380.0, -900.0), (-700.0, -760.0), (-900.0, -520.0), (-1000.0, -200.0), (-980.0, 150.0), (-880.0, 480.0),
]

LONG_WALL_NORTH = [(-1000.0, -200.0), (-1700.0, -560.0), (-2600.0, -1050.0), (-3700.0, -1650.0),
                   (-4900.0, -2300.0), (-5900.0, -2850.0), (-6500.0, -3150.0)]
LONG_WALL_MIDDLE = [(-920.0, -420.0), (-1650.0, -760.0), (-2550.0, -1250.0), (-3650.0, -1850.0),
                    (-4850.0, -2500.0), (-5850.0, -3050.0), (-6400.0, -3350.0)]
PHALERIC_WALL = [(-700.0, -760.0), (-950.0, -1400.0), (-1150.0, -2000.0), (-1350.0, -2700.0),
                 (-1550.0, -3350.0)]
PIRAEUS_WALL = [(-6500.0, -3150.0), (-7300.0, -2600.0), (-8100.0, -2700.0), (-8600.0, -3300.0),
                (-8500.0, -4300.0), (-7600.0, -4900.0), (-6600.0, -4700.0), (-6100.0, -4100.0),
                (-6400.0, -3350.0)]
