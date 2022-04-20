from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def recogida_entrega(request, id_coche, id_tarifa):
    if request.method == 'GET':
        form = forms.crearReserva()
        return render(request, 'home/recogida.html', {'form': form})
    
#render(request, 'recogida.html')
