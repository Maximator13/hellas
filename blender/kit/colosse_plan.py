import math

from mathutils import Matrix

from .terrain import GeoFrame

ORIGIN = (36.4458, 28.2240)
FRAME = GeoFrame(*ORIGIN)
SUN = (75.0, 19.0)
STATUE_AZIMUTH = 30.0
STATUE = (0.0, 0.0)
BASE_HEIGHT = 8.0

SITES = {
    "apollon": (36.43999, 28.21066),
    "stade": (36.43894, 28.21190),
    "ialysos": (36.39900, 28.14300),
    "camiros": (36.33612, 27.92124),
    "loryma": (36.57739, 28.00822),
    "syme": (36.61839, 27.84343),
}

NEAR_CENTRE = (-150.0, -50.0)
NEAR_HALF = 1500.0
MID_CENTRE = (-1500.0, -2500.0)
MID_HALF = 8000.0
FAR_HALF = 48000.0

MANDRAKI_MOLE = [(300.0, 175.0), (318.0, 300.0), (330.0, 450.0), (340.0, 600.0), (342.0, 640.0)]
MANDRAKI_NORTH = [(268.0, 808.0), (215.0, 812.0), (140.0, 800.0)]
GRAND_PORT_MOLE = [(702.0, -160.0), (704.0, 0.0), (702.0, 120.0), (694.0, 196.0)]
AKANDIA_MOLE = [(1250.0, -360.0), (1265.0, -120.0), (1240.0, 60.0)]
SHIPSHED_ROWS = [((180.0, 205.0), (290.0, 205.0), 0.0), ((168.0, 300.0), (168.0, 560.0), 90.0)]

SEA_ERASE = [
    [(1275.0, -420.0), (1420.0, -420.0), (1420.0, 300.0), (1275.0, 300.0)],
    [(372.0, 40.0), (520.0, 40.0), (520.0, 100.0), (372.0, 100.0)],
    [(245.0, 545.0), (285.0, 545.0), (285.0, 585.0), (245.0, 585.0)],
]
ACROPOLIS_ZONE = ((-1080.0, -585.0), 250.0)

CITY_WALL = [
    (-1760.0, -760.0), (-1450.0, -1260.0), (-900.0, -1500.0), (-250.0, -1520.0), (400.0, -1380.0),
    (950.0, -1080.0), (1180.0, -720.0), (1240.0, -380.0), (1000.0, 120.0), (760.0, 230.0), (520.0, 640.0),
    (300.0, 900.0), (-80.0, 1250.0), (-340.0, 1330.0), (-560.0, 1000.0), (-900.0, 560.0), (-1300.0, 120.0),
    (-1620.0, -380.0),
]
SOUTH_WALL = CITY_WALL[:7]

HELIOS_TERRACE = 62.0
AGORA = (260.0, -330.0)
AGORA_HALF = (70.0, 55.0)
PTOLEMAION = (-260.0, -720.0)
ATHENA_TEMPLE = (-1060.0, -470.0)
ATHENA_AZIMUTH = 90.0
GYMNASIUM = (-700.0, -900.0)


def local(name):
    return FRAME.to_local(*SITES[name])


APOLLO = local("apollon")
STADIUM = local("stade")


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
