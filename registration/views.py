from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .form import MyUserForm
import sys

def register(request):
    if request.method == 'POST':
        if MyUserForm(request.POST).is_valid:
            #return HttpResponseRedirect('/polls/')
            return HttpResponse('te registraste wey')
    else:
        form = MyUserForm()

    return render(request, 'registration/register.html', {'form' : form})

def jaja(request):
    return HttpResponse("jajaja")
