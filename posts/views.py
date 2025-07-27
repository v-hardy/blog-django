from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Articulo, Categoria, Foto
from .forms import BusquedaPostForm, ArticuloForm, FotoForm
from comments.forms import ComentarioForm
from comments.models import Comentario


# Crear foto (asociada a un artículo)
class SubirFoto(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Foto
    form_class = FotoForm
    template_name = 'posts/foto_form.html'

    def form_valid(self, form):
        articulo_id = self.kwargs['articulo_id']
        form.instance.articulo_id = articulo_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articulo', kwargs={'pk': self.object.articulo.pk})

    def test_func(self):
        return self.request.user.is_staff

# Editar foto
class EditarFoto(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Foto
    form_class = FotoForm
    template_name = 'posts/foto_form.html'

    def get_success_url(self):
        return reverse_lazy('articulo', kwargs={'pk': self.object.articulo.pk})

    def test_func(self):
        return self.request.user.is_staff

# Eliminar foto
class EliminarFoto(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Foto
    template_name = 'posts/foto_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('articulo', kwargs={'pk': self.object.articulo.pk})

    def test_func(self):
        return self.request.user.is_staff



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


class CrearArticulo(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'posts/articulo_form.html'
    success_url = reverse_lazy('articulos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarArticulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'posts/articulo_form.html'
    success_url = reverse_lazy('articulos')

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor or self.request.user.is_staff

class EliminarArticulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'posts/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulos')

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor or self.request.user.is_staff


def destacar_articulos(request):
    ultimos_articulos = Articulo.objects.select_related('autor', 'categoria').prefetch_related('fotos').order_by('-fecha_publicacion')[:10]
    return render(request, 'posts/articulos_destacados.html', {'articulos': ultimos_articulos})

def listar_articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'posts/articulos.html', {'articulos': articulos})

def detallar_articulo(request, pk):  # 👈 aquí agregas el argumento pk
    articulo = get_object_or_404(Articulo, pk=pk)
    comentarios = articulo.comentario_set.select_related('usuario').all()
    form = ComentarioForm()

    return render(request, 'posts/articulo.html', {
        'articulo': articulo,
        'comentarios': comentarios,
        'comentario_form': form
    })

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