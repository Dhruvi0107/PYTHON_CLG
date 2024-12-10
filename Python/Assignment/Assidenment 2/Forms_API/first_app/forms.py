from django import forms

class Registration(forms.Form):
    First_Name = forms.CharField(widget=forms.TextInput(attrs={'id':'fname','placeholder':'Enter Your First Name..!'}),required=False)
    Last_Name = forms.CharField(widget=forms.TextInput(attrs={'id':'lname','placeholder':'Enter Your Last Name..!'}),required=False)
    User_Name = forms.CharField(widget=forms.TextInput(attrs={'id':'uname','placeholder':'Enter Your User Name..!'}),required=False)
    Email_ID = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email_ID','placeholder':'Enter Your Email ID..!'}),required=False)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','placeholder':'Enter Your Password..!'}),required=False)
    Course = forms.ChoiceField(choices=[('Bsc.IT', 'Bsc.IT'), ('Msc.IT', 'Msc.IT'), ('Bca', 'Bca'),('Mca', 'Mca'), ('Bba', 'Bba'), ('Mba', 'Mba')])
    Age = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'age','placeholder':'Enter Your Age..!'}),required=False)
    Date_of_Birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id': 'dob_id'}))
    Gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], widget=forms.RadioSelect)
    Hobbies = forms.MultipleChoiceField(choices=[('Reading','Reading'),('Sports','Sports'),('Music','Music'),('Traveling','Traveling')],widget=forms.CheckboxSelectMultiple)
    Address = forms.CharField(widget=forms.Textarea(attrs={'id': 'address_id', 'placeholder': 'Enter your Address..!'}))
    # Agree_Terms = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'agree_terms'}), label="I agree to the terms and conditions", required=True)
    