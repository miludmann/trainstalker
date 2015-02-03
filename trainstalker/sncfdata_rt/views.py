from django.shortcuts import render
from django.http import HttpResponse

from sncfdata_rt.models import Station

# Create your views here.
def index(request):
    stations_list = Station.objects.order_by('station_name')[:5]
    context = {'stations_list': stations_list}
    return render(request, 'sncfdata_rt/index.html', context)


def train(request, number):
    response = "You are looking at train from station %s."
    return HttpResponse(response % number)

def station(request, station_code):
    response = "You are looking at train station %s."
    return HttpResponse(response % station_code)


def departure(request, departure_time):
    response = "You are looking at departure time from station %s."
    return HttpResponse(response % departure_time)
