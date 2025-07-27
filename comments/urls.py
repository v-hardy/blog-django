from django.urls import path
from .views import ComentarioCreateView, ComentarioUpdateView, ComentarioDeleteView

urlpatterns = [
    path('comments/<int:articulo_id>/new', ComentarioCreateView.as_view(), name='crear_comentario'),
    path('<int:pk>/editar', ComentarioUpdateView.as_view(), name='editar_comentario'),
    path('<int:pk>/eliminar', ComentarioDeleteView.as_view(), name='eliminar_comentario'),
]
