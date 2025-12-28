from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    daily_energy = models.IntegerField(default=5)  # 1 - 10
    stress_level = models.IntegerField(default=5)  # 1 - 10
    preferred_study_time = models.CharField(
        max_length=20,
        choices=[
            ('morning', 'Morning'),
            ('afternoon', 'Afternoon'),
            ('night', 'Night')
        ]
    )

    def __str__(self):
        return self.user.username
