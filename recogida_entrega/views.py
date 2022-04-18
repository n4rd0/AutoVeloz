from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def recogida_entrega(request):
    return render(request, 'home/recogida.html')
    
#render(request, 'recogida.html')