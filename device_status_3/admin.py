from django.contrib import admin
from .models import Device3Node2status
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['Device_3_Node2_Status', 'date']
	list_filter = ['date']
	search_fields = ['date']
admin.site.register((Device3Node2status), PostAdmin)