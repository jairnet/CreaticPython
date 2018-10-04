from django import forms
from django.contrib.auth.models import User
from apps.copropiedad.models import Copropiedad 

class CopropiedadForm(forms.ModelForm):
    class Meta:
        model = Copropiedad
        exclude = ['property_of']

    def __init__(self, user_id, *args, **kwargs):
        super(CopropiedadForm, self).__init__(*args, **kwargs)
        self.user_id = user_id

    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


    def save(self, commit=True):
        instance = super(CopropiedadForm, self).save(commit=False)
        
        user = User.objects.get(pk=self.user_id)
        instance.property_of = user
        instance.foto = self.cleaned_data.get('foto')
        if commit:
            instance.save()
        return instance