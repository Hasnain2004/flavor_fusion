from django import template

register = template.Library()

@register.filter
def split_lines(value):
    """
    Returns a list of lines from a text value
    """
    if value:
        return value.split('\n')
    return []

@register.filter
def strip(value):
    """
    Strips whitespace from a string
    """
    if value:
        return value.strip()
    return '' 