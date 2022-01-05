from django import template

from random import shuffle
from string import ascii_uppercase

register = template.Library()


def iterable(value: int) -> range:
    return range(value)


def add_true_answer(value: list, true_answer) -> list:
    value.append(true_answer)
    shuffle(value)

    return value


def add_ascii_uppercase(value: str) -> str:
    return ascii_uppercase


register.filter('iterable', iterable)
register.filter('answers', add_true_answer)
register.filter('ascii_uppercase', add_ascii_uppercase)
