# from django.shortcuts import render
from rest_framework import serializers
from apps.coopropiedad.models import *
from apps.residentes.models import *
from apps.inmueble.models import *

class coopropiedad_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coopropiedad
        fields = '__all__'

class residentes_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Residente
        fields = '__all__'

class inmuebles_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'


