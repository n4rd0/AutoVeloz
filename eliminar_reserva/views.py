from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def eliminar_reserva(request):
    return render(request, 'home/eliminar_reserva.html')
    
