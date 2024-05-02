from django.shortcuts import render
from api.noaa import NoaaData
from django.http import HttpResponse
from api.noaa import *
import datetime



def index(request):
    fargo = NoaaData.at_location(46.8772, -96.7898)
    new_york = NoaaData.at_location(40.7128, -74.0060)
    florida = NoaaData.at_location(27.6648, -81.5158)
    minnesota = NoaaData.at_location(46.392410, -94.636230)
    wahpeton = NoaaData.at_location(46.263920, -96.605507)
    south_dakota = NoaaData.at_location(44.5000, -100.0000)
    central_time = datetime.timezone(datetime.timedelta(hours=-6))

    #fargo hourly data
    hourlyFargo = fargo.hourly_forecast()
    fargoHourlyTemp = {}
    fargoHourlyTime = {}
    fargoHourlyWind = {}
    fargoHourlyShortForecast = {}
    #new_york hourly data
    hourlyNewYork= new_york.hourly_forecast()
    new_yorkHourlyTemp = {}
    new_yorkHourlyTime = {}
    new_yorkHourlyWind = {}
    new_yorkHourlyShortForecast = {}
    #florida hourly data
    hourlyFlorida = florida.hourly_forecast()
    floridaHourlyTemp = {}
    floridaHourlyTime = {}
    floridaHourlyWind = {}
    floridaHourlyShortForecast = {}
    #minnesota hourly data
    hourlyMinnesota = minnesota.hourly_forecast()
    minnesotaHourlyTemp = {}
    minnesotaHourlyTime = {}
    minnesotaHourlyWind = {}
    minnesotaHourlyShortForecast = {}
    #wahpeton hourly data
    hourlyWahpeton = wahpeton.hourly_forecast()
    wahpetonHourlyTemp = {}
    wahpetonHourlyTime = {}
    wahpetonHourlyWind = {}
    wahpetonHourlyShortForecast = {}
    #SD hourly data
    hourlySouthDakota = south_dakota.hourly_forecast()
    south_dakotaHourlyTemp = {}
    south_dakotaHourlyTime = {}
    south_dakotaHourlyWind = {}
    south_dakotaHourlyShortForecast = {}
    
    x = 0
    z = 0
    y = 0
    s = 0
    w = 0 
    q = 0

    for hour in hourlyFargo:
        time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
        fargoHourlyTime[x] = time
        fargoHourlyTemp[x] = hour.temperature
        fargoHourlyWind[x] = hour.windSpeed
        fargoHourlyShortForecast[x] = hour.shortForecast
        x += 1
    
    for hour in hourlyNewYork:
        time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
        new_yorkHourlyTime[y] = time
        new_yorkHourlyTemp[y] = hour.temperature
        new_yorkHourlyWind[y] = hour.windSpeed
        new_yorkHourlyShortForecast[y] = hour.shortForecast
        y += 1
    
    for hour in hourlyFlorida:
        time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
        floridaHourlyTime[z] = time
        floridaHourlyTemp[z] = hour.temperature
        floridaHourlyWind[z] = hour.windSpeed
        floridaHourlyShortForecast[z] = hour.shortForecast
        z += 1
    
    for hour in hourlyMinnesota:
        time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
        minnesotaHourlyTime[s] = time
        minnesotaHourlyTemp[s] = hour.temperature
        minnesotaHourlyWind[s] = hour.windSpeed
        minnesotaHourlyShortForecast[s] = hour.shortForecast
        s += 1
    
    for hour in hourlyWahpeton:
        time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
        wahpetonHourlyTime[w] = time
        wahpetonHourlyTemp[w] = hour.temperature
        wahpetonHourlyWind[w] = hour.windSpeed
        wahpetonHourlyShortForecast[w] = hour.shortForecast
        w += 1
    
    for hour in hourlySouthDakota:
        time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
        south_dakotaHourlyTime[q] = time
        south_dakotaHourlyTemp[q] = hour.temperature
        south_dakotaHourlyWind[q] = hour.windSpeed
        south_dakotaHourlyShortForecast[q] = hour.shortForecast
        q += 1

    fargo_conditions = fargo.current_conditions()
    new_york_conditions = new_york.current_conditions()
    florida_conditions = florida.current_conditions()
    minnesota_conditions = minnesota.current_conditions()
    wahpeton_conditions = wahpeton.current_conditions()
    south_dakota_conditions = south_dakota.current_conditions()

    context = {
        'current_temp1' : round(((fargo_conditions.temperature)*9/5)+32),
        'hour_11' : fargoHourlyTime[1],
        'hour_21' : fargoHourlyTime[2],
        'hour_31' : fargoHourlyTime[3],
        'hour_41' : fargoHourlyTime[4],
        'hour_51' : fargoHourlyTime[5],
        'hour_61' : fargoHourlyTime[6],
        'hour_71' : fargoHourlyTime[7],
        'hourly_temp_11' : fargoHourlyTemp[1],
        'hourly_temp_21' : fargoHourlyTemp[2],
        'hourly_temp_31' : fargoHourlyTemp[3],
        'hourly_temp_41' : fargoHourlyTemp[4],
        'hourly_temp_51' : fargoHourlyTemp[5],
        'hourly_temp_61' : fargoHourlyTemp[6],
        'hourly_temp_71' : fargoHourlyTemp[7],
        'hourly_wind_11' : fargoHourlyWind[1].replace(" ", ""),
        'hourly_wind_21' : fargoHourlyWind[2].replace(" ", ""),
        'hourly_wind_31' : fargoHourlyWind[3].replace(" ", ""),
        'hourly_wind_41' : fargoHourlyWind[4].replace(" ", ""),
        'hourly_wind_51' : fargoHourlyWind[5].replace(" ", ""),
        'hourly_wind_61' : fargoHourlyWind[6].replace(" ", ""),
        'hourly_wind_71' : fargoHourlyWind[7].replace(" ", ""),
        'hourly_short_forecast_11' : fargoHourlyShortForecast[1],
        'hourly_short_forecast_21' : fargoHourlyShortForecast[2],
        'hourly_short_forecast_31' : fargoHourlyShortForecast[3],
        'hourly_short_forecast_41' : fargoHourlyShortForecast[4],
        'hourly_short_forecast_51' : fargoHourlyShortForecast[5],
        'hourly_short_forecast_61' : fargoHourlyShortForecast[6],
        'hourly_short_forecast_71' : fargoHourlyShortForecast[7],
        #2nd set
        'current_temp2' : round(((new_york_conditions.temperature)*9/5)+32),
        'hour_12' : new_yorkHourlyTime[1],
        'hour_22' : new_yorkHourlyTime[2],
        'hour_32' : new_yorkHourlyTime[3],
        'hour_42' : new_yorkHourlyTime[4],
        'hour_52' : new_yorkHourlyTime[5],
        'hour_62' : new_yorkHourlyTime[6],
        'hour_72' : new_yorkHourlyTime[7],
        'hourly_temp_12' : new_yorkHourlyTemp[1],
        'hourly_temp_22' : new_yorkHourlyTemp[2],
        'hourly_temp_32' : new_yorkHourlyTemp[3],
        'hourly_temp_42' : new_yorkHourlyTemp[4],
        'hourly_temp_52' : new_yorkHourlyTemp[5],
        'hourly_temp_62' : new_yorkHourlyTemp[6],
        'hourly_temp_72' : new_yorkHourlyTemp[7],
        'hourly_wind_12' : new_yorkHourlyWind[1].replace(" ", ""),
        'hourly_wind_22' : new_yorkHourlyWind[2].replace(" ", ""),
        'hourly_wind_32' : new_yorkHourlyWind[3].replace(" ", ""),
        'hourly_wind_42' : new_yorkHourlyWind[4].replace(" ", ""),
        'hourly_wind_52' : new_yorkHourlyWind[5].replace(" ", ""),
        'hourly_wind_62' : new_yorkHourlyWind[6].replace(" ", ""),
        'hourly_wind_72' : new_yorkHourlyWind[7].replace(" ", ""),
        'hourly_short_forecast_12' : new_yorkHourlyShortForecast[1],
        'hourly_short_forecast_22' : new_yorkHourlyShortForecast[2],
        'hourly_short_forecast_32' : new_yorkHourlyShortForecast[3],
        'hourly_short_forecast_42' : new_yorkHourlyShortForecast[4],
        'hourly_short_forecast_52' : new_yorkHourlyShortForecast[5],
        'hourly_short_forecast_62' : new_yorkHourlyShortForecast[6],
        'hourly_short_forecast_72' : new_yorkHourlyShortForecast[7],
        #3rd set
        'current_temp3' : round(((florida_conditions.temperature)*9/5)+32),
        'hour_13' : floridaHourlyTime[1],
        'hour_23' : floridaHourlyTime[2],
        'hour_33' : floridaHourlyTime[3],
        'hour_43' : floridaHourlyTime[4],
        'hour_53' : floridaHourlyTime[5],
        'hour_63' : floridaHourlyTime[6],
        'hour_73' : floridaHourlyTime[7],
        'hourly_temp_13' : floridaHourlyTemp[1],
        'hourly_temp_23' : floridaHourlyTemp[2],
        'hourly_temp_33' : floridaHourlyTemp[3],
        'hourly_temp_43' : floridaHourlyTemp[4],
        'hourly_temp_53' : floridaHourlyTemp[5],
        'hourly_temp_63' : floridaHourlyTemp[6],
        'hourly_temp_73' : floridaHourlyTemp[7],
        'hourly_wind_13' : floridaHourlyWind[1].replace(" ", ""),
        'hourly_wind_23' : floridaHourlyWind[2].replace(" ", ""),
        'hourly_wind_33' : floridaHourlyWind[3].replace(" ", ""),
        'hourly_wind_43' : floridaHourlyWind[4].replace(" ", ""),
        'hourly_wind_53' : floridaHourlyWind[5].replace(" ", ""),
        'hourly_wind_63' : floridaHourlyWind[6].replace(" ", ""),
        'hourly_wind_73' : floridaHourlyWind[7].replace(" ", ""),
        'hourly_short_forecast_13' : floridaHourlyShortForecast[1],
        'hourly_short_forecast_23' : floridaHourlyShortForecast[2],
        'hourly_short_forecast_33' : floridaHourlyShortForecast[3],
        'hourly_short_forecast_43' : floridaHourlyShortForecast[4],
        'hourly_short_forecast_53' : floridaHourlyShortForecast[5],
        'hourly_short_forecast_63' : floridaHourlyShortForecast[6],
        'hourly_short_forecast_73' : floridaHourlyShortForecast[7],
        #4th set
        'current_temp4' : round(((minnesota_conditions.temperature)*9/5)+32),
        'hour_14' : minnesotaHourlyTime[1],
        'hour_24' : minnesotaHourlyTime[2],
        'hour_34' : minnesotaHourlyTime[3],
        'hour_44' : minnesotaHourlyTime[4],
        'hour_54' : minnesotaHourlyTime[5],
        'hour_64' : minnesotaHourlyTime[6],
        'hour_74' : minnesotaHourlyTime[7],
        'hourly_temp_14' : minnesotaHourlyTemp[1],
        'hourly_temp_24' : minnesotaHourlyTemp[2],
        'hourly_temp_34' : minnesotaHourlyTemp[3],
        'hourly_temp_44' : minnesotaHourlyTemp[4],
        'hourly_temp_54' : minnesotaHourlyTemp[5],
        'hourly_temp_64' : minnesotaHourlyTemp[6],
        'hourly_temp_74' : minnesotaHourlyTemp[7],
        'hourly_wind_14' : minnesotaHourlyWind[1].replace(" ", ""),
        'hourly_wind_24' : minnesotaHourlyWind[2].replace(" ", ""),
        'hourly_wind_34' : minnesotaHourlyWind[3].replace(" ", ""),
        'hourly_wind_44' : minnesotaHourlyWind[4].replace(" ", ""),
        'hourly_wind_54' : minnesotaHourlyWind[5].replace(" ", ""),
        'hourly_wind_64' : minnesotaHourlyWind[6].replace(" ", ""),
        'hourly_wind_74' : minnesotaHourlyWind[7].replace(" ", ""),
        'hourly_short_forecast_14' : minnesotaHourlyShortForecast[1],
        'hourly_short_forecast_24' : minnesotaHourlyShortForecast[2],
        'hourly_short_forecast_34' : minnesotaHourlyShortForecast[3],
        'hourly_short_forecast_44' : minnesotaHourlyShortForecast[4],
        'hourly_short_forecast_54' : minnesotaHourlyShortForecast[5],
        'hourly_short_forecast_64' : minnesotaHourlyShortForecast[6],
        'hourly_short_forecast_74' : minnesotaHourlyShortForecast[7],
        #5th set
        'current_temp5' : round(((wahpeton_conditions.temperature)*9/5)+32),
        'hour_15' : wahpetonHourlyTime[1],
        'hour_25' : wahpetonHourlyTime[2],
        'hour_35' : wahpetonHourlyTime[3],
        'hour_45' : wahpetonHourlyTime[4],
        'hour_55' : wahpetonHourlyTime[5],
        'hour_65' : wahpetonHourlyTime[6],
        'hour_75' : wahpetonHourlyTime[7],
        'hourly_temp_15' : wahpetonHourlyTemp[1],
        'hourly_temp_25' : wahpetonHourlyTemp[2],
        'hourly_temp_35' : wahpetonHourlyTemp[3],
        'hourly_temp_45' : wahpetonHourlyTemp[4],
        'hourly_temp_55' : wahpetonHourlyTemp[5],
        'hourly_temp_65' : wahpetonHourlyTemp[6],
        'hourly_temp_75' : wahpetonHourlyTemp[7],
        'hourly_wind_15' : wahpetonHourlyWind[1].replace(" ", ""),
        'hourly_wind_25' : wahpetonHourlyWind[2].replace(" ", ""),
        'hourly_wind_35' : wahpetonHourlyWind[3].replace(" ", ""),
        'hourly_wind_45' : wahpetonHourlyWind[4].replace(" ", ""),
        'hourly_wind_55' : wahpetonHourlyWind[5].replace(" ", ""),
        'hourly_wind_65' : wahpetonHourlyWind[6].replace(" ", ""),
        'hourly_wind_75' : wahpetonHourlyWind[7].replace(" ", ""),
        'hourly_short_forecast_15' : wahpetonHourlyShortForecast[1],
        'hourly_short_forecast_25' : wahpetonHourlyShortForecast[2],
        'hourly_short_forecast_35' : wahpetonHourlyShortForecast[3],
        'hourly_short_forecast_45' : wahpetonHourlyShortForecast[4],
        'hourly_short_forecast_55' : wahpetonHourlyShortForecast[5],
        'hourly_short_forecast_65' : wahpetonHourlyShortForecast[6],
        'hourly_short_forecast_75' : wahpetonHourlyShortForecast[7],
        #6th set
        'current_temp6' : round(((south_dakota_conditions.temperature)*9/5)+32),
        'hour_16' : south_dakotaHourlyTime[1],
        'hour_26' : south_dakotaHourlyTime[2],
        'hour_36' : south_dakotaHourlyTime[3],
        'hour_46' : south_dakotaHourlyTime[4],
        'hour_56' : south_dakotaHourlyTime[5],
        'hour_66' : south_dakotaHourlyTime[6],
        'hour_76' : south_dakotaHourlyTime[7],
        'hourly_temp_16' : south_dakotaHourlyTemp[1],
        'hourly_temp_26' : south_dakotaHourlyTemp[2],
        'hourly_temp_36' : south_dakotaHourlyTemp[3],
        'hourly_temp_46' : south_dakotaHourlyTemp[4],
        'hourly_temp_56' : south_dakotaHourlyTemp[5],
        'hourly_temp_66' : south_dakotaHourlyTemp[6],
        'hourly_temp_76' : south_dakotaHourlyTemp[7],
        'hourly_wind_16' : south_dakotaHourlyWind[1].replace(" ", ""),
        'hourly_wind_26' : south_dakotaHourlyWind[2].replace(" ", ""),
        'hourly_wind_36' : south_dakotaHourlyWind[3].replace(" ", ""),
        'hourly_wind_46' : south_dakotaHourlyWind[4].replace(" ", ""),
        'hourly_wind_56' : south_dakotaHourlyWind[5].replace(" ", ""),
        'hourly_wind_66' : south_dakotaHourlyWind[6].replace(" ", ""),
        'hourly_wind_76' : south_dakotaHourlyWind[7].replace(" ", ""),
        'hourly_short_forecast_16' : south_dakotaHourlyShortForecast[1],
        'hourly_short_forecast_26' : south_dakotaHourlyShortForecast[2],
        'hourly_short_forecast_36' : south_dakotaHourlyShortForecast[3],
        'hourly_short_forecast_46' : south_dakotaHourlyShortForecast[4],
        'hourly_short_forecast_56' : south_dakotaHourlyShortForecast[5],
        'hourly_short_forecast_66' : south_dakotaHourlyShortForecast[6],
        'hourly_short_forecast_76' : south_dakotaHourlyShortForecast[7],
    }
    return render(request, 'index.html', context=context)

