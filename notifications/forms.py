from django import forms
from .models import Recordatorio
class RecordatorioForm(forms.ModelForm):
    class Meta:
        model = Recordatorio
        fields = ["tipo_recordatorio","mensaje","hora_programada"]
        labels = {
            "tipo_recordatorio":"Tipo de recordatorio",
            "mensaje":"Mensaje",
            "hora_programada":"Hora programada"
        }
        