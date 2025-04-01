from django.db import models
from apps.utils.models import AuditMixin
from apps.utils.choices import EstadoRecepcionChoices

class RecepcionEquipo(AuditMixin):
    cliente = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='equipos_recibidos')
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=EstadoRecepcionChoices.choices)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)
    tecnico_asignado = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL, related_name='equipos_asignados')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Equipo de {self.cliente.nombre} {self.cliente.apellido} - Estado: {self.estado}"
