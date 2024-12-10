from django.contrib import admin
from Peon.models import *

# Register your models here.
class peonAdmin(admin.ModelAdmin):
	list_display = ["Peon_ID","Peon_Username","Peon_Password","Peon_Firstname","Peon_Lastname","Peon_Age","Peon_Salary","Peon_Contactno"]
	search_display = ["Peon_ID","Peon_Username","Peon_Password","Peon_Firstname","Peon_Lastname","Peon_Age","Peon_Salary","Peon_Contactno"]
admin.site.register(Peon,peonAdmin)