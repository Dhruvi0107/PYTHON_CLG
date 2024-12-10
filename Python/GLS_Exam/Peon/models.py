from django.db import models

# Create your models here.
class Peon(models.Model):
	Peon_ID = models.AutoField(primary_key=True)
	Peon_Username = models.CharField(max_length=20, null=False)
	Peon_Password = models.CharField(max_length=20, null=False)
	Peon_Firstname = models.CharField(max_length=20, null=False)
	Peon_Lastname = models.CharField(max_length=20, null=False)
	Peon_Age = models.IntegerField(null=False)
	Peon_Salary = models.IntegerField(null=False)
	Peon_Contactno = models.IntegerField(null=False)

	def __str__(self):
		return self.Peon_Username
