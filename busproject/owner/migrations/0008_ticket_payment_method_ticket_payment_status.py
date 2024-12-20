# Generated by Django 5.1 on 2024-09-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0007_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('G-Pay', 'G-Pay'), ('PhonePe', 'PhonePe'), ('Paytm', 'Paytm')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Failed', 'Failed')], default='Pending', max_length=20),
        ),
    ]
