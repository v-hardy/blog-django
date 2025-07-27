from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from users.models import Usuario

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class Foto(models.Model):
    imagen = models.ImageField(upload_to='fotos/', null=True, blank=True)  #📌 upload_to='fotos/' guardará las imágenes en MEDIA_ROOT/fotos/.
    descripcion = models.TextField(blank=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='fotos')

    def __str__(self):
        return f"Foto de {self.articulo.titulo}"

