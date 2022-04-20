from django import forms
from .models import TiposDeUsuarios

largeText = 128
smallText = 64

class MyUserForm(forms.Form):
    username = forms.CharField(label = 'DNI', max_length = 9, error_messages = {'required' : 'DNI no válido'})
    first_name = forms.CharField(label = 'Nombre', max_length = largeText)
    last_name = forms.CharField(label = 'Apellidos', max_length = largeText)
    email = forms.CharField(label = 'Correo', max_length = largeText, error_messages = {'required' : 'Formato incorrecto'})
    password = forms.CharField(
            widget = forms.PasswordInput, 
            label = 'Contraseña', 
            max_length = smallText, 
            error_messages = {'required' : 'Las contraseñas no coinciden'}
        )
    password_re = forms.CharField(
            widget = forms.PasswordInput, 
            label = 'Repetir contraseña', 
            max_length = smallText, 
            error_messages = {'required' : 'Las contraseñas no coinciden'}
        )
    user_type = forms.ChoiceField(label = 'Tipo usuario', choices = TiposDeUsuarios.choices)
