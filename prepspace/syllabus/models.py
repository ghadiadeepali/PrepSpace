from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    topic_name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    added_to_todo = models.BooleanField(default=False)
    remark = models.TextField(blank=True, null=True)
    time_spent = models.DurationField(default=0)  # Stores total time spent on this topic
    completed_on = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.topic_name} ({self.subject.subject_name})"
