from django.shortcuts import render
from .models import Device3Node2status
from .sub_temp_hum_node2 import *
import paho.mqtt.client as mqtt

def list(request):
	Data  = {'Status': Device3Node2status.objects.all().order_by("-date")[0:1]}
	return render(request, 'saveDBdevice3node2.html', Data)
def post(request, id):
	post = Device3Node2status.objects.get(id=id)

client.loop_start()#set at views only save() 1 time
