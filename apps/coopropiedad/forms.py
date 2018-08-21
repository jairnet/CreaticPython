from django import forms
from .import models 

class CoopropiedadForm(forms.ModelForm):
    class Meta:
        model = models.Coopropiedad
        fields = '__all__'

    def clean(self, *args, **kwargs):
	    cleaned_data = super(CoopropiedadForm, self).clean(*args, **kwargs)


