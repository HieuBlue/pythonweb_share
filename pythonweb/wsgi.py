import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import paho.mqtt.client as mqtt
from saveDB.sub_temp_hum import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythonweb.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
client.loop_start()