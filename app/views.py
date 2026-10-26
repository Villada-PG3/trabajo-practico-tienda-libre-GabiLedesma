from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Producto, Categoria


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
    paginate_by = 6

    def get_queryset(self):
        queryset = Producto.objects.filter(activo=True).order_by("-fecha_creacion")
        q = self.request.GET.get("q", "").strip()
        if q:
            queryset = queryset.filter(
                Q(nombre__icontains=q)
                | Q(marca__icontains=q)
                | Q(descripcion__icontains=q)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "").strip()
        return context


class CategoriaView(ListView):
    model = Producto
    template_name = "tiendalibre/categoria.html"
    context_object_name = "productos"
    paginate_by = 6

    def get_queryset(self):
        self.categoria = get_object_or_404(Categoria, slug=self.kwargs["slug"])
        return Producto.objects.filter(
            activo=True, categoria=self.categoria
        ).order_by("-fecha_creacion")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria"] = self.categoria
        return context


def acerca_de_mi(request):
    return render(request, "tiendalibre/acercademi.html")

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "tiendalibre/detalle.html"
    context_object_name = "producto"

    def get_queryset(self):
        return Producto.objects.filter(activo=True)