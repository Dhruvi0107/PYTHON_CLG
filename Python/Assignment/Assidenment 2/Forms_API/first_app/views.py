from django.shortcuts import render
from first_app.forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
	form_data = None

	form = Registration()

	if request.method == "POST":
		form = Registration(request.POST)

		if form.is_valid():
			form_data = form.cleaned_data

			first_Name = form_data['First_Name']
			last_Name = form_data['Last_Name']
			user_Name = form_data['User_Name']
			email_ID = form_data['Email_ID']
			password = form_data['Password']
			course = form_data['Course']
			age = form_data['Age']
			dob = form_data['Date_of_Birth']
			gender = form_data['Gender']
			hobbies = form_data['Hobbies']
			address = form_data['Address']

			Students = Student(First_Name=first_Name,Last_Name=last_Name,User_Name=user_Name,Email_ID=email_ID,
								Password=password,Course=course,Age=age,Date_of_Birth=dob,Gender=gender,Hobbies=hobbies,Address=address)
			Students.save()

			return HttpResponse("Thank You For Registration "+first_Name+'...!')

			# return HttpResponse('app1/thanks/')

			# my_dict = {
			# 	'First_Name':first_Name,
			# 	'Last_Name':last_Name,
			# 	'User_Name':user_Name,
			# 	'Email_ID':email_ID,
			# 	'Password':password,
			# 	'Course':course,
			# 	'Age':age,
			# 	'Date_of_Birth':dob,
			# 	'Gender':gender,
			# 	'Address':address,
			# 	}
			# print(my_dict)

			# print(form_data)
	else:
		form = Registration()
	return render(request, "first_app/form.html", {'form': form, 'form_data': form_data})
