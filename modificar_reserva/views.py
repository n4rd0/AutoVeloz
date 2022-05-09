from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from modificar_reserva.models import Reserva
from recogida_entrega.forms import crearReserva
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from account.models import Usuario

# Create your views here.

@login_required
def ver_reservas(request):
    reservas_list = Reserva.objects.filter(usuario__dni = request.user.username)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(reservas_list, 3)
    try:
        reservas = paginator.page(page)
    except PageNotAnInteger:
        reservas = paginator.page(1)
    except EmptyPage:
        reservas = paginator.page(paginator.num_pages)
    
    return render(request, 'home/ver_reservas.html', {'reservas' : reservas})

def modificar_reserva(request, id_reserva):
    reserva = Reserva.objects.get(id = id_reserva)
    tipo_usuario = Usuario.objects.get(dni = request.user.username).user_type
    if request.method == 'GET':
        form = crearReserva(instance = reserva)
        penalizacion = penalizacion_reserva(reserva.fecha_rec,tipo_usuario)
        return render(request, 'home-1/modificar_reserva.html', {'form' : form,'penalizacion' : penalizacion})
    else:
        form = crearReserva(request.POST, instance = reserva)
        form.save()
        return HttpResponseRedirect('/reservas/')

def penalizacion_reserva(fecha_rec,tipo_usuario):
    if tipo_usuario == 'Particular':
        if fecha_rec-datetime.date.today() < datetime.timedelta(days=5):
            return 25

        elif fecha_rec-datetime.date.today() <= datetime.timedelta(days=1):
            return 50

    else:
        if fecha_rec-datetime.date.today() <= datetime.timedelta(days=1):
            return 50

    return 0
