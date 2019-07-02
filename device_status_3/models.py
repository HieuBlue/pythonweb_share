from django.db import models
class Device3Node2status(models.Model):
	Device_3_Node2_Status = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.Device_3_Node2_Status    
def store_data_node2(msg_payload):
	store_node2 = Device3Node2status()
	store_node2.Device_3_Node2_Status = msg_payload
	store_node2.save()
