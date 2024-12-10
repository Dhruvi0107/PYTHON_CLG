from django.shortcuts import render

# Create your views here.

num_list = {'Number':[12,67,34,90,44,55,19,67,92,100]}

def number_iseven(request):
	return render(request,'four_app/num_iseven.html',context=num_list)