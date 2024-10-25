from django.db import models

class Recordatorio(models.Model):
    TIPO_RECORDATORIO_CHOICES = [
        ('diario', 'Diario'),
        ('semanal', 'Semanal'),
        ('mensual', 'Mensual'),
    ]
    id_hábito = models.ForeignKey('Habito', on_delete=models.CASCADE)
    tipo_recordatorio = models.CharField(max_length=50, choices=TIPO_RECORDATORIO_CHOICES)
    mensaje = models.TextField()
    hora_programada = models.TimeField()

    def __str__(self):
        return f"{self.tipo_recordatorio} - {self.mensaje}"
