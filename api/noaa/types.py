from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Literal

CoverageType = Literal[
    None,
    'areas',
    'brief',
    'chance',
    'definite',
    'few',
    'frequent',
    'intermittent',
    'isolated',
    'likely',
    'numerous',
    'occasional',
    'patchy',
    'periods',
    'scattered',
    'slight_chance',
    'widespread',
]

WeatherType = Literal[
    None,
    'blowing_dust',
    'blowing_sand',
    'blowing_snow',
    'drizzle',
    'fog',
    'freezing_drizzle',
    'freezing_fog',
    'freezing_rain',
    'freezing_spray',
    'frost',
    'hail',
    'haze',
    'ice_crystals',
    'ice_fog',
    'rain',
    'rain_showers',
    'sleet',
    'smoke',
    'snow',
    'snow_showers',
    'thunderstorms',
    'volcanic_ash',
    'water_spouts',
]

IntensityType = Literal[
    None,
    'very_light',
    'light',
    'moderate',
    'heavy',
]

NotableAttributesType = Literal[
    'damaging_wind',
    'dry_thunderstorms',
    'flooding',
    'gusty_wind',
    'heavy_rain',
    'large_hail',
    'small_hail',
    'tornadoes',  # as if one tornado wasn't enough
]


class VtecFixedIdentifier(Enum):
    Operational = "O"
    Test = "T"
    Experimental = "E"
    ExperimentalInOperations = "X"


class VtecAction(Enum):
    """The action associated with a VTEC code."""
    New = "NEW"
    Continue = "CON"
    TimeExtension = "EXT"
    AreaExtension = "EXA"
    TimeAndAreaExtension = "EXB"
    Cancel = "CAN"
    Upgrade = "UPG"
    Expiry = "EXP"
    Correction = "COR"
    Routine = "ROU"


class VtecPhenomenon(Enum):
    # Winter
    Blizzard = "BZ"
    WinterStorm = "WS"
    WinterWeather = "WW"
    LakeEffectSnow = "LE"  # no, not little-endian
    IceStorm = "IS"  # yes, it is
    WindChill = "WC"  # no, not water closet
    SnowSquall = "SQ"  # no, not square

    # Non-preciptation
    BlowingDust = "DU"  # no, not Duluth
    DustStorm = "DS"  # no, not the handheld console
    Wind = "WI"  # no, not Wisconsin
    HighWind = "HW"  # no, not a highway
    LakeWind = "LW"
    DenseSmoke = "SM"
    DenseFog = "FG"  # no, not foreground
    FreezingFog = "ZF"
    HardFreeze = "HZ"
    Freeze = "FZ"
    Frost = "FR"  # no, not France
    Heat = "HT"
    ExcessiveHeat = "EH"  # eh, idk
    ExtremeCold = "EC"
    AirStagnation = "AS"  # as if
    Ashfall = "AF"

    # Water resources
    DebrisFlow = "DF"
    FloodForecastPoint = "FL",  # no, not Florida
    Flood = "FA"
    FlashFlood = "FF"
    Hydrologic = "HY"

    # Severe storms
    SevereThunderstorm = "SV"
    Tornado = "TO"  # to be or not to be

    # Marine and coastal
    Marine = "MA"
    FreezingSpray = "ZY"
    HeavyFreezingSpray = "UP"  # ok hold on why is it "up" all of a sudden
    SmallCraft = "SC"  # no, not South Carolina
    BriskWind = "BW"
    Gale = "GL"
    HazardousSeas = "SE"
    Storm = "SR"  # as if the labeling wasn't confusing enough
    HurricaneForceWind = "HF"
    LakeshoreFlood = "LS"  # no, not the popular Unix command
    CoastalFlood = "CF"
    HighSurf = "SU"  # no, not the command to switch users
    Tsunami = "TS"  # no, not the popular programming language
    LowWater = "LO"
    DenseFog_Marine = "MF"
    DenseSmoke_Marine = "MS"  # no, not Massachusetts (or Microsoft)
    Ashfall_Marine = "MH"
    BeachHazard = "BH"
    RipCurrentRisk = "RP"  # no, not FRC ranking points

    # Tropical
    TropicalStorm = "TR"  # no, not the useful CLI tool
    Hurricane = "HU"
    Typhoon = "TY"  # thank you!
    ExtremeWind = "EW"  # ew, there's too much wind
    StormSurge = "SS"

    # Other (just a category for fire and nothing else)
    FireWeather = "FW"  # no, not forward


