from django.shortcuts import render
from .models import *
from .forms import * 
from django.http import HttpResponse

# Create your views here.
def registration(request):
	if request.method == "POST":
		form = Register(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data

			stu_Name = form_data['Stu_Name']
			stu_Email = form_data['Stu_Email']
			stu_Password = form_data['Stu_Password']
			stu_Age = form_data['Stu_Age']

			students = Student(Stu_Name=stu_Name,Stu_Email=stu_Email,Stu_Password=stu_Password,Stu_Age=stu_Age)
			students.save()

			return HttpResponse("Data Added Succsfully..!")
	else:
		form = Register()

	return render(request,"First_App/Forms_Model.html",{'form':form})
