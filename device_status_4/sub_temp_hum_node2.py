#!/usr/bin/python
import paho.mqtt.client as mqtt
#MQTT_SERVER = "192.168.1.197" #IP broker 
MQTT_SERVER = "broker.hivemq.com"
MQTT_PATH = "Device_4_Status"
def on_connect1(client, userdata, flags, rc):
	print("connected with broker")
	print("connected with code "+str(rc))
	client.subscribe(MQTT_PATH)
	
def on_message1(client, userdata, msg):
	from .models import store_data_node2
	msg_payload =str(msg.payload.decode("utf-8"))
	store_data_node2(msg_payload)
client = mqtt.Client()
client.on_connect = on_connect1
client.on_message = on_message1
client.connect(MQTT_SERVER,1883,60)	
#client.loop_start()
