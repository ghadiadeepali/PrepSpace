from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject

# Create your views here.
def syllabus_home(request):
    subjects = Subject.objects.all()
    return render(request,'syllabus_home.html',{'subjects': subjects} )