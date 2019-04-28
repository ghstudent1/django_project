from django.shortcuts import render
from .models import Person
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello this is the home page")
#create linbk in url.py then  create this funct def peron then in templates make your html template in which the mix of dynamic data
#create the static dir and configure it in the settings

def person(request):
    persons=Person.objects.all()
    return render(request,'person_home.html',{'person': persons})
