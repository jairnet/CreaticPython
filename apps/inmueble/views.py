# Django
from django.urls import reverse_lazy
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from apps.inmueble.forms import InmuebleForm
from apps.home.mixins import DashboardLoginRequiredMixin

from apps.inmueble.models import Inmueble
from apps.copropiedad.models import Copropiedad


class InmuebleCreateView(DashboardLoginRequiredMixin, CreateView):
    form_class = InmuebleForm
    template_name = 'inmueble/inmueble_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['copropiedad_id'] = self.kwargs['pk']
        return kwargs
    
    def get_success_url(self):
        return reverse('detalle', args=[self.kwargs['pk']])

    
class InmuebleDetailView(DashboardLoginRequiredMixin, DetailView):
    model = Inmueble
    template_name = 'inmueble/inmueble_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['detalle_id'] =  args=[self.kwargs['pk']]
    #     print(self.object.pk)
    #     return context

    # def get_success_url(self):
    #     return reverse("lista")


class InmuebleUpdateView(DashboardLoginRequiredMixin, UpdateView):
    model = Inmueble
    template_name = 'inmueble/inmueble_update.html'
    fields = ['tipo_inmueble', 'nombre', 'area', 'piso', 'bloque', 'observacion', 'fecha_construcion']

    def save(self, commit=True):
        instance = super(InmuebleUpdateView, self).save(commit=False)
        inmueble = Inmueble.objects.get(pk=self.object.pk)
        copropiedad = Copropiedad.objects.get(pk=inmueble.copropiedad_id)
        instance.copropiedad = copropiedad
        if commit:
            instance.save()
        return instance

    def get_success_url(self):
        return reverse('detalle_inmueble', args=[self.object.pk])


class InmuebleDeleteView(DashboardLoginRequiredMixin, DeleteView):
    model = Inmueble
    success_url = reverse_lazy('lista')
    template_name = 'inmueble/inmueble_confirm_delete.html'
    
    
    

