"""contract system all database models ddeclared here"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import UserManager
from django.conf import settings
from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.http import urlquote
import datetime




class Tenant(models.Model):
    tenant_Name = models.CharField(max_length=50)
    class Meta:
        db_table = "Tenant"
    def __unicode__(self):
        return str(self.tenant_Name)

# class Employee(models.Model):
#     """User extended fields """
#     # user = models.OneToOneField(User)  
#     Tenantid = models.ForeignKey(Tenant)
#     status = models.CharField(max_length=10, choices=(('ACTIVE','ACTIVE'),   ('INACTIVE','INACTIVE'),))
#     is_admin = models.BooleanField()
#     Employee_id = models.CharField(max_length=10, primary_key=True)
#     def __unicode__(self):
#         return str(self.Employee_id)

# class Employee(AbstractBaseUser,PermissionsMixin):
#     """User extended fields """
#     tenantid = models.ForeignKey(Tenant)
#     status = models.CharField(max_length=10, choices=(('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'),))
#     is_admin = models.BooleanField()
#     employee_id = models.CharField(max_length=10, primary_key=True)

#     USERNAME_FIELD = 'employee_id'
#     REQUIRED_FIELDS = []

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = CustomUserManager.normalize_email(email)
        user = self.model(email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class Employee(AbstractBaseUser, PermissionsMixin):
    # userid = models.ForeignKey(User, null=True)
    tenantid = models.ForeignKey(Tenant)
    employee_id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    mobile_no = models.CharField(null=True, max_length=13, blank=True)
    remarks = models.TextField(blank=True, null=True)
    profilepic = models.ImageField(upload_to='images/', max_length=100, blank=True, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    createdBy = models.CharField(max_length=50, null=True)
    modifiedOn = models.DateTimeField(auto_now=True, blank=True, null=True)
    modifiedBy = models.CharField(max_length=50, null=True)
    recVersion = models.IntegerField(default=1, null=True)
    status = models.CharField(max_length=1,
                            choices=[('0', 'inactive'), ('1', 'active'), ],
                            default='1')
    # ismanager = models.BooleanField(default=False)
    is_staff = models.BooleanField(('staff status'), default=False)
    # help_text=('Designates whether the user can log into this admin site.')
    is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def get_absolute_url(self):
        return "/contractapp/Employee/%s/" % urlquote(self.pk)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

class Contracts(models.Model):
    """Create contract table."""
    tenantid = models.ForeignKey(Tenant)
    entrydate = models.DateField(default=datetime.date)
    expirydate = models.DateField(auto_now=False)
    # contractNumber = uuid.uuid4().get_hex().upper()[0:10]
    contractNumber = models.CharField(max_length=50, primary_key=True)
    ctype = models.CharField(max_length=10)
    customerid = models.CharField(max_length=50)
    customername = models.CharField(max_length=50)
    services = models.TextField()
    worksummary = models.TextField()
    details = models.TextField()
    expectedresults = models.TextField()
    estimatedhours = models.IntegerField()
    hourlyrate = models.FloatField()
    totalestimate = models.FloatField()
    deposit = models.FloatField()
    approved = models.BooleanField()
    verified = models.BooleanField()
    rejected = models.BooleanField()
    issigned = models.BooleanField()
    depositpd = models.BooleanField()
    dateupdated = models.DateField()
    accepted = models.BooleanField()
    dateaccepted = models.DateField()
    completed = models.BooleanField()
    datecompleted = models.DateField()
    systemid = models.CharField(max_length=20)
    PSCtype = models.CharField(max_length=20)
    summary = models.TextField()
    introduction = models.TextField()
    terms = models.TextField()
    jobcompletion = models.TextField()
    cancellation = models.TextField()
    maintenance = models.TextField()
    closing = models.TextField()
    attachment = models.TextField()
    websubid = models.CharField(max_length=20)
    jobno = models.IntegerField()
    status = models.CharField(max_length=20)
    scheduledtime = models.TextField()
    scheduleddtimechanges = models.TextField()
    travelcosts = models.TextField()
    timezone = models.CharField(max_length=40)
    invoicenumbers = models.CharField(max_length=50)
    maillingaddress = models.TextField()
    limitofliability = models.TextField()
    startwork = models.BooleanField()
    expired = models.BooleanField()
    categeory = models.CharField(max_length=20)
    def __unicode__(self):
        return self.contractNumber

class Customer(models.Model):
    """custmmer table """
    tenantid = models.ForeignKey(Tenant)
    customer_id = models.CharField(max_length=10, primary_key=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    def __unicode__(self):
        return self.customer_id
