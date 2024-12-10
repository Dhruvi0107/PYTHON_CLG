from django.db import models

# Create your models here.
class Student(models.Model):
	Student_ID = models.AutoField(primary_key=True)
	Student_Username = models.CharField(max_length=20 ,null=False)
	Student_Password = models.CharField(max_length=20 ,null=False)
	Student_Firstname = models.CharField(max_length=20 ,null=False)
	Student_Lastname = models.CharField(max_length=20 ,null=False)
	Student_Age = models.IntegerField(null=False)
	Student_Course = models.CharField(max_length=20 ,null=False)

	def __str__(self):
		return self.Student_Username

# Foreigi Key
# Stu_ID = models.ForeignKey(Student,on_delete=models.CASCADE)

# Auto Increment
# Stu_ID = AutoField(primary_key=True)