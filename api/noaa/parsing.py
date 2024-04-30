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


def __current_hazards(data: list) -> list[Hazard]:
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


def current_conditions_from_observation(data: dict) -> CurrentObservation:
    """Parse current conditions from a gridpoint forecast."""

    observation_time = datetime.fromisoformat(data['timestamp'])
    text_description = data['textDescription']
    icon = data['icon']
    present_weather: list[MetarPhenomenon] = data['presentWeather']
    temperature = data['temperature']['value']
    dewpoint = data['dewpoint']['value']
    wind_direction = data['windDirection']['value']
    wind_speed = data['windSpeed']['value']
    wind_gust = data['windGust']['value']
    barometric_pressure = data['barometricPressure']['value']
    sea_level_pressure = data['seaLevelPressure']['value']
    visibility = data['visibility']['value']
    max_temperature = data['maxTemperatureLast24Hours']['value']
    min_temperature = data['minTemperatureLast24Hours']['value']
    precipitation_last_hour = data['precipitationLastHour']['value']
    precipitation_last_3_hours = data['precipitationLast3Hours']['value']
    precipitation_last_6_hours = data['precipitationLast6Hours']['value']
    relative_humidity = data['relativeHumidity']['value']
    wind_chill = data['windChill']['value']
    heat_index = data['heatIndex']['value']

    return CurrentObservation(observation_time, text_description, icon, present_weather, temperature, dewpoint,
                              wind_direction, wind_speed, wind_gust, barometric_pressure, sea_level_pressure,
                              visibility, max_temperature, min_temperature, precipitation_last_hour,
                              precipitation_last_3_hours, precipitation_last_6_hours, relative_humidity,
                              wind_chill, heat_index)
