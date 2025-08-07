from django import forms
from .models import Categoria, Articulo, Foto

# forms.py
from django import forms
from .models import Foto

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['imagen', 'descripcion']

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')

        if not self.instance.pk and not imagen:
            # Si es una nueva instancia y no hay imagen, lanzamos error
            raise forms.ValidationError("Debes subir una imagen.")

        return imagen


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
