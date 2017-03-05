from __future__ import unicode_literals

from django.db import models

# Create your models here.

class entered(models.Model):
    timeEntered = models.DateTimeField()
    timeStep = models.IntegerField()
    sensorType = models.CharField(max_length=50)

    # class Meta:
    #     enters = ["timeEntered", "timeStep", 'sensorType']

class sat(models.Model):
    timeSat = models.DateTimeField()
    tableNumber = models.IntegerField()
    totalNumber = models.IntegerField()


class order(models.Model):
    timeOrdered = models.DateTimeField()
    waiterNumber = models.IntegerField()
    tableNumber = models.IntegerField()


class arrived(models.Model):
    timeArrived = models.DateTimeField()
    waiterNumber = models.IntegerField()
    tableNumber = models.IntegerField()


class finished(models.Model):
    timeFinished = models.DateTimeField()
    tableNumber = models.IntegerField()
    waiterTookBill = models.IntegerField()


class left(models.Model):
    timeLeft = models.DateTimeField()
    tableNumber = models.IntegerField()
