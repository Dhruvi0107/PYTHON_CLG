from django.shortcuts import render
from .models import *

# Create your views here.
def studentindex(request):
    students = Student.objects.all()  # Correct the query
    employee = Employee.objects.all()
    employeedetails = Employee_Details.objects.all()

    context = {
        'students': students,  # Correct the context dictionary
        'employees' : employee,
        'employee_detailss' : employeedetails
    }

    return render(request, "Student/index.html", context)
