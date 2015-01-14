from django.contrib import admin
from sncfdata_rt.models import Station, Train, DepartureTime


class DepartureTimeInline(admin.TabularInline):
    model = DepartureTime
    extra = 3


class StationAdmin(admin.ModelAdmin):
    inlines = [DepartureTimeInline]
    search_fields = ['station_name']


class DepartureAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,                  {'fields': ['station', 'train']}),
            ('Date information',    {'fields': ['departure_time']}),
    ]
    list_display = ('station', 'train', 'departure_time', 'isInThePast',
                    'isComingInNext10Minutes')
    list_filter = ['departure_time']


class TrainAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,                  {'fields': ['destination', 'number',
                                     'model_type', 'status']}),
            ('Plus d\'information', {'fields': ['info'], 'classes':
                                     ['collapse']}),
    ]
    list_display = ('destination', 'number', 'model_type', 'status', 'info')
    search_fields = ['destination']


# Register your models here.
admin.site.register(Station, StationAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(DepartureTime, DepartureAdmin)
