from django import forms
from django.contrib.auth.models import User
from apps.copropiedad.models import Copropiedad
from apps.inmueble.models import Inmueble 


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        exclude = ['copropiedad']

    def __init__(self, copropiedad_id, *args, **kwargs):
        super(InmuebleForm, self).__init__(*args, **kwargs)
        self.copropiedad_id = copropiedad_id
        print(self.copropiedad_id)

    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


    def save(self, commit=True):
        instance = super(InmuebleForm, self).save(commit=False)
        copropiedad = Copropiedad.objects.get(pk=self.copropiedad_id)
        
        instance.copropiedad = copropiedad
        # instance.foto = self.cleaned_data.get('foto')
        if commit:
            instance.save()
        return instance