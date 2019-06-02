from django.db import models
class Node2(models.Model):
	DATA_MQTT_Node2 = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.DATA_MQTT_Node2     
def store_data_node2(msg_payload):
	store_node2 = Node2()
	store_node2.DATA_MQTT_Node2 = msg_payload
	store_node2.save()
