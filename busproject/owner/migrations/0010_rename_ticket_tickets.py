# Generated by Django 5.1 on 2024-09-16 14:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0009_remove_ticket_payment_method_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ticket',
            new_name='Tickets',
        ),
    ]
