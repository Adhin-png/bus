# Generated by Django 5.1 on 2024-09-20 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0014_bus_total_fare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='total_fare',
        ),
    ]
