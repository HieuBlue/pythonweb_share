from django.db import models

# Create your models here.
class Humidity(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
class Temperature(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
class Time(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
def __str__(self):
	return self.title		