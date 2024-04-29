from .parsing import *
import requests


def current_data(latitude: float, longitude: float) -> Conditions:
    """Fetch the current weather data for a given latitude and longitude."""
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    forecast_url = data['properties']['forecastGridData']
    response = requests.get(forecast_url)
    response.raise_for_status()
    data = response.json()
    return current_conditions_from_gridpoint(data['properties'])
