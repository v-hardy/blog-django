from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Usuario personalizado
class Usuario(AbstractUser):
    # Agrega un campo para roles: 'admin' o 'miembro'
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('miembro', 'Miembro'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='miembro')

    def es_admin(self):
        return self.rol == 'admin'

    def es_miembro(self):
        return self.rol == 'miembro'
    
    def __str__(self):
        return self.username