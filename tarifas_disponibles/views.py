from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarifas, TiposDeTarifas
from account.models import Usuario
#from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#@csrf_exempt
def tarifas_disponibles(request, gama, temporada):
    tipo_usuario = Usuario.objects.get(dni = request.user.username).user_type
    tarifas = Tarifas.objects.filter(gama = gama, temporada = temporada)

    # descuento al usuario tipo negocio del 30% salvo tarifa fin de semana
    if tipo_usuario == 'Negocio':
        for tarifa in tarifas:
            if tarifa['tipo'] != TiposDeTarifas.FIN_SEMANA:
                tarifa['precio'] *= 0.7

    print(tipo_usuario)
    print(tarifas)
    
    return render(request, 'home/tarifas.html', {'tarifas' : tarifas})
