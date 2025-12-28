from django.db import models
from django.utils import timezone

class DailyCheckin(models.Model):
    mood = models.IntegerField()      # من 1 لـ 5
    energy = models.IntegerField()    # من 1 لـ 10
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Mood: {self.mood}, Energy: {self.energy} ({self.created_at.date()})"
