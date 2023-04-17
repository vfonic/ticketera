# Generated by Django 3.2.9 on 2023-01-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0019_tickettransfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='donation_grant',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Para ayudar a quienes necesitan una mano con su bono contribución.', max_digits=10, null=True, verbose_name='Beca Inclusión Radical'),
        ),
        migrations.AlterField(
            model_name='order',
            name='donation_venue',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Para mejorar el espacio donde nos encontramos todo el año.', max_digits=10, null=True, verbose_name='Donaciones a La Sede'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='volunteer_umpalumpa',
            field=models.BooleanField(verbose_name='CAOS (Armado y Desarme de la Ciudad)'),
        ),
        migrations.AlterField(
            model_name='tickettransfer',
            name='volunteer_umpalumpa',
            field=models.BooleanField(verbose_name='CAOS (Armado y Desarme de la Ciudad)'),
        ),
    ]