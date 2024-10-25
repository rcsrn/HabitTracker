
from django.db import models
from habits.models import Habit

class Notification(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    scheduled_time = models.TimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.habit.name} at {self.scheduled_time}"
