from django.db import models

# Create your models here.
class Student(models.Model):
	Student_ID = models.AutoField(primary_key = True)
	Student_Name = models.CharField(max_length=30)
	Student_Age = models.IntegerField()
	Student_Email = models.EmailField(max_length=50)
	Student_City = models.CharField(max_length=20)
