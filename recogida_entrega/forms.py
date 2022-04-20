from django import forms
from modificar_reserva import models

class DateInput(forms.DateInput):
    input_format = '%d/%m/%Y'
    input_type = 'date'

class TimeInput(forms.TimeInput):
	input_format ='%M:%H' 
	input_type = 'time'

class crearReserva(forms.ModelForm):
    class Meta: 
        model = models.Reserva
        fields = [ 
                'oficina_dev',
                'fecha_rec',
                'hora_rec',
                'fecha_dev',
                'hora_dev',
                'tarjeta_credito',
            ]
        widgets = {
            'fecha_rec' : forms.DateInput(format=('%d-%m-%Y')),#DateInput(format = '%d/%m/%Y'),
            'fecha_dev' : DateInput(),
            'hora_rec': TimeInput(),
            'hora_dev': TimeInput()
        }
        labels = { 
                'oficina_dev' : 'Oficina devolución', 
                'fecha_rec' : 'Fecha recogida',
                'fecha_dev' : 'Fecha devolución',
                'hora_rec' : 'Hora recogida',
                'hora_dev' : 'Hora devolución',
                'tarjeta_credito' : 'Tarjeta de crédito',
        }
        error_messages = {
            'fecha_rec': {
                'required': 'El mes de recogida debe ser de la temporada elegida',
                'invalid': 'Las fechas deben ser consistentes',
            },
            'tarjeta_credito': {
                'required': 'La tarjeta debe tener 16 dígitos',
            },
        }
