from django.db import models
from django.contrib.auth.models import User

class MoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.IntegerField()   # 1 (bad) → 5 (great)
    energy = models.IntegerField() # 1 → 10
    note = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
