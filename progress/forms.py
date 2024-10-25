# progress/forms.py

from django import forms
from .models import Progress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress  # Referencia al modelo Progress
        fields = ['habit', 'date', 'estado']  # Campos a incluir en el formulario
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Selector de fecha en HTML5
        }
