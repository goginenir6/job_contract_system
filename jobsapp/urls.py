"""job system urls use this urls """
from django.conf.urls import include, url

urlpatterns = [
    url(r'^contactapp/', include('contractapp.urls')),
]