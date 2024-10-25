
from django.db import models
from habits.models import Habit

class Progress(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='progress')
    date = models.DateField()
    completions = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('habit', 'date')

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {self.completions}"
