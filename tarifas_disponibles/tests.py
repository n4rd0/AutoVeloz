from django.test import TestCase, Client

# Create your tests here.
#class TarifasTestCase(TestCase):
    #def test_devuelve_tarifas(self):

# para probar en shell, aun no controlo los tests estos
from django.test.utils import setup_test_environment
from django.test import Client
setup_test_environment()
c = Client(SERVER_NAME = 'localhost')
c.login(username = '83140123X', password = 'Pass_word42')
r = c.post('/tarifas_disponibles/', {'gama' : 'Media', 'temporada' : 1})
r.context