class VtecSignificance(Enum):
    """The significance of a VTEC code."""
    Warning = "W"
    Watch = "A"
    Advisory = "Y"
    Statement = "S"
    Forecast = "F"
    Outlook = "O"
    Synopsis = "N"


@dataclass
class VtecCode:
    """A representation of a P-VTEC code.
    P-VTEC codes are used to identify weather events other than flood reports.
    A P-VTEC code has the following format:

        k.aaa.cccc.pp.s.####.yymmddThhmmZ-yymmddThhmmZ
        ^ ^^^ ^^^^ ^^ ^ ^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^
        |  |    |   | |   |  Time period of the event
        |  |    |   | |   Event tracking number
        |  |    |   | Significance
        |  |    |   Phenomenon
        |  |    Office ID
        |  Action
        Identifier

    """
    identifier: VtecFixedIdentifier
    action: VtecAction
    officeId: str
    phenomenon: VtecPhenomenon
    significance: VtecSignificance
    eventTrackingNumber: int
    beginTime: datetime
    endTime: datetime

    @classmethod
    def from_string(cls, code: str) -> VtecCode:
        """Create a VTEC code from a string."""
        if not code:
            raise ValueError("VTEC code cannot be empty")

        parts = code.strip('/').split(".")
        if len(parts) != 9:
            raise ValueError("Invalid VTEC code")

        identifier = VtecFixedIdentifier(parts[0])
        action = VtecAction(parts[1])
        officeId = parts[2]
        phenomenon = VtecPhenomenon(parts[3])
        significance = VtecSignificance(parts[4])
        eventTrackingNumber = int(parts[5])
        beginTime = datetime.strptime(parts[6], "%y%m%dT%H%MZ")
        endTime = datetime.strptime(parts[7], "%y%m%dT%H%MZ")

        return cls(identifier, action, officeId, phenomenon, significance, eventTrackingNumber, beginTime, endTime)


@dataclass
class WeatherCondition:
    coverage: CoverageType
    """The coverage of the weather condition."""

    weather: WeatherType
    """The type of weather condition."""

    intensity: IntensityType
    """The intensity of the weather condition."""

    visibility: float | None
    """The visibility in kilometers."""

    attributes: list[NotableAttributesType]
    """Notable attributes of the weather condition."""


@dataclass
class Hazard:
    """A weather hazard, using a subset of the P-VTEC code."""

    phenomenon: VtecPhenomenon
    """The type of weather hazard."""

    significance: VtecSignificance
    """The significance of the weather hazard."""

    eventNumber: int | None
    """The event number of the weather hazard."""

    beginTime: datetime
    """The start time of the hazard alert."""

    endTime: datetime
    """The end time of the hazard alert."""


@dataclass
class Conditions:
    temperature: float
    """The temperature in degrees Celsius."""

    dewpoint: float
    """The dew point in degrees Celsius."""

    humidity: int
    """The relative humidity, in percent (scaled to 0-100)"""

    apparentTemperature: float
    """The feels-like temperature in degrees Celsius."""

    heatIndex: float | None
    """The heat index (hot feels-like), or None if not present"""

    windChill: float | None
    """The wind chill (cold feels-like), or None if not present"""

    skyCover: int
    """The cloud coverage, in percent (scaled to 0-100)"""

    windDirection: int
    """The wind direction (direction it's coming from), in degrees."""

    windSpeed: float
    """The wind speed in kilometers per hour."""

    windGust: float | None
    """The wind gust speed in kilometers per hour, or None if not present"""

    weather: WeatherCondition
    """The current precipitation-driven weather condition."""

    hazards: list[Hazard]
    """The current weather hazards."""
