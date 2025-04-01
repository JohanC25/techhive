from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.views import APIView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "cedula": user.cedula,
            "nombre": user.nombre,
            "apellido": user.apellido,
            "email": user.email,
            "rol": user.rol
        })

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.rol == 'admin':
            data = {"msg": "Panel del administrador", "rol": user.rol}
        elif user.rol == 'tecnico':
            data = {"msg": "Panel del técnico", "rol": user.rol}
        elif user.rol == 'cliente':
            data = {"msg": "Panel del cliente", "rol": user.rol}
        else:
            return Response({"error": "Rol no reconocido"}, status=400)
        return Response(data)
