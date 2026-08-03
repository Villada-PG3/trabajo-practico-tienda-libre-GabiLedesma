from django.contrib import admin
from django.utils.html import format_html
from .models import Producto, Categoria



class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "mostrar_miniatura")
    readonly_fields = ("mostrar_imagen_detalle",)

    def mostrar_miniatura(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;">',
                obj.imagen.url
            )
        return "Sin imagen"

    def mostrar_imagen_detalle(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-width:300px;">',
                obj.imagen.url
            )
        return "Sin imagen"


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)