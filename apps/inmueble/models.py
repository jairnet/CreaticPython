from django.db import models

from apps.core import choices
from apps.coopropiedad.models import Coopropiedad

# Create your models here.

class Inmueble(models.Model):
    tipo_inmueble = models.CharField(max_length=15, blank=False, choices=choices.TIPO_INMUEBLE, default=0)
    nombre_inmueble = models.CharField(max_length=50, help_text="Apto 102, Casa 3")
    nombre_propietario = models.CharField(max_length=50, help_text="Nombre(s)")
    apellidos_propietario = models.CharField(max_length=50, help_text="Apellido(s)")
    telefono = models.CharField(max_length=50, help_text="Numero de contacto")
    correo = models.CharField(max_length=50, help_text="Correo electronico")
    grupo = models.CharField(max_length=15, blank=False, choices=choices.GRUPO_INMUEBLE, default=0)
    fecha_inicio_residencia = models.DateField(null=True, blank=True)

    # foreign keys
    coopropiedad = models.ForeignKey(Coopropiedad, null=True, blank=True, related_name='inmuebles', on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-nombre_inmueble"]

    def __str__(self):
        return self.nombre_inmueble
