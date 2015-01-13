from django.contrib import admin
from sncfdata_rt.models import Station, Train, DepartureTime

# Register your models here.
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(DepartureTime)
