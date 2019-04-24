from django.db import models
import paho.mqtt.client as mqtt
# Create your models here.
class Time_Hum_Tem(models.Model):
	DATA_MQTT = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.DATA_MQTT

MQTT_SERVER = "192.168.1.197" #IP broker 
MQTT_PATH = "Temp-Hum-Time"
def on_connect1(client, userdata, flags, rc):
	print("connected with code "+str(rc))
	client.subscribe(MQTT_PATH)
	
def on_message1(client, userdata, msg):
    print(MQTT_PATH+" "+str(msg.payload))       
def store_data():
	store = Time_Hum_Tem()
	store.DATA_MQTT = "ksdjhfkj"
	store.save()
store_data()
client = mqtt.Client() 
client.on_connect = on_connect1
client.on_message = on_message1
client.connect(MQTT_SERVER,1883,60)	
#client.loop_forever()	
