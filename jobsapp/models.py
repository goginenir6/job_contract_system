"""
Db models all created here.
"""
from __future__ import unicode_literals
import datetime
import uuid
from django.db import models

# Create your models here.


class Tenant(models.Model):
    """Tenant table."""
    Tenantid = models.AutoField(primary_key=True)
    TenantName = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Tenantid

class Contracts(models.Model):
    """Create contract table."""
    # str(uuid.uuid4().get_hex().upper()[0:10])
    entrydate = models.DateField(default=datetime.date)
    expirydate = models.DateField(auto_now=False)
    contractNumber = uuid.uuid4().get_hex().upper()[0:10]
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

# def __init__(self) :
#     self.seq = 0

# def getNextSeqNo(self) :
#     self.seq += 1
#     return '%010d' % self.seq
