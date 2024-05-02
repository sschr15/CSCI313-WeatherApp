import datetime

from django.shortcuts import render

from api.noaa import *
from api.noaa.types import Forecast, CurrentObservation

_cached_hourlies: dict[tuple[float, float], tuple[datetime, Forecast]] = {}
_cached_weeklies: dict[tuple[float, float], tuple[datetime, Forecast]] = {}
_cached_currents: dict[tuple[float, float], tuple[datetime, CurrentObservation]] = {}

_fifteen_minutes = datetime.timedelta(minutes=15)
_one_hour = datetime.timedelta(hours=1)

central_time = datetime.timezone(datetime.timedelta(hours=-6))
eastern_time = datetime.timezone(datetime.timedelta(hours=-5))

locations = {
    'Fargo': (46.8772, -96.7898),
    'New York': (40.7128, -74.0060),
    'Florida': (27.6648, -81.5158),
    'Minnesota': (46.392410, -94.636230),
    'Wahpeton': (46.263920, -96.605507),
    'South Dakota': (44.5000, -100.0000),
}

time_zones = {
    'Fargo': central_time,
    'New York': eastern_time,
    'Florida': eastern_time,
    'Minnesota': central_time,
    'Wahpeton': central_time,
    'South Dakota': central_time,
}

favorites = ['Fargo', 'New York', 'Florida']
nearby = ['Minnesota', 'Wahpeton', 'South Dakota']


def index(request):
    request_time = datetime.datetime.now()

    data = {k: NoaaData.at_location(*v) for k, v in locations.items()}
    hourly_forecasts = {
        k: data[k].hourly_forecast()
        if _cached_hourlies.get(v) is None or _cached_hourlies[v][0] + _fifteen_minutes < request_time
        else _cached_hourlies[v][1]
        for k, v in locations.items()
    }

    current_conditions = {
        k: data[k].current_conditions()
        if _cached_currents.get(v) is None or _cached_currents[v][0] + _fifteen_minutes < request_time
        else _cached_currents[v][1]
        for k, v in locations.items()
    }

    for location, forecast in hourly_forecasts.items():
        now = current_conditions[location]
        lat_long = locations[location]

        if _cached_hourlies.get(lat_long) is None or _cached_hourlies[lat_long][1] != forecast:
            _cached_hourlies[lat_long] = (request_time, forecast)

        if _cached_currents.get(lat_long) is None or _cached_currents[lat_long][1] != now:
            _cached_currents[lat_long] = (request_time, current_conditions[location])

        for hour in forecast:
            hour.time_string = hour.startTime.astimezone(time_zones[location]).strftime('%I:00%p')
            hour.icon = hour.icon.split('?')[0]  # Remove sizing

            if hour.icon.endswith(',0'):
                hour.icon = hour.icon[:-2]  # Remove "0% chance of precipitation" from icon (there is no such icon)

        temperature_c = now.temperature
        temperature_f = f'{round((temperature_c * 9 / 5) + 32)}°F' if temperature_c is not None else 'Unknown'

        forecast.current_temp = temperature_f
        forecast.current_icon = now.icon

        forecast.location = ','.join(map(str, lat_long))

    return render(request, 'index.html', context={
        'favorites': {k: hourly_forecasts[k] for k in favorites},
        'nearby': {k: hourly_forecasts[k] for k in nearby},
    })


def weekly_view(request):
    request_time = datetime.datetime.now()

    data = {k: NoaaData.at_location(*v) for k, v in locations.items()}
    weekly_forecasts = {
        k: data[k].week_forecast()
        if _cached_weeklies.get(v) is None or _cached_weeklies[v][0] + _one_hour < request_time
        else _cached_weeklies[v][1]
        for k, v in locations.items()
    }

    current_conditions = {
        k: data[k].current_conditions()
        if _cached_currents.get(v) is None or _cached_currents[v][0] + _fifteen_minutes < request_time
        else _cached_currents[v][1]
        for k, v in locations.items()
    }

    for location, forecast in weekly_forecasts.items():
        lat_long = locations[location]

        if _cached_weeklies.get(lat_long) is None or _cached_weeklies[lat_long][1] != forecast:
            _cached_weeklies[lat_long] = (request_time, forecast)

        if _cached_currents.get(lat_long) is None or _cached_currents[lat_long][1] != current_conditions[location]:
            _cached_currents[lat_long] = (request_time, current_conditions[location])

        for day in forecast:
            day.time_string = day.startTime.astimezone(time_zones[location]).strftime('%m/%d')
            day.icon = day.icon.split('?')[0]  # Remove sizing but not precipitation chance

        temperature_c = current_conditions[location].temperature
        temperature_f = f'{round((temperature_c * 9 / 5) + 32)}°F' if temperature_c is not None else 'Unknown'

        forecast.current_temp = temperature_f
        forecast.current_icon = current_conditions[location].icon

        forecast.location = ','.join(map(str, lat_long))

    return render(request, 'weekly_view.html', context={
        'favorites': {k: weekly_forecasts[k] for k in favorites},
        'nearby': {k: weekly_forecasts[k] for k in nearby},
    })


