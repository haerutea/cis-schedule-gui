# https://stackoverflow.com/a/29664945
from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]