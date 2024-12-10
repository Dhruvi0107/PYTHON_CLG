from django.shortcuts import render

# Create your views here.

user_dict = {"Name":"Dhruvi"}

def user_uppercase(request):
	return render(request,"third_app/upper_case.html",context=user_dict)
