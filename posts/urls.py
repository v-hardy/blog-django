from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('search/', views.buscar_articulos, name='buscar_articulos'),
]