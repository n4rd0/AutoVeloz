from django.db import models
from recogida_entrega.models import Oficina

largeText = 128
smallText = 64

class TiposDeGamas(models.TextChoices):
     ALTA = 'Alta'
     MEDIA = 'Media'
     BAJA = 'Baja'
     
class TiposDeEstados(models.TextChoices):
     LIBRE = 'Libre'
     RESERVADO = 'Reservado'
     NO_DISPONIBLE = 'No disponible'
     
class Coches(models.Model):
     oficina = models.ForeignKey(
          Oficina,
          on_delete=models.CASCADE
     )
     marca = models.CharField(max_length = largeText)
     modelo = models.CharField(max_length = largeText)
     gama = models.CharField(max_length = smallText, choices = TiposDeGamas.choices)
     estado = models.CharField(max_length = smallText, choices = TiposDeEstados.choices)
     url = models.CharField(max_length = largeText, default="")

     def __str__(self):
        return self.marca + ' ' + self.modelo
     
class TiposDeOpciones(models.TextChoices):
    AUTOMATICO = 'Cambio automático'
    PUERTAS_5 = '5 puertas'
    TECHO_SOLAR = 'Techo solar'

class Opciones(models.Model):
     coche = models.ForeignKey(
           Coches,
           on_delete = models.CASCADE
     )
     opcion = models.CharField(max_length = largeText, choices = TiposDeOpciones.choices)
     def __str__(self):
        return str(self.coche) + ' opcion: ' + self.opcion
