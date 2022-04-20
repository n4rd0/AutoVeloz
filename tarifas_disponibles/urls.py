from django.urls import path
from . import views


app_name = 'tarifas'
urlpatterns = [
    path('<int:id_coche>/<int:temporada>/', views.tarifas_disponibles, name = 'tarifas_disponibles'),
    path('temporadas/<int:id_coche>/', views.temporadas, name = 'temporadas'),
]
