from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    productos = Producto.objects.filter(activo=True).order_by("-fecha_creacion")[:3]
    return render(request, "tiendalibre/home.html", {"productos": productos})

def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by("-fecha_creacion")
    return render(request, "tiendalibre/catalogo.html", {"productos": productos})

def acerca_de_mi(request):
    return render(request, "tiendalibre/acercademi.html")

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tiendalibre/detalle.html", {"producto": producto})