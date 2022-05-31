from django.urls import path
from . import views

app_name = 'reservas_'
urlpatterns = [
    path('', views.ver_reservas),
    path('eliminar_reserva/<int:id_reserva>', views.eliminar_reserva, name = 'eliminar_reserva'),
]
