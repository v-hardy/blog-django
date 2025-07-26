# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_articulos')  # o la página que quieras
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
