from django.urls import path
from . import views

urlpatterns = [
    path('', views.destacar_articulos, name='destacados'),  
    path('destacados', views.destacar_articulos, name='destacados'),  
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:id>/', views.detallar_categoria, name='categoria'),
    path('articulos/', views.listar_articulos, name='articulos'),
    path('<int:pk>/', views.detallar_articulo, name='articulo'),
    path('search/', views.buscar_articulos, name='buscar_articulos'),
]