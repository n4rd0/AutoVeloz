from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from modificar_reserva.models import Reserva
from recogida_entrega.forms import crearReserva
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def ver_reservas(request):
    reservas_list = Reserva.objects.filter(usuario__dni = request.user.username, pagada = True)
    
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

    if request.method == 'GET':
        form = crearReserva(instance = reserva)
        return render(request, 'home/modificar_reserva.html', {'form' : form})
    else:
        form = crearReserva(request.POST, instance = reserva)
        form.save()
        return HttpResponseRedirect('/reservas/')
