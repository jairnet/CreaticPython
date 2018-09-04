from django.urls import path
from . import views

urlpatterns = [
    path('crear',views.CopropiedadCreateView.as_view(), name="crear"),
    path('lista',views.CopropiedadListView.as_view(), name="lista"),
    path('detalle/<int:pk>',views.CopropiedadDetailView.as_view(), name="detalle"),
    path('detalle/<int:pk>/editar',views.CopropiedadUpdateView.as_view(), name="editar")
]