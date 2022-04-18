from django import forms
from .models import TiposDeUsuarios

largeText = 128
smallText = 64

class MyUserForm(forms.Form):
    username = forms.CharField(label = 'DNI', max_length = 9)
    first_name = forms.CharField(label = 'Nombre', max_length = largeText)
    last_name = forms.CharField(label = 'Apellidos', max_length = largeText)
    email = forms.CharField(label = 'Correo', max_length = largeText)
    password = forms.CharField(label = 'Contraseña', max_length = smallText)
    password_re = forms.CharField(label = 'Repetir contraseña', max_length = smallText)
    user_type = forms.ChoiceField(label = 'Tipo usuario', choices = TiposDeUsuarios.choices)
