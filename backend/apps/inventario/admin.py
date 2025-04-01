from django.contrib import admin
from .models import Inventario

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_barras', 'cantidad', 'estado', 'precio', 'updated_at', 'editado_por')
    search_fields = ('nombre', 'codigo_barras')
    list_filter = ('estado',)