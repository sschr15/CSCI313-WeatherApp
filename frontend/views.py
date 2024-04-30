from django.shortcuts import render
from api.noaa.api_calls import *
from django.http import HttpResponse
from api.noaa import *


def index(request):
    context = {
        'current_temp' : round(current_data(46.8772, -96.7898).temperature, 2)
        #'hour_11' : (hourly method here.time)
        #'hour_21' : (hourly method here.time)
        #'hour_31' : (hourly method here.time)
        #'hour_41' : (hourly method here.time)
        #'hour_51' : (hourly method here.time)
        #'hour_61' : (hourly method here.time)
        #'hour_71' : (hourly method here.time)
        #'hourly_temp_11' : round(hourly method will go here.temp, 2)
        #'hourly_temp_21' : round(hourly method will go here.temp, 2)
        #'hourly_temp_31' : round(hourly method will go here.temp, 2)
        #'hourly_temp_41' : round(hourly method will go here.temp, 2)
        #'hourly_temp_51' : round(hourly method will go here.temp, 2)
        #'hourly_temp_61' : round(hourly method will go here.temp, 2)
        #'hourly_temp_71' : round(hourly method will go here.temp, 2)
        #'hourly_wind_11' : round(hourly method will go here.wind, 2)
        #'hourly_wind_21' : round(hourly method will go here.wind, 2)
        #'hourly_wind_31' : round(hourly method will go here.wind, 2)
        #'hourly_wind_41' : round(hourly method will go here.wind, 2)
        #'hourly_wind_51' : round(hourly method will go here.wind, 2)
        #'hourly_wind_61' : round(hourly method will go here.wind, 2)
        #'hourly_wind_71' : round(hourly method will go here.wind, 2)
        #'hourly_short_forecast_11' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_21' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_31' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_41' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_51 : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_61' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_71' : not 100% sure how this will be formatted, i assume string
        #2nd set
        #'hour_12' : (hourly method here.time)
        #'hour_22' : (hourly method here.time)
        #'hour_32' : (hourly method here.time)
        #'hour_42' : (hourly method here.time)
        #'hour_52' : (hourly method here.time)
        #'hour_62' : (hourly method here.time)
        #'hour_72' : (hourly method here.time)
        #'hourly_temp_12' : round(hourly method will go here.temp, 2)
        #'hourly_temp_22' : round(hourly method will go here.temp, 2)
        #'hourly_temp_32' : round(hourly method will go here.temp, 2)
        #'hourly_temp_42' : round(hourly method will go here.temp, 2)
        #'hourly_temp_52' : round(hourly method will go here.temp, 2)
        #'hourly_temp_62' : round(hourly method will go here.temp, 2)
        #'hourly_temp_72' : round(hourly method will go here.temp, 2)
        #'hourly_wind_12' : round(hourly method will go here.wind, 2)
        #'hourly_wind_22' : round(hourly method will go here.wind, 2)
        #'hourly_wind_32' : round(hourly method will go here.wind, 2)
        #'hourly_wind_42' : round(hourly method will go here.wind, 2)
        #'hourly_wind_52' : round(hourly method will go here.wind, 2)
        #'hourly_wind_62' : round(hourly method will go here.wind, 2)
        #'hourly_wind_72' : round(hourly method will go here.wind, 2)
        #'hourly_short_forecast_12' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_22' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_32' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_42' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_52' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_62' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_72' : not 100% sure how this will be formatted, i assume string
        #3rd set
        #'hour_13' : (hourly method here.time)
        #'hour_23' : (hourly method here.time)
        #'hour_33' : (hourly method here.time)
        #'hour_43' : (hourly method here.time)
        #'hour_53' : (hourly method here.time)
        #'hour_63' : (hourly method here.time)
        #'hour_73' : (hourly method here.time)
        #'hourly_temp_13' : round(hourly method will go here.temp, 2)
        #'hourly_temp_23' : round(hourly method will go here.temp, 2)
        #'hourly_temp_33' : round(hourly method will go here.temp, 2)
        #'hourly_temp_43' : round(hourly method will go here.temp, 2)
        #'hourly_temp_53' : round(hourly method will go here.temp, 2)
        #'hourly_temp_63' : round(hourly method will go here.temp, 2)
        #'hourly_temp_73' : round(hourly method will go here.temp, 2)
        #'hourly_wind_13' : round(hourly method will go here.wind, 2)
        #'hourly_wind_23' : round(hourly method will go here.wind, 2)
        #'hourly_wind_33' : round(hourly method will go here.wind, 2)
        #'hourly_wind_43' : round(hourly method will go here.wind, 2)
        #'hourly_wind_53' : round(hourly method will go here.wind, 2)
        #'hourly_wind_63' : round(hourly method will go here.wind, 2)
        #'hourly_wind_73' : round(hourly method will go here.wind, 2)
        #'hourly_short_forecast_13' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_23' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_33' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_43' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_53' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_63' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_73' : not 100% sure how this will be formatted, i assume string
        #4th set
        #'hour_14' : (hourly method here.time)
        #'hour_24' : (hourly method here.time)
        #'hour_34' : (hourly method here.time)
        #'hour_44' : (hourly method here.time)
        #'hour_54' : (hourly method here.time)
        #'hour_64' : (hourly method here.time)
        #'hour_74' : (hourly method here.time)
        #'hourly_temp_14' : round(hourly method will go here.temp, 2)
        #'hourly_temp_24' : round(hourly method will go here.temp, 2)
        #'hourly_temp_34' : round(hourly method will go here.temp, 2)
        #'hourly_temp_44' : round(hourly method will go here.temp, 2)
        #'hourly_temp_54' : round(hourly method will go here.temp, 2)
        #'hourly_temp_64' : round(hourly method will go here.temp, 2)
        #'hourly_temp_74' : round(hourly method will go here.temp, 2)
        #'hourly_wind_14' : round(hourly method will go here.wind, 2)
        #'hourly_wind_24' : round(hourly method will go here.wind, 2)
        #'hourly_wind_34' : round(hourly method will go here.wind, 2)
        #'hourly_wind_44' : round(hourly method will go here.wind, 2)
        #'hourly_wind_54' : round(hourly method will go here.wind, 2)
        #'hourly_wind_64' : round(hourly method will go here.wind, 2)
        #'hourly_wind_74' : round(hourly method will go here.wind, 2)
        #'hourly_short_forecast_14' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_24' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_34' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_44' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_54' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_64' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_74' : not 100% sure how this will be formatted, i assume string
        #5th set
        #'hour_15' : (hourly method here.time)
        #'hour_25' : (hourly method here.time)
        #'hour_35' : (hourly method here.time)
        #'hour_45' : (hourly method here.time)
        #'hour_55' : (hourly method here.time)
        #'hour_65' : (hourly method here.time)
        #'hour_75' : (hourly method here.time)
        #'hourly_temp_15' : round(hourly method will go here.temp, 2)
        #'hourly_temp_25' : round(hourly method will go here.temp, 2)
        #'hourly_temp_35' : round(hourly method will go here.temp, 2)
        #'hourly_temp_45' : round(hourly method will go here.temp, 2)
        #'hourly_temp_55' : round(hourly method will go here.temp, 2)
        #'hourly_temp_65' : round(hourly method will go here.temp, 2)
        #'hourly_temp_75' : round(hourly method will go here.temp, 2)
        #'hourly_wind_15' : round(hourly method will go here.wind, 2)
        #'hourly_wind_25' : round(hourly method will go here.wind, 2)
        #'hourly_wind_35' : round(hourly method will go here.wind, 2)
        #'hourly_wind_45' : round(hourly method will go here.wind, 2)
        #'hourly_wind_55' : round(hourly method will go here.wind, 2)
        #'hourly_wind_65' : round(hourly method will go here.wind, 2)
        #'hourly_wind_75' : round(hourly method will go here.wind, 2)
        #'hourly_short_forecast_15' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_25' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_35' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_45' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_55' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_65' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_75' : not 100% sure how this will be formatted, i assume string
        #6th set
        #'hour_16' : (hourly method here.time)
        #'hour_26' : (hourly method here.time)
        #'hour_36' : (hourly method here.time)
        #'hour_46' : (hourly method here.time)
        #'hour_56' : (hourly method here.time)
        #'hour_66' : (hourly method here.time)
        #'hour_76' : (hourly method here.time)
        #'hourly_temp_16' : round(hourly method will go here.temp, 2)
        #'hourly_temp_26' : round(hourly method will go here.temp, 2)
        #'hourly_temp_36' : round(hourly method will go here.temp, 2)
        #'hourly_temp_46' : round(hourly method will go here.temp, 2)
        #'hourly_temp_56' : round(hourly method will go here.temp, 2)
        #'hourly_temp_66' : round(hourly method will go here.temp, 2)
        #'hourly_temp_76' : round(hourly method will go here.temp, 2)
        #'hourly_wind_16' : round(hourly method will go here.wind, 2)
        #'hourly_wind_26' : round(hourly method will go here.wind, 2)
        #'hourly_wind_36' : round(hourly method will go here.wind, 2)
        #'hourly_wind_46' : round(hourly method will go here.wind, 2)
        #'hourly_wind_56' : round(hourly method will go here.wind, 2)
        #'hourly_wind_66' : round(hourly method will go here.wind, 2)
        #'hourly_wind_76' : round(hourly method will go here.wind, 2)
        #'hourly_short_forecast_16' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_26' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_36' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_46' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_56' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_66' : not 100% sure how this will be formatted, i assume string
        #'hourly_short_forecast_76' : not 100% sure how this will be formatted, i assume string
    }
    return render(request, 'index.html', context=context)

