"""pythonweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url ,include 
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('firstapps.urls')), # dau '' de trong thi se chay ham nay dau tien
    path('Realtime/', include('Realtime.urls')),
    path('datamqttnode1/', include('datamqttnode1.urls')),
    path('LTE/', include('LTE.urls')),
    path('datamqttnode2/', include('datamqttnode2.urls')),
    path('turnondevicenode1/', include('turnondevicenode1.urls')),
    path('turnoffdevicenode1/', include('turnoffdevicenode1.urls')),
    path('turnondevicenode2/', include('turnondevicenode2.urls')),
    path('turnoffdevicenode2/', include('turnoffdevicenode2.urls')),
]
