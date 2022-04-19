from django.shortcuts import render
from django.http import HttpResponse
from .models import Coches

# Create your views here.

def coches_disponibles(request):
    coches = Coches.objects.all()
    return render(request, 'home/cochesdisponibles.html',{'coches': coches})
    
#render(request, 'recogida.html')