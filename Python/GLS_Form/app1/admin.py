from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = ['Name','Age','Email_ID','Password']
	search_display = ['Name','Age','Email_ID','Password']

admin.site.register(Student,StudentAdmin)
