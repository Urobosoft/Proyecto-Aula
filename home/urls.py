from django.urls import path
from .views import index, inicio, contacto, acerca,registro

urlpatterns = [
    path('', index, name='index'),
    path('inicio/', inicio, name='inicio'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('acerca/', acerca, name='acerca'),
]
