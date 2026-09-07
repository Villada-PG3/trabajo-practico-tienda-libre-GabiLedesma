from app.models import Producto, Categoria

Producto.objects.all()

Producto.objects.filter(precio__gt=10000)

Producto.objects.filter(precio__lt=20000)

Producto.objects.filter(nombre__icontains="a")

Producto.objects.exclude(stock__lt=10)

Producto.objects.order_by("precio")

Producto.objects.order_by("-stock")

Producto.objects.filter(nombre__in=["Remera", "Gorra", "Mochila"])

Producto.objects.filter(stock__gte=10).order_by("-precio")

Categoria.objects.first().productos.all()

producto = Producto.objects.create(
    nombre="Buzo",
    descripcion="Buzo cómodo para días fríos.",
    precio=20000,
    stock=7,
    marca="Adidas",
    categoria=categoria
)