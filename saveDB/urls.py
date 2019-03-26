from django.urls import path, re_path
from . import views
from django.conf.urls import url
from saveDB.views import requestAjax
urlpatterns = [
	path('', views.list),
	path('<int:id>/', views.post),
	path('my_ajax_request', requestAjax, name='my_ajax_request'),
]