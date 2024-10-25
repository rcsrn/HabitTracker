
# from django.contrib.auth.models import AbstractUser
from django.db import models

class Perfil(models.Model):
    avatar = models.CharField(max_length=100, default='/static/avatar1.jpg', null=False, blank=True)

    def __str__(self):
        return self.username
