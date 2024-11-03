from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['nombre_habito', 'frecuencia', 'categoria', 'objetivo']
        widgets = {
            'frecuencia': forms.Select(choices=Habit.FREQUENCY_CHOICES),
            'objetivo': forms.NumberInput(attrs={'min': 1}),
        }