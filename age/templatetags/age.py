
from django import template
import datetime
import pytz


register = template.Library()

@register.filter(name="showage")
def showage(value, args):
    now = datetime.date.today()
    if now.month > args.month: #その一年で誕生日の月が過ぎている
        return now.year - args.year
    elif now.month == args.month: #誕生月
        if now.day == args.day: #今日が誕生日！！！！！！
            return now.year - args.year
        elif now.day > args.day: #誕生日は過ぎている
            return now.year - args.year
        else: #まだ誕生日を迎えていない
            return now.year - args.year - 1
    elif now.year - args.year <= 0: #マイナス防止
        return 0
    else:
        return now.year - args.year - 1 #まだ誕生日を迎えていない