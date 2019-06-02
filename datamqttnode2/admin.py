from django.contrib import admin
from .models import Node2
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['DATA_MQTT_Node2', 'date']
	list_filter = ['date']
	search_fields = ['date']
admin.site.register((Node2), PostAdmin)