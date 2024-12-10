from django.contrib import admin
from Student.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','age']
	search_display = ('first_name','last_name','age')
admin.site.register(Student,StudentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['Emp_ID','First_Name','Last_Name']
	search_display = ('Emp_ID','First_Name','Last_Name')
admin.site.register(Employee,EmployeeAdmin)

class Employee_DetailsAdmin(admin.ModelAdmin):
	list_display = ['Employee_ID','Department','Salary','Date_Of_Join']
	search_display = ('Employee_ID','Department','Salary','Date_Of_Join')
admin.site.register(Employee_Details,Employee_DetailsAdmin)
