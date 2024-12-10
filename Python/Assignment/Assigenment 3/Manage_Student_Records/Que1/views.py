from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,"Que1/Home.html")

def addStudent(request):
	if request.method == "POST":
		form = Add_Student(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data

			stu_Name = form_data['Student_Name']
			stu_Age = form_data['Student_Age']
			stu_Email = form_data['Student_Email']
			stu_City = form_data['Student_City']

			students = Student(Student_Name=stu_Name,Student_Age=stu_Age,Student_Email=stu_Email,Student_City=stu_City)
			students.save()

			return HttpResponse("Data Added Succsfully..!")
	else:
		form = Add_Student()

	return render(request,"Que1/add_student.html",{'form':form})

def listStudent(request):

	students = Student.objects.all()
	
	context = {
		'studentss':students
	}

	return render(request,"Que1/student_list.html",context)

def filterStudent(request):
	if request.method == "POST":
		city = request.POST.get('Student_City')
		students = Student.objects.filter(Student_City=city)
	else:
		students = Student.objects.all()

	return render(request,"Que1/Filter_Student.html",{'students': students})

def deleteStudent(request):
    message = ""
    
    if request.method == "POST":
        student_id = request.POST.get('Student_ID')
        
        try:
            student = Student.objects.get(Student_ID=student_id)
            student.delete()
            message = f"Student with ID {student_id} has been deleted successfully."
        except Student.DoesNotExist:
            message = f"No student found with ID {student_id}."

    return render(request, "Que1/delete_student.html", {'message': message})

def updateStudent(request, student_ID):
    if request.method == 'POST':
        student = Student.objects.get(Student_ID=student_ID)

        name = request.POST.get('Student_Name')
        email = request.POST.get('Student_Email')
        city = request.POST.get('Student_City')
        age = request.POST.get('Student_Age')

        try:
            student.Student_Name = name
            student.Student_Email = email
            student.Student_City = city
            student.Student_Age = age
            student.save()

            return redirect('List_Student')
        except Student.DoesNotExist:
            return HttpResponse("Student not found", status=404)

    student = Student.objects.get(Student_ID=student_ID)
    return render(request, "Que1/update_student.html", {'student': student})
