from saveDB.sub_temp_hum import *
import paho.mqtt.client as mqtt
import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythonweb.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
client.loop_forever()