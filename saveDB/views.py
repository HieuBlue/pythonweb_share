from django.shortcuts import render
from .models import Time_Hum_Tem
#from .sub_temp_hum import *
def list(request):
	Data  = {'TimeHumTem': Time_Hum_Tem.objects.all().order_by("-date")[0:12]}
	return render(request, 'saveDB/saveDB.html', Data)
def post(request, id):
	post = Time_Hum_Tem.objects.get(id=id)