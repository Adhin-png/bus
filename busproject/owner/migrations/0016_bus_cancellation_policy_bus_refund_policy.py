# Generated by Django 5.1 on 2024-09-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0015_remove_bus_total_fare'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='cancellation_policy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='refund_policy',
            field=models.TextField(blank=True, null=True),
        ),
    ]