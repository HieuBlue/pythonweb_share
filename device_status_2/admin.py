from django.contrib import admin
from .models import Device2Node1status
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['Device_2_Node1_Status', 'date']
	list_filter = ['date']
	search_fields = ['date']
admin.site.register((Device2Node1status), PostAdmin)