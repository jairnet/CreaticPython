from django import forms

class Contacto_form(forms.Form):
    correo = forms.EmailField(widget=forms.TextInput())
    asunto = forms.CharField(widget=forms.TextInput())
    texto = forms.CharField(widget=forms.TextInput())