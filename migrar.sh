rm db.sqlite3

python3 manage.py makemigrations account
python3 manage.py makemigrations paginaprincipal
python3 manage.py makemigrations coches_disponibles
python3 manage.py makemigrations eliminar_reserva
python3 manage.py makemigrations modificar_reserva
python3 manage.py makemigrations recogida_entrega
python3 manage.py makemigrations tarifas_disponibles
python3 manage.py migrate

echo 'import generarbbdd' | python3 manage.py shell
