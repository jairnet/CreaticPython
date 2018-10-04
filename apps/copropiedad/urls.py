from django.urls import path
from . import views

urlpatterns = [
    path('crear',views.CopropiedadCreateView.as_view(), name="crear"),
    path('lista',views.CopropiedadListView.as_view(), name="lista"),
    path('detalle/<int:pk>',views.CopropiedadDetailView.as_view(), name="detalle"),
    path('eliminar/<int:pk>',views.CopropiedadDeleteView.as_view(), name="eliminar"),
    path('detalle/<int:pk>/editar',views.CopropiedadUpdateView.as_view(), name="editar")
]