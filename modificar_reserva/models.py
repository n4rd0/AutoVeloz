from django.db import models
from account.models import Usuario
from recogida_entrega.models import Oficina
from coches_disponibles.models import Coches, Opciones
from tarifas_disponibles.models import Tarifas

class Extras(models.Model):
     extra = models.CharField(max_length = 128)
     precio = models.IntegerField()
     def __str__(self):
        return self.extra + " " + str(precio)

class Reserva(models.Model):
     usuario = models.ForeignKey(
          Usuario,
          on_delete = models.CASCADE
     )
     oficina_rec = models.ForeignKey(
          Oficina,
          on_delete = models.CASCADE,
          related_name = 'lugar_recogida'
     )
     oficina_dev = models.ForeignKey(
          Oficina,
          on_delete = models.CASCADE,
          related_name = 'lugar_devolucion'
     )
     coche = models.ForeignKey(
          Coches,
          on_delete = models.CASCADE
     )
     tarifa = models.ForeignKey(
          Tarifas,
          on_delete = models.CASCADE
     )
     extra = models.ManyToManyField(Extras)
     opciones = models.ManyToManyField(Opciones)
     fecha_rec = models.DateField()
     fecha_dev = models.DateField()
     hora_rec = models.TimeField()
     hora_dev = models.TimeField()
     tarjeta_credito = models.CharField(max_length=16)
     precio = models.DecimalField(max_digits=19, decimal_places=2)
     pagada = models.BooleanField(default = False)

     def __str__(self):
        return f'Coche {self.coche}, Oficina recogida {self.oficina_rec}, Oficina devolución {self.oficina_dev}'

class Descuentos(models.Model):
     porcentaje = models.DecimalField(max_digits=3, decimal_places=2)
     codigo = models.CharField(max_length = 5, default = '')
     def __str__(self):
        return str(self.porcentaje) + " " + self.codigo
