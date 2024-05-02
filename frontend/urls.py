from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('weekly_view', weekly_view, name='weekly_view'),
    path('city_view_hourly', city_view_hourly, name='city_view_hourly'),
    path('city_view_weekly', city_view_weekly, name='city_view_weekly'),
    path('about_view', about_view, name='about_view' ),
    path('faq_view', faq_view, name='faq_view' ),
    path('careers_view', careers_view, name='careers_view'),
]
