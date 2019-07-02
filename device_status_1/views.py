from django.shortcuts import render
from .models import DeviceNode1status
from .sub_temp_hum_node1 import *
import paho.mqtt.client as mqtt

def list(request):
	Data  = {'Status': DeviceNode1status.objects.all().order_by("-date")[0:1]}
	return render(request, 'saveDBdevicenode1.html', Data)
def post(request, id):
	post = DeviceNode1status.objects.get(id=id)

client.loop_start()#set at views only save() 1 time
