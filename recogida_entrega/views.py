from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from account.models import Usuario
from tarifas_disponibles.models import Tarifas
from coches_disponibles.models import Coches
from modificar_reserva.models import Reserva
import datetime

def get_temporada(fecha_rec):
    month = fecha_rec.month
    if 1 <= month <= 5:
        return 1
    elif 6 <= month <= 9:
        return 2
    else:
        return 3

# Create your views here.

def recogida_entrega(request, id_coche, id_tarifa):
    if request.method == 'GET':
        form = forms.crearReserva()
        return render(request, 'home/recogida.html', {'form': form})
    else:
        post = request.POST
        form = forms.crearReserva(post)
        tarifa = Tarifas.objects.get(id = id_tarifa)

        if form.is_valid():
            dat = form.cleaned_data
            rec = datetime.datetime.combine(dat['fecha_rec'], dat['hora_rec'])
            dev = datetime.datetime.combine(dat['fecha_dev'], dat['hora_dev'])
            # ver mensajes de error personalizados en forms.py
            if get_temporada(dat['fecha_rec']) != tarifa.temporada:
                dat['fecha_rec'] = ''
                form = forms.crearReserva(dat)
                return render(request, 'home/recogida.html', {'form' : form})
            elif dev <= rec:
                dat['fecha_rec'] = 'invalid'
                form = forms.crearReserva(dat)
                return render(request, 'home/recogida.html', {'form' : form})
            else:
                coche = Coches.objects.get(id = id_coche)
                Reserva.objects.create(
                        **dat, 
                        coche = coche,
                        oficina_rec = coche.oficina,
                        tarifa = Tarifas.objects.get(id = id_tarifa),
                        usuario = Usuario.objects.get(dni = request.user.username),
                    )
                return HttpResponseRedirect('/reservas/')
        else:
            form = forms.crearReserva()
            return render(request, 'home/recogida.html', {'form' : form})
