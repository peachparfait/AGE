"""
WSGI config for myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import threading
import requests
import time
from django.core.wsgi import get_wsgi_application
import schedule
from django.contrib.auth import get_user_model
from age import views

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

application = get_wsgi_application()
ntctime = ""
def awake():
    while True:
        global ntctime
        User=get_user_model()
        noticeuser = User.objects.get(pk=1)
        ntctime = str(noticeuser.noticetime)
        schedule.run_pending()
        time.sleep(1)

t = threading.Thread(target=awake)
t.start()
