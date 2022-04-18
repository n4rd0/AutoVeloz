Instalar Django (tras instalar python):
pip install django
No hace falta nada mas

El proyecto se divide en "apps", que son como partes independientes. Se puede crear app desde el directorio principal haciendo
python3 manage.py startapp nombre
Se tiene que añadir tambien a la variable INSTALLED_APPS de gpi/settings.py

Ficheros principales de app:

- models.py: incluye modelos para la base de datos. Cuando se tengan, django los introduce automaticamente a la base de datos con
python3 manage.py migrate
No hay que hacer nada especial para usar la base de datos (no es mysql)
Se puede interactuar con la base de datos gracias a la api que ofrece django automaticamente. Se pueden ejecutar scripts
(ver algunos ejemplos de queries en polls/create_questions.py) o hacer queries de forma interactiva con
python3 manage.py shell
y haciendo los imports necesarios de modelos

- urls.py: incluye "endpoints" (direcciones url que se van a usar para las distintas paginas). Especificar view
(ver siguiente punto). Son direcciones locales, a partir de la direccion de la app. Especificar en gpi/urls.py (fichero de urls general)

- views.py: incluye los metodos a los que se va a llamar cuando se acceda a los distintos endpoints. Al final se debe devolver
un HTTPResponse (hay muchas formas). La practica comun es indicar que pagina quieres mostrar. Se indica un template .html y un contexto.
El contexto es un conjunto de variables que se van a poder usar en el template para facilitar el trabajo.

Templates:
Django permite usar una sintaxis especial sobre ficheros html para usar ifs, fors, etc y variables del contexto indicado en la view
(ver ejemplos). Otra practica comun es extender templates a partir de otro template base (ver ejemplos base.html, login.html...)
Se pueden introducir templates en nombreapp/templates/nombreapp/ o templates/, o especificar otros directorios en 'DIRS' de la variable TEMPLATES
en gpi/settings.py

Ejecutar proyecto:
python3 manage.py runserver


Un mensaje indicara la pagina donde se puede acceder. No hace falta correr de nuevo el servidor tras cada cambio, solo guardar fichero con cambios
y Django lo detecta. Unica excepcion crear una app nueva, ahi hace falta correr de nuevo.

Id a esa página desde el navegador, suele ser 127.0.0.1:8000
Y añadid /home al final
se suele acortar a localhost:8000/home

La app polls no tiene que ver con nuestra practica, es un ejemplo que he hecho siguiendo el tutorial oficial para acostumbrarme a Django.
Si quereis verlo es https://docs.djangoproject.com/en/4.0/intro/tutorial01/ y sucesivos
Tambien tiene documentacion muy util https://docs.djangoproject.com/en/4.0/
Echando un vistazo a los distintos ficheros podeis haceros una idea de como funciona

---===========---
RESUMEN:

PRIMERA VEZ:
$ git clone git@github.com:lbm364dl/gpi.git (El que pone en el github)
$ pip instal django

CADA VEZ QUE SE BORRA EL CACHE:
$ python3 manage.py makemigrations <carpetas con modelos>
	ahora mismo es: paginaprincipal modificar_reserva recogida_entrega tarifas_disponibles coches_disponibles eliminar_reserva account
$ python3 manage.py migrate
$ echo "import generarbbdd" | python3 manage.py shell
	O $python3 manage.py shell y escribir a mano (Se sale con Ctrl+D)

PARA INICIAR EL SERVIDOR:
$ python3 manage.py runserver
Chrome/Firefox: ir a localhost:8000/home (Suele ser 8000, de todos modos lo pone)
---===========---
