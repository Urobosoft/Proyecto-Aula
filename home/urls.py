from django.urls import path
from .views import index, inicio

urlpatterns = [
    path('', index, name='index'),
    path('inicio/', inicio, name='inicio'),
]
