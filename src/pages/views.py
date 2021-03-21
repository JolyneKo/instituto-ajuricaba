"""
===============
     Views
===============
"""

from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")


def about_view(request):
    return render(request, "about.html")


def diretoria_view(request):
    return render(request, "diretoria.html")


def expresidentes_view(request):
    return render(request, "ex-presidentes.html")
