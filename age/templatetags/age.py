
from django import template
import datetime
import pytz


register = template.Library()

@register.filter(name="showage")
def showage(value, args):
    now = datetime.datetime.now()
    timezone = pytz.timezone('Asia/Tokyo')
    now = timezone.localize(now)
    return now.year - args.year