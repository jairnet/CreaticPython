from django.shortcuts import render
from django.views.generic import TemplateView
from . mixins import DashboardLoginRequiredMixin


# Create your views here.
class index(TemplateView):
    template_name = 'home/index.html'

class DashboardView(DashboardLoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(DashboardView, self).get_context_data(*args, **kwargs)
    #     context["titulo"]= Copropiedad.objects.get(pk = self.object.pk)
    #     print(context)
    #     return context
    




