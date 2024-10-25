from django.db import models
from django.contrib.auth import get_user_model

# Obtener el modelo de usuario personalizado
Usuario = get_user_model()

class Habit(models.Model):
    DIARIO = 'Diario'
    SEMANAL = 'Semanal'
    MENSUAL = 'Mensual'

    FREQUENCY_CHOICES = [
        (DIARIO, 'Diario'),
        (SEMANAL, 'Semanal'),
        (MENSUAL, 'Mensual'),
    ]

    # Campos del modelo
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='habitos')
    nombre_habito = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    categoria = models.CharField(max_length=50)
    objetivo = models.PositiveIntegerField(help_text="Repeticiones necesarias para completar el hábito.")

    def __str__(self):
        return f"{self.nombre_habito} ({self.id_usuario.username})"
