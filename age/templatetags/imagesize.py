from django import template


register = template.Library()

@register.filter(name="size")
def size(value, args):
    if args != 0:
        size = 100 * args
        return size
    else:
        return 50
@register.filter(name="listsum")
def size(value, args):
        return value + args