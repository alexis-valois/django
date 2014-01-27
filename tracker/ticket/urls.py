__author__ = 'Alexis'
from django.conf.urls import patterns, url
from views import home

urlpatterns = patterns('',
    url(r'^home/$', home, name="home")
)
