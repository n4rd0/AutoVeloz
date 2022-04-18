from django.db import models

largeText = 128
smallText = 64

class TiposDeGama(models.TextChoices):
     ALTA = 'Alta'
     MEDIA = 'Media'
     BAJA = 'Baja'
     
class TiposDeUsuarios(models.TextChoices):
     NEGOCIO = 'Negocio'
     PARTICULAR = 'Particular'
     
class TiposDeEstados(models.TextChoices):
     LIBRE = 'Libre'
     RESERVADO = 'Reservado'
     NO_DISPONIBLE = 'No disponible'

class Usuario(models.Model):
     dni = models.IntegerField(primary_key = True)
     nombre = models.CharField(max_length = largeText)
     apellidos = models.CharField(max_length = largeText)
     correo = models.CharField(max_length = largeText)
     contraseña = models.CharField(max_length = smallText)
     tipo = models.CharField(max_length = smallText, choices = TiposDeUsuarios.choices)
     
class Tarifas(models.Model):
     tipo = models.IntegerField()
     gama = models.CharField(max_length = smallText, choices = TiposDeGama.choices, default = 'No Disponible')
     
class Oficina(models.Model):
     ciudad = models.CharField(max_length = largeText)
     facturado = models.DecimalField(default = 0.0)
     
class Descuentos(models.Model):
     porcentaje = models.DecimalField()
     
class Extras(models.Model):
     extra = models.CharField(max_length = largeText)
     
class Coches(models.Model):
     id_oficina = models.ForeignKey(
          Oficinas
          on_delete = models.CASCADE
     )
     marca = models.CharField(max_length = largeText)
     modelo = models.CharField(max_length = largeText)
     gama = models.ForeignKey(
          TiposDeGama,
          on_delete = models.CASCADE
     )
     estado = models.CharField(max_length = smallText, )
     
class Opciones(models.Model):
     id_coche = models.ForeignKey(
           Coches
           on_delete = models.CASCADE
      )
      opcion = models.CharField(max_length = largeText)
      
class Reserva(models.Model):
     id_usuario = models.ForeignKey(
          Usuario
          on_delete = models.CASCADE
     )
     id_oficina_rec = models.ForeignKey(
          Oficina
          on_delete = models.CASCADE
     )
     id_oficina_dev = models.ForeignKey(
          Oficina
          on_delete = models.CASCADE
     )
     id_coche = models.ForeignKey(
          Coche
          on_delete = models.CASCADE
     )
     id_tarifa = models.ForeignKey(
          Tarifas
          on_delete = models.CASCADE
     )
     id_extra = models.ManytToManyField(Extras)
     id_opciones = models.ManyToManyField(Opciones)
     fecha_rec = models.DateField()
     fecha_dev = models.DateField()
     hora_rec = models.TimeField()
     hota_rec = models.TimeField()
     tarjeta_credito = models.IntegerField()
     
      
