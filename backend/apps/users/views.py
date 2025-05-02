from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User
from .serializers import CustomTokenObtainPairSerializer, UserSerializer
from .permissions import EsAdminOTecnico
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

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
    
class BuscarClientePorCedulaView(APIView):
    def get(self, request):
        cedula = request.query_params.get('cedula')
        try:
            cliente = User.objects.get(cedula=cedula, rol='cliente')
            serializer = UserSerializer(cliente)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        current_user = self.request.user
        rol_creado = self.request.data.get('rol')

        if current_user.rol == 'admin':
            serializer.save()
        elif current_user.rol == 'tecnico':
            if rol_creado == 'cliente':
                serializer.save()
            else:
                raise permissions.PermissionDenied("Técnicos solo pueden crear clientes.")
        else:
            raise permissions.PermissionDenied("No tienes permiso para crear usuarios.")

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.rol == 'admin':
            return User.objects.all()
        elif user.rol == 'tecnico':
            return User.objects.filter(rol='cliente')
        return User.objects.none()

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user = self.request.user
        target_user = self.get_object()

        if user.rol == 'admin':
            serializer.save()
        elif user.rol == 'tecnico' and target_user.rol == 'cliente':
            serializer.save()
        else:
            raise permissions.PermissionDenied("No puedes editar este usuario.")

    def perform_destroy(self, instance):
        user = self.request.user
        if user.rol == 'admin':
            instance.delete()
        elif user.rol == 'tecnico' and instance.rol == 'cliente':
            instance.delete()
        else:
            raise permissions.PermissionDenied("No puedes eliminar este usuario.")

class CrearUsuarioView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [EsAdminOTecnico]