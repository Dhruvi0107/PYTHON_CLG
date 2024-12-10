from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

my_dict = {'greeting' : 'Hello Good Morning', 'name' : 'My name is Priya Christian'}

def firstapp_index(request):
	return render(request, 'first_app/index.html', context=my_dict)