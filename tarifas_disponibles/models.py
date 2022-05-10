from django.db import models

class TiposDeGamas(models.TextChoices):
     ALTA = 'Alta'
     MEDIA = 'Media'
     BAJA = 'Baja'

class TiposDeTarifas(models.TextChoices):
     DIA_KM = 'Por día y por kilometraje'
     DIA_KM_ILIM = 'Por día y kilometraje ilimitado'
     FIN_SEMANA = 'Por fin de semana'
     SEMANAL = 'Por semana'
     LARGA_DURACION = 'Larga duración'

class Tarifas(models.Model):
     tipo = models.CharField(max_length = 64, choices = TiposDeTarifas.choices, default = 'No Disponible')
     gama = models.CharField(max_length = 64, choices = TiposDeGamas.choices, default = 'No Disponible')
     precio = models.FloatField()
     def __str__(self):
        return 'Tipo ' + self.tipo + ' Gama ' + self.gama + ' Precio ' + str(self.precio)
