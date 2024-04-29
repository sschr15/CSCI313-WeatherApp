from .utils import parse_iso_interval
from .types import *


def __current_weather(data: dict) -> WeatherCondition:
    """Parse the current weather condition from a gridpoint forecast."""
    coverage = data['coverage']
    weather = data['weather']
    intensity = data['intensity']
    visibility = data['visibility']['value']
    attributes = data['attributes']

    return WeatherCondition(coverage, weather, intensity, visibility, attributes)


def __current_hazards(data: dict) -> list[Hazard]:
    """Parse the current weather hazards from a gridpoint forecast."""
    hazards = []
    for hazard_period in data:
        start, end = parse_iso_interval(hazard_period['validTime'])
        for hazard in hazard_period['value']:
            phenomenon = VtecPhenomenon(hazard['phenomenon'])
            significance = VtecSignificance(hazard['significance'])
            event_number = hazard['eventNumber']
            hazards.append(Hazard(phenomenon, significance, event_number, start, end))
    return hazards


def current_conditions_from_gridpoint(data: dict) -> Conditions:
    """Parse current conditions from a gridpoint forecast."""

    temperature = data['temperature']['values'][0]['value']
    if data['temperature']['uom'] == 'wmoUnit:degF':
        temperature = (temperature - 32) * 5 / 9

    dewpoint = data['dewpoint']['values'][0]['value']
    if data['dewpoint']['uom'] == 'wmoUnit:degF':
        dewpoint = (dewpoint - 32) * 5 / 9

    relative_humidity = data['relativeHumidity']['values'][0]['value']

    apparent_temperature = data['apparentTemperature']['values'][0]['value']
    if data['apparentTemperature']['uom'] == 'wmoUnit:degF':
        apparent_temperature = (apparent_temperature - 32) * 5 / 9

    heat_index = data['heatIndex']['values'][0]['value']
    if data['heatIndex']['uom'] == 'wmoUnit:degF' and heat_index is not None:
        heat_index = (heat_index - 32) * 5 / 9

    wind_chill = data['windChill']['values'][0]['value']
    if data['windChill']['uom'] == 'wmoUnit:degF' and wind_chill is not None:
        wind_chill = (wind_chill - 32) * 5 / 9

    sky_cover = data['skyCover']['values'][0]['value']
    wind_direction = data['windDirection']['values'][0]['value']
    wind_speed = data['windSpeed']['values'][0]['value']
    wind_gust = data['windGust']['values'][0]['value'] if 'windGust' in data else None

    weather = __current_weather(data['weather']['values'][0]['value'])
    hazards = __current_hazards(data['hazards'])

    return Conditions(temperature, dewpoint, relative_humidity, apparent_temperature, heat_index, wind_chill,
                      sky_cover, wind_direction, wind_speed, wind_gust, weather, hazards)
