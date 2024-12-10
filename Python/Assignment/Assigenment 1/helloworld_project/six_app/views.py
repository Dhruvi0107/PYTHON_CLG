from django.shortcuts import render

# Create your views here.
def base_template(request):
	return render(request,"six_app/index.html")

def base_template1(request):
	return render(request,"six_app/index1.html")
