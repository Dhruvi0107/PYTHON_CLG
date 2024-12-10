from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.

def thannks(request):
	return render(request,'Forms/Thank_you.html')

def addMobile(request):
	form_data = None

	form = Mobile()

	if request.method ==  "POST":
		form = Mobile(request.POST)

		if form.is_valid():
			form_data = form.cleaned_data	

			mobile_Name = form_data['Mobile_Name']
			mobile_Ram = form_data['Mobile_Ram']
			mobile_Price = form_data['Mobile_Price']
			mobile_Battery = form_data['Mobile_Battery']
			mobile_Final_Price = form_data['Mobile_Final_Price']

			mobile = MobileRegister(Mobile_Name=mobile_Name,Mobile_Ram=mobile_Ram,Mobile_Price=mobile_Price,
									Mobile_Battery=mobile_Battery,Mobile_Final_Price=mobile_Final_Price)
			mobile.save()

			return HttpResponse('forms/thanks/')

	# else:
	# 	form = Mobile()
	return render(request,'Forms/form.html',{'form':form,'form_data':form_data})
