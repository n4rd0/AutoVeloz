from django.shortcuts import render
from django.http import HttpResponse
from modificar_reserva.models import Reserva

# Create your views here.

def modificar_reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'home/modificar_reserva.html', {'reservas' : reservas})
    
