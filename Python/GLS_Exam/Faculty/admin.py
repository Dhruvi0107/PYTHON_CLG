from django.contrib import admin
from Faculty.models import *

# Register your models here.
class facultyAdmin(admin.ModelAdmin):
	list_display = ["Faculty_ID","Faculty_Username","Faculty_Password","Faculty_Firstname","Faculty_Lastname","Faculty_Age","Faculty_Salary","Faculty_Contactno"]
	search_display = ["Faculty_ID","Faculty_Username","Faculty_Password","Faculty_Firstname","Faculty_Lastname","Faculty_Age","Faculty_Salary","Faculty_Contactno"]
admin.site.register(Faculty,facultyAdmin)
