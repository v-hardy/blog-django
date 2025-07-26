from django.urls import path
from . import views  # importa tus vistas si es necesario

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulosNO'),
]
