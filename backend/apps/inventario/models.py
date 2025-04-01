from django.db import models
from apps.utils.models import AuditMixin
from apps.utils.choices import EstadoInventarioChoices

class Inventario(AuditMixin):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    codigo_barras = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=EstadoInventarioChoices.choices)
    stock_minimo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo_barras})"
