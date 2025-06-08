from django.contrib import admin
from .models import Subject, Topic

# Register your models here so that they can be shown on Django Admin Dashboard
admin.site.register(Subject)
admin.site.register(Topic)