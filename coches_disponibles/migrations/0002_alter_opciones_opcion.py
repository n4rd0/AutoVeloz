# Generated by Django 4.0.4 on 2022-05-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coches_disponibles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opciones',
            name='opcion',
            field=models.CharField(choices=[('Cambio automático', 'Automatico'), ('5 puertas', 'Puertas 5'), ('Techo solar', 'Techo Solar')], max_length=128),
        ),
    ]
