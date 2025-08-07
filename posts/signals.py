from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Foto
import os

if settings.DEBUG:
    print("📣 Señales de Foto cargadas")  # DEBUG TEMPORAL

    @receiver(post_delete, sender=Foto)
    def eliminar_archivo_imagen(sender, instance, **kwargs):
        if instance.imagen and instance.imagen.path and os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)
            print(f"🗑️ Imagen eliminada: {instance.imagen.path}")  # DEBUG
        else:
            print("⚠️ No se encontró el archivo para eliminar")  # DEBUG
else:
    @receiver(post_delete, sender=Foto)
    def eliminar_archivo_imagen(sender, instance, **kwargs):
        if instance.imagen and instance.imagen.path and os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)