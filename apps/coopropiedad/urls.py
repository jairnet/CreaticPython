from django.urls import path
from . import views

urlpatterns = [
    path('crear',views.CoopropiedadCreateView.as_view(), name="crear"),
    path('lista',views.CoopropiedadListView.as_view(), name="lista"),
    path('detalle/<int:pk>',views.CoopropiedadDetailView.as_view(), name="detalle"),
    path('editar/<int:pk>',views.CoopropiedadUpdateView.as_view(), name="editar")
]