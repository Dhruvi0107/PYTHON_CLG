from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['Stu_ID','Stu_Name','Stu_Email','Stu_Password','Stu_Age']
	search_display = ['Stu_ID','Stu_Name','Stu_Email','Stu_Password','Stu_Age']
admin.site.register(Student,StudentAdmin)