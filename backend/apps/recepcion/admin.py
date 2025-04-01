from django.contrib import admin
from .models import RecepcionEquipo

@admin.register(RecepcionEquipo)
class RecepcionEquipoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'estado', 'tecnico_asignado', 'costo', 'updated_at', 'editado_por')
    search_fields = ('cliente__cedula', 'cliente__nombre', 'cliente__apellido')
    list_filter = ('estado',)