from django.urls import path
from . import views

urlpatterns = [
    path('', views.destacar_articulos, name='destacados'),  
    
    path('featured', views.destacar_articulos, name='destacados'),  
    
    path('categories/', views.categorias, name='categorias'),
    path('categories/<int:id>/', views.detallar_categoria, name='categoria'),
    
    path('nuevo', views.CrearArticulo.as_view(), name='crear_articulo'),
    path('<int:pk>/editar', views.EditarArticulo.as_view(), name='editar_articulo'),
    path('<int:pk>/eliminar', views.EliminarArticulo.as_view(), name='eliminar_articulo'),
    path('alls', views.listar_articulos, name='articulos'),
    path('<int:pk>/', views.detallar_articulo, name='articulo'),

    # URLs de fotos dentro de posts
    path('<int:articulo_id>/foto/nueva/', views.SubirFoto.as_view(), name='subir_foto'),
    path('foto/<int:pk>/editar/', views.EditarFoto.as_view(), name='editar_foto'),
    path('foto/<int:pk>/eliminar/', views.EliminarFoto.as_view(), name='eliminar_foto'),

    path('search/', views.buscar_articulos, name='buscar_articulos'),
]