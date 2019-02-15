from django.contrib import admin
from .models import Time_Hum_Tem
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'body', 'date']
	list_filter = ['date']
	search_fields = ['title']
admin.site.register((Time_Hum_Tem), PostAdmin)