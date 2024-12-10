from django.db import models

# Create your models here.
class Faculty(models.Model):
	Faculty_ID = models.AutoField(primary_key=True)
	Faculty_Username = models.CharField(max_length=20 , null=False)
	Faculty_Password = models.CharField(max_length=20 , null=False)
	Faculty_Firstname = models.CharField(max_length=20 , null=False)
	Faculty_Lastname = models.CharField(max_length=20 , null=False)
	Faculty_Age = models.IntegerField(null=False)
	Faculty_Salary = models.IntegerField(null=False)
	Faculty_Contactno = models.IntegerField(null=False)

	def __str__(self):
		return self.Faculty_Username

