from rest_framework import viewsets
from renda.api import serializers
from renda import models

class RendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RendaSerializers
    queryset = models.Renda.objects.all()