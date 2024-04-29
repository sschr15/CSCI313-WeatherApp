from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('city_view', city_view, name='city_view' ),
    path('lunar_view', lunar_view, name='lunar_view' ),
    path('radar_view', radar_view, name='radar_view' ),
]
