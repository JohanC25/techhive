from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            "rol": self.user.rol,
            "nombre": self.user.nombre,
            "apellido": self.user.apellido
        })
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'nombre',
            'apellido',
            'cedula',
            'email',
            'celular',
            'convencional',
            'rol'
        ]
