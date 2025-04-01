from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # 👈 Forzamos a que valide con email

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            "rol": self.user.rol,
            "nombre": self.user.nombre,
            "apellido": self.user.apellido
        })
        return data
