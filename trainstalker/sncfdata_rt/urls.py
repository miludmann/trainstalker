from django.conf.urls import patterns, url

from sncfdata_rt import views

urlpatterns = patterns('',
        # ex: /sncfdata_rt/
        url(r'^$', views.index, name='index'),
        # ex: /sncfdata_rt/OCE87757674
        url(r'^(?P<station_code>[A-Z0-9]+)/$', views.station, name='station'),
        # ex: /sncfdata_rt/OCE87757674/train
        url(r'^(?P<number>[A-Z0-9]+)/train/$', views.train, name='train'),
        # ex: /sncfdata_rt/OCE87757674/departure
        url(r'^(?P<departure_time>[A-Z0-9]+)/$/departure',
            views.departure, name='departure'),
                       )