def weekly_view(request):
    fargo = NoaaData.at_location(46.8772, -96.7898)
    new_york = NoaaData.at_location(40.7128, -74.0060)
    florida = NoaaData.at_location(27.6648, -81.5158)
    minnesota = NoaaData.at_location(46.392410, -94.636230)
    wahpeton = NoaaData.at_location(46.263920, -96.605507)
    south_dakota = NoaaData.at_location(44.5000, -100.0000)
    central_time = datetime.timezone(datetime.timedelta(hours=-6))

    #fargo weekly data
    weeklyFargo = fargo.week_forecast()
    fargoWeeklyTemp = {}
    fargoWeeklyDate = {}
    fargoWeeklyWind = {}
    fargoWeeklyShortForecast = {}
    #new_york weekly data
    weeklyNewYork= new_york.week_forecast()
    new_yorkWeeklyTemp = {}
    new_yorkWeeklyDate = {}
    new_yorkWeeklyWind = {}
    new_yorkWeeklyShortForecast = {}
    #florida weekly data
    weeklyFlorida = florida.week_forecast()
    floridaWeeklyTemp = {}
    floridaWeeklyDate = {}
    floridaWeeklyWind = {}
    floridaWeeklyShortForecast = {}
    #minnesota weekly data
    weeklyMinnesota = minnesota.week_forecast()
    minnesotaWeeklyTemp = {}
    minnesotaWeeklyDate = {}
    minnesotaWeeklyWind = {}
    minnesotaWeeklyShortForecast = {}
    #wahpeton weekly data
    weeklyWahpeton = wahpeton.week_forecast()
    wahpetonWeeklyTemp = {}
    wahpetonWeeklyDate = {}
    wahpetonWeeklyWind = {}
    wahpetonWeeklyShortForecast = {}
    #SD weekly data
    weeklySouthDakota = south_dakota.week_forecast()
    south_dakotaWeeklyTemp = {}
    south_dakotaWeeklyDate = {}
    south_dakotaWeeklyWind = {}
    south_dakotaWeeklyShortForecast = {}

    x=0
    for week in weeklyFargo:
        day = week.startTime.astimezone(central_time).strftime('%m/%d')
        fargoWeeklyDate[x] = day
        fargoWeeklyTemp[x] = week.temperature
        fargoWeeklyWind[x] = week.windSpeed
        fargoWeeklyShortForecast[x] = week.shortForecast
        x += 1
    y=0
    for week in weeklyNewYork:
        day = week.startTime.astimezone(central_time).strftime('%m/%d')
        new_yorkWeeklyDate[y] = day
        new_yorkWeeklyTemp[y] = week.temperature
        new_yorkWeeklyWind[y] = week.windSpeed
        new_yorkWeeklyShortForecast[y] = week.shortForecast
        y += 1
    z=0
    for week in weeklyFlorida:
        day = week.startTime.astimezone(central_time).strftime('%m/%d')
        floridaWeeklyDate[z] = day
        floridaWeeklyTemp[z] = week.temperature
        floridaWeeklyWind[z] = week.windSpeed
        floridaWeeklyShortForecast[z] = week.shortForecast
        z += 1
    s=0
    for week in weeklyMinnesota:
        day = week.startTime.astimezone(central_time).strftime('%m/%d')
        minnesotaWeeklyDate[s] = day
        minnesotaWeeklyTemp[s] = week.temperature
        minnesotaWeeklyWind[s] = week.windSpeed
        minnesotaWeeklyShortForecast[s] = week.shortForecast
        s += 1
    w=0
    for week in weeklyWahpeton:
        day = week.startTime.astimezone(central_time).strftime('%m/%d')
        wahpetonWeeklyDate[w] = day
        wahpetonWeeklyTemp[w] = week.temperature
        wahpetonWeeklyWind[w] = week.windSpeed
        wahpetonWeeklyShortForecast[w] = week.shortForecast
        w += 1
    q=0
    for week in weeklySouthDakota:
        day = week.startTime.astimezone(central_time).strftime('%m/%d')
        south_dakotaWeeklyDate[q] = day
        south_dakotaWeeklyTemp[q] = week.temperature
        south_dakotaWeeklyWind[q] = week.windSpeed
        south_dakotaWeeklyShortForecast[q] = week.shortForecast
        q += 1

    fargo_conditions = fargo.current_conditions()
    new_york_conditions = new_york.current_conditions()
    florida_conditions = florida.current_conditions()
    minnesota_conditions = minnesota.current_conditions()
    wahpeton_conditions = wahpeton.current_conditions()
    south_dakota_conditions = south_dakota.current_conditions()

    context = {
        'current_temp1' : round(((fargo_conditions.temperature)*9/5)+32),
        'week_date_11' : fargoWeeklyDate[1],
        'week_date_21' : fargoWeeklyDate[2],
        'week_date_31' : fargoWeeklyDate[3],
        'week_date_41' : fargoWeeklyDate[4],
        'week_date_51' : fargoWeeklyDate[5],
        'week_date_61' : fargoWeeklyDate[6],
        'week_date_71' : fargoWeeklyDate[7],
        'week_temp_11' : fargoWeeklyTemp[1],
        'week_temp_21' : fargoWeeklyTemp[2],
        'week_temp_31' : fargoWeeklyTemp[3],
        'week_temp_41' : fargoWeeklyTemp[4],
        'week_temp_51' : fargoWeeklyTemp[5],
        'week_temp_61' : fargoWeeklyTemp[6],
        'week_temp_71' : fargoWeeklyTemp[7],
        'week_wind_11' : fargoWeeklyWind[1].replace(" ", "").replace("to", "-"),
        'week_wind_21' : fargoWeeklyWind[2].replace(" ", "").replace("to", "-"),
        'week_wind_31' : fargoWeeklyWind[3].replace(" ", "").replace("to", "-"),
        'week_wind_41' : fargoWeeklyWind[4].replace(" ", "").replace("to", "-"),
        'week_wind_51' : fargoWeeklyWind[5].replace(" ", "").replace("to", "-"),
        'week_wind_61' : fargoWeeklyWind[6].replace(" ", "").replace("to", "-"),
        'week_wind_71' : fargoWeeklyWind[7].replace(" ", "").replace("to", "-"),
        'week_forecast_11' : fargoWeeklyShortForecast[1],
        'week_forecast_21' : fargoWeeklyShortForecast[2],
        'week_forecast_31' : fargoWeeklyShortForecast[3],
        'week_forecast_41' : fargoWeeklyShortForecast[4],
        'week_forecast_51' : fargoWeeklyShortForecast[5],
        'week_forecast_61' : fargoWeeklyShortForecast[6],
        'week_forecast_71' : fargoWeeklyShortForecast[7],
        #2nd set
        'current_temp2' : round(((new_york_conditions.temperature)*9/5)+32),
        'week_date_12' : new_yorkWeeklyDate[1],
        'week_date_22' : new_yorkWeeklyDate[2],
        'week_date_32' : new_yorkWeeklyDate[3],
        'week_date_42' : new_yorkWeeklyDate[4],
        'week_date_52' : new_yorkWeeklyDate[5],
        'week_date_62' : new_yorkWeeklyDate[6],
        'week_date_72' : new_yorkWeeklyDate[7],
        'week_temp_12' : new_yorkWeeklyTemp[1],
        'week_temp_22' : new_yorkWeeklyTemp[2],
        'week_temp_32' : new_yorkWeeklyTemp[3],
        'week_temp_42' : new_yorkWeeklyTemp[4],
        'week_temp_52' : new_yorkWeeklyTemp[5],
        'week_temp_62' : new_yorkWeeklyTemp[6],
        'week_temp_72' : new_yorkWeeklyTemp[7],
        'week_wind_12' : new_yorkWeeklyWind[1].replace(" ", "").replace("to", "-"),
        'week_wind_22' : new_yorkWeeklyWind[2].replace(" ", "").replace("to", "-"),
        'week_wind_32' : new_yorkWeeklyWind[3].replace(" ", "").replace("to", "-"),
        'week_wind_42' : new_yorkWeeklyWind[4].replace(" ", "").replace("to", "-"),
        'week_wind_52' : new_yorkWeeklyWind[5].replace(" ", "").replace("to", "-"),
        'week_wind_62' : new_yorkWeeklyWind[6].replace(" ", "").replace("to", "-"),
        'week_wind_72' : new_yorkWeeklyWind[7].replace(" ", "").replace("to", "-"),
        'week_forecast_12' : new_yorkWeeklyShortForecast[1],
        'week_forecast_22' : new_yorkWeeklyShortForecast[2],
        'week_forecast_32' : new_yorkWeeklyShortForecast[3],
        'week_forecast_42' : new_yorkWeeklyShortForecast[4],
        'week_forecast_52' : new_yorkWeeklyShortForecast[5],
        'week_forecast_62' : new_yorkWeeklyShortForecast[6],
        'week_forecast_72' : new_yorkWeeklyShortForecast[7],
        #3rd set
        'current_temp3' : round(((florida_conditions.temperature)*9/5)+32),
        'week_date_13' : floridaWeeklyDate[1],
        'week_date_23' : floridaWeeklyDate[2],
        'week_date_33' : floridaWeeklyDate[3],
        'week_date_43' : floridaWeeklyDate[4],
        'week_date_53' : floridaWeeklyDate[5],
        'week_date_63' : floridaWeeklyDate[6],
        'week_date_73' : floridaWeeklyDate[7],
        'week_temp_13' : floridaWeeklyTemp[1],
        'week_temp_23' : floridaWeeklyTemp[2],
        'week_temp_33' : floridaWeeklyTemp[3],
        'week_temp_43' : floridaWeeklyTemp[4],
        'week_temp_53' : floridaWeeklyTemp[5],
        'week_temp_63' : floridaWeeklyTemp[6],
        'week_temp_73' : floridaWeeklyTemp[7],
        'week_wind_13' : floridaWeeklyWind[1].replace(" ", "").replace("to", "-"),
        'week_wind_23' : floridaWeeklyWind[2].replace(" ", "").replace("to", "-"),
        'week_wind_33' : floridaWeeklyWind[3].replace(" ", "").replace("to", "-"),
        'week_wind_43' : floridaWeeklyWind[4].replace(" ", "").replace("to", "-"),
        'week_wind_53' : floridaWeeklyWind[5].replace(" ", "").replace("to", "-"),
        'week_wind_63' : floridaWeeklyWind[6].replace(" ", "").replace("to", "-"),
        'week_wind_73' : floridaWeeklyWind[7].replace(" ", "").replace("to", "-"),
        'week_forecast_13' : floridaWeeklyShortForecast[1],
        'week_forecast_23' : floridaWeeklyShortForecast[2],
        'week_forecast_33' : floridaWeeklyShortForecast[3],
        'week_forecast_43' : floridaWeeklyShortForecast[4],
        'week_forecast_53' : floridaWeeklyShortForecast[5],
        'week_forecast_63' : floridaWeeklyShortForecast[6],
        'week_forecast_73' : floridaWeeklyShortForecast[7],
        #4th set
        'current_temp4' : round(((minnesota_conditions.temperature)*9/5)+32),
        'week_date_14' : minnesotaWeeklyDate[1],
        'week_date_24' : minnesotaWeeklyDate[2],
        'week_date_34' : minnesotaWeeklyDate[3],
        'week_date_44' : minnesotaWeeklyDate[4],
        'week_date_54' : minnesotaWeeklyDate[5],
        'week_date_64' : minnesotaWeeklyDate[6],
        'week_date_74' : minnesotaWeeklyDate[7],
        'week_temp_14' : minnesotaWeeklyTemp[1],
        'week_temp_24' : minnesotaWeeklyTemp[2],
        'week_temp_34' : minnesotaWeeklyTemp[3],
        'week_temp_44' : minnesotaWeeklyTemp[4],
        'week_temp_54' : minnesotaWeeklyTemp[5],
        'week_temp_64' : minnesotaWeeklyTemp[6],
        'week_temp_74' : minnesotaWeeklyTemp[7],
        'week_wind_14' : minnesotaWeeklyWind[1].replace(" ", "").replace("to", "-"),
        'week_wind_24' : minnesotaWeeklyWind[2].replace(" ", "").replace("to", "-"),
        'week_wind_34' : minnesotaWeeklyWind[3].replace(" ", "").replace("to", "-"),
        'week_wind_44' : minnesotaWeeklyWind[4].replace(" ", "").replace("to", "-"),
        'week_wind_54' : minnesotaWeeklyWind[5].replace(" ", "").replace("to", "-"),
        'week_wind_64' : minnesotaWeeklyWind[6].replace(" ", "").replace("to", "-"),
        'week_wind_74' : minnesotaWeeklyWind[7].replace(" ", "").replace("to", "-"),
        'week_forecast_14' : minnesotaWeeklyShortForecast[1],
        'week_forecast_24' : minnesotaWeeklyShortForecast[2],
        'week_forecast_34' : minnesotaWeeklyShortForecast[3],
        'week_forecast_44' : minnesotaWeeklyShortForecast[4],
        'week_forecast_54' : minnesotaWeeklyShortForecast[5],
        'week_forecast_64' : minnesotaWeeklyShortForecast[6],
        'week_forecast_74' : minnesotaWeeklyShortForecast[7],
        #5th set
        'current_temp5' : round(((wahpeton_conditions.temperature)*9/5)+32),
        'week_date_15' : wahpetonWeeklyDate[1],
        'week_date_25' : wahpetonWeeklyDate[2],
        'week_date_35' : wahpetonWeeklyDate[3],
        'week_date_45' : wahpetonWeeklyDate[4],
        'week_date_55' : wahpetonWeeklyDate[5],
        'week_date_65' : wahpetonWeeklyDate[6],
        'week_date_75' : wahpetonWeeklyDate[7],
        'week_temp_15' : wahpetonWeeklyTemp[1],
        'week_temp_25' : wahpetonWeeklyTemp[2],
        'week_temp_35' : wahpetonWeeklyTemp[3],
        'week_temp_45' : wahpetonWeeklyTemp[4],
        'week_temp_55' : wahpetonWeeklyTemp[5],
        'week_temp_65' : wahpetonWeeklyTemp[6],
        'week_temp_75' : wahpetonWeeklyTemp[7],
        'week_wind_15' : wahpetonWeeklyWind[1].replace(" ", "").replace("to", "-"),
        'week_wind_25' : wahpetonWeeklyWind[2].replace(" ", "").replace("to", "-"),
        'week_wind_35' : wahpetonWeeklyWind[3].replace(" ", "").replace("to", "-"),
        'week_wind_45' : wahpetonWeeklyWind[4].replace(" ", "").replace("to", "-"),
        'week_wind_55' : wahpetonWeeklyWind[5].replace(" ", "").replace("to", "-"),
        'week_wind_65' : wahpetonWeeklyWind[6].replace(" ", "").replace("to", "-"),
        'week_wind_75' : wahpetonWeeklyWind[7].replace(" ", "").replace("to", "-"),
        'week_forecast_15' : wahpetonWeeklyShortForecast[1],
        'week_forecast_25' : wahpetonWeeklyShortForecast[2],
        'week_forecast_35' : wahpetonWeeklyShortForecast[3],
        'week_forecast_45' : wahpetonWeeklyShortForecast[4],
        'week_forecast_55' : wahpetonWeeklyShortForecast[5],
        'week_forecast_65' : wahpetonWeeklyShortForecast[6],
        'week_forecast_75' : wahpetonWeeklyShortForecast[7],
        #6th set
        'current_temp6' : round(((south_dakota_conditions.temperature)*9/5)+32),
        'week_date_16' : south_dakotaWeeklyDate[1],
        'week_date_26' : south_dakotaWeeklyDate[2],
        'week_date_36' : south_dakotaWeeklyDate[3],
        'week_date_46' : south_dakotaWeeklyDate[4],
        'week_date_56' : south_dakotaWeeklyDate[5],
        'week_date_66' : south_dakotaWeeklyDate[6],
        'week_date_76' : south_dakotaWeeklyDate[7],
        'week_temp_16' : south_dakotaWeeklyTemp[1],
        'week_temp_26' : south_dakotaWeeklyTemp[2],
        'week_temp_36' : south_dakotaWeeklyTemp[3],
        'week_temp_46' : south_dakotaWeeklyTemp[4],
        'week_temp_56' : south_dakotaWeeklyTemp[5],
        'week_temp_66' : south_dakotaWeeklyTemp[6],
        'week_temp_76' : south_dakotaWeeklyTemp[7],
        'week_wind_16' : south_dakotaWeeklyWind[1].replace(" ", "").replace("to", "-"),
        'week_wind_26' : south_dakotaWeeklyWind[2].replace(" ", "").replace("to", "-"),
        'week_wind_36' : south_dakotaWeeklyWind[3].replace(" ", "").replace("to", "-"),
        'week_wind_46' : south_dakotaWeeklyWind[4].replace(" ", "").replace("to", "-"),
        'week_wind_56' : south_dakotaWeeklyWind[5].replace(" ", "").replace("to", "-"),
        'week_wind_66' : south_dakotaWeeklyWind[6].replace(" ", "").replace("to", "-"),
        'week_wind_76' : south_dakotaWeeklyWind[7].replace(" ", "").replace("to", "-"),
        'week_forecast_16' : south_dakotaWeeklyShortForecast[1],
        'week_forecast_26' : south_dakotaWeeklyShortForecast[2],
        'week_forecast_36' : south_dakotaWeeklyShortForecast[3],
        'week_forecast_46' : south_dakotaWeeklyShortForecast[4],
        'week_forecast_56' : south_dakotaWeeklyShortForecast[5],
        'week_forecast_66' : south_dakotaWeeklyShortForecast[6],
        'week_forecast_76' : south_dakotaWeeklyShortForecast[7],
    }
    return render(request, 'weekly_view.html', context)

