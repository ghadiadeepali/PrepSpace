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
from .views import dashboard
from syllabus import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", dashboard),
    path("syllabus/", include(urls)), # include urls of syllabus app and the urlpattern in syllabus/{}
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
# “When the URL starts with /media/ (from MEDIA_URL), look for the corresponding file inside the folder media/ (from MEDIA_ROOT).”
# A user uploads image.jpg
# Saved at: /your_project/media/subject_images/image.jpg
# Accessible at: http://127.0.0.1:8000/media/subject_images/image.jpg