""" contarct app urls use this urls py file """
from django.conf.urls import  url
from contractapp.views import (
    index,
    login,
    home,
    pageredirect, createpsc,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^home$', home, name='home'),
    url(r'^pageredirect/(?P<name>\w+)/$', pageredirect, name='pageredirect'),
    url(r'^createpsc$', createpsc, name='createpsc'),
]
