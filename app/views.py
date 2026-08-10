from django.shortcuts import render

def home(request):
    return render(request, "tiendalibre/home.html")
# Create your views here.
def acerca_de_mi(request):
    return render(request, "tiendalibre/acercademi.html")