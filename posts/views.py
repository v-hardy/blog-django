from django.shortcuts import get_object_or_404, render
from .models import Articulo, Categoria
from .forms import BusquedaPostForm


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'posts/categorias.html', {'categorias': categorias})

def detallar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    articulos = Articulo.objects.filter(categoria=categoria).order_by('-fecha_publicacion')
    return render(request, 'posts/categoria.html', {
        'categoria': categoria,
        'articulos': articulos
    })


def destacar_articulos(request):
    ultimos_articulos = Articulo.objects.select_related('autor', 'categoria').prefetch_related('fotos').order_by('-fecha_publicacion')[:10]
    return render(request, 'posts/articulos_destacados.html', {'articulos': ultimos_articulos})

def listar_articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'posts/articulos.html', {'articulos': articulos})

def detallar_articulo(request, pk):  # 👈 aquí agregas el argumento pk
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'posts/articulo.html', {'articulo': articulo})

def buscar_articulos(request):
    form = BusquedaPostForm(request.GET or None)
    articulos = Articulo.objects.all()

    if form.is_valid():
        categoria = form.cleaned_data.get('categoria')
        orden_fecha = form.cleaned_data.get('orden_fecha')
        orden_alfabetico = form.cleaned_data.get('orden_alfabetico')

        if categoria:
            articulos = articulos.filter(categoria=categoria)

        # Orden por fecha
        if orden_fecha:
            if orden_fecha == 'asc':
                articulos = articulos.order_by('fecha_publicacion')
            elif orden_fecha == 'desc':
                articulos = articulos.order_by('-fecha_publicacion')

        # Orden alfabético
        if orden_alfabetico:
            if orden_alfabetico == 'az':
                articulos = articulos.order_by('titulo')
            elif orden_alfabetico == 'za':
                articulos = articulos.order_by('-titulo')

    return render(request, 'posts/busqueda.html', {
        'form': form,
        'articulos': articulos
    })