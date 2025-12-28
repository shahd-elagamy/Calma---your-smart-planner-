from django.db import models
from django.contrib.auth.models import User
from .subject import Subject

class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    planned_duration = models.IntegerField()  # minutes
    actual_duration = models.IntegerField(null=True, blank=True)

    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject.name} - {self.date}"
