"" 'Django' ""
from django.db import models
from apps.core import choices
from apps.residentes.models import Residente


class Pqr(models.Model):
    residente = models.ForeignKey(Residente, null=True, blank=True, related_name='residentes', on_delete=models.SET_NULL)
    motivo = models.CharField(max_length=15, blank=False, choices=choices.MOTIVO_PQR)
    estado = models.CharField(max_length=15, blank=True, choices=choices.ESTADO_PQR)

    class Meta:
        ordering = ["motivo"]

    def __str__(self):
        return self.motivo


class Comentarios(models.Model):
    pqr = models.ForeignKey(Pqr, null=True, blank=True, related_name='pqrs', on_delete=models.SET_NULL)
    texto = models.TextField(max_length=1000, blank=True)
    fecha = models.DateField(2)
    emisor = models.CharField(max_length=15, blank=False, choices=choices.EMISOR)
    estado = models.CharField(max_length=15, blank=True, choices=choices.ESTADO_PQR)


