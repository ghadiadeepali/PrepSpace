from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, Topic

# Create your views here.
def syllabus_home(request):
    subjects = Subject.objects.all()
    return render(request,'syllabus_home.html',{'subjects': subjects} )

def view_subject_details(request, subject_id):
    topics = Topic.objects.filter(subject_id=subject_id)
    return render(request, 'subject_details.html', {'topics': topics} )