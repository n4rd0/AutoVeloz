from django.db import models

largeText = 128
smallText = 64

class TiposDeGamas(models.TextChoices):
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
     dni = models.CharField(max_length = smallText, primary_key = True)
     nombre = models.CharField(max_length = largeText)
     apellidos = models.CharField(max_length = largeText)
     correo = models.CharField(max_length = largeText)
     contraseña = models.CharField(max_length = smallText)
     tipo = models.CharField(max_length = smallText, choices = TiposDeUsuarios.choices)
     def __str__(self):
        return self.dni
     
class Tarifas(models.Model):
     tipo = models.IntegerField()
     gama = models.CharField(max_length = smallText, choices = TiposDeGamas.choices, default = 'No Disponible')
     def __str__(self):
        return 'Tipo ' + self.tipo + ' Gama ' +self.gama 
     
class Oficina(models.Model):
     ciudad = models.CharField(max_length = largeText)
     facturado = models.DecimalField(default = 0.0, max_digits=19, decimal_places=2)
     def __str__(self):
        return self.ciudad
     
class Descuentos(models.Model):
     porcentaje = models.DecimalField(max_digits=3, decimal_places=2)
     def __str__(self):
        return self.porcentaje
     
class Extras(models.Model):
     extra = models.CharField(max_length = largeText)
     def __str__(self):
        return self.extra
     
class Coches(models.Model):
     id_oficina = models.ForeignKey(
          Oficina,
          on_delete=models.CASCADE
     )
     marca = models.CharField(max_length = largeText)
     modelo = models.CharField(max_length = largeText)
     gama = models.CharField(max_length = smallText, choices = TiposDeGamas.choices)
     estado = models.CharField(max_length = smallText, choices = TiposDeEstados.choices)
     def __str__(self):
        return self.marca + ' ' + self.modelo
     
class Opciones(models.Model):
     id_coche = models.ForeignKey(
           Coches,
           on_delete = models.CASCADE
     )
     opcion = models.CharField(max_length = largeText)
     def __str__(self):
        return self.id_coche + ' opcion: ' + self.opcion
      
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
     
      
