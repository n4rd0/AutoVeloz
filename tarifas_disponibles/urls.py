from django.urls import path
from . import views


urlpatterns = [

    path('', views.tarifas_disponibles, name = 'tarifas_disponibles'),
]
