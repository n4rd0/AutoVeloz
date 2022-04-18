from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def coches_disponibles(request):
    return render(request, 'home/cochesdisponibles.html')
    
#render(request, 'recogida.html')