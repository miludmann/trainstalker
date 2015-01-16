from django.conf.urls import patterns, url

from sncfdata_rt import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )
