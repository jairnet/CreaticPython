from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Copropiedad(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=50)
    nit = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=200)
    foto = models.ImageField(upload_to='coporpiedades/imagen', null=True, blank=True,)
    property_of = models.ForeignKey(User, null=True, blank=True, related_name='copropiedades', on_delete=models.SET_NULL)


    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        view_name = "detalle"
        return reverse(view_name, kwargs={"pk": self.id})

