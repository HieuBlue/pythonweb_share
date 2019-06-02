from django.shortcuts import render
from .models import Node2
#from .sub_temp_hum_node2 import *
#import paho.mqtt.client as mqtt

def list(request):
	Data  = {'TimeHumTem': Node2.objects.all().order_by("-date")[0:1]}
	return render(request, 'saveDBnode2.html', Data)
def post(request, id):
	post = Node2.objects.get(id=id)

#client.loop_start()#set at views only save() 1 time
