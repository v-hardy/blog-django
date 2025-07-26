from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages  # Para mostrar mensajes flash (opcional)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Aquí podés hacer lo que quieras con los datos:
            # Enviar un email, guardarlo en la base de datos, etc.
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Ejemplo: mostrar mensaje de éxito
            messages.success(request, "Tu mensaje fue enviado correctamente.")
            return redirect('contacto')  # Redirecciona a la misma página
    else:
        form = ContactoForm()

    return render(request, 'contact/contacto.html', {'form': form})
