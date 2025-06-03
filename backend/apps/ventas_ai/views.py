from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum
from .models import RegistroVenta
from .serializers import RegistroVentaSerializer

class RegistroVentaViewSet(viewsets.ModelViewSet):
    queryset = RegistroVenta.objects.all()
    serializer_class = RegistroVentaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        fecha = self.request.query_params.get('fecha')
        desde = self.request.query_params.get('desde')
        hasta = self.request.query_params.get('hasta')

        if fecha:
            queryset = queryset.filter(fecha_venta=fecha)
        elif desde and hasta:
            queryset = queryset.filter(fecha_venta__range=[desde, hasta])
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total = queryset.aggregate(total=Sum('monto_venta'))['total'] or 0

        return Response({
            'ventas': serializer.data,
            'total': round(total, 2)
        })
