# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-04 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='arrived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeArrived', models.DateTimeField()),
                ('waiterNumber', models.IntegerField()),
                ('tableNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='entered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeEntered', models.DateTimeField()),
                ('timeStep', models.IntegerField()),
                ('sensorType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='finished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeFinished', models.DateTimeField()),
                ('tableNumber', models.IntegerField()),
                ('waiterTookBill', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='left',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeLeft', models.DateTimeField()),
                ('tableNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOrdered', models.DateTimeField()),
                ('waiterNumber', models.IntegerField()),
                ('tableNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeSat', models.DateTimeField()),
                ('tableNumber', models.IntegerField()),
                ('totalNumber', models.IntegerField()),
            ],
        ),
    ]