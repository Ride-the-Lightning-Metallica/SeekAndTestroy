from django import template
from random import shuffle

register = template.Library()

def iterable(value:int) -> range:
    return range(value)

def add_true_answer(value:list, true_answer) -> None:
    value.append(true_answer)
    shuffle(value)
    
    return value

register.filter('iterable', iterable)
register.filter('answers', add_true_answer)