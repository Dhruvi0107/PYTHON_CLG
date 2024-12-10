from django.contrib import admin
from Student.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['Student_ID','Student_Username','Student_Password','Student_Firstname','Student_Lastname','Student_Age','Student_Course']
	search_display = ['Student_ID','Student_Username','Student_Password','Student_Firstname','Student_Lastname','Student_Age','Student_Course']
admin.site.register(Student,StudentAdmin)

