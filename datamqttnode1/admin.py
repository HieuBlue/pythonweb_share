from django.contrib import admin
from .models import Node1
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['DATA_MQTT_Node1', 'date']
	list_filter = ['date']
	search_fields = ['date']
admin.site.register((Node1), PostAdmin)