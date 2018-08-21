from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Contacto_form

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

class DashboardView(TemplateView):
    template_name = 'home/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context["titulo"]= "Altos de Pamba"
        return context 
        # {'variable':'Altos de la Pamba'}

def nosotros(request):
    return render(request, 'home/nosotros.html')

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
            return render(request, 'home/contacto.html', locals())
        else:
            msg = 'La informacion no es correcta'
    else:
        formulario = Contacto_form()
    return render(request, 'home/contacto.html', locals())
    




