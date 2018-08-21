from django.db import models

from apps.core import choices
from apps.inmueble.models import Inmueble
# Create your models here.

class Residente(models.Model):
    nombre_residente = models.CharField(max_length=50, help_text="Nombre(s) residente")
    apellidos_propietario = models.CharField(max_length=50, help_text="Apellido(s) residente")
    telefono = models.CharField(max_length=50, help_text="Numero de contacto")
    correo = models.CharField(max_length=50, help_text="Correo electronico")
    grupo = models.CharField(max_length=15, blank=False, choices=choices.GRUPO_RESIDENTE)
    fecha_inicio_residencia = models.DateField(null=True, blank=True)
    arrendador = models.BooleanField(default=False, choices=choices.BOOL)

    # foreign keys
    inmueble = models.ForeignKey(Inmueble, null=True, blank=True, related_name='inmuebles', on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-nombre_residente"]

    def __str__(self):
        return self.nombre_residente
