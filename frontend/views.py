from django.shortcuts import render
from api.noaa import NoaaData
from django.http import HttpResponse
from api.noaa import *
import datetime



def index(request):
    fargo = NoaaData.at_location(46.8772, -96.7898)
    new_york = NoaaData.at_location(40.7128, -74.0060)
    florida = NoaaData.at_location(27.6648, -81.5158)
    minnesota = NoaaData.at_location(46.7296, -94.6859)
    wahpeton = NoaaData.at_location(46.2652, -96.6059)
    south_dakota = NoaaData.at_location(43.9695, -99.9018)
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

    


    context = {
        'current_temp1' : round(((fargo.current_conditions().temperature)*9/5)+32),
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
        'hourly_wind_11' : fargoHourlyWind[1],
        'hourly_wind_21' : fargoHourlyWind[2],
        'hourly_wind_31' : fargoHourlyWind[3],
        'hourly_wind_41' : fargoHourlyWind[4],
        'hourly_wind_51' : fargoHourlyWind[5],
        'hourly_wind_61' : fargoHourlyWind[6],
        'hourly_wind_71' : fargoHourlyWind[7],
        'hourly_short_forecast_11' : fargoHourlyShortForecast[1],
        'hourly_short_forecast_21' : fargoHourlyShortForecast[2],
        'hourly_short_forecast_31' : fargoHourlyShortForecast[3],
        'hourly_short_forecast_41' : fargoHourlyShortForecast[4],
        'hourly_short_forecast_51' : fargoHourlyShortForecast[5],
        'hourly_short_forecast_61' : fargoHourlyShortForecast[6],
        'hourly_short_forecast_71' : fargoHourlyShortForecast[7],
        #2nd set
        'current_temp2' : round(((new_york.current_conditions().temperature)*9/5)+32),
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
        'hourly_wind_12' : new_yorkHourlyWind[1],
        'hourly_wind_22' : new_yorkHourlyWind[2],
        'hourly_wind_32' : new_yorkHourlyWind[3],
        'hourly_wind_42' : new_yorkHourlyWind[4],
        'hourly_wind_52' : new_yorkHourlyWind[5],
        'hourly_wind_62' : new_yorkHourlyWind[6],
        'hourly_wind_72' : new_yorkHourlyWind[7],
        'hourly_short_forecast_12' : new_yorkHourlyShortForecast[1],
        'hourly_short_forecast_22' : new_yorkHourlyShortForecast[2],
        'hourly_short_forecast_32' : new_yorkHourlyShortForecast[3],
        'hourly_short_forecast_42' : new_yorkHourlyShortForecast[4],
        'hourly_short_forecast_52' : new_yorkHourlyShortForecast[5],
        'hourly_short_forecast_62' : new_yorkHourlyShortForecast[6],
        'hourly_short_forecast_72' : new_yorkHourlyShortForecast[7],
        #3rd set
        'current_temp3' : round(((florida.current_conditions().temperature)*9/5)+32),
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
        'hourly_wind_13' : floridaHourlyWind[1],
        'hourly_wind_23' : floridaHourlyWind[2],
        'hourly_wind_33' : floridaHourlyWind[3],
        'hourly_wind_43' : floridaHourlyWind[4],
        'hourly_wind_53' : floridaHourlyWind[5],
        'hourly_wind_63' : floridaHourlyWind[6],
        'hourly_wind_73' : floridaHourlyWind[7],
        'hourly_short_forecast_13' : floridaHourlyShortForecast[1],
        'hourly_short_forecast_23' : floridaHourlyShortForecast[2],
        'hourly_short_forecast_33' : floridaHourlyShortForecast[3],
        'hourly_short_forecast_43' : floridaHourlyShortForecast[4],
        'hourly_short_forecast_53' : floridaHourlyShortForecast[5],
        'hourly_short_forecast_63' : floridaHourlyShortForecast[6],
        'hourly_short_forecast_73' : floridaHourlyShortForecast[7],
        #4th set
        'current_temp4' : round(((minnesota.current_conditions().temperature)*9/5)+32),
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
        'hourly_wind_14' : minnesotaHourlyWind[1],
        'hourly_wind_24' : minnesotaHourlyWind[2],
        'hourly_wind_34' : minnesotaHourlyWind[3],
        'hourly_wind_44' : minnesotaHourlyWind[4],
        'hourly_wind_54' : minnesotaHourlyWind[5],
        'hourly_wind_64' : minnesotaHourlyWind[6],
        'hourly_wind_74' : minnesotaHourlyWind[7],
        'hourly_short_forecast_14' : minnesotaHourlyShortForecast[1],
        'hourly_short_forecast_24' : minnesotaHourlyShortForecast[2],
        'hourly_short_forecast_34' : minnesotaHourlyShortForecast[3],
        'hourly_short_forecast_44' : minnesotaHourlyShortForecast[4],
        'hourly_short_forecast_54' : minnesotaHourlyShortForecast[5],
        'hourly_short_forecast_64' : minnesotaHourlyShortForecast[6],
        'hourly_short_forecast_74' : minnesotaHourlyShortForecast[7],
        #5th set
        'current_temp5' : round(((wahpeton.current_conditions().temperature)*9/5)+32),
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
        'hourly_wind_15' : wahpetonHourlyWind[1],
        'hourly_wind_25' : wahpetonHourlyWind[2],
        'hourly_wind_35' : wahpetonHourlyWind[3],
        'hourly_wind_45' : wahpetonHourlyWind[4],
        'hourly_wind_55' : wahpetonHourlyWind[5],
        'hourly_wind_65' : wahpetonHourlyWind[6],
        'hourly_wind_75' : wahpetonHourlyWind[7],
        'hourly_short_forecast_15' : wahpetonHourlyShortForecast[1],
        'hourly_short_forecast_25' : wahpetonHourlyShortForecast[2],
        'hourly_short_forecast_35' : wahpetonHourlyShortForecast[3],
        'hourly_short_forecast_45' : wahpetonHourlyShortForecast[4],
        'hourly_short_forecast_55' : wahpetonHourlyShortForecast[5],
        'hourly_short_forecast_65' : wahpetonHourlyShortForecast[6],
        'hourly_short_forecast_75' : wahpetonHourlyShortForecast[7],
        #6th set
        'current_temp6' : round(((south_dakota.current_conditions().temperature)*9/5)+32),
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
        'hourly_wind_16' : south_dakotaHourlyWind[1],
        'hourly_wind_26' : south_dakotaHourlyWind[2],
        'hourly_wind_36' : south_dakotaHourlyWind[3],
        'hourly_wind_46' : south_dakotaHourlyWind[4],
        'hourly_wind_56' : south_dakotaHourlyWind[5],
        'hourly_wind_66' : south_dakotaHourlyWind[6],
        'hourly_wind_76' : south_dakotaHourlyWind[7],
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
    minnesota = NoaaData.at_location(46.7296, -94.6859)
    wahpeton = NoaaData.at_location(46.2652, -96.6059)
    south_dakota = NoaaData.at_location(43.9695, -99.9018)
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
    weekMinnesota = minnesota.week_forecast()
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



    context = {
        'current_temp1' : round(((fargo.current_conditions().temperature)*9/5)+32),
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
        'week_wind_11' : fargoWeeklyWind[1],
        'week_wind_21' : fargoWeeklyWind[2],
        'week_wind_31' : fargoWeeklyWind[3],
        'week_wind_41' : fargoWeeklyWind[4],
        'week_wind_51' : fargoWeeklyWind[5],
        'week_wind_61' : fargoWeeklyWind[6],
        'week_wind_71' : fargoWeeklyWind[7],
        'week_forecast_11' : fargoWeeklyShortForecast[1],
        'week_forecast_21' : fargoWeeklyShortForecast[2],
        'week_forecast_31' : fargoWeeklyShortForecast[3],
        'week_forecast_41' : fargoWeeklyShortForecast[4],
        'week_forecast_51' : fargoWeeklyShortForecast[5],
        'week_forecast_61' : fargoWeeklyShortForecast[6],
        'week_forecast_71' : fargoWeeklyShortForecast[7],
        #2nd set
        'current_temp2' : round(((new_york.current_conditions().temperature)*9/5)+32),
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
        'week_wind_12' : new_yorkWeeklyWind[1],
        'week_wind_22' : new_yorkWeeklyWind[2],
        'week_wind_32' : new_yorkWeeklyWind[3],
        'week_wind_42' : new_yorkWeeklyWind[4],
        'week_wind_52' : new_yorkWeeklyWind[5],
        'week_wind_62' : new_yorkWeeklyWind[6],
        'week_wind_72' : new_yorkWeeklyWind[7],
        'week_forecast_12' : new_yorkWeeklyShortForecast[1],
        'week_forecast_22' : new_yorkWeeklyShortForecast[2],
        'week_forecast_32' : new_yorkWeeklyShortForecast[3],
        'week_forecast_42' : new_yorkWeeklyShortForecast[4],
        'week_forecast_52' : new_yorkWeeklyShortForecast[5],
        'week_forecast_62' : new_yorkWeeklyShortForecast[6],
        'week_forecast_72' : new_yorkWeeklyShortForecast[7],
        #3rd set
        #'current_temp3' : round(((current_data(19.8987, -155.6659).temperature)*9/5)+32),
        #'sunday_temp3' : round(weekly method).temperatureSunday, 2),
        #'monday_temp3' : round(weekly method).temperatureMonday, 2),
        #'tuesday_temp3' : round(weekly method).temperatureTuesday, 2),
        #'wednesday_temp3' : round(weekly method).temperatureWednesday, 2),
        #'thursday_temp3' : round(weekly method).temperatureThursday, 2),
        #'friday_temp3' : round(weekly method).temperatureFriday, 2),
        #'saturday_temp3' : round(weekly method).temperatureSaturday, 2),
        #'sunday_wind3' : round(hourly method will go here.wind, 2),
        #'monday_wind3' : round(hourly method will go here.wind, 2),
        #'tuesday_wind3' : round(hourly method will go here.wind, 2),
        #'wednesday_wind3' : round(hourly method will go here.wind, 2),
        #'thursday_wind3' : round(hourly method will go here.wind, 2),
        #'friday_wind3' : round(hourly method will go here.wind, 2),
        #'saturday_wind3' : round(hourly method will go here.wind, 2),
        #'sunday_short_forecast3' : not 100% sure how this will be formatted, i assume string,
        #'monday_short_forecast3' : not 100% sure how this will be formatted, i assume string,
        #'tuesday_short_forecast3' : not 100% sure how this will be formatted, i assume string,
        #'wednesday_short_forecast3' : not 100% sure how this will be formatted, i assume string,
        #'thursday_short_forecast3' : not 100% sure how this will be formatted, i assume string,
        #'friday_short_forecast3' : not 100% sure how this will be formatted, i assume string,
        #'saturday_short_forecast3' : not 100% sure how this will be formatted, i assume string,
        #4th set
        #'current_temp4' : round(((current_data(46.7296, -94.6859).temperature)*9/5)+32),
        #'sunday_temp4' : round(weekly method).temperatureSunday, 2),
        #'monday_temp4' : round(weekly method).temperatureMonday, 2),
        #'tuesday_temp4' : round(weekly method).temperatureTuesday, 2),
        #'wednesday_temp4' : round(weekly method).temperatureWednesday, 2),
        #'thursday_temp4' : round(weekly method).temperatureThursday, 2),
        #'friday_temp4' : round(weekly method).temperatureFriday, 2),
        #'saturday_temp4' : round(weekly method).temperatureSaturday, 2),
        #'sunday_wind4' : round(hourly method will go here.wind, 2),
        #'monday_wind4' : round(hourly method will go here.wind, 2),
        #'tuesday_wind4' : round(hourly method will go here.wind, 2),
        #'wednesday_wind4' : round(hourly method will go here.wind, 2),
        #'thursday_wind4' : round(hourly method will go here.wind, 2),
        #'friday_wind4' : round(hourly method will go here.wind, 2),
        #'saturday_wind4' : round(hourly method will go here.wind, 2),
        #'sunday_short_forecast4' : not 100% sure how this will be formatted, i assume string,
        #'monday_short_forecast4' : not 100% sure how this will be formatted, i assume string,
        #'tuesday_short_forecast4' : not 100% sure how this will be formatted, i assume string,
        #'wednesday_short_forecast4' : not 100% sure how this will be formatted, i assume string,
        #'thursday_short_forecast4' : not 100% sure how this will be formatted, i assume string,
        #'friday_short_forecast4' : not 100% sure how this will be formatted, i assume string,
        #'saturday_short_forecast4' : not 100% sure how this will be formatted, i assume string,
        #5th set
        #'current_temp5' : round(((current_data(46.2652, -96.6059).temperature)*9/5)+32),
        #'sunday_temp5' : round(weekly method).temperatureSunday, 2),
        #'monday_temp5' : round(weekly method).temperatureMonday, 2),
        #'tuesday_temp5' : round(weekly method).temperatureTuesday, 2),
        #'wednesday_temp5' : round(weekly method).temperatureWednesday, 2),
        #'thursday_temp5' : round(weekly method).temperatureThursday, 2),
        #'friday_temp5' : round(weekly method).temperatureFriday, 2),
        #'saturday_temp5' : round(weekly method).temperatureSaturday, 2),
        #'sunday_wind5' : round(hourly method will go here.wind, 2),
        #'monday_wind5' : round(hourly method will go here.wind, 2),
        #'tuesday_wind5' : round(hourly method will go here.wind, 2),
        #'wednesday_wind5' : round(hourly method will go here.wind, 2),
        #'thursday_wind5' : round(hourly method will go here.wind, 2),
        #'friday_wind5' : round(hourly method will go here.wind, 2),
        #'saturday_wind5' : round(hourly method will go here.wind, 2),
        #'sunday_short_forecast5' : not 100% sure how this will be formatted, i assume string,
        #'monday_short_forecast5' : not 100% sure how this will be formatted, i assume string,
        #'tuesday_short_forecast5' : not 100% sure how this will be formatted, i assume string,
        #'wednesday_short_forecast5' : not 100% sure how this will be formatted, i assume string,
        #'thursday_short_forecast5' : not 100% sure how this will be formatted, i assume string,
        #'friday_short_forecast5' : not 100% sure how this will be formatted, i assume string,
        #'saturday_short_forecast5' : not 100% sure how this will be formatted, i assume string,
        #6th set
        #'current_temp6' : round(((current_data(46.9105, -98.7084).temperature)*9/5)+32),
        #'sunday_temp6' : round(weekly method).temperatureSunday, 2),
        #'monday_temp6' : round(weekly method).temperatureMonday, 2),
        #'tuesday_temp6' : round(weekly method).temperatureTuesday, 2),
        #'wednesday_temp6' : round(weekly method).temperatureWednesday, 2),
        #'thursday_temp6' : round(weekly method).temperatureThursday, 2),
        #'friday_temp6' : round(weekly method).temperatureFriday, 2),
        #'saturday_temp6' : round(weekly method).temperatureSaturday, 2),
        #'sunday_wind6' : round(hourly method will go here.wind, 2),
        #'monday_wind6' : round(hourly method will go here.wind, 2),
        #'tuesday_wind6' : round(hourly method will go here.wind, 2),
        #'wednesday_wind6' : round(hourly method will go here.wind, 2),
        #'thursday_wind6' : round(hourly method will go here.wind, 2),
        #'friday_wind6' : round(hourly method will go here.wind, 2),
        #'saturday_wind6' : round(hourly method will go here.wind, 2),
        #'sunday_short_forecast6' : not 100% sure how this will be formatted, i assume string,
        #'monday_short_forecast6' : not 100% sure how this will be formatted, i assume string,
        #'tuesday_short_forecast6' : not 100% sure how this will be formatted, i assume string,
        #'wednesday_short_forecast6' : not 100% sure how this will be formatted, i assume string,
        #'thursday_short_forecast6' : not 100% sure how this will be formatted, i assume string,
        #'friday_short_forecast6' : not 100% sure how this will be formatted, i assume string,
        #'saturday_short_forecast6' : not 100% sure how this will be formatted, i assume string,
    }
    return render(request, 'weekly_view.html', context)

def city_view(request):
    return render(request, 'expanded_city_view.html')

def lunar_view(request):
    return render(request, 'expanded_lunar_view.html')

def radar_view(request):
    return render(request, 'expanded_radar_view.html')
