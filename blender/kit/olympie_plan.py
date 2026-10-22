import math

from mathutils import Matrix

from .terrain import GeoFrame

ORIGIN = (37.63781, 21.63005)
FRAME = GeoFrame(*ORIGIN)
SUN = (90.0, 27.0)
LENS = 24.4

TEMPLE = (0.0, 0.0)
TEMPLE_AZIMUTH = 90.0
HERAION = (-23.0, 118.0)
PELOPION = (-10.0, 60.0)
ALTAR = (25.0, 75.0)
WORKSHOP = (-115.0, 20.0)
PRYTANEION = (-70.0, 130.0)
BOULEUTERION = (20.0, -72.0)
NIKE = (45.0, -10.0)
STADIUM_WEST = (205.0, 150.0)
STADIUM_AZIMUTH = 80.0
STADIUM_LENGTH = 212.5
STADIUM_WIDTH = 30.0
TREASURY_LINE = ((32.0, 129.0), (182.0, 151.0))
TREASURY_COUNT = 11
KRONION = (110.0, 320.0)
HIPPODROME = (430.0, -110.0)
HIPPODROME_AZIMUTH = 80.0

NEAR_CENTRE = (120.0, 80.0)
NEAR_HALF = 700.0
MID_HALF = 5000.0
FAR_HALF = 25000.0

ALTIS = [(-62.0, -42.0), (100.0, -42.0), (100.0, 40.0), (195.0, 118.0), (190.0, 160.0), (40.0, 150.0),
         (-60.0, 160.0), (-75.0, 60.0)]
SANCTUARY = [(-150.0, -110.0), (90.0, -110.0), (120.0, -40.0), (380.0, 80.0), (395.0, 210.0), (180.0, 200.0),
             (-30.0, 215.0), (-105.0, 175.0), (-150.0, 60.0)]
KLADEOS = [(-235.0, 900.0), (-215.0, 600.0), (-205.0, 300.0), (-200.0, 100.0), (-205.0, -100.0), (-230.0, -280.0),
           (-275.0, -420.0)]
ALPHEIOS = [(3500.0, -200.0), (2400.0, -330.0), (1500.0, -430.0), (800.0, -470.0), (200.0, -500.0),
            (-300.0, -490.0), (-900.0, -520.0), (-1700.0, -620.0), (-2600.0, -760.0), (-3600.0, -900.0)]
ALPHEIOS_WIDTH = 150.0
CAMPS = [((150.0, -260.0), 170.0), ((450.0, -300.0), 160.0), ((-60.0, -330.0), 120.0), ((-300.0, -120.0), 70.0),
         ((-300.0, 200.0), 60.0), ((700.0, -250.0), 140.0)]
ARGIVE_CAMP = ((600.0, 60.0), 70.0)

EYES = {
    "vue-d-ensemble": (450.0, -350.0),
    "campements-et-garde": (200.0, -250.0),
    "grand-autel": (60.0, 50.0),
    "heraion-et-pelopion": (10.0, 85.0),
    "terrasse-des-tresors": (60.0, 100.0),
    "stade": (303.2, 139.9),
    "temple-de-zeus": (75.0, -20.0),
    "atelier-de-phidias": (-50.0, -32.0),
}


def local(latitude, longitude):
    return FRAME.to_local(latitude, longitude)


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


def treasury_sites():
    (x0, y0), (x1, y1) = TREASURY_LINE
    return [(x0 + (x1 - x0) * k / (TREASURY_COUNT - 1), y0 + (y1 - y0) * k / (TREASURY_COUNT - 1))
            for k in range(TREASURY_COUNT)]


def treasury_azimuth():
    (x0, y0), (x1, y1) = TREASURY_LINE
    return math.degrees(math.atan2(x1 - x0, y1 - y0)) + 90.0


def stadium_point(along, north):
    return to_world(STADIUM_WEST, STADIUM_AZIMUTH, -north, along)
