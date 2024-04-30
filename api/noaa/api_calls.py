from .parsing import *
import requests


def current_data(latitude: float, longitude: float) -> CurrentObservation:
    """Fetch the current weather data for a given latitude and longitude."""
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    stations_url = data['properties']['observationStations']
    response = requests.get(stations_url)
    response.raise_for_status()
    data = response.json()
    station_url = data['observationStations'][0]
    latest_observation_url = f"{station_url}/observations/latest"
    response = requests.get(latest_observation_url)
    response.raise_for_status()
    data = response.json()
    return current_conditions_from_observation(data['properties'])
