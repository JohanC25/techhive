from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from apps.utils.models import AuditMixin
from apps.utils.choices import RolChoices

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser debe tener is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, AuditMixin):
    cedula = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    celular = models.CharField(max_length=20)
    convencional = models.CharField(max_length=20, blank=True, null=True)
    rol = models.CharField(max_length=20, choices=RolChoices.choices)

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'cedula', 'celular', 'rol']

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cedula}"
