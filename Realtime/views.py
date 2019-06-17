from django.shortcuts import render
# Create your views here.
def displaydata(request):
	return render(request,'pages/base.html')
