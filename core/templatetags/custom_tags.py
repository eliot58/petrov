from django import template

register = template.Library()

def intt(value):
    return value.split(".")[0]

def roundd(value):
    return value.split(".")[0]+ '.' + value.split(".")[1][:2]
    
register.filter('intt', intt)
register.filter('roundd', roundd)