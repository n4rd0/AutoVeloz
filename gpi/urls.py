"""gpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('home/', TemplateView.as_view(template_name = 'home/home.html')),
    path('polls/', include('polls.urls')),
    path('recogida_entrega/', include('recogida_entrega.urls')),
    path('coches_disponibles/', include('coches_disponibles.urls')),
    path('tarifas_disponibles/', include('tarifas_disponibles.urls')),
    path('modificar_reserva/', include('modificar_reserva.urls')),
    path('eliminar_reserva/', include('eliminar_reserva.urls')),
    path('welcome/', include('paginaprincipal.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]
