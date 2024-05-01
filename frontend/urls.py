from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('weekly_view', weekly_view, name='weekly_view'),
    path('city_view_hourly', city_view_hourly, name='city_view_hourly'),
    path('city_view_weekly', city_view_weekly, name='city_view_weekly'),
    path('lunar_view', lunar_view, name='lunar_view' ),
    path('radar_view', radar_view, name='radar_view' ),
]
