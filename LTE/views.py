from django.shortcuts import render

# Create your views here.
def displaychart(request):
	return render(request,'AdminLTE/pages/charts/chart.html')