from django.shortcuts import render
from django.http import HttpResponse
from .models import Coches, TiposDeEstados
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def coches_disponibles(request):
    coches_list = Coches.objects.filter(estado = TiposDeEstados.LIBRE)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(coches_list, 3)
    try:
        coches = paginator.page(page)
    except PageNotAnInteger:
        coches = paginator.page(1)
    except EmptyPage:
        coches = paginator.page(paginator.num_pages)
        
    return render(request, 'home/cochesdisponibles.html',{'coches': coches})
