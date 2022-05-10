from django.urls import path
from . import views


app_name = 'recogida_entrega'
urlpatterns = [
    path('<int:id_coche>/<int:id_tarifa>', views.recogida_entrega, name = 'reserva'),
    path('pago/<int:id_reserva>', views.pago, name = 'pago'),
]
