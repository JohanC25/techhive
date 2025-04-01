from django.urls import path
from .views import CustomTokenObtainPairView, MeView, DashboardView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', MeView.as_view(), name='me'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
