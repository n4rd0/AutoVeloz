# Generated by Django 4.0.4 on 2022-05-10 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recogida_entrega', '__first__'),
        ('account', '0001_initial'),
        ('tarifas_disponibles', '__first__'),
        ('coches_disponibles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=3)),
                ('codigo', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(max_length=128)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_rec', models.DateField()),
                ('fecha_dev', models.DateField()),
                ('hora_rec', models.TimeField()),
                ('hora_dev', models.TimeField()),
                ('tarjeta_credito', models.CharField(max_length=16)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19)),
                ('pagada', models.BooleanField(default=False)),
                ('coche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coches_disponibles.coches')),
                ('extra', models.ManyToManyField(to='modificar_reserva.extras')),
                ('oficina_dev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lugar_devolucion', to='recogida_entrega.oficina')),
                ('oficina_rec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lugar_recogida', to='recogida_entrega.oficina')),
                ('opciones', models.ManyToManyField(to='coches_disponibles.opciones')),
                ('tarifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarifas_disponibles.tarifas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.usuario')),
            ],
        ),
    ]
