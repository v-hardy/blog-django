from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
]