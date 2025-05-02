from django.db import models
from apps.utils.models import AuditMixin
from apps.utils.choices import EstadoRecepcionChoices


class Equipo(AuditMixin):
    cliente = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='equipos')
    observaciones = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.marca or 'Sin marca'} {self.modelo or ''} - {self.observaciones}"


class RecepcionEquipo(AuditMixin):
    cliente = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='recepciones')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='recepciones')
    diagnostico = models.TextField()
    estado = models.CharField(max_length=20, choices=EstadoRecepcionChoices.choices)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    tecnico_asignado = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL, related_name='recepciones_asignadas')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Recepción ({self.equipo}) - Diagnóstico: {self.diagnostico[:30]}"
