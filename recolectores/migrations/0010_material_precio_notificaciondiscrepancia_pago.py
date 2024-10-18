# Generated by Django 5.1.1 on 2024-10-17 21:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recolectores', '0009_ordendistribucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.CreateModel(
            name='NotificacionDiscrepancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recolectores.orden')),
            ],
            options={
                'db_table': 'notificaciones_discrepancias',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pagado', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recolectores.orden')),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
    ]