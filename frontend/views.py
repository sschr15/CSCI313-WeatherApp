from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def city_view(request):
    return render(request, 'expanded_city_view.html')

def lunar_view(request):
    return render(request, 'expanded_lunar_view.html')

def radar_view(request):
    return render(request, 'expanded_radar_view.html')