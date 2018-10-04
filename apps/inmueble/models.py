from django.db import models

from apps.core import choices
from apps.copropiedad.models import Copropiedad

# Create your models here.

class Inmueble(models.Model):
    tipo_inmueble = models.CharField(max_length=15, blank=False, choices=choices.TIPO_INMUEBLE)
    nombre = models.CharField(max_length=50)
    area = models.IntegerField()
    piso = models.IntegerField()
    bloque = models.CharField(max_length=10)
    observacion = models.TextField(max_length=1000)
    fecha_construcion = models.DateField()

    # foreign keys
    copropiedad = models.ForeignKey(Copropiedad, null=True, blank=True, related_name='inmuebles', on_delete=models.SET_NULL)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
