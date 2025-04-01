from django.utils.deprecation import MiddlewareMixin
from .signals import set_current_user

class CurrentUserMiddleware(MiddlewareMixin):
    """
    Middleware para capturar automáticamente el request.user
    y asignarlo al thread-local usado por AuditMixin.
    """

    def process_request(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            set_current_user(request.user)
        else:
            set_current_user(None)
