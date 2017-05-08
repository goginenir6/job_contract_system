""" contarct app urls use this urls py file """
from django.conf.urls import  url
from contractapp.views import (
    index,
    login,
    home,
    redirect_to, createpsc,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^home$', home, name='home'),
    url(r'^redirect_to/(?P<name>\w+)/$', redirect_to, name='redirect_to'),
    url(r'^createpsc$', createpsc, name='createpsc'),
]
