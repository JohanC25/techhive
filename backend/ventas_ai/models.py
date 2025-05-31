from django.db import models
import holidays

class RegistroVenta(models.Model):
    fecha_venta = models.DateField()
    monto_venta = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    es_feriado = models.BooleanField(default=False)
    es_fin_de_semana = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Detectar si es fin de semana
        self.es_fin_de_semana = self.fecha_venta.weekday() >= 5  # 5 = sábado, 6 = domingo

        # Detectar si es feriado en Ecuador
        ecuador_holidays = holidays.CountryHoliday('EC')
        self.es_feriado = self.fecha_venta in ecuador_holidays

        super().save(*args, **kwargs)
