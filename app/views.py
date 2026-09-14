from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.filter(activo=True).order_by("-fecha_creacion")[:3]
    return render(request, "tiendalibre/home.html", {"productos": productos})

def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by("-fecha_creacion")
    return render(request, "tiendalibre/catalogo.html", {"productos": productos})

def acerca_de_mi(request):
    return render(request, "tiendalibre/acercademi.html")