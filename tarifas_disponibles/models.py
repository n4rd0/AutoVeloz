from django.db import models

class TiposDeGamas(models.TextChoices):
     ALTA = 'Alta'
     MEDIA = 'Media'
     BAJA = 'Baja'

class Tarifas(models.Model):
     tipo = models.IntegerField()
     gama = models.CharField(max_length = 64, choices = TiposDeGamas.choices, default = 'No Disponible')
     def __str__(self):
        return 'Tipo ' + self.tipo + ' Gama ' +self.gama 
