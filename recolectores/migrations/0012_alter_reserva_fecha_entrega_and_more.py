# Generated by Django 5.1.1 on 2024-10-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recolectores', '0011_reserva_deposito_encargado_reserva_fecha_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_prevista',
            field=models.DateField(blank=True, null=True),
        ),
    ]
