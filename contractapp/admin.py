# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import User
from contractapp.models import Contracts, Tenant, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Tenant)
# admin.site.unregister(User)
admin.site.register(Contracts)