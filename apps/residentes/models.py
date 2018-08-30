from django.db import models

from apps.core import choices
# from apps.usuarios.models import Usuario
from apps.inmueble.models import Inmueble


class Residente(models.Model):
    # perfil = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    grupo = models.CharField(max_length=15, blank=False, choices=choices.GRUPO_RESIDENTE, default=0)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    es_propietario = models.BooleanField(default=False, choices=choices.BOOL, default=0)

    # foreign keys
    inmueble = models.ForeignKey(Inmueble, null=True, blank=True, related_name='inmuebles', on_delete=models.SET_NULL)

    class Meta:
        ordering = ["grupo"]

    def __str__(self):
        return self.grupo
