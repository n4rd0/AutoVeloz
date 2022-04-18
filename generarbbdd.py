from account.models import Usuario, TiposDeUsuarios
from django.contrib.auth.models import User
from modificar_reserva.models import Reserva, Extras, Descuentos
from tarifas_disponibles.models import Tarifas
from coches_disponibles.models import Coches, Opciones, TiposDeGamas, TiposDeEstados
from recogida_entrega.models import Oficina

"""
Para tener las tablas actualizadas:
python3 manage.py makemigrations
python3 manage.py migrate

Para ejecutar este script:

Linux al menos:
    echo 'import generarbbdd' | python3 manage.py shell

Windows o Linux:
    python3 manage.py shell
    Dentro del shell hacer
    import generarbbdd

En el shell normal de Python no sirve, usar lo anterior
"""

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

Usuario.objects.all().delete()
User.objects.all().delete()
#Generar dato
user_data = {
        'username' : '83140123X',
        'first_name' : 'Nombre',
        'last_name' : 'Apellidos',
        'email' : 'correofalso@yopmail.com',
        'password' : 'Pass_word42',
    }
# usuario de Django necesario para que lo reconozca en login
auth_user = User.objects.create_user(**user_data)

user_data['dni'] = user_data.pop('username')
user_data['user_type'] = TiposDeUsuarios.PARTICULAR
# usuario nuestro
user = Usuario(**user_data, auth_user = auth_user)
user.save()


#/////////////////TARIFAS/////////////////

Tarifas.objects.all().delete()

#Generar dato
t1 = Tarifas(tipo=1, gama=TiposDeGamas.MEDIA)
t1.save()


#/////////////////OFICINA/////////////////

Oficina.objects.all().delete()

#Generar dato sin facturado
of1 = Oficina(ciudad="Nombre ciudad")
of1.save()

#Generar dato con facturado dado
of2 = Oficina(ciudad="Nombre ciudad", facturado=262.1)
of2.save()

#/////////////////DESCUENTOS/////////////////

Descuentos.objects.all().delete()

#Generar dato
Descuentos(porcentaje = 0.15).save()


#/////////////////EXTRAS/////////////////

Extras.objects.all().delete()

#Generar dato
ex1 = Extras(extra="Nombre del extra")
ex1.save()


#/////////////////COCHES/////////////////

Coches.objects.all().delete()

#Generar dato
Coches(id_oficina=of1, marca="Marca del coche", modelo="Modelo del coche", gama=TiposDeGamas.ALTA, estado=TiposDeEstados.NO_DISPONIBLE).save()

c1 = Coches(id_oficina=of2, marca="Marca del coche 2", modelo="Modelo del coche 2", gama=TiposDeGamas.BAJA, estado=TiposDeEstados.LIBRE)
c1.save()


#/////////////////OPCIONES/////////////////

Opciones.objects.all().delete()

#Generar dato
opc1 = Opciones(id_coche=c1, opcion="Opcion disponible para el coche")
opc1.save()


#/////////////////RESERVA/////////////////

Reserva.objects.all().delete()

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
