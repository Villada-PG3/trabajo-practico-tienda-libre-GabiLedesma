from django.shortcuts import render


def home(request):
    productos_empty=[]
    productos = [ 
        { "nombre": "Remera", "descripcion": "Remera de algodón suave y cómoda, ideal para usar todos los días. Disponible en diferentes talles y colores.", "stock": 15, "precio": 5000.212, },
    { "nombre": "Pantalón", "descripcion": "Pantalón de jean clásico confeccionado con materiales resistentes y cómodos. Ideal para combinar con cualquier tipo de calzado.", "stock": 8, "precio": None, }, 
    { "nombre": "Zapatillas", "descripcion": "Zapatillas deportivas livianas y cómodas, pensadas para actividades cotidianas y momentos de ejercicio.", "stock": 12, "precio": 25000.99, }, 
    { "nombre": "Campera", "descripcion": "Campera impermeable y abrigada, perfecta para protegerse del frío y la lluvia durante los días de invierno.", "stock": 5, "precio": 30000.101, },
    { "nombre": "Gorra", "descripcion": "Gorra deportiva ajustable con diseño moderno. Cuenta con una visera que ayuda a proteger del sol y es fácil de combinar con distintos estilos.", "stock": 20, "precio": 7000.600, }, 
    { "nombre": "Mochila", "descripcion": "Mochila amplia y resistente con varios compartimentos para organizar libros, útiles, dispositivos y objetos personales.", "stock": 10, "precio": 18000.99, }, ]

    return render(
        request,
        "tiendalibre/home.html",
        {"productos": productos}
    )


def acerca_de_mi(request):
    return render(request, "tiendalibre/acercademi.html")