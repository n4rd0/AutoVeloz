from django.shortcuts import render
from django.http import HttpResponse
from modificar_reserva.models import Reserva
from recogida_entrega.forms import crearReserva

# Create your views here.

def ver_reservas(request):
    reservas = Reserva.objects.filter(usuario__dni = request.user.username)
    return render(request, 'home/ver_reservas.html', {'reservas' : reservas})

def modificar_reserva(request, id_reserva):
    reserva = Reserva.objects.get(id = id_reserva)
    print(reserva)
    form = crearReserva(instance = reserva, initial = {'fecha_rec' : reserva.fecha_rec})
    print(form)
    print(form.fields)

    if request.method == 'GET':
        return render(request, 'home/modificar_reserva.html', {'form' : form})

    print(form.fields)
    return HttpResponse('jajaxd')
