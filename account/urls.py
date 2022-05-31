from django.urls import path, include

from . import views

app_name = 'account'
urlpatterns = [
    # /login/ y otros que ya vienen
    path('', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
]
