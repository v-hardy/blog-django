from django.shortcuts import render, HttpResponse

def lista_articulos(request):
    return HttpResponse("hola")
    #return render(request, 'comments/lista_articulos.html', context)

