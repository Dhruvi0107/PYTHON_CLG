	from django.shortcuts import render
from Student.models import *

# Create your views here.
def indexPage(request):
	return render(request,"Student/index.html")

def showstudent(request):

	students = Student.objects.all()

	contaxt = {
		'studentss':students
	}

	return render(request,"Student/show_students.html",contaxt)

my_dict = {'data':[56,89,23,12,67,11,90,18],'name':'Dhruvi'}
def allnumbers(request):
	return render(request,"Student/All_number.html",context=my_dict)

def evennumbers(request):
	return render(request,"Student/custome_filter_even.html",context=my_dict)
