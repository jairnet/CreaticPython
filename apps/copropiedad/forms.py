from django import forms
from django.forms import ModelForm
from .import models 

class CopropiedadForm(forms.ModelForm):
    class Meta:
        model = models.Copropiedad
        fields = ['nombre_copropiedad', 'direccion', 'telefono', 'nit', 'descripcion', 'foto']

    def clean(self, *args, **kwargs):
	    cleaned_data = super(CopropiedadForm, self).clean(*args, **kwargs)


