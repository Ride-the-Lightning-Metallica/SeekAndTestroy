from django import template

register = template.Library()

def iterable(value:int) -> range:
    return range(value)

register.filter('iterable', iterable)