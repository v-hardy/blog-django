from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio con destacados o recientes
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:id>/', views.categoria_detalle, name='categoria_detalle'),
    path('', views.lista_articulos, name='articulos'),
    path('<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('search/', views.buscar_articulos, name='buscar_articulos'),
]