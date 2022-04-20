from account.models import Usuario, TiposDeUsuarios
from django.contrib.auth.models import User
from modificar_reserva.models import Reserva, Extras, Descuentos
from tarifas_disponibles.models import Tarifas, TiposDeTarifas
from coches_disponibles.models import Coches, Opciones, TiposDeGamas, TiposDeEstados
from recogida_entrega.models import Oficina

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
t1 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.BAJA, precio = 63, temporada = 1)
t2 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.BAJA, precio = 61, temporada = 2)
t3 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.BAJA, precio = 67, temporada = 3)
t4 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.MEDIA, precio = 68, temporada = 1)
t5 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.MEDIA, precio = 66, temporada = 2)
t6 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.MEDIA, precio = 72, temporada = 3)
t7 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.ALTA, precio = 78, temporada = 1)
t8 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.ALTA, precio = 76, temporada = 2)
t9 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM, gama=TiposDeGamas.ALTA, precio = 82, temporada = 3)
t10 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.BAJA, precio = 87, temporada = 1)
t11 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.BAJA, precio = 85, temporada = 2)
t12 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.BAJA, precio = 91, temporada = 3)
t13 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.MEDIA, precio = 92, temporada = 1)
t14 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.MEDIA, precio = 90, temporada = 2)
t15 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.MEDIA, precio = 96, temporada = 3)
t16 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.ALTA, precio = 102, temporada = 1)
t17 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.ALTA, precio = 100, temporada = 2)
t18 = Tarifas.objects.create(tipo=TiposDeTarifas.DIA_KM_ILIM, gama=TiposDeGamas.ALTA, precio = 106, temporada = 3)
t19 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.BAJA, precio = 84, temporada = 1)
t20 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.BAJA, precio = 82, temporada = 2)
t21 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.BAJA, precio = 88, temporada = 3)
t22 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.MEDIA, precio = 89, temporada = 1)
t23 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.MEDIA, precio = 87, temporada = 2)
t24 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.MEDIA, precio = 93, temporada = 3)
t25 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.ALTA, precio = 99, temporada = 1)
t26 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.ALTA, precio = 97, temporada = 2)
t27 = Tarifas.objects.create(tipo=TiposDeTarifas.FIN_SEMANA, gama=TiposDeGamas.ALTA, precio = 103, temporada = 3)
t28 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.BAJA, precio = 73, temporada = 1)
t29 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.BAJA, precio = 71, temporada = 2)
t30 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.BAJA, precio = 77, temporada = 3)
t31 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.MEDIA, precio = 78, temporada = 1)
t32 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.MEDIA, precio = 76, temporada = 2)
t33 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.MEDIA, precio = 82, temporada = 3)
t34 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.ALTA, precio = 88, temporada = 1)
t35 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.ALTA, precio = 86, temporada = 2)
t36 = Tarifas.objects.create(tipo=TiposDeTarifas.SEMANAL, gama=TiposDeGamas.ALTA, precio = 92, temporada = 3)
t37 = Tarifas.objects.create(tipo=TiposDeTarifas.LARGA_DURACION, gama=TiposDeGamas.BAJA, precio = 568, temporada = 0)
t38 = Tarifas.objects.create(tipo=TiposDeTarifas.LARGA_DURACION, gama=TiposDeGamas.MEDIA, precio = 573, temporada = 0)
t39 = Tarifas.objects.create(tipo=TiposDeTarifas.LARGA_DURACION, gama=TiposDeGamas.ALTA, precio = 583, temporada = 0)

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
Coches(id_oficina=of1, marca="Mercedes", modelo="GLC 43", gama=TiposDeGamas.ALTA, estado=TiposDeEstados.NO_DISPONIBLE).save()

c1 = Coches(id_oficina=of2, marca="Seat", modelo="Ibiza", gama=TiposDeGamas.BAJA, estado=TiposDeEstados.LIBRE)
c2 = Coches(id_oficina=of2, marca="BMW", modelo="X5", gama=TiposDeGamas.ALTA, estado=TiposDeEstados.LIBRE)
c1.save()
c2.save()


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
