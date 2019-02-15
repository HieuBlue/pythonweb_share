from django.db import models

# Create your models here.
class Time_Hum_Tem(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return self.title		