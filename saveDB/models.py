from django.db import models
# Create your models here.
class Time_Hum_Tem(models.Model):
	topic = models.CharField(max_length=100)
	message = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
class store_data():
	store = Time_Hum_Tem()
	store.topic = 'Thời Gian-Độ Ẩm-Nhiệt Độ'
	store.message = '16:37/15/02/19-50-27'
	store.save()

def __str__(self):
	return self.topic		
	store_data()