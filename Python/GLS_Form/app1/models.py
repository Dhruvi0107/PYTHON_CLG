from django.db import models

# Create your models here.
class Student(models.Model):
	Name = models.CharField(max_length=20)
	Age = models.IntegerField()
	Email_ID = models.CharField(max_length=20)
	Password = models.CharField(max_length=20)
