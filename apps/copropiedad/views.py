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
from . models import Copropiedad


class CopropiedadCreateView(DashboardLoginRequiredMixin, CreateView):
    
    form_class = CopropiedadForm
    template_name = 'copropiedad/copropiedad_form.html'
    success_url = reverse_lazy('lista')


class CopropiedadListView(DashboardLoginRequiredMixin, ListView):
    model = Copropiedad
    template_name = 'copropiedad_list.html'

    # def get_queryset(self, *args, **kwars):
    #     qs = super(CoopropiedadListView, self).get_queryset(*args, **kwars)
    #     query = Coopropiedad.objects.filter(nombre_coopropiedad == 'Altos de la Pamba')
    #     return query

class CopropiedadDetailView(DashboardLoginRequiredMixin, DetailView):
    model = Copropiedad
    template_name = 'copropiedad/copropiedad_detail.html'

    def get_success_url(self):
        return reverse("lista")


class CopropiedadUpdateView(DashboardLoginRequiredMixin, UpdateView):
    model = Copropiedad
    form_class = CopropiedadForm
    template_name = 'copropiedad/copropiedad_update.html'

    
    
    

