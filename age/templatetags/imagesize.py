from django import template


register = template.Library()

@register.filter(name="size")
def size(value, args):
    size = 100 * args
    return size