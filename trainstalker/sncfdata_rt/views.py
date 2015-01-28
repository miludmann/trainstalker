from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("You are at the real-time train data index.")


def train(request, number):
    response = "You are looking at train from station %s."
    return HttpResponse(response % number)

def station(request, station_code):
    response = "You are looking at train station %s."
    return HttpResponse(response % station_code)


def departure(request, departure_time):
    response = "You are looking at departure time from station %s."
    return HttpResponse(response % departure_time)
