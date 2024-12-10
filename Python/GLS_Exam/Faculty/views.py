from django.shortcuts import render
from Faculty.models import *

# Create your views here.
def indexPage(request):
	return render(request,"Faculty/index.html")

def showFaculty(request):
	Facultys = Faculty.objects.all()

	context = {
		'Facultyss':Facultys
	}
	
	return render(request,"Faculty/show_faculty.html",context)
