from django.db import models

# Create your models here.
class Time_Hum_Tem(models.Model):
	topic = models.CharField(max_length=100)
	message = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return self.topic		