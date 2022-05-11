from django import forms
from modificar_reserva import models

class DateInput(forms.DateInput):
    #input_format no funciona
    #input_format = '%d/%m/%Y'
    input_type = 'date'

class TimeInput(forms.TimeInput):
	#input_format ='%M:%H' 
	input_type = 'time'

class Extras(forms.ModelForm):
    class Meta: 
        model = models.Extras
        fields = [ 
                'extra',
            ]
        widgets = {
                'extra' : forms.CheckboxSelectMultiple
        }
        labels = { 
                'extra' : 'Extras',
        }
        error_messages = {
        }

class Pago(forms.Form):
    tarjeta_credito = forms.CharField(
            label = 'Tarjeta de crédito', 
            max_length = 16, 
            error_messages = {'required': 'La tarjeta debe tener 16 dígitos'},
        )

    titular = forms.CharField(max_length = 30)
    cvv = forms.CharField(
            label = 'CVV',
            max_length = 3,
            error_messages = {'required' : 'CVV debe tener 3 dígitos'},
        )
    fecha_caducidad = forms.DateField(
            label = 'Fecha de caducidad',
            widget = DateInput(),
            error_messages = {'required' : 'Tarjeta caducada'},
        )
