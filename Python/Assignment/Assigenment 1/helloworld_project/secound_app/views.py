from django.shortcuts import render

# Create your views here.

user_dict = {'Name':'Dhruvi','Age':'20','Stream':'IMSC(it)'}

def user_details(request):
	return render(request,"secound_app/user.html",context=user_dict)
