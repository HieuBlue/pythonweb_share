from django.urls import path, re_path
from . import views
from django.conf.urls import url
urlpatterns = [
	path('', views.list),
	path('<int:id>/', views.post),
]