from django.shortcuts import render
from .MQTT_control import *
# Create your views here.
def controldevice(request):
	publish.single(MQTT_TOPIC,"Node1-ON",hostname=MQTT_SERVER)
	return render(request,'Turned_on.html')