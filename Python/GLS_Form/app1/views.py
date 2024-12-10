from django.shortcuts import render
from . forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.

def thank(request):
	return render(request,"app1/thanks.html")

def index(request):
    form_data = None

    form = Registration()

    if request.method == "POST":
        form = Registration(request.POST)  # Handle POST data

        if form.is_valid():
            form_data = form.cleaned_data

            name = form_data['Name']
            age = form_data['Age']
            email_ID = form_data['Email_ID']
            password = form_data['Password']

            student = Student(Name=name, Age=age, Email_ID=email_ID, Password=password)
            student.save()

            return HttpResponse('app1/thanks/')

    return render(request, 'app1/index.html', {'form': form, 'form_data': form_data})