def city_view_hourly(request):
    central_time = datetime.timezone(datetime.timedelta(hours=-6))
    fargo = NoaaData.at_location(46.8772, -96.7898)
    radar = fargo.radar_gif_url
    hourlyFargo = fargo.hourly_forecast()
    fargoHourlyTemp = {}
    fargoHourlyTime = {}
    fargoHourlyWindS = {}
    fargoHourlyShortForecast = {}
    fargoHourlyWindD = {}
    fargoHourlyDewPoint = {}
    fargoHourlyHumidity = {}
    fargoHourlyPrecip = {}
    fargoHourlyHazards = fargo.alerts()

    x=0
    for hour in hourlyFargo:    
        time = hour.startTime.astimezone(central_time).strftime('%I:00%p')
        fargoHourlyTime[x] = time
        fargoHourlyTemp[x] = hour.temperature
        fargoHourlyWindS[x] = hour.windSpeed
        fargoHourlyWindD[x] = hour.windDirection
        fargoHourlyShortForecast[x] = hour.shortForecast
        fargoHourlyDewPoint[x] = hour.dewpoint
        fargoHourlyHumidity[x] = hour.relativeHumidity
        fargoHourlyPrecip[x] = hour.probabilityOfPrecipitation
        
        x += 1

    fargo_conditions = fargo.current_conditions()
    
    context = {
        'radar' : radar,
        'current_temp1' : round(((fargo_conditions.temperature)*9/5)+32),
       #'hazards' : fargo.current_conditions().
        'hour_11' : fargoHourlyTime[1],
        'hour_21' : fargoHourlyTime[2],
        'hour_31' : fargoHourlyTime[3],
        'hour_41' : fargoHourlyTime[4],
        'hour_51' : fargoHourlyTime[5],
        'hour_61' : fargoHourlyTime[6],
        'hour_71' : fargoHourlyTime[7],
        'hourly_temp_11' : fargoHourlyTemp[1],
        'hourly_temp_21' : fargoHourlyTemp[2],
        'hourly_temp_31' : fargoHourlyTemp[3],
        'hourly_temp_41' : fargoHourlyTemp[4],
        'hourly_temp_51' : fargoHourlyTemp[5],
        'hourly_temp_61' : fargoHourlyTemp[6],
        'hourly_temp_71' : fargoHourlyTemp[7],
        'hourly_wind_11' : fargoHourlyWindS[1],
        'hourly_wind_21' : fargoHourlyWindS[2],
        'hourly_wind_31' : fargoHourlyWindS[3],
        'hourly_wind_41' : fargoHourlyWindS[4],
        'hourly_wind_51' : fargoHourlyWindS[5],
        'hourly_wind_61' : fargoHourlyWindS[6],
        'hourly_wind_71' : fargoHourlyWindS[7],
        'hourly_windD_11' : fargoHourlyWindD[1],
        'hourly_windD_21' : fargoHourlyWindD[2],
        'hourly_windD_31' : fargoHourlyWindD[3],
        'hourly_windD_41' : fargoHourlyWindD[4],
        'hourly_windD_51' : fargoHourlyWindD[5],
        'hourly_windD_61' : fargoHourlyWindD[6],
        'hourly_windD_71' : fargoHourlyWindD[7],
        'hourly_dp_11' : round(fargoHourlyDewPoint[1], 2),
        'hourly_dp_21' : round(fargoHourlyDewPoint[2], 2),
        'hourly_dp_31' : round(fargoHourlyDewPoint[3], 2),
        'hourly_dp_41' : round(fargoHourlyDewPoint[4], 2),
        'hourly_dp_51' : round(fargoHourlyDewPoint[5], 2),
        'hourly_dp_61' : round(fargoHourlyDewPoint[6], 2),
        'hourly_dp_71' : round(fargoHourlyDewPoint[7], 2),
        'hourly_rh_11' : round(fargoHourlyHumidity[1], 2),
        'hourly_rh_21' : round(fargoHourlyHumidity[2], 2),
        'hourly_rh_31' : round(fargoHourlyHumidity[3], 2),
        'hourly_rh_41' : round(fargoHourlyHumidity[4], 2),
        'hourly_rh_51' : round(fargoHourlyHumidity[5], 2),
        'hourly_rh_61' : round(fargoHourlyHumidity[6], 2),
        'hourly_rh_71' : round(fargoHourlyHumidity[7], 2),
        'hourly_p_11' : round(fargoHourlyPrecip[1], 2),
        'hourly_p_21' : round(fargoHourlyPrecip[2], 2),
        'hourly_p_31' : round(fargoHourlyPrecip[3], 2),
        'hourly_p_41' : round(fargoHourlyPrecip[4], 2),
        'hourly_p_51' : round(fargoHourlyPrecip[5], 2),
        'hourly_p_61' : round(fargoHourlyPrecip[6], 2),
        'hourly_p_71' : round(fargoHourlyPrecip[7], 2),
        'hourly_short_forecast_11' : fargoHourlyShortForecast[1],
        'hourly_short_forecast_21' : fargoHourlyShortForecast[2],
        'hourly_short_forecast_31' : fargoHourlyShortForecast[3],
        'hourly_short_forecast_41' : fargoHourlyShortForecast[4],
        'hourly_short_forecast_51' : fargoHourlyShortForecast[5],
        'hourly_short_forecast_61' : fargoHourlyShortForecast[6],
        'hourly_short_forecast_71' : fargoHourlyShortForecast[7],
        'hourly_hazards_11' : fargoHourlyHazards,

    }
    return render(request, 'expanded_city_view_hourly.html', context)

