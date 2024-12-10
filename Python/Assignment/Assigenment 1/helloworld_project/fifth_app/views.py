from django.shortcuts import render
from .models import *

# Create your views here.
def student_details(request):

	student = Student.objects.all()

	context = {
		'studentss':student
	}

	return render(request,"fifth_app/show_details.html",context)
