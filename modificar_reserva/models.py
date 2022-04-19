from django.db import models
from account.models import Usuario
from recogida_entrega.models import Oficina
from coches_disponibles.models import Coches, Opciones
from tarifas_disponibles.models import Tarifas

class Extras(models.Model):
     extra = models.CharField(max_length = 128)
     def __str__(self):
        return self.extra

class Reserva(models.Model):
     id_usuario = models.ForeignKey(
          Usuario,
          on_delete = models.CASCADE
     )
     id_oficina_rec = models.ForeignKey(
          Oficina,
          on_delete = models.CASCADE,
          related_name = 'lugar_recogida'
     )
     id_oficina_dev = models.ForeignKey(
          Oficina,
          on_delete = models.CASCADE,
          related_name = 'lugar_devolucion'
     )
     id_coche = models.ForeignKey(
          Coches,
          on_delete = models.CASCADE
     )
     id_tarifa = models.ForeignKey(
          Tarifas,
          on_delete = models.CASCADE
     )
     id_extra = models.ManyToManyField(Extras)
     id_opciones = models.ManyToManyField(Opciones)
     fecha_rec = models.DateField()
     fecha_dev = models.DateField()
     hora_rec = models.TimeField()
     hora_dev = models.TimeField()
     tarjeta_credito = models.IntegerField()
     def __str__(self):
        return 'Coche ' + self.id_coche
        
class Descuentos(models.Model):
     porcentaje = models.DecimalField(max_digits=3, decimal_places=2)
     def __str__(self):
        return self.porcentaje
