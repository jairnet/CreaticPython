from rest_framework import viewsets
from apps.copropiedad.models import *
from apps.residentes.models import *
from apps.inmueble.models import *
from . serializers import *

class copropiedad_viewset(viewsets.ModelViewSet):
    queryset = Copropiedad.objects.all()
    serializer_class = copropiedad_serializer

class residentes_viewset(viewsets.ModelViewSet):
    queryset = Residente.objects.all()
    serializer_class = residentes_serializer

class inmuebles_viewset(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = inmuebles_serializer

