from rest_framework import serializers
from .models import RegistroVenta
from datetime import date

class RegistroVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVenta
        fields = '__all__'
    
    def validate_fecha_venta(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha no puede ser futura.")
        return value

    def validate_monto_venta(self, value):
        if value < 0:
            raise serializers.ValidationError("El monto debe ser positivo.")
        return value