from django.urls import path
from . import views

app_name = 'reservas'
urlpatterns = [
    path('', views.ver_reservas),
    path('modificar_reserva/<int:id_reserva>', views.modificar_reserva, name = 'modificar_reserva'),
]
