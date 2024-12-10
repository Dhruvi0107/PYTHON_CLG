from django.contrib import admin
from .models import *

# Register your models here.
class MobileAdmin(admin.ModelAdmin):
	list_display = ['Mobile_ID','Mobile_Name','Mobile_Ram','Mobile_Price','Mobile_Battery','Mobile_Final_Price']
	search_display = ['Mobile_ID','Mobile_Name','Mobile_Ram','Mobile_Price','Mobile_Battery','Mobile_Final_Price']

admin.site.register(MobileRegister,MobileAdmin)