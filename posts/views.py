from django.shortcuts import get_object_or_404, render
from .models import Articulo
from .forms import BusquedaPostForm

def lista_articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'posts/lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, pk):  # 👈 aquí agregas el argumento pk
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'posts/detalle_articulo.html', {'articulo': articulo})

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