from django import forms
from modificar_reserva.models import TiposDeExtras
from coches_disponibles.models import TiposDeOpciones

class DateInput(forms.DateInput):
    #input_format no funciona
    #input_format = '%d/%m/%Y'
    input_type = 'date'

class TimeInput(forms.TimeInput):
	#input_format ='%M:%H' 
	input_type = 'time'

class ExtrasOpcionesDescuento(forms.Form):
    extra = forms.ChoiceField(
            label = 'Extras',
            widget = forms.CheckboxSelectMultiple,
            choices = [
                ('Wi-Fi', 'Wi-Fi'),
                ('GPS', 'GPS'),
                ('Silla para niños', 'Silla para niños'),
                ('Cadenas de nieve', 'Cadenas de nieve'),
            ]
        )
    opcion = forms.MultipleChoiceField(
            label = 'Opciones',
            widget = forms.CheckboxSelectMultiple,
            # no deja pasar un TextChoices
            choices = [
                ('Cambio automático', 'Cambio automático'),
                ('5 puertas', '5 puertas'),
                ('Techo solar', 'Techo solar'),
            ]
        )
    descuento = forms.CharField(max_length = 5, label = 'Código descuento', required = False)

class Pago(forms.Form):
    tarjeta_credito = forms.CharField(
            label = 'Tarjeta de crédito', 
            max_length = 16, 
            #error_messages = {'required': 'La tarjeta debe tener 16 dígitos'},
        )

    titular = forms.CharField(max_length = 30)
    cvv = forms.CharField(
            label = 'CVV',
            max_length = 3,
            #error_messages = {'required' : 'CVV debe tener 3 dígitos'},
        )
    fecha_caducidad = forms.DateField(
            label = 'Fecha de caducidad',
            widget = DateInput(),
            #error_messages = {'required' : 'Tarjeta caducada'},
        )
