#!/usr/bin/python
import paho.mqtt.client as mqtt
MQTT_SERVER = "192.168.1.197" #IP broker 
MQTT_PATH = "Temp-Hum-Time"
def on_connect1(client, userdata, flags, rc):
	print("connected with code "+str(rc))
	client.subscribe(MQTT_PATH)
	
def on_message1(client, userdata, msg):
	from .models import store_data
	msg_payload =str(msg.payload)
	#print(str(msg_payload))
	store_data(msg_payload)
client = mqtt.Client()
client.on_connect = on_connect1
client.on_message = on_message1
client.connect(MQTT_SERVER,1883,60)	
#client.loop_forever()
