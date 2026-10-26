from .models import Categoria


def categorias(request):
    return {"categorias_menu": Categoria.objects.all()}