from django.db import models
import paho.mqtt.client as mqtt
class Time_Hum_Tem(models.Model):
	DATA_MQTT = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.DATA_MQTT     
def store_data():
	store = Time_Hum_Tem()
	store.DATA_MQTT = 'ksdjhfkj'
	store.save()
#store_data()

