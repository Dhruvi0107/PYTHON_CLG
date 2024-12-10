from django.db import models

# Create your models here.
class MobileRegister(models.Model):
	Mobile_ID = models.AutoField(primary_key=True)
	Mobile_Name = models.CharField(max_length=20)
	Mobile_Ram = models.CharField(max_length=20)
	Mobile_Price = models.CharField(max_length=20)
	Mobile_Battery = models.CharField(max_length=20)
	Mobile_Final_Price = models.IntegerField()
