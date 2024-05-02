from django import template

register = template.Library()


@register.filter(name='c2f')
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 if celsius is not None else None


@register.filter(name='pa2inhg')
def pascals_to_inches_of_mercury(pascals):
    return pascals * 0.0002953


@register.filter(name='kmh2mph')
def kilometers_per_hour_to_miles_per_hour(kmh):
    return kmh * 0.621371


@register.filter(name='m2mi')
def meters_to_miles(meters):
    return meters * 0.000621371


@register.filter(name='deg2dir')
def degrees_to_direction(degrees):
    from api.noaa.utils import closest_direction
    return closest_direction(degrees)
