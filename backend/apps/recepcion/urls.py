from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecepcionEquipoViewSet, EquipoViewSet
from .views_estados import EstadoRecepcionChoicesView

router = DefaultRouter()
router.register(r'equipos', RecepcionEquipoViewSet, basename='recepcion-equipos')

urlpatterns = [
    path('estados/', EstadoRecepcionChoicesView.as_view(), name='estado-recepcion-choices'),
    path('', include(router.urls)),
]
