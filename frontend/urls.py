from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('weekly_view', weekly_view, name='weekly_view'),
    path('city_view/<str:lat_long>', city_view, name='city_view'),
    path('about_view', about_view, name='about_view'),
    path('faq_view', faq_view, name='faq_view'),
    path('careers_view', careers_view, name='careers_view'),
]
