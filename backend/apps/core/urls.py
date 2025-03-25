from django.urls import path
from .views import hello_vue

urlpatterns = [
    path('hello/', hello_vue),
]