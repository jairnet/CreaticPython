from django.urls import path
from . import views

urlpatterns = [
    path('crear/<int:pk>',views.InmuebleCreateView.as_view(), name="crear_inmueble"),
    path('detalle-inmueble/<int:pk>',views.InmuebleDetailView.as_view(), name="detalle_inmueble"),
    path('eliminar-inmueble/<int:pk>',views.InmuebleDeleteView.as_view(), name="eliminar_inmueble"),
    path('detalle-inmueble/<int:pk>/editar',views.InmuebleUpdateView.as_view(), name="editar_inmueble")
]