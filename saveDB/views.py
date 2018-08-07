from django.shortcuts import render
from .models import Humidity
from .models import Temperature
# Create your views here.
def list(request):
	Data  = {'Humidity': Humidity.objects.all().order_by("-date")}	#neu xep theo gia tri thi :.count()
	return render(request, 'saveDB/saveDB.html', Data)
	