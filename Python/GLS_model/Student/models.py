from django.db import models

# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.IntegerField()

	# def __str__(self):
	# 	return self.first_name

class Employee(models.Model):
	Emp_ID = models.AutoField(primary_key=True)
	First_Name = models.CharField(max_length=20,null=False)
	Last_Name = models.CharField(max_length=20,null=False)

	def __str__(self):
		return f"{self.Emp_ID}"

class Employee_Details(models.Model):
	Employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
	Department = models.CharField(max_length=20,null=False)
	Salary = models.IntegerField(null=False)
	Date_Of_Join = models.DateField(null=False)
