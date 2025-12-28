from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField()  # 1 (easy) → 5 (hard)
    priority = models.IntegerField()    # 1 (low) → 5 (high)

    def __str__(self):
        return self.name
