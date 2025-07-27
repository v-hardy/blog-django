from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ComentarioForm
from .models import Comentario
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comments/comentario_form.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.articulo_id = self.kwargs['articulo_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articulo', kwargs={'pk': self.object.articulo.pk})

class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comments/comentario_form.html'

    def get_success_url(self):
        return reverse('articulo', kwargs={'pk': self.object.articulo.pk})

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comments/comentario_borrar.html'

    def get_success_url(self):
        return reverse('articulo', kwargs={'pk': self.object.articulo.pk})
