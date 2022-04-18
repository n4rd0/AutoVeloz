from account.models import Usuario, TiposDeUsuarios
from modificar_reserva.models import Reserva, Extras, Descuentos
from tarifas_disponibles.models import Tarifas
from coches_disponibles.models import Coches, Opciones, TiposDeGamas, TiposDeEstados
from recogida_entrega.models import Oficina

"""
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
"""

#/////////////////USUARIO/////////////////

#Generar dato
user = Usuario(dni="83140123X", nombre="Nombre", apellidos="Apellidos", correo="correofalso@yopmail.com", contraseña="Pass_word42", tipo=TiposDeUsuarios.PARTICULAR)
user.save()


#/////////////////TARIFAS/////////////////

#Generar dato
t1 = Tarifas(tipo=1, gama=TiposDeGamas.MEDIA)
t1.save()


#/////////////////OFICINA/////////////////

#Generar dato sin facturado
of1 = Oficina(ciudad="Nombre ciudad")
of1.save()

#Generar dato con facturado dado
of2 = Oficina(ciudad="Nombre ciudad", facturado=262.1)
of2.save()

#/////////////////DESCUENTOS/////////////////

#Generar dato
Descuentos(porcentaje = 0.15).save()


#/////////////////EXTRAS/////////////////

#Generar dato
ex1 = Extras(extra="Nombre del extra")
ex1.save()


#/////////////////COCHES/////////////////

#Generar dato
Coches(id_oficina=of1, marca="Marca del coche", modelo="Modelo del coche", gama=TiposDeGamas.ALTA, estado=TiposDeEstados.NO_DISPONIBLE).save()

c1 = Coches(id_oficina=of2, marca="Marca del coche 2", modelo="Modelo del coche 2", gama=TiposDeGamas.BAJA, estado=TiposDeEstados.LIBRE)
c1.save()


#/////////////////OPCIONES/////////////////

#Generar dato
opc1 = Opciones(id_coche=c1, opcion="Opcion disponible para el coche")
opc1.save()


#/////////////////RESERVA/////////////////

#Generar dato
r1 = Reserva(id_usuario=user, id_oficina_rec=of1, id_oficina_dev=of1, id_coche=c1, id_tarifa=t1, fecha_rec='2020-05-01', fecha_dev='2020-05-26', hora_rec='15:00:00', hora_dev='9:30:00', tarjeta_credito=1234567890123456)
r1.save()

#Añadir extra
r1.id_extra.add(ex1)

#Repetir no añade duplicados
r1.id_extra.add(ex1)

#Añadir opciones
r1.id_opciones.add(opc1)

#Repetir no añade duplicados
r1.id_opciones.add(opc1)
