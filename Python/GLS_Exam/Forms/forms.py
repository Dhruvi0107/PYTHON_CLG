from django import forms

class Mobile(forms.Form):
	Mobile_Name = forms.CharField(widget=forms.TextInput(attrs={'id':'mnam','placeholder':'Enter Mobile Name For You Added.!'}))
	Mobile_Ram = forms.CharField(widget=forms.TextInput(attrs={'id':'mram','placeholder':'Entre Your Mobile Ram..!'}))
	Mobile_Price = forms.ChoiceField(choices=[('10000-20000','20000-30000'),('30000-40000','40000-50000'),('50000-60000','60000-70000')])
	Mobile_Battery = forms.ChoiceField(choices=[('82%','90%'),('95%','100%'),('85%','80%')],widget=forms.RadioSelect)
	Mobile_Final_Price = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'mfprice','placeholder':'Enter Your Mobile Final Price..!'}))
	# Agree_Terms = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'agree_terms'}), label="I agree to the terms and conditions", required=True)