from django.shortcuts import render
from .models import Node1
#from .sub_temp_hum_node1 import *
#import paho.mqtt.client as mqtt

def list(request):
	Data  = {'TimeHumTem': Node1.objects.all().order_by("-date")[0:1]}
	return render(request, 'saveDBnode1.html', Data)
def post(request, id):
	post = Node1.objects.get(id=id)

#client.loop_start()#set at views only save() 1 time
