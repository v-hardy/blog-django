from django.urls import path
from .views import ComentarioCreateView, ComentarioUpdateView, ComentarioDeleteView

urlpatterns = [
    path('new/<int:articulo_id>', ComentarioCreateView.as_view(), name='crear_comentario'),
    path('<int:pk>/editar/', ComentarioUpdateView.as_view(), name='editar_comentario'),
    path('<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='eliminar_comentario'),
]
