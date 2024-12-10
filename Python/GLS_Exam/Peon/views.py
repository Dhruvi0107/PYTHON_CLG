from django.shortcuts import render
from Peon.models import *

# Create your views here.
def indexPage(request):
	return render(request,"Peon/index.html")

def showPeon(request):

	Peons = Peon.objects.all()

	context = {
		'Peonss':Peons
	}

	return render(request,"Peon/show_peon.html",context)