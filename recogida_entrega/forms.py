from django import forms
from modificar_reserva import models

class DateInput(forms.DateInput):
	input_type = 'date'

class TimeInput(forms.TimeInput):
	input_format ='%H:%M' 
	input_type = 'time'

class crearReserva(forms.ModelForm):
	class Meta: 
		model = models.Reserva
		fields = [
		'id_usuario','id_oficina_rec','id_oficina_dev','id_coche','fecha_rec','fecha_dev','hora_rec','hora_dev','id_tarifa','tarjeta_credito'
		]
		widgets = {
			'fecha_rec' : DateInput(),
			'fecha_dev' : DateInput(),
			'hora_rec': TimeInput(),
			'hora_dev': TimeInput()
		}