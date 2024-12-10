from django import forms
from .models import *

class Add_Student(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"