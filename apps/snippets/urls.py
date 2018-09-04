from django.urls import path, include
from rest_framework import routers
from apps.copropiedad.models import *
from apps.residentes.models import *
from apps.inmueble.models import *
from .serializers import *
from apps.snippets.views import copropiedad_viewset,residentes_viewset,inmuebles_viewset
# from . import views

router = routers.DefaultRouter()
router.register('copropiedad', copropiedad_viewset)
router.register('residentes', residentes_viewset)
router.register('inmueble', inmuebles_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]