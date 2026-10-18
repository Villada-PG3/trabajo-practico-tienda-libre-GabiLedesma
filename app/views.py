from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Producto


class HomeView(TemplateView):
    template_name = "tiendalibre/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos"] = Producto.objects.filter(activo=True).order_by("-fecha_creacion")[:3]
        return context


class CatalogoView(ListView):
    model = Producto
    template_name = "tiendalibre/catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.filter(activo=True).order_by("-fecha_creacion")


def acerca_de_mi(request):
    return render(request, "tiendalibre/acercademi.html")

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tiendalibre/detalle.html", {"producto": producto})