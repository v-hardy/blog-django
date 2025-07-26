from django.shortcuts import get_object_or_404, render
from .models import Articulo

def lista_articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'posts/lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, pk):  # 👈 aquí agregas el argumento pk
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'posts/detalle_articulo.html', {'articulo': articulo})
