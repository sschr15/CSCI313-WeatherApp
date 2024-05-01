from .types import *


def current_conditions_from_observation(data: dict) -> CurrentObservation:
    """Parse current conditions from an observation data object."""
    return CurrentObservation(**data)


def forecast_from_data(data: dict) -> Forecast:
    """Parse a forecast data object."""
    return Forecast(**data)
