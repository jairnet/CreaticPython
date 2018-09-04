from django.db import models
from django.urls import reverse

# Create your models here.

class Copropiedad(models.Model):
    nombre_copropiedad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=50)
    nit = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=200)
    foto = models.ImageField(upload_to='coporpiedades/imagen')

    class Meta:
        ordering = ["nombre_copropiedad"]

    def __str__(self):
        return self.nombre_copropiedad

    def get_absolute_url(self):
        view_name = "detalle"
        return reverse(view_name, kwargs={"pk": self.id})

