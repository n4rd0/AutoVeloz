from django.db import models
from django.contrib.auth.models import User

largeText = 128
smallText = 64
     
class TiposDeUsuarios(models.TextChoices):
     NEGOCIO = 'Negocio'
     PARTICULAR = 'Particular'

class Usuario(models.Model):
     dni = models.CharField(max_length = smallText, primary_key = True)
     first_name = models.CharField(max_length = largeText)
     last_name = models.CharField(max_length = largeText)
     email = models.CharField(max_length = largeText)
     password = models.CharField(max_length = smallText)
     user_type = models.CharField(max_length = smallText, choices = TiposDeUsuarios.choices)
     auth_user = models.OneToOneField(User, on_delete = models.CASCADE)
     def __str__(self):
        return self.dni
