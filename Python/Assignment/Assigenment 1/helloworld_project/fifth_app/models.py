from django.db import models

# Create your models here.
class Student(models.Model):
	Student_ID = models.AutoField(primary_key=True)
	Student_Name = models.CharField(max_length=20)
	Student_Age = models.IntegerField()
	Student_Stream = models.CharField(max_length=20)

	def __init__(self):
		return self.Student_Name