def weekly_view(request):
    context = {
        'current_temp' : round(current_data(46.8772, -96.7898).temperature, 2)
        #'sunday_temp1' : round(weekly method).temperatureSunday, 2)
        #'monday_temp1' : round(weekly method).temperatureMonday, 2)
        #'tuesday_temp1' : round(weekly method).temperatureTuesday, 2)
        #'wednesday_temp1' : round(weekly method).temperatureWednesday, 2)
        #'thursday_temp1' : round(weekly method).temperatureThursday, 2)
        #'friday_temp1' : round(weekly method).temperatureFriday, 2)
        #'saturday_temp1' : round(weekly method).temperatureSaturday, 2)
        #'sunday_wind1' : round(hourly method will go here.wind, 2)
        #'monday_wind1' : round(hourly method will go here.wind, 2)
        #'tuesday_wind1' : round(hourly method will go here.wind, 2)
        #'wednesday_wind1' : round(hourly method will go here.wind, 2)
        #'thursday_wind1' : round(hourly method will go here.wind, 2)
        #'friday_wind1' : round(hourly method will go here.wind, 2)
        #'saturday_wind1' : round(hourly method will go here.wind, 2)
        #'sunday_short_forecast1' : not 100% sure how this will be formatted, i assume string
        #'monday_short_forecast1' : not 100% sure how this will be formatted, i assume string
        #'tuesday_short_forecast1' : not 100% sure how this will be formatted, i assume string
        #'wednesday_short_forecast1' : not 100% sure how this will be formatted, i assume string
        #'thursday_short_forecast1' : not 100% sure how this will be formatted, i assume string
        #'friday_short_forecast1' : not 100% sure how this will be formatted, i assume string
        #'saturday_short_forecast1' : not 100% sure how this will be formatted, i assume string
        #2nd set
        #'sunday_temp2' : round(weekly method).temperatureSunday, 2)
        #'monday_temp2' : round(weekly method).temperatureMonday, 2)
        #'tuesday_temp2' : round(weekly method).temperatureTuesday, 2)
        #'wednesday_temp2' : round(weekly method).temperatureWednesday, 2)
        #'thursday_temp2' : round(weekly method).temperatureThursday, 2)
        #'friday_temp2' : round(weekly method).temperatureFriday, 2)
        #'saturday_temp2' : round(weekly method).temperatureSaturday, 2)
        #'sunday_wind2' : round(hourly method will go here.wind, 2)
        #'monday_wind2' : round(hourly method will go here.wind, 2)
        #'tuesday_wind2' : round(hourly method will go here.wind, 2)
        #'wednesday_wind2' : round(hourly method will go here.wind, 2)
        #'thursday_wind2' : round(hourly method will go here.wind, 2)
        #'friday_wind2' : round(hourly method will go here.wind, 2)
        #'saturday_wind2' : round(hourly method will go here.wind, 2)
        #'sunday_short_forecast2' : not 100% sure how this will be formatted, i assume string
        #'monday_short_forecast2' : not 100% sure how this will be formatted, i assume string
        #'tuesday_short_forecast2' : not 100% sure how this will be formatted, i assume string
        #'wednesday_short_forecast2' : not 100% sure how this will be formatted, i assume string
        #'thursday_short_forecast2' : not 100% sure how this will be formatted, i assume string
        #'friday_short_forecast2' : not 100% sure how this will be formatted, i assume string
        #'saturday_short_forecast2' : not 100% sure how this will be formatted, i assume string
        #3rd set
        #'sunday_temp3' : round(weekly method).temperatureSunday, 2)
        #'monday_temp3' : round(weekly method).temperatureMonday, 2)
        #'tuesday_temp3' : round(weekly method).temperatureTuesday, 2)
        #'wednesday_temp3' : round(weekly method).temperatureWednesday, 2)
        #'thursday_temp3' : round(weekly method).temperatureThursday, 2)
        #'friday_temp3' : round(weekly method).temperatureFriday, 2)
        #'saturday_temp3' : round(weekly method).temperatureSaturday, 2)
        #'sunday_wind3' : round(hourly method will go here.wind, 2)
        #'monday_wind3' : round(hourly method will go here.wind, 2)
        #'tuesday_wind3' : round(hourly method will go here.wind, 2)
        #'wednesday_wind3' : round(hourly method will go here.wind, 2)
        #'thursday_wind3' : round(hourly method will go here.wind, 2)
        #'friday_wind3' : round(hourly method will go here.wind, 2)
        #'saturday_wind3' : round(hourly method will go here.wind, 2)
        #'sunday_short_forecast3' : not 100% sure how this will be formatted, i assume string
        #'monday_short_forecast3' : not 100% sure how this will be formatted, i assume string
        #'tuesday_short_forecast3' : not 100% sure how this will be formatted, i assume string
        #'wednesday_short_forecast3' : not 100% sure how this will be formatted, i assume string
        #'thursday_short_forecast3' : not 100% sure how this will be formatted, i assume string
        #'friday_short_forecast3' : not 100% sure how this will be formatted, i assume string
        #'saturday_short_forecast3' : not 100% sure how this will be formatted, i assume string
        #4th set
        #'sunday_temp4' : round(weekly method).temperatureSunday, 2)
        #'monday_temp4' : round(weekly method).temperatureMonday, 2)
        #'tuesday_temp4' : round(weekly method).temperatureTuesday, 2)
        #'wednesday_temp4' : round(weekly method).temperatureWednesday, 2)
        #'thursday_temp4' : round(weekly method).temperatureThursday, 2)
        #'friday_temp4' : round(weekly method).temperatureFriday, 2)
        #'saturday_temp4' : round(weekly method).temperatureSaturday, 2)
        #'sunday_wind4' : round(hourly method will go here.wind, 2)
        #'monday_wind4' : round(hourly method will go here.wind, 2)
        #'tuesday_wind4' : round(hourly method will go here.wind, 2)
        #'wednesday_wind4' : round(hourly method will go here.wind, 2)
        #'thursday_wind4' : round(hourly method will go here.wind, 2)
        #'friday_wind4' : round(hourly method will go here.wind, 2)
        #'saturday_wind4' : round(hourly method will go here.wind, 2)
        #'sunday_short_forecast4' : not 100% sure how this will be formatted, i assume string
        #'monday_short_forecast4' : not 100% sure how this will be formatted, i assume string
        #'tuesday_short_forecast4' : not 100% sure how this will be formatted, i assume string
        #'wednesday_short_forecast4' : not 100% sure how this will be formatted, i assume string
        #'thursday_short_forecast4' : not 100% sure how this will be formatted, i assume string
        #'friday_short_forecast4' : not 100% sure how this will be formatted, i assume string
        #'saturday_short_forecast4' : not 100% sure how this will be formatted, i assume string
        #5th set
        #'sunday_temp5' : round(weekly method).temperatureSunday, 2)
        #'monday_temp5' : round(weekly method).temperatureMonday, 2)
        #'tuesday_temp5' : round(weekly method).temperatureTuesday, 2)
        #'wednesday_temp5' : round(weekly method).temperatureWednesday, 2)
        #'thursday_temp5' : round(weekly method).temperatureThursday, 2)
        #'friday_temp5' : round(weekly method).temperatureFriday, 2)
        #'saturday_temp5' : round(weekly method).temperatureSaturday, 2)
        #'sunday_wind5' : round(hourly method will go here.wind, 2)
        #'monday_wind5' : round(hourly method will go here.wind, 2)
        #'tuesday_wind5' : round(hourly method will go here.wind, 2)
        #'wednesday_wind5' : round(hourly method will go here.wind, 2)
        #'thursday_wind5' : round(hourly method will go here.wind, 2)
        #'friday_wind5' : round(hourly method will go here.wind, 2)
        #'saturday_wind5' : round(hourly method will go here.wind, 2)
        #'sunday_short_forecast5' : not 100% sure how this will be formatted, i assume string
        #'monday_short_forecast5' : not 100% sure how this will be formatted, i assume string
        #'tuesday_short_forecast5' : not 100% sure how this will be formatted, i assume string
        #'wednesday_short_forecast5' : not 100% sure how this will be formatted, i assume string
        #'thursday_short_forecast5' : not 100% sure how this will be formatted, i assume string
        #'friday_short_forecast5' : not 100% sure how this will be formatted, i assume string
        #'saturday_short_forecast5' : not 100% sure how this will be formatted, i assume string
        #6th set
        #'sunday_temp6' : round(weekly method).temperatureSunday, 2)
        #'monday_temp6' : round(weekly method).temperatureMonday, 2)
        #'tuesday_temp6' : round(weekly method).temperatureTuesday, 2)
        #'wednesday_temp6' : round(weekly method).temperatureWednesday, 2)
        #'thursday_temp6' : round(weekly method).temperatureThursday, 2)
        #'friday_temp6' : round(weekly method).temperatureFriday, 2)
        #'saturday_temp6' : round(weekly method).temperatureSaturday, 2)
        #'sunday_wind6' : round(hourly method will go here.wind, 2)
        #'monday_wind6' : round(hourly method will go here.wind, 2)
        #'tuesday_wind6' : round(hourly method will go here.wind, 2)
        #'wednesday_wind6' : round(hourly method will go here.wind, 2)
        #'thursday_wind6' : round(hourly method will go here.wind, 2)
        #'friday_wind6' : round(hourly method will go here.wind, 2)
        #'saturday_wind6' : round(hourly method will go here.wind, 2)
        #'sunday_short_forecast6' : not 100% sure how this will be formatted, i assume string
        #'monday_short_forecast6' : not 100% sure how this will be formatted, i assume string
        #'tuesday_short_forecast6' : not 100% sure how this will be formatted, i assume string
        #'wednesday_short_forecast6' : not 100% sure how this will be formatted, i assume string
        #'thursday_short_forecast6' : not 100% sure how this will be formatted, i assume string
        #'friday_short_forecast6' : not 100% sure how this will be formatted, i assume string
        #'saturday_short_forecast6' : not 100% sure how this will be formatted, i assume string
    }
    return render(request, 'weekly_view.html', context)

def city_view(request):
    return render(request, 'expanded_city_view.html')

def lunar_view(request):
    return render(request, 'expanded_lunar_view.html')

def radar_view(request):
    return render(request, 'expanded_radar_view.html')
