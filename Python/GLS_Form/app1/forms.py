from django import forms

class Registration(forms.Form):
	Name = forms.CharField(widget=forms.TextInput(attrs={'id':'Name_id','placeholder':'Enter Your Name..!'}))
	Age = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'Age_id','placeholder':'Enter Your Age..!'}))
	Email_ID = forms.EmailField(widget=forms.EmailInput(attrs={'id':'Email_id','placeholder':'Enter Your Email ID..!'}))
	Password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'Password_id','placeholder':'Enter Your Password..!'}))
	