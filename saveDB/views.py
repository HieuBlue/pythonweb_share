from django.shortcuts import render
from .models import Time_Hum_Tem# Create your views here.
from django.http import JsonResponse
def list(request):
	Data  = {'TimeHumTem': Time_Hum_Tem.objects.all().order_by("-date")}	#neu xep theo gia tri thi :.count()
	return render(request, 'saveDB/saveDB.html', Data)
def post(request, id):
	post = Time_Hum_Tem.objects.get(id=id)
	return render(request, 'saveDB/saveDB.html', {'post': post})
def requestAjax(request):
   data = {
        'is_valid': False,}
   if request.is_ajax():
      message = request.POST.get('message')
      if message == 'I want an AJAX response':
         data.update(is_valid=True)
         data.update(response='This is the response you wanted')

   return JsonResponse(data)	