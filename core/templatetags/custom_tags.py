from django import template
from datetime import datetime
from random import choice

register = template.Library()

@register.filter(name='dateFormat')
def dateFormat(value):
    d = datetime.strptime(value[:20], "%b %d %Y %H:%M:%S")
    return d.strftime("%Y.%m.%d")


@register.filter(name='multiply')
def multiply(value):
    return value * 20


@register.filter(name='gradient')
def gradient(value):
    return choice(["background: linear-gradient(250.9deg, #FFAE35 6.4%, #DA001A 99.41%);", "background: linear-gradient(250.5deg, #4D26BD 7%, #200767 99.4%);", "background: linear-gradient(251.99deg, #04B393 -16.32%, #009950 105.52%);"])

@register.filter(name='color')
def color(value):
    return choice(["#FF00C7", "#00C2FF", "#42FF00"])