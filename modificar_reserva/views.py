from django.shortcuts import render
from django.http import HttpResponse
from modificar_reserva.models import Reserva

# Create your views here.

def ver_reservas(request):
    reservas = Reserva.objects.filter(usuario__dni = request.user.username)
    return render(request, 'home/ver_reservas.html', {'reservas' : reservas})

def modificar_reserva(request, id_reserva):
    return HttpResponse('jajaxd')
