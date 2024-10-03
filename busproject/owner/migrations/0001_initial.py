# Generated by Django 5.1 on 2024-08-30 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=100)),
                ('seat_available', models.IntegerField(default=0)),
                ('seat_remaining', models.IntegerField(default=0)),
                ('source', models.CharField(default='', max_length=200)),
                ('destination', models.CharField(max_length=200, null=True)),
                ('bus_fare', models.IntegerField()),
                ('date', models.DateField(null=True)),
                ('bus_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.category')),
            ],
        ),
    ]
