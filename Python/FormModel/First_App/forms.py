from django import forms
from .models import *

class Register(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"