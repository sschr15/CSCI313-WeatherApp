from .utils import parse_iso_interval
from .types import *


def current_conditions_from_observation(data: dict) -> CurrentObservation:
    """Parse current conditions from an observation data object."""

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


def _period(data: dict) -> ForecastPeriod:
    """Parse a single forecast period."""
    number = data['number']
    name = data['name']
    startTime = datetime.fromisoformat(data['startTime'])
    endTime = datetime.fromisoformat(data['endTime'])
    is_daytime = data['isDaytime']
    temperature = data['temperature']
    temperature_unit = data['temperatureUnit']
    temperature_trend = data['temperatureTrend']
    probability_of_precipitation = data['probabilityOfPrecipitation']
    dewpoint = data['dewpoint']
    relative_humidity = data['relativeHumidity']
    wind_speed = data['windSpeed']
    wind_direction = data['windDirection']
    icon = data['icon']
    short_forecast = data['shortForecast']
    detailed_forecast = data['detailedForecast']

    return ForecastPeriod(number, name, startTime, endTime, is_daytime, temperature, temperature_unit,
                          temperature_trend, probability_of_precipitation, dewpoint, relative_humidity, wind_speed,
                          wind_direction, icon, short_forecast, detailed_forecast)


def forecast_from_data(data: dict) -> Forecast:
    """Parse a forecast data object."""
    units = data['units']
    forecast_generator = ForecastGeneration(data['forecastGenerator'])
    generated_at = datetime.fromisoformat(data['generatedAt'])
    update_time = datetime.fromisoformat(data['updateTime'])
    start, end = parse_iso_interval(data['validTimes'])
    periods = [_period(period) for period in data['periods']]

    return Forecast(units, forecast_generator, generated_at, update_time, start, end, periods)
