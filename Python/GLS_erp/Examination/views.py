from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def examination_index(request):
	return render(request,'Examination/index.html')