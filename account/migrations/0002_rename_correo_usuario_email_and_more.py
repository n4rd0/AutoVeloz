# Generated by Django 4.0.3 on 2022-04-18 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='apellidos',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='tipo',
            new_name='user_type',
        ),
    ]
