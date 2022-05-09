from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarifas, TiposDeTarifas
from coches_disponibles.models import Coches
from account.models import Usuario
#from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#@csrf_exempt
def tarifas_disponibles(request, id_coche):
    tipo_usuario = Usuario.objects.get(dni = request.user.username).user_type
    coche = Coches.objects.get(id = id_coche)
    tarifas = Tarifas.objects.filter(gama = coche.gama)

    # descuento al usuario tipo negocio del 30% salvo tarifa fin de semana
    if tipo_usuario == 'Negocio':
        for tarifa in tarifas:
            if tarifa.tipo != TiposDeTarifas.FIN_SEMANA:
                tarifa.precio = round(tarifa.precio * 0.7, 2)

    return render(request, 'home/tarifas.html', {'tarifas' : tarifas, 'id_coche' : id_coche})

