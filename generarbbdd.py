from account.models import Usuario, TiposDeUsuarios
from django.contrib.auth.models import User
from modificar_reserva.models import Reserva, Extras, Descuentos
from tarifas_disponibles.models import Tarifas, TiposDeTarifas
from coches_disponibles.models import Coches, Opciones, TiposDeGamas, TiposDeEstados
from recogida_entrega.models import Oficina
import datetime

"""
Para tener las tablas actualizadas:
python3 manage.py makemigrations <lista de directorios con modelos, excluir polls/__pycache__/templates/gpi>
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
     
class TiposDeTarifas(models.TextChoices):
     DIA_KM = 'Por día y por kilometraje'
     DIA_KM_ILIM = 'Por día y kilometraje ilimitado'
     FIN_SEMANA = 'Por fin de semana'
     SEMANAL = 'Por semana'
     LARGA_DURACION = 'Larga duración'

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
        'password' : 'pass',
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
t1 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.BAJA, precio = 63)
t2 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.MEDIA, precio = 68)
t3 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.ALTA, precio = 78)
t4 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.BAJA, precio = 87)
t5 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.MEDIA, precio = 92)
t6 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.ALTA, precio = 102)
t7 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.BAJA, precio = 84)
t8 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.MEDIA, precio = 89)
t9 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.ALTA, precio = 99)
t10 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.BAJA, precio = 73)
t11 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.MEDIA, precio = 78)
t12 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.ALTA, precio = 88)
t13 = Tarifas.objects.create(tipo=TiposDeTarifas.LARGA_DURACION, gama=TiposDeGamas.BAJA, precio = 568)
t14 = Tarifas.objects.create(tipo=TiposDeTarifas.LARGA_DURACION, gama=TiposDeGamas.MEDIA, precio = 573)
t15 = Tarifas.objects.create(tipo=TiposDeTarifas.LARGA_DURACION, gama=TiposDeGamas.ALTA, precio = 583)

#/////////////////OFICINA/////////////////

Oficina.objects.all().delete()

#Generar dato sin facturado
of1 = Oficina(ciudad="Madrid", facturado = 299.12)
of1.save()

#Generar dato con facturado dado
of2 = Oficina(ciudad="Barcelona", facturado=262.1)
of2.save()

#/////////////////DESCUENTOS/////////////////

Descuentos.objects.all().delete()

#Generar dato
Descuentos(porcentaje = 0.15).save()


#/////////////////EXTRAS/////////////////

Extras.objects.all().delete()

#Generar dato
ex1 = Extras(extra="Wi-Fi",precio=55)
ex2 = Extras(extra="GPS",precio=60)
ex3 = Extras(extra="Silla",precio=150)
ex4 = Extras(extra="Cadenas",precio=40)
ex1.save()
ex2.save()
ex3.save()
ex4.save()


#/////////////////COCHES/////////////////

Coches.objects.all().delete()

#Generar dato
Coches(oficina=of1, marca="Mercedes", modelo="GLC 43", gama=TiposDeGamas.ALTA, estado=TiposDeEstados.LIBRE, url = "https://seetech-corp.com/wp-content/uploads/2016/10/Car-PNG-File.png").save()

c1 = Coches(oficina=of2, marca="Seat", modelo="Ibiza", gama=TiposDeGamas.BAJA, estado=TiposDeEstados.LIBRE, url = "https://www.alquiber.es/wp-content/uploads/2020/11/seat-ibiza.png")
c2 = Coches(oficina=of2, marca="BMW", modelo="X5", gama=TiposDeGamas.ALTA, estado=TiposDeEstados.LIBRE, url = "https://cdn.wheel-size.com/automobile/body/bmw-x5-m-2020-2021-1586281570.61.png")
c3 = Coches(oficina=of1, marca="FIAT", modelo="Multipla", gama=TiposDeGamas.ALTA, estado=TiposDeEstados.LIBRE, url = "https://ik.imagekit.io/2ero5nzbxo2/FILES/generations/QF4sm55jOryvQbeC2NN9SXiczkDKfjlLZBmj8Ywm.png?ik-sdk-version=php-2.0.0")

c1.save()
c2.save()
c3.save()


#/////////////////OPCIONES/////////////////

Opciones.objects.all().delete()

#Generar dato
opc1 = Opciones(coche=c1, opcion="Opcion disponible para el coche")
opc1.save()


#/////////////////RESERVA/////////////////

Reserva.objects.all().delete()

#Generar dato
now = datetime.datetime.now()
r1 = Reserva.objects.create(
    usuario=user, 
    oficina_rec=of1, 
    oficina_dev=of1, 
    coche=c1, 
    tarifa=t1,
    precio= 123.0,
    fecha_rec= now.date(),
    fecha_dev= (now + datetime.timedelta(days = 3)),
    hora_rec= now.time(),
    hora_dev= (now + datetime.timedelta(hours = 6)),
    tarjeta_credito = 1234567890123456,
)

#Añadir extra
r1.extra.add(ex1)
r1.extra.add(ex2)
r1.extra.add(ex3)
r1.extra.add(ex4)


#Repetir no añade duplicados
r1.extra.add(ex1)

#Añadir opciones
r1.opciones.add(opc1)

#Repetir no añade duplicados
r1.opciones.add(opc1)
