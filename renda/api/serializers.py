from rest_framework import serializers
from renda import models

class RendaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Renda
        fields = "__all__"