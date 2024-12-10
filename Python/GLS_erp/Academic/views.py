from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def academic_index(request):
	return render(request,'Academic/index.html')