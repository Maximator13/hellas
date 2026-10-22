import math

from mathutils import Matrix

from .terrain import GeoFrame

ORIGIN = (37.03783, 27.42416)
FRAME = GeoFrame(*ORIGIN)
SUN = (121.0, 34.0)
LENS = 24.4

SITES = {
    "palais": (37.03206, 27.42913),
    "theatre": (37.04018, 27.42151),
    "salmakis": (37.03026, 27.42103),
    "myndos": (37.04355, 27.41160),
}

NEAR_CENTRE = (-20.0, -205.0)
NEAR_HALF = 1300.0
MID_CENTRE = (0.0, -2000.0)
MID_HALF = 8000.0
FAR_HALF = 40000.0

MAUSOLEUM = (0.0, 0.0)
TERRACE = (-81.0, -22.0, 121.0, 52.5)
TERRACE_LEVEL = 10.5
PROPYLON = (40.0, -15.0)
AGORA = (150.0, -100.0)
AGORA_HALF = (50.0, 32.0)
PALACE_PLATEAU = 21.0
GOKTEPE = (-400.0, 600.0)
AVENUE = [(560.0, 52.0), (300.0, 50.0), (60.0, 48.0), (-120.0, 52.0), (-330.0, 120.0), (-560.0, 260.0),
          (-800.0, 420.0), (-1020.0, 580.0), (-1300.0, 720.0), (-1700.0, 900.0)]
AVENUE_WIDTH = 15.0

SEA_ERASE = [
    [(-150.0, -470.0), (90.0, -470.0), (90.0, -720.0), (-150.0, -720.0)],
    [(-260.0, -585.0), (-150.0, -585.0), (-150.0, -720.0), (-260.0, -720.0)],
    [(80.0, -600.0), (330.0, -600.0), (330.0, -700.0), (80.0, -700.0)],
]

ZEPHYRION = [(330.0, -560.0), (420.0, -505.0), (500.0, -520.0), (555.0, -600.0), (560.0, -700.0), (520.0, -790.0),
             (440.0, -800.0), (370.0, -760.0), (330.0, -680.0)]
ISTHMUS = [(390.0, -440.0), (500.0, -440.0), (500.0, -540.0), (390.0, -540.0)]
SECRET_HARBOUR = (470.0, -790.0)
SALMAKIS_SITE = (-284.0, -840.0)
KAPLAN = [(-430.0, -640.0), (-280.0, -650.0), (-250.0, -760.0), (-262.0, -900.0), (-320.0, -990.0),
          (-420.0, -980.0), (-450.0, -820.0)]

CITY_WALL = [
    (-1110.0, 640.0), (-900.0, 900.0), (-620.0, 1080.0), (-300.0, 1150.0), (40.0, 1180.0), (380.0, 1150.0),
    (700.0, 1060.0), (900.0, 880.0), (1080.0, 620.0), (1180.0, 300.0), (1200.0, -40.0), (1150.0, -380.0),
    (980.0, -470.0), (700.0, -440.0), (560.0, -450.0), (520.0, -540.0),
    (330.0, -560.0), (200.0, -560.0), (-260.0, -600.0), (-300.0, -660.0), (-420.0, -640.0), (-560.0, -560.0),
    (-760.0, -360.0), (-980.0, -100.0), (-1150.0, 200.0), (-1200.0, 420.0),
]
LAND_WALL = [
    (-260.0, -600.0), (-420.0, -640.0), (-560.0, -560.0), (-760.0, -360.0), (-980.0, -100.0), (-1150.0, 200.0),
    (-1200.0, 420.0), (-1110.0, 640.0), (-900.0, 900.0), (-620.0, 1080.0), (-300.0, 1150.0), (40.0, 1180.0),
    (380.0, 1150.0), (700.0, 1060.0), (900.0, 880.0), (1080.0, 620.0), (1180.0, 300.0), (1200.0, -40.0),
    (1150.0, -380.0),
]


def local(name):
    return FRAME.to_local(*SITES[name])


PALACE = local("palais")
THEATRE = local("theatre")
SALMAKIS = local("salmakis")
MYNDOS = local("myndos")


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
