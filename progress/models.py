from django.db import models
from habits.models import Habit

class ProgresoHabito(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    id_habito = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='progresos')
    fecha = models.DateField()
    estado = models.CharField(max_length=50) 

    class Meta:
        unique_together = ('id_habito', 'fecha')
        verbose_name = "Progreso del Hábito"
        verbose_name_plural = "Progresos de los Hábitos"

    def __str__(self):
        return f"{self.id_habito.name} - {self.fecha} - {self.estado}"
