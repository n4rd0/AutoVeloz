from django.db import models

largeText = 128
smallText = 64
     
class TiposDeUsuarios(models.TextChoices):
     NEGOCIO = 'Negocio'
     PARTICULAR = 'Particular'

class Usuario(models.Model):
     dni = models.CharField(max_length = smallText, primary_key = True)
     nombre = models.CharField(max_length = largeText)
     apellidos = models.CharField(max_length = largeText)
     correo = models.CharField(max_length = largeText)
     contraseña = models.CharField(max_length = smallText)
     tipo = models.CharField(max_length = smallText, choices = TiposDeUsuarios.choices)
     def __str__(self):
        return self.dni