def city_view_weekly(request):
    central_time = datetime.timezone(datetime.timedelta(hours=-6))
    fargo = NoaaData.at_location(46.8772, -96.7898)
    radar = fargo.radar_gif_url
    weeklyFargo = fargo.week_forecast()
    fargoWeeklyTemp = {}
    fargoWeeklyTime = {}
    fargoWeeklyWindS = {}
    fargoWeeklyShortForecast = {}
    fargoWeeklyWindD = {}
    fargoWeeklyDewPoint = {}
    fargoWeeklyHumidity = {}
    fargoWeeklyDetailedForecast = {}
    fargoWeeklyHazards = fargo.alerts

    x=0
    for week in weeklyFargo:    
            time = week.startTime.astimezone(central_time).strftime('%m/%d')
            fargoWeeklyTime[x] = time
            fargoWeeklyTemp[x] = week.temperature
            fargoWeeklyWindS[x] = week.windSpeed
            fargoWeeklyWindD[x] = week.windDirection
            fargoWeeklyShortForecast[x] = week.shortForecast
            fargoWeeklyDewPoint[x] = week.dewpoint
            fargoWeeklyHumidity[x] = week.relativeHumidity
            fargoWeeklyDetailedForecast[x] = week.detailedForecast
        
            x += 1

    fargo_conditions = fargo.current_conditions()
    
    context = {
        'radar' : radar,
        'current_temp1' : round(((fargo_conditions.temperature)*9/5)+32),
       #'hazards' : fargo.current_conditions().
        'weekly_11' : fargoWeeklyTime[1],
        'weekly_21' : fargoWeeklyTime[2],
        'weekly_31' : fargoWeeklyTime[3],
        'weekly_41' : fargoWeeklyTime[4],
        'weekly_51' : fargoWeeklyTime[5],
        'weekly_61' : fargoWeeklyTime[6],
        'weekly_71' : fargoWeeklyTime[7],
        'weekly_temp_11' : fargoWeeklyTemp[1],
        'weekly_temp_21' : fargoWeeklyTemp[2],
        'weekly_temp_31' : fargoWeeklyTemp[3],
        'weekly_temp_41' : fargoWeeklyTemp[4],
        'weekly_temp_51' : fargoWeeklyTemp[5],
        'weekly_temp_61' : fargoWeeklyTemp[6],
        'weekly_temp_71' : fargoWeeklyTemp[7],
        'weekly_wind_11' : fargoWeeklyWindS[1],
        'weekly_wind_21' : fargoWeeklyWindS[2],
        'weekly_wind_31' : fargoWeeklyWindS[3],
        'weekly_wind_41' : fargoWeeklyWindS[4],
        'weekly_wind_51' : fargoWeeklyWindS[5],
        'weekly_wind_61' : fargoWeeklyWindS[6],
        'weekly_wind_71' : fargoWeeklyWindS[7],
        'weekly_windD_11' : fargoWeeklyWindD[1],
        'weekly_windD_21' : fargoWeeklyWindD[2],
        'weekly_windD_31' : fargoWeeklyWindD[3],
        'weekly_windD_41' : fargoWeeklyWindD[4],
        'weekly_windD_51' : fargoWeeklyWindD[5],
        'weekly_windD_61' : fargoWeeklyWindD[6],
        'weekly_windD_71' : fargoWeeklyWindD[7],
        'weekly_dp_11' : round(fargoWeeklyDewPoint[1], 2),
        'weekly_dp_21' : round(fargoWeeklyDewPoint[2], 2),
        'weekly_dp_31' : round(fargoWeeklyDewPoint[3], 2),
        'weekly_dp_41' : round(fargoWeeklyDewPoint[4], 2),
        'weekly_dp_51' : round(fargoWeeklyDewPoint[5], 2),
        'weekly_dp_61' : round(fargoWeeklyDewPoint[6], 2),
        'weekly_dp_71' : round(fargoWeeklyDewPoint[7], 2),
        'weekly_rh_11' : round(fargoWeeklyHumidity[1], 2),
        'weekly_rh_21' : round(fargoWeeklyHumidity[2], 2),
        'weekly_rh_31' : round(fargoWeeklyHumidity[3], 2),
        'weekly_rh_41' : round(fargoWeeklyHumidity[4], 2),
        'weekly_rh_51' : round(fargoWeeklyHumidity[5], 2),
        'weekly_rh_61' : round(fargoWeeklyHumidity[6], 2),
        'weekly_rh_71' : round(fargoWeeklyHumidity[7], 2),
        'weekly_short_forecast_11' : fargoWeeklyShortForecast[1],
        'weekly_short_forecast_21' : fargoWeeklyShortForecast[2],
        'weekly_short_forecast_31' : fargoWeeklyShortForecast[3],
        'weekly_short_forecast_41' : fargoWeeklyShortForecast[4],
        'weekly_short_forecast_51' : fargoWeeklyShortForecast[5],
        'weekly_short_forecast_61' : fargoWeeklyShortForecast[6],
        'weekly_short_forecast_71' : fargoWeeklyShortForecast[7],
        'weekly_detailed_forecast_11' : fargoWeeklyDetailedForecast[1],
        'weekly_hazards_11' : fargoWeeklyHazards,
    }
    return render(request, 'expanded_city_view_weekly.html', context)

def about_view(request):
    return render(request, 'about_view.html')

def careers_view(request):
    return render(request, 'careers_view.html')

def faq_view(request):
    return render(request, 'faq_view.html')
