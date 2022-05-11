from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from account.models import Usuario
from tarifas_disponibles.models import Tarifas
from coches_disponibles.models import Coches
from modificar_reserva.models import Reserva
import datetime
import re

def get_temporada(fecha_rec):
    month = fecha_rec.month
    if 1 <= month <= 5:
        return 1
    elif 6 <= month <= 9:
        return 1.2
    else:
        return 0.9

def deadlines(fecha, fecha_dev, semanas = 1):
    y=fecha.year
    if 1<=fecha.month<=5:
        deadline=datetime.datetime(y,6,1)
        if fecha_dev<=deadline:
            dif=fecha_dev-fecha
            return round(dif.days/semanas)
        dif=deadline-fecha
        return round(dif.days/semanas) + deadlines(deadline, fecha_dev)
    if 6<=fecha.month<=9:
        deadline=datetime.datetime(y,10,1)
        dif=deadline-fecha
        if fecha_dev<=deadline:
            dif=fecha_dev-fecha
            return round((dif.days*1.2)/semanas)
        dif=deadline-fecha
        return round((dif.days*1.2)/semanas) + deadlines(deadline, fecha_dev)
    else:
        deadline=datetime.datetime(y+1,1,1)
        if fecha_dev<=deadline:
            dif=fecha_dev-fecha
            return round((dif.days*0.9)/semanas)
        dif=deadline-fecha
        return round((dif.days*0.9)/semanas) + deadlines(deadline, fecha_dev)

# Create your views here.

def recogida_entrega(request, id_reserva):
    if request.method == 'GET':
        form = forms.crearReserva()
        return render(request, 'home/recogida.html', {'form': form})
    else:
        post = request.POST
        form = forms.crearReserva(post)
        res = Reserva.objects.get(id = id_reserva)
        tarifa = res.tarifa

        if form.is_valid():
            dat = form.cleaned_data
            rec = datetime.datetime.combine(dat['fecha_rec'], dat['hora_rec'])
            dev = datetime.datetime.combine(dat['fecha_dev'], dat['hora_dev'])
            delta=dev-rec
            # ver mensajes de error personalizados en forms.py

            if tarifa.tipo=='Por fin de semana' and (rec.weekday()<4 or dev.weekday()<4 or delta.days>3):
                dat['fecha_rec'] = ''
                form = forms.crearReserva(dat)
                return render(request, 'home/recogida.html', {'form' : form})
            elif dev <= rec or rec <= datetime.datetime.now():
                dat['fecha_rec'] = 'invalid'
                form = forms.crearReserva(dat)
                return render(request, 'home/recogida.html', {'form' : form})
            else:
                coche = res.coche
                # calcular el precio
                precio=0
                if tarifa.tipo=='Por fin de semana':
                    precio=tarifa.precio*get_temporada(rec)
                elif tarifa.tipo=='Larga duración':
                    precio=(delta.days//30+1)*tarifa.precio
                elif tarifa.tipo=='Por día y por kilometraje' or tarifa.tipo=='Por día y kilometraje ilimitado':
                    precio=deadlines(rec, dev)*tarifa.precio
                elif tarifa.tipo=='Por semana':
                    precio=max(get_temporada(dat['fecha_rec']),deadlines(rec, dev, 7))*tarifa.precio

                for ex in res.extra.all():
                    precio += ex.precio

                res.oficina_rec = coche.oficina
                res.fecha_rec = dat['fecha_rec']
                res.fecha_dev = dat['fecha_dev']
                res.hora_rec = dat['hora_rec']
                res.hora_dev = dat['hora_dev']
                res.precio = precio
                res.save()
                return HttpResponseRedirect(f'/recogida_entrega/pago/{res.id}')
        else:
            form = forms.crearReserva()
            return render(request, 'home/recogida.html', {'form' : form})

def pago(request, id_reserva):
    reserva = Reserva.objects.get(id = id_reserva)
    if request.method == 'GET':
        form = forms.Pago()
        return render(request, 'home/pago.html', {'form': form, 'precio': reserva.precio})
    else:
        post = request.POST
        form = forms.Pago(post)

        if form.is_valid():
            dat = form.cleaned_data
            # ver mensajes de error personalizados en forms.py
            if not re.match(r'^[0-9]{16}$', dat['tarjeta_credito']):
                dat['tarjeta_credito'] = ''
                form = forms.Pago(dat)
                return render(request, 'home/pago.html', {'form' : form, 'precio': reserva.precio})
            elif not re.match(r'^[0-9]{3}$', dat['cvv']):
                dat['cvv'] = ''
                form = forms.Pago(dat)
                return render(request, 'home/pago.html', {'form' : form, 'precio': reserva.precio})
            elif dat['fecha_caducidad'] < datetime.date.today():
                dat['fecha_caducidad'] = ''
                form = forms.Pago(dat)
                return render(request, 'home/pago.html', {'form' : form, 'precio': reserva.precio})
            else:
                oficina = reserva.oficina_rec
                oficina.facturado += reserva.precio
                oficina.save()
                reserva.pagada = True
                reserva.save()
                return HttpResponseRedirect('/reservas/')
        else:
            form = forms.Pago()
            return render(request, 'home/pago.html', {'form' : form, 'precio': reserva.precio})
