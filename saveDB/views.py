from django.shortcuts import render
from .models import Time_Hum_Tem# Create your views here.
def list(request):
	Data  = {'TimeHumTem': Time_Hum_Tem.objects.all().order_by("-date")}	#neu xep theo gia tri thi :.count()
	return render(request, 'saveDB/saveDB.html', Data)
def post(request, id):
	post = Time_Hum_Tem.objects.get(id=id)
	return render(request, 'saveDB/saveDB.html', {'post': post})