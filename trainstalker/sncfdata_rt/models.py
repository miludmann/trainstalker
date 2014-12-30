from django.db import models

# Create your models here.


class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_code = models.CharField(max_length=11)


class Train(models.Model):
    destination = models.CharField(max_length=100)
    number = models.IntegerField()
    model_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    info = models.URLField('additional information', max_length=200)


class DepartureTime(models.Model):
    departure_time = models.DateTimeField('departure time')
    station = models.ForeignKey(Station)
    train = models.ForeignKey(Train)
