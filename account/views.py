from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .form import MyUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    post = request.POST
    if request.method == 'POST':
        my_user = MyUserForm(request.POST)
        if my_user.is_valid():
            User.objects.create_user(
                    username = post['DNI'], 
                    email = post['email'], 
                    password = post['password'], 
                    first_name = post['name'],
                )
            #return HttpResponseRedirect('/polls/')
            return HttpResponse('te registraste wey')
    else:
        form = MyUserForm()

    return render(request, 'registration/register.html', {'form' : form})

def jaja(request):
    return HttpResponse("jajaja")
