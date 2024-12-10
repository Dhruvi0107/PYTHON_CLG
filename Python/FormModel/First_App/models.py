from django.db import models

# Create your models here.
class Student(models.Model):
	Stu_ID = models.AutoField(primary_key=True)
	Stu_Name = models.CharField(max_length=20)
	Stu_Email = models.CharField(max_length=20)
	Stu_Password = models.CharField(max_length=10)
	Stu_Age = models.IntegerField()
