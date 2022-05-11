from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarifas, TiposDeTarifas
from coches_disponibles.models import Coches
from account.models import Usuario
from modificar_reserva.models import Extras
from . import forms
#from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#@csrf_exempt
def tarifas_disponibles(request, id_coche):
    tipo_usuario = Usuario.objects.get(dni = request.user.username).user_type
    coche = Coches.objects.get(id = id_coche)
    tarifas = Tarifas.objects.filter(gama = coche.gama)
    extras = Extras.objects.all()

    # descuento al usuario tipo negocio del 30% salvo tarifa fin de semana
    if tipo_usuario == 'Negocio':
        for tarifa in tarifas:
            if tarifa.tipo != TiposDeTarifas.FIN_SEMANA:
                tarifa.precio = round(tarifa.precio * 0.7, 2)

    return render(request, 'home-1/tarifas.html', {'tarifas' : tarifas, 'id_coche' : id_coche,'extras' : extras})

def ver_extras(request, id_coche, id_tarifa):
    coche = Coches.objects.get(id = id_coche)
    tarifa = Tarifas.objects.get(id = id_tarifa)

    if request.method == 'GET':
        form = forms.Extras()
        return render(request, 'home/extras.html', {'form' : form})
    else:
        post = request.POST
        print(post['extra'])
        form = forms.Extras()
        return render(request, 'home/extras.html', {'form' : form})




