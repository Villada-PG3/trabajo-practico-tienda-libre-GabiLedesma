from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("acercademi/", views.acerca_de_mi, name="acerca_de_mi"),
    path("catalogo/", views.catalogo, name="catalogo"),
]