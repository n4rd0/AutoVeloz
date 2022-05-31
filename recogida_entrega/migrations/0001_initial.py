# Generated by Django 4.0.4 on 2022-05-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=128)),
                ('facturado', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
            ],
        ),
    ]