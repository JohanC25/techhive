from django.db import models

class RolChoices(models.TextChoices):
    ADMIN = "admin", "Administrador"
    TECNICO = "tecnico", "Técnico"
    CLIENTE = "cliente", "Cliente"

class EstadoInventarioChoices(models.TextChoices):
    DISPONIBLE = "disponible", "Disponible"
    VENDIDO = "vendido", "Vendido"
    DAÑADO = "dañado", "Dañado"
    RESERVADO = "reservado", "Reservado"

class EstadoRecepcionChoices(models.TextChoices):
    DIAGNOSTICO = "diagnostico", "En Diagnóstico"
    REPARACION = "reparacion", "En Reparación"
    REPARADO = "reparado", "Reparado"
    ENTREGADO = "entregado", "Entregado"
    CANCELADO = "cancelado", "Cancelado"
