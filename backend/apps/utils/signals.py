from django.db.models.signals import pre_save
from django.dispatch import receiver
from threading import local
from .models import AuditMixin

_user = local()

def set_current_user(user):
    _user.value = user

def get_current_user():
    return getattr(_user, 'value', None)

@receiver(pre_save)
def add_editado_por(sender, instance, **kwargs):
    if issubclass(sender, AuditMixin) and not isinstance(instance, type):
        user = get_current_user()
        if user and hasattr(instance, 'editado_por'):
            instance.editado_por = user
