from django.db import models
from django.conf import settings
from posts.models import Articulo  # O ajusta si es diferente

class Comentario(models.Model):
    contenido = models.TextField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, related_name='comentarios', on_delete=models.CASCADE)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario} en {self.articulo}'
