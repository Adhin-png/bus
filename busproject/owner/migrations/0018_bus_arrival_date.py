# Generated by Django 5.1 on 2024-09-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0017_bus_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='arrival_date',
            field=models.DateField(null=True),
        ),
    ]