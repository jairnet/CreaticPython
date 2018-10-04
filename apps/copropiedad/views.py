# Django
from django.urls import reverse_lazy
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from apps.copropiedad.forms import CopropiedadForm
from apps.home.mixins import DashboardLoginRequiredMixin
from apps.copropiedad.models import Copropiedad
from apps.inmueble.models import Inmueble
from apps.usuarios.models import Perfil


class CopropiedadCreateView(DashboardLoginRequiredMixin, CreateView):
    form_class = CopropiedadForm
    template_name = 'copropiedad/copropiedad_form.html'
    success_url = reverse_lazy('lista')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_id'] = self.request.user.pk
        return kwargs


class CopropiedadListView(DashboardLoginRequiredMixin, ListView):
    model = Copropiedad
    template_name = 'copropiedad_list.html'

    def get_queryset(self):
        user = self.request.user.id
        query = Copropiedad.objects.filter(property_of = user)
        return query   
    
class CopropiedadDetailView(DashboardLoginRequiredMixin, DetailView):
    model = Copropiedad
    second_model = Inmueble
    template_name = 'copropiedad/copropiedad_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CopropiedadDetailView, self).get_context_data(**kwargs)
        # context['object'] = TuModelo.objects.all()
        context['inmuebles'] = Inmueble.objects.filter(copropiedad=self.object.pk)
        return context


class CopropiedadUpdateView(DashboardLoginRequiredMixin, UpdateView):
    model = Copropiedad
    form_class = CopropiedadForm
    template_name = 'copropiedad/copropiedad_update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_id'] = self.request.user.pk
        return kwargs


class CopropiedadDeleteView(DashboardLoginRequiredMixin, DeleteView):
    model = Copropiedad
    success_url = reverse_lazy('lista')
    template_name = 'copropiedad/copropiedad_confirm_delete.html'
    
    
    

