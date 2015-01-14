from django.db import models
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
    info = models.URLField('Additional information', max_length=200, 
            default='http://www.infolignes.com/', blank=True)

    def __str__(self):
        return str(self.number)


class DepartureTime(models.Model):
    '''Departure time of a train at a specific station'''
    # date = timezone.datetime(timezone.now().year, timezone.now().month, timezone.now().day, 17, 00)
    departure_time = models.DateTimeField('departure time')
    station = models.ForeignKey(Station)
    train = models.ForeignKey(Train)

    def __str__(self):
        return str(self.departure_time)

    def isComingInNextXMinutes(self, nb_minutes):
        return (timezone.now() + timezone.timedelta(minutes=nb_minutes)
            >= self.departure_time) and not self.isInThePast()

    def isComingInNext10Minutes(self):
        return self.isComingInNextXMinutes(10)
    isComingInNext10Minutes.admin_order_field = 'departure_time'
    isComingInNext10Minutes.boolean = True
    isComingInNext10Minutes.short_description = 'Leaving in the next 10 minutes?'

    def isInThePast(self):
        return timezone.now() > self.departure_time
    isInThePast.admin_order_field = 'departure_time'
    isInThePast.boolean = True
    isInThePast.short_description = 'Already left?'
