from django.shortcuts import render
from django.http import HttpResponse
from .models import Coches, TiposDeEstados

# Create your views here.

def coches_disponibles(request):
    coches = Coches.objects.filter(estado = TiposDeEstados.LIBRE)
    return render(request, 'home/cochesdisponibles.html',{'coches': coches})
    
