""" contarct app urls use this urls py file """
from django.conf.urls import include, url

urlpatterns = [
    url(r'^contactapp/', include('contractapp.urls')),
]