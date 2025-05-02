from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import RecepcionEquipo, Equipo
from .serializers import RecepcionEquipoSerializer, EquipoSerializer

class RecepcionEquipoViewSet(viewsets.ModelViewSet):
    queryset = RecepcionEquipo.objects.all()
    serializer_class = RecepcionEquipoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("❌ Errores del serializer:")
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(tecnico_asignado=request.user)  # 👈 El técnico se pasa aquí
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EquipoViewSet(viewsets.ModelViewSet):
    serializer_class = EquipoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cliente_id = self.request.query_params.get('cliente_id')
        queryset = Equipo.objects.all()
        if cliente_id:
            queryset = queryset.filter(cliente_id=cliente_id)
        return queryset