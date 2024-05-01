from __future__ import annotations
from typing import Literal, overload, ClassVar
from .types import CurrentObservation, Forecast, Alert


class NoaaData:
    """A wrapper around NOAA weather data.
    To get an instance, call `NoaaData.at_location(latitude, longitude)`.
    """

    @classmethod
    def at_location(cls, latitude: float, longitude: float) -> NoaaData:
        """Get a reference for finding weather data at a specific location.
        This must be in the form of a latitude and longitude.
        """
        ...

    def current_conditions(self) -> CurrentObservation:
        """Get the current weather conditions at the location."""
        ...

    def week_forecast(self) -> Forecast:
        """Get the forecast for the next week.
        Each entry in the forecast represents a 12-hour period. The periods specify
        name and detailed information, along with the standard always-available data.
        """
        ...

    def hourly_forecast(self) -> Forecast:
        """Get the forecast for the next 24 hours.
        Each entry in the forecast represents a 1-hour period. The periods omit
        name and detailed information.
        """
        ...

    def alerts(self) -> list[Alert]:
        """Get any weather alerts for the location.
        This will return a list of alerts, each with a headline, description, and related data.
        """
        ...

    @property
    def radar_gif_url(self) -> str:
        """Get the URL for the radar station closest to the location.
        This is a looping GIF of the past approximately-hour of radar data.
        """
        ...

    @property
    def enhanced_radar_url(self) -> str:
        """Get the URL for the enhanced radar.
        This is a fullscreen radar. The link this provides is set to the current weather station
        centered on the given location.
        """
        ...

    @overload
    def __getitem__(self, item: Literal['week', 'hour', 'weekly', 'hourly']) -> Forecast:
        """Get a forecast for a time period."""
        ...

    @overload
    def __getitem__(self, item: Literal['current', 'conditions']) -> CurrentObservation:
        """Get the current weather conditions."""
        ...

    @overload
    def __getitem__(self, item: Literal['radar', 'radar_station', 'advanced_radar', 'enhanced_radar', 'radar_map']) -> str:
        """Get a URL for the closest radar station."""
        ...

    def __init__(self, data, lat, lon):
        """Do not call this directly. Use the at_location class method instead."""
        self.__data: dict[Literal['forecast', 'forecastHourly', 'observationStations', 'radarStation'], str] = data
        self.__lat: float = lat
        self.__lon: float = lon

    __radar_url: ClassVar[str]
    __alerts_url: ClassVar[str]


def get_alert(alert_id: str) -> Alert:
    """Get a specific alert by its ID."""
    ...
