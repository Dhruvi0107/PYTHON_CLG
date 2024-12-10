from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['Student_ID','Student_Name','Student_Age','Student_Stream']
	search_display = ['Student_ID','Student_Name','Student_Age','Student_Stream']
admin.site.register(Student,StudentAdmin)
