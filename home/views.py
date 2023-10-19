from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def registro(request):
    return render(request, 'home/registro.html')

def inicio(request):
    return render(request, 'home/inicio.html')

def acerca(request):
    return render(request, 'home/acerca.html')

def contacto(request):
    return render(request, 'home/contacto.html')

