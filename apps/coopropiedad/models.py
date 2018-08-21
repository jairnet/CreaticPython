from django.db import models
from django.urls import reverse

# Create your models here.

class Coopropiedad(models.Model):
    nombre_coopropiedad = models.CharField(max_length=50, help_text="Nombre del condominio")
    direccion = models.CharField(max_length=30, help_text="Direccion del condominio")
    telefono = models.CharField(max_length=50, help_text="Numero telefonico del condominio")
    nit = models.CharField(max_length=20, help_text="NIT del condominio")
    descripcion = models.TextField(max_length=200, help_text="Descripcion del condominio")

    class Meta:
        ordering = ["nombre_coopropiedad"]

    def __str__(self):
        return self.nombre_coopropiedad

    def get_absolute_url(self):
        view_name = "detalle"
        return reverse(view_name, kwargs={"pk": self.id})

