from django import template

register = template.Library()


@register.filter(name='alert')
def severity_to_color(severity):
    match severity:
        case 'Extreme', 'Severe':
            return 'danger'
        case 'Moderate':
            return 'warning'
        case 'Minor':
            return 'info'
        case _:
            return 'secondary'
