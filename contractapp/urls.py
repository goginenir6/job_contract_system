""" contarct app urls use this urls py file """
from django.conf.urls import  url
from contractapp.views import (
    index,
    login,
    home,
    redirect_to,  createpsc_save, posttenant, customer_save, employee_save, postEmployeeForm
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^home$', home, name='home'),
    url(r'^redirect_to/(?P<name>\w+)/$', redirect_to, name='redirect_to'),
    # url(r'^createpsc$', createpsc, name='createpsc'),
    url(r'^createpsc_save/$', createpsc_save, name='createpsc_save'),
    url(r'^posttenant/$', posttenant, name='posttenant'),
    url(r'^customer_save/$', customer_save, name='customer_save'),
    url(r'^employee_save/$', employee_save, name='employee_save'),
    url(r'^postEmployeeForm/$', postEmployeeForm, name='postEmployeeForm'),
]
