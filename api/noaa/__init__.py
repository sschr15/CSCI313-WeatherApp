from __future__ import annotations
from .api_calls import current_data
from base64 import b64encode
from json import dumps
from urllib.parse import quote as encode_url
from .parsing import current_conditions_from_observation, forecast_from_data
from .types import *
import requests


def _request(url):
    response = requests.get(
        url,
        headers={
            'User-Agent': '(CSCI-313 students; steven.sschr15@hotmail.com)',
            'Accept': 'application/geo+json',
        }
    )
    response.raise_for_status()
    return response.json()


class NoaaData:
    __radar_url = 'https://radar.weather.gov/ridge/standard/%s_loop.gif'
    __alerts_url = 'https://api.weather.gov/alerts/active?point=%s,%s'

    def __init__(self, _data, lat, lon):
        self.__data = _data
        self.__lat = lat
        self.__lon = lon

    @classmethod
    def at_location(cls, latitude, longitude):
        url = f"https://api.weather.gov/points/{latitude},{longitude}"
        data = _request(url)
        return cls(data['properties'], latitude, longitude)

    def week_forecast(self):
        url = self.__data['forecast']
        data = _request(url)
        return forecast_from_data(data['properties'])

    def hourly_forecast(self):
        url = self.__data['forecastHourly']
        data = _request(url)
        return forecast_from_data(data['properties'])

    def current_conditions(self):
        url = self.__data['observationStations']
        data = _request(url)
        station_url = data['observationStations'][0]
        latest_observation_url = f'{station_url}/observations/latest'
        response = requests.get(latest_observation_url)
        response.raise_for_status()
        data = response.json()
        return current_conditions_from_observation(data['properties'])

    def alerts(self):
        url = NoaaData.__alerts_url % (self.__lat, self.__lon)
        data = _request(url)
        return [Alert(alert['properties']) for alert in data['features']]

    @property
    def radar_gif_url(self):
        station_id = self.__data['radarStation']
        return NoaaData.__radar_url % station_id

    @property
    def enhanced_radar_url(self):
        station_id = self.__data['radarStation']
        obj = {
            'agenda': {
                'id': 'local',  # single radar view
                'center': [self.__lon, self.__lat],
                'zoom': 8,
                'filter': 'WSR-88D',  # only show radars, not forecast offices
                'layer': 'sr_bref',  # base reflectivity
                'station': station_id,
            }
        }

        json = dumps(obj)
        settings = f'v1_{b64encode(json.encode()).decode()}'
        return f'https://radar.weather.gov/?settings={encode_url(settings)}'

    def __getitem__(self, key):
        if key in ('week', 'weekly'):
            return self.week_forecast()
        elif key in ('hour', 'hourly'):
            return self.hourly_forecast()
        elif key in ('current', 'conditions'):
            return self.current_conditions()
        elif key in ('radar', 'radar_station'):
            return self.radar_gif_url
        elif key in ('enhanced_radar', 'radar_map', 'advanced_radar'):
            return self.enhanced_radar_url
        else:
            raise KeyError(f'Invalid key: {key}')

    def __repr__(self):
        return f'NoaaData({self.__data})'


def get_alert(alert_id):
    url = f'https://api.weather.gov/alerts/{alert_id}'
    data = _request(url)
    return Alert(data['properties'])


__all__ = ['NoaaData', 'get_alert']
