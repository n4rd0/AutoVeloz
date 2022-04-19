from django.urls import path
from . import views


app_name = 'tarifas'
urlpatterns = [
    path('<str:gama>/<int:temporada>/', views.tarifas_disponibles, name = 'tarifas_disponibles'),
]
