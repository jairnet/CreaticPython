from django.db import models

from apps.core import choices
from apps.copropiedad.models import Copropiedad

# Create your models here.

class Inmueble(models.Model):
    tipo_inmueble = models.CharField(max_length=15, blank=False, choices=choices.TIPO_INMUEBLE, default=0)
    nombre_inmueble = models.CharField(max_length=50)
    nombre_propietario = models.CharField(max_length=50)
    apellidos_propietario = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, max_length=254, null=True)
    grupo = models.CharField(max_length=15, blank=False, choices=choices.GRUPO_INMUEBLE, default=0)
    fecha_inicio_residencia = models.DateField(null=True, blank=True)

    # foreign keys
    copropiedad = models.ForeignKey(Copropiedad, null=True, blank=True, related_name='inmuebles', on_delete=models.SET_NULL)

    class Meta:
        ordering = ["nombre_inmueble"]

    def __str__(self):
        return self.nombre_inmueble
