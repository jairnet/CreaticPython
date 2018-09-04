"""Modelo Usuarios"""

# Django
from django.db import models
from django.contrib.auth.models import User

from apps.core import choices


class Perfil(models.Model):
    """Modelo Perfil"""
    usuraio = models.OneToOneField(User, on_delete=models.PROTECT)
    direccion = models.CharField(blank=True, max_length=100)
    telefono = models.CharField(blank=True, max_length=20)
    rol = models.CharField(max_length=20, blank=False, choices=choices.ROL_USUARIO)
    foto = models.ImageField(upload_to='usuarios/fotos')
    codigo_invitacion = models.CharField(blank=True, max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modifacion = models.DateField(auto_now=True)

    def __str__(self):
        """Retorna Username"""
        return self.user.username
