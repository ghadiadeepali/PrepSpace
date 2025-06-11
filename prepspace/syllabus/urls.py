"""
URL configuration for prepspace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import syllabus_home, view_subject_details

urlpatterns = [
    path('', syllabus_home, name='syllabus_home'),
    # name is used while we specify the url to be hit when we want to redirect to this page i.e syllabus_tracker/
    path('/subject/<int:subject_id>',view_subject_details, name='subject_detail')
    
]