def city_view(request, lat_long):
    # Specify location in two parts for typing reasons
    lat, long = map(float, lat_long.split(','))
    location = (lat, long)

    data = NoaaData.at_location(*location)

    current_conditions = _cached_currents.get(location)
    if current_conditions is None or current_conditions[0] + _fifteen_minutes < datetime.datetime.now():
        current_conditions = (datetime.datetime.now(), data.current_conditions())
        _cached_currents[location] = current_conditions

    hourly_forecast = _cached_hourlies.get(location)
    if hourly_forecast is None or hourly_forecast[0] + _fifteen_minutes < datetime.datetime.now():
        hourly_forecast = (datetime.datetime.now(), data.hourly_forecast())
        _cached_hourlies[location] = hourly_forecast

    weekly_forecast = _cached_weeklies.get(location)
    if weekly_forecast is None or weekly_forecast[0] + _one_hour < datetime.datetime.now():
        weekly_forecast = (datetime.datetime.now(), data.week_forecast())
        _cached_weeklies[location] = weekly_forecast

    temp = round((current_conditions[1].temperature * 9 / 5) + 32) if current_conditions[1].temperature is not None else None
    # noinspection PyUnresolvedReferences
    current_conditions[1].temp_string = f'{temp}°F' if temp is not None else 'Unknown'

    for hour in hourly_forecast[1]:
        hour.time_string = hour.startTime.astimezone(time_zones['Fargo']).strftime('%I:00%p')
        hour.icon = hour.icon.split('?')[0]

        if hour.icon.endswith(',0'):
            hour.icon = hour.icon[:-2]

    for day in weekly_forecast[1]:
        day.time_string = day.startTime.astimezone(time_zones['Fargo']).strftime('%m/%d')
        day.icon = day.icon.split('?')[0]

    context = {
        'where_am_i': data.relative_location,
        'current': current_conditions[1],
        'hourly': hourly_forecast[1],
        'weekly': weekly_forecast[1],
        'radar': data.radar_gif_url,
        'enhanced_radar': data.enhanced_radar_url,
    }

    return render(request, 'city_view.html', context)


