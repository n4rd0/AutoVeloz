from django.db import models

class Oficina(models.Model):
     ciudad = models.CharField(max_length = 128)
     facturado = models.DecimalField(default = 0.0, max_digits=19, decimal_places=2)
     def __str__(self):
        return self.ciudad
