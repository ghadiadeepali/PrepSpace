from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    return render(request,'base.html' )
    # return render(request, 'theme/templates/base.html')
    # Django will look for base.html inside any templates/ folder of installed apps, like theme/templates/base.html, because of APP_DIRS=True.