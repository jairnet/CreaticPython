from django.shortcuts import render
from .forms import Contacto_form

# Create your views here.
def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    email = ""
    subject = ""
    text = ""
    info_enviado = False
    if request.method  == 'POST':
        formulario = Contacto_form(request.POST)
        if formulario.is_valid():
            email = formulario.cleaned_data['correo']
            subject = formulario.cleaned_data['asunto']
            text = formulario.cleaned_data['texto']
            info_enviado = True
            return render(request, 'contacto.html', locals())
        else:
            msg = 'La informacion no es correcta'
    else:
        formulario = Contacto_form()
    return render(request, 'contacto.html', locals())
    




