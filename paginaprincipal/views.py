from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render(request, 'home/welcome.html')
    
#render(request, 'recogida.html')