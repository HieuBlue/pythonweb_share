from django.db import models
class Node1(models.Model):
	DATA_MQTT_Node1 = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.DATA_MQTT_Node1     
def store_data_node1(msg_payload):
	store_node1 = Node1()
	store_node1.DATA_MQTT_Node1 = msg_payload
	store_node1.save()
