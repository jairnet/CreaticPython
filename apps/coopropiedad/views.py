from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import forms
from . models import Coopropiedad

# Create your views here.

class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self, request, *args, **kwargs):
		return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class CoopropiedadCreateView(StaffRequiredMixin, CreateView):
    model = Coopropiedad
    form_class = forms.CoopropiedadForm
    template_name = 'coopropiedad/coopropiedad_form.html'

    def get_success_url(self):
        return reverse("lista")


class CoopropiedadListView(ListView):
    model = Coopropiedad
    template_name = 'coopropiedad_list.html'

    # def get_queryset(self, *args, **kwars):
    #     qs = super(CoopropiedadListView, self).get_queryset(*args, **kwars)
    #     query = Coopropiedad.objects.filter(nombre_coopropiedad == 'Altos de la Pamba')
    #     return query

class CoopropiedadDetailView(DetailView):
    model = Coopropiedad
    template_name = 'coopropiedad/coopropiedad_detail.html'

    def get_success_url(self):
        return reverse("lista")


class CoopropiedadUpdateView(StaffRequiredMixin, UpdateView):
    model = Coopropiedad
    form_class = forms.CoopropiedadForm
    template_name = 'coopropiedad/coopropiedad_update.html'


    
    

