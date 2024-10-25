
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Habit(models.Model):
    DAILY = 'Daily'
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'
    
    FREQUENCY_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    category = models.CharField(max_length=50)
    goal = models.PositiveIntegerField(help_text="Number of repetitions needed to complete the habit.")

    def __str__(self):
        return f"{self.name} ({self.user.username})"
