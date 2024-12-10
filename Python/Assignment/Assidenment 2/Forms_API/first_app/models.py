from django.db import models

# Create your models here.
class Student(models.Model):
	Student_ID = models.AutoField(primary_key=True)
	First_Name = models.CharField(max_length=20)
	Last_Name = models.CharField(max_length=20)
	User_Name = models.CharField(max_length=20)
	Email_ID = models.CharField(max_length=20)
	Password = models.CharField(max_length=20)
	Course = models.CharField(max_length=20)
	Age = models.IntegerField(max_length=20)
	Date_of_Birth = models.DateField()
	Gender = models.CharField(max_length=20)
	Hobbies = models.CharField(max_length=20)
	Address = models.CharField(max_length=100)
