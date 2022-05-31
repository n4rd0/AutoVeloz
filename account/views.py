import polls.models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .form import MyUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from .models import Usuario

def register(request):
    if request.method == 'POST':
        post = request.POST
        my_user = MyUserForm(request.POST)
        if not my_user.is_valid():
            form = MyUserForm()
        else:
            ok_format = True

            # se pone dni como username en el User de Django
            if Usuario.objects.filter(dni = my_user.cleaned_data['username']) \
                    or not re.match(r'^[A-Z0-9]\d{7}[A-Z]$', post['username']):
                ok_format = False
                my_user.cleaned_data['username'] = ''
                messages.error(request, "DNI no válido")

            if post['password'] != post['password_re']:
                ok_format = False
                my_user.cleaned_data['password'] = ''
                my_user.cleaned_data['password_re'] = ''
                messages.error(request, "Las contraseñas no coinciden")

            if not re.match(r'^[a-zA-Z0-9_\.]+@[a-zA-Z0-9]+\.[a-zA-Z]+$', post['email']):
                ok_format = False
                my_user.cleaned_data['email'] = ''
                messages.error(request, "Correo no válido")

            if not ok_format:
                my_user = MyUserForm(my_user.cleaned_data)
                return render(request, 'registration/register.html', {'form' : my_user})

            user_type = my_user.cleaned_data.pop('user_type')
            my_user.cleaned_data.pop('password_re')
            auth_user = User.objects.create_user(**my_user.cleaned_data)

            dni = my_user.cleaned_data.pop('username')
            u = Usuario.objects.create(
                    **my_user.cleaned_data, 
                    dni = dni,
                    user_type = user_type, 
                    auth_user = auth_user,
                )
            messages.success(request, "Registrado Correctamente")
            return HttpResponseRedirect('/account/login/')
    else:
        form = MyUserForm()

    return render(request, 'registration/register.html', {'form' : form})
