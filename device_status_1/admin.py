from django.contrib import admin
from .models import DeviceNode1status
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['Device_Node1_Status', 'date']
	list_filter = ['date']
	search_fields = ['date']
admin.site.register((DeviceNode1status), PostAdmin)