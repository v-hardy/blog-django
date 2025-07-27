from django import forms
from .models import Categoria, Articulo, Foto

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['imagen', 'descripcion']


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria']

class BusquedaPostForm(forms.Form):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        label='Categoría',
        empty_label='Todas'
    )

    orden_fecha = forms.ChoiceField(
        choices=[
            ('', '---'),
            ('asc', 'Más antiguas'),
            ('desc', 'Más recientes')
        ],
        required=False,
        label='Antigüedad'
    )

    orden_alfabetico = forms.ChoiceField(
        choices=[
            ('', '---'),
            ('az', 'A - Z'),
            ('za', 'Z - A')
        ],
        required=False,
        label='Alfabético'
    )
