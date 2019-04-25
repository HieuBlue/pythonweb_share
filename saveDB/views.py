from django.shortcuts import render
from .models import Time_Hum_Tem# Create your views here.
from .models import store_data
import paho.mqtt.client as mqtt
def list(request):
	Data  = {'TimeHumTem': Time_Hum_Tem.objects.all().order_by("-date")}	#neu xep theo gia tri thi :.count()
	return render(request, 'saveDB/saveDB.html', Data)
def post(request, id):
	post = Time_Hum_Tem.objects.get(id=id)

MQTT_SERVER = "192.168.1.197" #IP broker 
MQTT_PATH = "Temp-Hum-Time"
def on_connect1(client, userdata, flags, rc):
	print("connected with code "+str(rc))
	client.subscribe(MQTT_PATH)
	
def on_message1(client, userdata, msg):
    print(MQTT_PATH+" "+str(msg.payload)) 
client = mqtt.Client() 
client.on_connect = on_connect1
client.on_message = on_message1
client.connect(MQTT_SERVER,1883,60)	
#client.loop_forever()		