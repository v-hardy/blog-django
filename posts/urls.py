from django.urls import path
from . import views

urlpatterns = [
    path('', views.destacar_articulos, name='destacados'),  
    
    path('featured', views.destacar_articulos, name='destacados'),  
    
    path('categories/', views.categorias, name='categorias'),
    path('categories/<int:id>/', views.detallar_categoria, name='categoria'),
    
    path('nuevo', views.CrearArticulo.as_view(), name='crear'),
    path('<int:pk>/editar', views.EditarArticulo.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarArticulo.as_view(), name='eliminar'),
    path('alls', views.listar_articulos, name='articulos'),
    path('<int:pk>/', views.detallar_articulo, name='articulo'),

    path('search/', views.buscar_articulos, name='buscar_articulos'),
]