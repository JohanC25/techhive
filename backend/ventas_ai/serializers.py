from rest_framework import serializers
from .models import RegistroVenta

class RegistroVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVenta
        fields = '__all__'
