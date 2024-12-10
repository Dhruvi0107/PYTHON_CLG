from django.contrib import admin
from Que1.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['Student_ID','Student_Name','Student_Age','Student_Email','Student_City']
	search_fields = ['Student_ID','Student_Name','Student_Age','Student_Email','Student_City']
	list_filter = ['Student_City']


admin.site.register(Student,StudentAdmin)
