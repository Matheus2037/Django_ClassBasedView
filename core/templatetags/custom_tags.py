# templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    if number is None:
        return range(0)
    return range(number)

