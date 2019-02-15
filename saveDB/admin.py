from django.contrib import admin
from .models import Time_Hum_Tem
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['topic', 'message', 'date']
	list_filter = ['date']
	search_fields = ['topic']
admin.site.register((Time_Hum_Tem), PostAdmin)