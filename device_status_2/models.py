from django.db import models
class Device2Node1status(models.Model):
	Device_2_Node1_Status = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.Device_2_Node1_Status    
def store_data_node1(msg_payload):
	store_node1 = Device2Node1status()
	store_node1.Device_2_Node1_Status = msg_payload
	store_node1.save()
