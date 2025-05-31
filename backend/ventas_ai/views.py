from rest_framework import viewsets
from .models import RegistroVenta
from .serializers import RegistroVentaSerializer
from django.utils.dateparse import parse_date

class RegistroVentaViewSet(viewsets.ModelViewSet):
    queryset = RegistroVenta.objects.all()
    serializer_class = RegistroVentaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        fecha = self.request.query_params.get('fecha')
        if fecha:
            queryset = queryset.filter(fecha_venta=fecha)
        return queryset