# def city_view_hourly(request):
#     central_time = datetime.timezone(datetime.timedelta(hours=-6))
#     fargo = NoaaData.at_location(46.8772, -96.7898)
#     radar = fargo.radar_gif_url
#     hourlyFargo = fargo.hourly_forecast()
#     fargoHourlyTemp = {}
#     fargoHourlyTime = {}
#     fargoHourlyWindS = {}
#     fargoHourlyShortForecast = {}
#     fargoHourlyWindD = {}
#     fargoHourlyDewPoint = {}
#     fargoHourlyHumidity = {}
#     fargoHourlyPrecip = {}
#     fargoHourlyHazards = fargo.alerts()
#
#     x=0
#     for hour in hourlyFargo:
#         time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
#         fargoHourlyTime[x] = time
#         fargoHourlyTemp[x] = hour.temperature
#         fargoHourlyWindS[x] = hour.windSpeed
#         fargoHourlyWindD[x] = hour.windDirection
#         fargoHourlyShortForecast[x] = hour.shortForecast
#         fargoHourlyDewPoint[x] = hour.dewpoint
#         fargoHourlyHumidity[x] = hour.relativeHumidity
#         fargoHourlyPrecip[x] = hour.probabilityOfPrecipitation
#
#         x += 1
#
#     fargo_conditions = fargo.current_conditions()
#
#     context = {
#         'radar' : radar,
#         'current_temp1' : round(((fargo_conditions.temperature)*9/5)+32),
#        #'hazards' : fargo.current_conditions().
#         'hour_11' : fargoHourlyTime[1],
#         'hour_21' : fargoHourlyTime[2],
#         'hour_31' : fargoHourlyTime[3],
#         'hour_41' : fargoHourlyTime[4],
#         'hour_51' : fargoHourlyTime[5],
#         'hour_61' : fargoHourlyTime[6],
#         'hour_71' : fargoHourlyTime[7],
#         'hourly_temp_11' : fargoHourlyTemp[1],
#         'hourly_temp_21' : fargoHourlyTemp[2],
#         'hourly_temp_31' : fargoHourlyTemp[3],
#         'hourly_temp_41' : fargoHourlyTemp[4],
#         'hourly_temp_51' : fargoHourlyTemp[5],
#         'hourly_temp_61' : fargoHourlyTemp[6],
#         'hourly_temp_71' : fargoHourlyTemp[7],
#         'hourly_wind_11' : fargoHourlyWindS[1],
#         'hourly_wind_21' : fargoHourlyWindS[2],
#         'hourly_wind_31' : fargoHourlyWindS[3],
#         'hourly_wind_41' : fargoHourlyWindS[4],
#         'hourly_wind_51' : fargoHourlyWindS[5],
#         'hourly_wind_61' : fargoHourlyWindS[6],
#         'hourly_wind_71' : fargoHourlyWindS[7],
#         'hourly_windD_11' : fargoHourlyWindD[1],
#         'hourly_windD_21' : fargoHourlyWindD[2],
#         'hourly_windD_31' : fargoHourlyWindD[3],
#         'hourly_windD_41' : fargoHourlyWindD[4],
#         'hourly_windD_51' : fargoHourlyWindD[5],
#         'hourly_windD_61' : fargoHourlyWindD[6],
#         'hourly_windD_71' : fargoHourlyWindD[7],
#         'hourly_dp_11' : round(fargoHourlyDewPoint[1], 2),
#         'hourly_dp_21' : round(fargoHourlyDewPoint[2], 2),
#         'hourly_dp_31' : round(fargoHourlyDewPoint[3], 2),
#         'hourly_dp_41' : round(fargoHourlyDewPoint[4], 2),
#         'hourly_dp_51' : round(fargoHourlyDewPoint[5], 2),
#         'hourly_dp_61' : round(fargoHourlyDewPoint[6], 2),
#         'hourly_dp_71' : round(fargoHourlyDewPoint[7], 2),
#         'hourly_rh_11' : round(fargoHourlyHumidity[1], 2),
#         'hourly_rh_21' : round(fargoHourlyHumidity[2], 2),
#         'hourly_rh_31' : round(fargoHourlyHumidity[3], 2),
#         'hourly_rh_41' : round(fargoHourlyHumidity[4], 2),
#         'hourly_rh_51' : round(fargoHourlyHumidity[5], 2),
#         'hourly_rh_61' : round(fargoHourlyHumidity[6], 2),
#         'hourly_rh_71' : round(fargoHourlyHumidity[7], 2),
#         'hourly_p_11' : round(fargoHourlyPrecip[1], 2),
#         'hourly_p_21' : round(fargoHourlyPrecip[2], 2),
#         'hourly_p_31' : round(fargoHourlyPrecip[3], 2),
#         'hourly_p_41' : round(fargoHourlyPrecip[4], 2),
#         'hourly_p_51' : round(fargoHourlyPrecip[5], 2),
#         'hourly_p_61' : round(fargoHourlyPrecip[6], 2),
#         'hourly_p_71' : round(fargoHourlyPrecip[7], 2),
#         'hourly_short_forecast_11' : fargoHourlyShortForecast[1],
#         'hourly_short_forecast_21' : fargoHourlyShortForecast[2],
#         'hourly_short_forecast_31' : fargoHourlyShortForecast[3],
#         'hourly_short_forecast_41' : fargoHourlyShortForecast[4],
#         'hourly_short_forecast_51' : fargoHourlyShortForecast[5],
#         'hourly_short_forecast_61' : fargoHourlyShortForecast[6],
#         'hourly_short_forecast_71' : fargoHourlyShortForecast[7],
#         'hourly_hazards_11' : fargoHourlyHazards,
#
#     }
#     return render(request, 'expanded_city_view_hourly.html', context)
#
# def city_view_weekly(request):
#     central_time = datetime.timezone(datetime.timedelta(hours=-6))
#     fargo = NoaaData.at_location(46.8772, -96.7898)
#     radar = fargo.radar_gif_url
#     weeklyFargo = fargo.week_forecast()
#     fargoWeeklyTemp = {}
#     fargoWeeklyTime = {}
#     fargoWeeklyWindS = {}
#     fargoWeeklyShortForecast = {}
#     fargoWeeklyWindD = {}
#     fargoWeeklyDewPoint = {}
#     fargoWeeklyHumidity = {}
#     fargoWeeklyDetailedForecast = {}
#     fargoWeeklyHazards = fargo.alerts
#
#     x=0
#     for week in weeklyFargo:
#             time = week.startTime.astimezone(central_time).strftime('%m/%d')
#             fargoWeeklyTime[x] = time
#             fargoWeeklyTemp[x] = week.temperature
#             fargoWeeklyWindS[x] = week.windSpeed
#             fargoWeeklyWindD[x] = week.windDirection
#             fargoWeeklyShortForecast[x] = week.shortForecast
#             fargoWeeklyDewPoint[x] = week.dewpoint
#             fargoWeeklyHumidity[x] = week.relativeHumidity
#             fargoWeeklyDetailedForecast[x] = week.detailedForecast
#
#             x += 1
#
#     fargo_conditions = fargo.current_conditions()
#
#     context = {
#         'radar' : radar,
#         'current_temp1' : round(((fargo_conditions.temperature)*9/5)+32),
#        #'hazards' : fargo.current_conditions().
#         'weekly_11' : fargoWeeklyTime[1],
#         'weekly_21' : fargoWeeklyTime[2],
#         'weekly_31' : fargoWeeklyTime[3],
#         'weekly_41' : fargoWeeklyTime[4],
#         'weekly_51' : fargoWeeklyTime[5],
#         'weekly_61' : fargoWeeklyTime[6],
#         'weekly_71' : fargoWeeklyTime[7],
#         'weekly_temp_11' : fargoWeeklyTemp[1],
#         'weekly_temp_21' : fargoWeeklyTemp[2],
#         'weekly_temp_31' : fargoWeeklyTemp[3],
#         'weekly_temp_41' : fargoWeeklyTemp[4],
#         'weekly_temp_51' : fargoWeeklyTemp[5],
#         'weekly_temp_61' : fargoWeeklyTemp[6],
#         'weekly_temp_71' : fargoWeeklyTemp[7],
#         'weekly_wind_11' : fargoWeeklyWindS[1],
#         'weekly_wind_21' : fargoWeeklyWindS[2],
#         'weekly_wind_31' : fargoWeeklyWindS[3],
#         'weekly_wind_41' : fargoWeeklyWindS[4],
#         'weekly_wind_51' : fargoWeeklyWindS[5],
#         'weekly_wind_61' : fargoWeeklyWindS[6],
#         'weekly_wind_71' : fargoWeeklyWindS[7],
#         'weekly_windD_11' : fargoWeeklyWindD[1],
#         'weekly_windD_21' : fargoWeeklyWindD[2],
#         'weekly_windD_31' : fargoWeeklyWindD[3],
#         'weekly_windD_41' : fargoWeeklyWindD[4],
#         'weekly_windD_51' : fargoWeeklyWindD[5],
#         'weekly_windD_61' : fargoWeeklyWindD[6],
#         'weekly_windD_71' : fargoWeeklyWindD[7],
#         'weekly_dp_11' : round(fargoWeeklyDewPoint[1], 2),
#         'weekly_dp_21' : round(fargoWeeklyDewPoint[2], 2),
#         'weekly_dp_31' : round(fargoWeeklyDewPoint[3], 2),
#         'weekly_dp_41' : round(fargoWeeklyDewPoint[4], 2),
#         'weekly_dp_51' : round(fargoWeeklyDewPoint[5], 2),
#         'weekly_dp_61' : round(fargoWeeklyDewPoint[6], 2),
#         'weekly_dp_71' : round(fargoWeeklyDewPoint[7], 2),
#         'weekly_rh_11' : round(fargoWeeklyHumidity[1], 2),
#         'weekly_rh_21' : round(fargoWeeklyHumidity[2], 2),
#         'weekly_rh_31' : round(fargoWeeklyHumidity[3], 2),
#         'weekly_rh_41' : round(fargoWeeklyHumidity[4], 2),
#         'weekly_rh_51' : round(fargoWeeklyHumidity[5], 2),
#         'weekly_rh_61' : round(fargoWeeklyHumidity[6], 2),
#         'weekly_rh_71' : round(fargoWeeklyHumidity[7], 2),
#         'weekly_short_forecast_11' : fargoWeeklyShortForecast[1],
#         'weekly_short_forecast_21' : fargoWeeklyShortForecast[2],
#         'weekly_short_forecast_31' : fargoWeeklyShortForecast[3],
#         'weekly_short_forecast_41' : fargoWeeklyShortForecast[4],
#         'weekly_short_forecast_51' : fargoWeeklyShortForecast[5],
#         'weekly_short_forecast_61' : fargoWeeklyShortForecast[6],
#         'weekly_short_forecast_71' : fargoWeeklyShortForecast[7],
#         'weekly_detailed_forecast_11' : fargoWeeklyDetailedForecast[1],
#         'weekly_hazards_11' : fargoWeeklyHazards,
#     }
#     return render(request, 'expanded_city_view_weekly.html', context)

def about_view(request):
    return render(request, 'about_view.html')

def careers_view(request):
    return render(request, 'careers_view.html')

def faq_view(request):
    return render(request, 'faq_view.html')
