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

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

application = get_wsgi_application()

def awake():
    while True:
        schedule.run_pending()
        time.sleep(1)

t = threading.Thread(target=awake)
t.start()
