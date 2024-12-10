from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['Student_ID','First_Name','Last_Name','User_Name','Email_ID','Password','Course','Age','Date_of_Birth','Gender','Address']
	search_display = ['Student_ID','First_Name','Last_Name','User_Name','Email_ID','Password','Course','Age','Date_of_Birth','Gender','Address']
admin.site.register(Student,StudentAdmin)