from django.db import models
from django.utils import timezone

class AuditMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    editado_por = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL, related_name="%(class)s_editados")

    class Meta:
        abstract = True