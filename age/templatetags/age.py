
from django import template
import datetime
import pytz
import requests

webhook_url = 'https://discordapp.com/api/webhooks/693136691346669640/g7AluYkGKBzc1p_ri9GPEKtuesSVl7rE_edxKEiKnbFLxfG5oXu0AGg5i4JV0KtGcymi'
 
register = template.Library()

@register.filter(name="showage")
def showage(value, args):
    now = datetime.date.today()
    if now.month > args.month: #その一年で誕生日の月が過ぎている
        return now.year - args.year
    elif now.month == args.month: #誕生月
        if now.day == args.day: #今日が誕生日！！！！！！
            main_content = {
                "content": "今日は" + str(value) + "の誕生日です！"
            }
            requests.post(webhook_url,main_content)
            return now.year - args.year
        elif now.day > args.day: #誕生日は過ぎている
            return now.year - args.year
        else: #まだ誕生日を迎えていない
            return now.year - args.year - 1
    elif now.year - args.year <= 0: #マイナス防止
        return 0
    else:
        return now.year - args.year - 1 #まだ誕生日を迎えていない