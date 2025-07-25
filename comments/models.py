from django.db import models
from users.models import Usuario
from posts.models import Articulo

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.articulo.titulo}"
