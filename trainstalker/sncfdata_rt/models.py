from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.


class Station(models.Model):
    '''Train station'''
    station_name = models.CharField(max_length=100)
    station_code = models.CharField(max_length=11)
    def __str__(self):
        return self.station_name
    

class Train(models.Model):
    '''Actual train'''
    destination = models.CharField(max_length=100)
    number = models.IntegerField()
    model_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    info = models.URLField('additional information', max_length=200)
    def __str__(self):
        return str(self.number)


class DepartureTime(models.Model):
    '''Departure time of a train at a specific station'''
    departure_time = models.DateTimeField('departure time')
    station = models.ForeignKey(Station)
    train = models.ForeignKey(Train)
    def __str__(self):
        return self.str(self.departure_time)
    def isLeavingBeforeXMinutes(self, nb_minutes):
        return timezone.now() + timedelta(minutes=nb_minutes) > self.departure_time
