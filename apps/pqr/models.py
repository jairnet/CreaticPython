"" 'Django' ""
from django.db import models
from django.contrib.auth.models import User
from apps.core import choices
from apps.usuarios.models import Perfil


class Pqr(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT) 
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=15, blank=False, choices=choices.MOTIVO_PQR)
    comentario = models.TextField(max_length=1000, blank=True)
    estado = models.CharField(max_length=15, blank=True, choices=choices.ESTADO_PQR)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modifacion = models.DateField(auto_now=True)
    class Meta:
        ordering = ["motivo"]

    def __str__(self):
        return '{} por @{}'.format(self.motivo, self.user.username)


