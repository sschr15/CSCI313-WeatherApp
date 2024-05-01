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

MetarIntensityType = Literal[
    'light',
    'heavy',
]

MetarModifierType = Literal[
    'patches',
    'blowing',
    'low_drifting',
    'freezing',
    'shallow',
    'partial',
    'showers',
]

MetarWeatherType = Literal[
    'fog_mist',
    'dust_storm',
    'dust',
    'drizzle',
    'funnel_cloud',  # mmm, funnel cake
    'fog',
    'smoke',
    'hail',
    'snow_pellets',
    'haze',
    'ice_crystals',
    'ice_pellets',
    'dust_whirls',
    'spray',
    'rain',
    'sand',
    'snow_grains',
    'snow',
    'squalls',
    'sand_storm',
    'thunderstorms',
    'unknown',
    'volcanic_ash',
]

WindDirectionType = Literal[
    'N', 'NNE', 'NE', 'ENE',
    'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW',
    'W', 'WNW', 'NW', 'NNW',
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


@dataclass
class MetarPhenomenon:  # yes this is the name NOAA uses
    """A representation of a decoded METAR phenomenon string."""

    intensity: MetarIntensityType | None
    """The intensity of the phenomenon, if applicable."""

    modifier: MetarModifierType | None
    """The modifier of the phenomenon, if applicable."""

    weather: MetarWeatherType
    """The type of weather phenomenon."""

    rawString: str
    """The raw METAR string for the phenomenon."""


@dataclass
class CurrentObservation:
    """A snippet of the current weather observation."""

    timestamp: datetime
    """The timestamp of the observation."""

    textDescription: str
    """A short text description of the weather."""

    icon: str  # deprecated by NOAA, but I care not one bit
    """A URL to an icon representing the weather."""

    presentWeather: list[MetarPhenomenon]
    """The current weather conditions."""

    temperature: float
    """The temperature in degrees Celsius."""

    dewpoint: float
    """The dew point in degrees Celsius."""

    windDirection: int
    """The wind direction (direction it's coming from), in degrees."""

    windSpeed: float
    """The wind speed in kilometers per hour."""

    windGust: float | None
    """The wind gust speed in kilometers per hour, or None if not present in the data."""

    barometricPressure: float
    """The barometric pressure in pascals."""

    seaLevelPressure: float
    """The pressure if measured at sea level in pascals."""

    visibility: float
    """The visibility in kilometers."""

    maxTemperatureLast24Hours: float | None
    """The maximum temperature in the last 24 hours, or None if not present in the data."""

    minTemperatureLast24Hours: float | None
    """The minimum temperature in the last 24 hours, or None if not present in the data."""

    precipitationLastHour: float
    """The precipitation in the last hour in millimeters."""

    precipitationLast3Hours: float | None
    """The precipitation in the last 3 hours in millimeters, or None if not present in the data."""

    precipitationLast6Hours: float | None
    """The precipitation in the last 6 hours in millimeters, or None if not present in the data."""

    relativeHumidity: float
    """The relative humidity, in percent (scaled to 0-100, not rounded)."""

    windChill: float | None
    """The wind chill (cold feels-like), or None if not present in the data."""

    heatIndex: float | None
    """The heat index (hot feels-like), or None if not present in the data."""


@dataclass
class ForecastPeriod:
    """A period of weather forecast data."""

    number: int

    name: str
    """A name for the forecast period. May be empty."""

    startTime: datetime
    """The start time of the forecast period."""

    endTime: datetime
    """The end time of the forecast period."""

    isDaytime: bool
    """Whether the forecast period is during the day."""

    temperature: int
    """The temperature in the unit specified by temperatureUnit."""

    temperatureUnit: Literal["F", "C"]
    """The unit of the temperature. Either degrees Fahrenheit or Celsius."""

    temperatureTrend: Literal["falling", "rising"] | None
    """The trend of the temperature."""

    precipProbability: int
    """The probability of precipitation, in percent (scaled to 0-100)."""

    dewpoint: float
    """The dew point in degrees Celsius."""

    relativeHumidity: int
    """The relative humidity, in percent (scaled to 0-100)."""

    windSpeed: str
    """A string representation of the wind speed."""

    windDirection: WindDirectionType
    """A string representation of the wind direction."""

    icon: str  # again deprecated by NOAA, but their own API completely ignores feature flags...
    """A URL to an icon representing the weather."""

    shortForecast: str
    """A brief description of the weather."""

    detailedForecast: str
    """A detailed description of the weather. May be empty if none is provided."""


class ForecastGeneration(Enum):
    WeekForecast = "BaselineForecastGenerator"
    HourForecast = "HourlyForecastGenerator"


@dataclass
class Forecast:
    """A weather forecast."""

    units: Literal["us", "si"]
    """The units used in the forecast. Either US or metric (denoted as SI)."""

    generation: ForecastGeneration
    """The type of forecast generator used.
    This identifies whether this forecast details extended periods or hourly data.
    """

    generatedAt: datetime
    """The time the forecast was generated."""

    updateTime: datetime
    """The time the forecast was last updated."""

    validPeriodStart: datetime
    """The start of the forecast period."""

    validPeriodEnd: datetime
    """The end of the forecast period."""

    periods: list[ForecastPeriod]
    """The forecast periods."""

    def __getitem__(self, item: int) -> ForecastPeriod:
        return self.periods[item]

    def __iter__(self):
        return iter(self.periods)
