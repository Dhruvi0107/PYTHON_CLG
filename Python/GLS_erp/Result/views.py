from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def result_index(request):
	return render(request,'Result/index.html')