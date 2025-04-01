from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'rol', 'email', 'is_active', 'created_at', 'updated_at', 'editado_por')
    search_fields = ('cedula', 'nombre', 'apellido', 'email')
    list_filter = ('rol', 'is_active')