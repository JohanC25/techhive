from django.urls import path
from .views import CustomTokenObtainPairView, MeView, DashboardView, BuscarClientePorCedulaView, UserListView, UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', MeView.as_view(), name='me'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('buscar/', BuscarClientePorCedulaView.as_view(), name='buscar-cliente'),
    path('', UserCreateView.as_view(), name='crear-usuario'),
    path('listado/', UserListView.as_view(), name='listar-usuarios'),
    path('crear/', UserCreateView.as_view(), name='crear-usuario'),
    path('<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='detalle-usuario'),
]
