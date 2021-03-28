"""
===============
     Views
===============
"""

from django.shortcuts import render
from .models import Evento


def home_view(request):
    return render(request, "home.html")


def about_view(request):
    return render(request, "about.html")


def diretoria_view(request):
    return render(request, "diretoria.html")


def expresidentes_view(request):
    return render(request, "ex-presidentes.html")

def eventosanteriores_view(request):
	context = {
		"eventos": Evento.objects.all().order_by('-created_at')
	}

	return render(request, "eventos-anteriores.html", context)