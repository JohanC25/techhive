from rest_framework import serializers
from .models import RecepcionEquipo, Equipo
from users.serializers import UserSerializer
from users.models import User


class EquipoSerializer(serializers.ModelSerializer):
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    cliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Equipo
        fields = '__all__'

    def create(self, validated_data):
        cliente = validated_data.pop('cliente_id')
        return Equipo.objects.create(cliente=cliente, **validated_data)

class RecepcionEquipoSerializer(serializers.ModelSerializer):
    cliente = UserSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    equipo = EquipoSerializer(read_only=True)
    equipo_id = serializers.PrimaryKeyRelatedField(queryset=Equipo.objects.all(), write_only=True)

    tecnico_nombre = serializers.CharField(source='tecnico_asignado.nombre', read_only=True)
    tecnico_apellido = serializers.CharField(source='tecnico_asignado.apellido', read_only=True)

    class Meta:
        model = RecepcionEquipo
        fields = '__all__'
        read_only_fields = ['fecha_ingreso']

    def create(self, validated_data):
        cliente = validated_data.pop('cliente_id')
        equipo = validated_data.pop('equipo_id')
        tecnico = validated_data.pop('tecnico_asignado', None)

        return RecepcionEquipo.objects.create(
            cliente=cliente,
            equipo=equipo,
            tecnico_asignado=tecnico,
            **validated_data
        )