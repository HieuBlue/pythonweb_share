from django.shortcuts import render
from .models import Post
# Create your views here.
def list(request):
	Data  = {'Posts': Post.objects.all().order_by("-date")}	#neu xep theo gia tri thi :.count()
	return render(request, 'saveDB/saveDB.html', Data)
	