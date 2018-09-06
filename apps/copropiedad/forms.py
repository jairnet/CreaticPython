from django import forms

from apps.copropiedad.models import Copropiedad 

class CopropiedadForm(forms.ModelForm):
    class Meta:
        model = Copropiedad
        fields = '__all__'

    # def clean(self, *args, **kwargs):
	#     cleaned_data = super(CopropiedadForm, self).clean(*args, **kwargs)


