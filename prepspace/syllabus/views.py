from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, Topic
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

# Create your views here.
def syllabus_home(request):
    subjects = Subject.objects.all()
    return render(request,'syllabus_home.html',{'subjects': subjects} )

def view_subject_details(request, subject_id):
    topics = Topic.objects.filter(subject_id=subject_id)
    return render(request, 'subject_details.html', {'topics': topics} )

@require_POST
def update_topic_status(request,topic_id):
    print("POST data:", request.POST)
    print("********************************")
    print(topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    print("********************************")
    print(topic)
    # HTMX sends "is_completed=on" if checked, otherwise nothing
    # value of is_completed is set by the value keyword in HTML file
    # .get('') is the name that we have mentioned in the input tag in html file
    is_completed = request.POST.get('is_completed') == 'on'
    print("********************************")
    print(is_completed)
    topic.is_completed = is_completed
    topic.completed_on = now() if is_completed else None
    topic.save()

    return HttpResponse(status=204) 