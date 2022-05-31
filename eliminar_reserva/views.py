from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from modificar_reserva.models import Reserva

# Create your views here.

def ver_reservas(request):
    reservas = Reserva.objects.filter(usuario__dni = request.user.username)
    return render(request, 'home/ver_reservas.html', {'reservas' : reservas})

def eliminar_reserva(request, id_reserva):
    reserva = Reserva.objects.get(id = id_reserva)
    reserva.delete()
    return HttpResponseRedirect('/reservas/')
    
