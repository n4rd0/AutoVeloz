from django import forms
from modificar_reserva import models

class DateInput(forms.DateInput):
    #input_format no funciona
    #input_format = '%d/%m/%Y'
    input_type = 'date'

class TimeInput(forms.TimeInput):
	#input_format ='%M:%H' 
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
            ]
        widgets = {
            'fecha_rec' : DateInput(),#forms.DateInput(format=('%d-%m-%Y')),#DateInput(format = '%d/%m/%Y'),
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
        }
        error_messages = {
            'fecha_rec': {
                'required': 'Elija un fin de semana',
                'invalid': 'Las fechas deben ser consistentes',
            },
        }

class Pago(forms.Form):
    tarjeta_credito = forms.CharField(
            label = 'Tarjeta de crédito', 
            max_length = 16, 
            error_messages = {'required': 'La tarjeta debe tener 16 dígitos'},
        )
    fecha_caducidad = forms.DateField(
            label = 'Fecha de caducidad',
            widget = DateInput(),
            error_messages = {'required' : 'Tarjeta caducada'},
        )
    titular = forms.CharField(max_length = 30)
    cvv = forms.CharField(
            label = 'CVV',
            max_length = 3,
            error_messages = {'required' : 'CVV debe tener 3 dígitos'},
        )

