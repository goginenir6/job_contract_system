"""contract system all views declared here"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from contractapp.models import Contracts, Tenant, Employee, Customer
from forms import TenantForm, EmployeeForm
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password

def index(request):
    """login page rediret"""
    return render(request, 'contract_login.html', {})


@login_required
def home(request):
    """home page redirect"""
    return render(request, 'contract_index.html', {})

def login(request):
    """login functionality"""
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        try:
            user = authenticate(email=request.POST.get("username"),
                                password=request.POST.get("inputPassword"))
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('home')
            else:
                return render(request, 'contract_login.html', {
                    'login_message' : 'Please Enter correct username and password.',})
        except:
            return render(request, 'contract_login.html', {
                'login_message' : 'Enter the username and password correctly'})


def redirect_to(request, name, context=None):
    """dynamic link to get urls"""
    if name != "":
        return render(request, name+'.html')
    else:
        return home

def createpsc_save(request):
    """ save psc """
    if request.method == "POST":
        import pdb
        pdb.set_trace()
        uni_code = request.body.decode('utf-8')
        user_inputs = json.loads(uni_code)
        try:
            contract_rec = Contracts.objects.get(contractNumber=user_inputs.get('txtCacntno')).first()
            contract_rec.entrydate = user_inputs.get('txtcDate')
            contract_rec.expirydate = user_inputs.get('txtCExdate')
            contract_rec.ctype = user_inputs.get('psctype')
            contract_rec.customerid = user_inputs.get('ddlCustomerid')
            contract_rec.customername = user_inputs.get('txtCcustidname')
            contract_rec.services = user_inputs.get('ddlsystems')
            contract_rec.worksummary = user_inputs.get('txtSummary')
            contract_rec.introduction = user_inputs.get('txtIntrod')
            contract_rec.expectedresults = user_inputs.get('expectedresults')
            contract_rec.estimatedhours = user_inputs.get('entrydate')
            contract_rec.hourlyrate = user_inputs.get('hourlyrate')
            contract_rec.totalestimate = user_inputs.get('totalestimate')
            contract_rec.deposit = user_inputs.get('deposit')
            contract_rec.approved = user_inputs.get('approved')
            contract_rec.verified = user_inputs.get('verified')
            contract_rec.rejected = user_inputs.get('rejected')
            contract_rec.issigned = user_inputs.get('issigned')
            contract_rec.depositpd = user_inputs.get('depositpd')
            contract_rec.dateupdated = user_inputs.get('dateupdated')
            contract_rec.accepted = user_inputs.get('accepted')
            contract_rec.dateaccepted = user_inputs.get('dateaccepted')
            contract_rec.completed = user_inputs.get('completed')
            contract_rec.datecompleted = user_inputs.get('datecompleted')
            contract_rec.systemid = user_inputs.get('systemid')
            contract_rec.PSCtype = user_inputs.get('PSCtype')
            contract_rec.summary = user_inputs.get('summary')
            contract_rec.details = user_inputs.get('details')
            contract_rec.terms = user_inputs.get('terms')
            contract_rec.jobcompletion = user_inputs.get('jobcompletion')
            contract_rec.cancellation = user_inputs.get('cancellation')
            contract_rec.maintenance = user_inputs.get('maintenance')
            contract_rec.closing = user_inputs.get('closing')
            contract_rec.attachment = user_inputs.get('attachment')
            contract_rec.jobno = user_inputs.get('jobno')
            contract_rec.status = user_inputs.get('status')
            contract_rec.scheduledtime = user_inputs.get('scheduledtime')
            contract_rec.scheduleddtimechanges = user_inputs.get('scheduleddtimechanges')
            contract_rec.travelcosts = user_inputs.get('travelcosts')
            contract_rec.timezone = user_inputs.get('timezone')
            contract_rec.invoicenumbers = user_inputs.get('invoicenumbers')
            contract_rec.maillingaddress = user_inputs.get('txtMailingAddress')
            contract_rec.limitofliability = user_inputs.get('limitofliability')
            contract_rec.startwork = user_inputs.get('startwork')
            contract_rec.expired = user_inputs.get('expired')
            contract_rec.categeory = user_inputs.get('categeory')
            contract_rec.save()
        except:
            contract_creat = Contracts(
                Tenantid = Tenant.objects.first(),
                entrydate = user_inputs.get('txtcDate'),
                expirydate = user_inputs.get('txtCExdate'),
                ctype = user_inputs.get('psctype'),
                customerid = user_inputs.get('ddlCustomerid'),
                customername = user_inputs.get('txtCcustidname'),
                services = user_inputs.get('ddlsystems'),
                worksummary = user_inputs.get('txtSummary'),
                introduction = user_inputs.get('txtIntrod'),
                expectedresults = user_inputs.get('expectedresults'),
                estimatedhours = user_inputs.get('entrydate'),
                hourlyrate = user_inputs.get('hourlyrate'),
                totalestimate = user_inputs.get('totalestimate'),
                deposit = user_inputs.get('deposit'),
                approved = user_inputs.get('approved'),
                verified = user_inputs.get('verified'),
                rejected = user_inputs.get('rejected'),
                issigned = user_inputs.get('issigned'),
                depositpd = user_inputs.get('depositpd'),
                dateupdated = user_inputs.get('dateupdated'),
                accepted = user_inputs.get('accepted'),
                dateaccepted = user_inputs.get('dateaccepted'),
                completed = user_inputs.get('completed'),
                datecompleted = user_inputs.get('datecompleted'),
                systemid = user_inputs.get('systemid'),
                PSCtype = user_inputs.get('PSCtype'),
                summary = user_inputs.get('summary'),
                details = user_inputs.get('details'),
                terms = user_inputs.get('terms'),
                jobcompletion = user_inputs.get('jobcompletion'),
                cancellation = user_inputs.get('cancellation'),
                maintenance = user_inputs.get('maintenance'),
                closing = user_inputs.get('closing'),
                attachment = user_inputs.get('attachment'),
                jobno = user_inputs.get('jobno'),
                status = user_inputs.get('status'),
                scheduledtime = user_inputs.get('scheduledtime'),
                scheduleddtimechanges = user_inputs.get('scheduleddtimechanges'),
                travelcosts = user_inputs.get('travelcosts'),
                timezone = user_inputs.get('timezone'),
                invoicenumbers = user_inputs.get('invoicenumbers'),
                maillingaddress = user_inputs.get('txtMailingAddress'),
                limitofliability = user_inputs.get('limitofliability'),
                startwork = user_inputs.get('startwork'),
                expired = user_inputs.get('expired'),
                categeory = user_inputs.get('categeory')
            )
            contract_creat.save()
            pass
        context = {user_inputs}
        return redirect_to(request, 'createPSC', context=context)
    return redirect_to(request, 'createPSC', context={})

def posttenant(request):
    form = TenantForm(request.POST or None)
    if request.method == "POST":
        print request.POST.get('TenantName')
        Tenant.objects.create(TenantName = request.POST.get('TenantName'))
    context = {
        'form': form
    }
    return render(request, 'tenant_form.html', context)

def postEmployeeForm(request):
    if request.method == 'POST':
            form = EmployeeForm(request.POST or None, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.password = make_password(form.cleaned_data['password'])
                instance.save()
                return HttpResponseRedirect('/contractapp/postEmployeeForm/')
    else:
        # empno = increment_emp_number(Employee)
        form = EmployeeForm()

    return render(request, 'contract_frmemployee.html', {'form':form})


def customer_save(request):
    if request.method == "POST":
        uni_code = request.body.decode('utf-8')
        user_inputs = json.loads(uni_code)
        cust_id = increment_primary_number(Customer, 'customer_id')
        try:
            cust = Customer.objects.create(Tenantid=Tenant.objects.first() , customer_id=cust_id, firstname=user_inputs.get('txt_first_name'), lastname=user_inputs.get('txt_last_name'), address=user_inputs.get('txt_address'), phone=user_inputs.get('txt_mobile'))
        except:
            return render(request, 'contract_customer.html', {})
    return render(request, 'contract_customer.html', {})

def employee_save(request):
    if request.method == "POST":
        uni_code = request.body.decode('utf-8')
        user_inputs = json.loads(uni_code)
        emp_id = increment_emp_number(Employee)
        # try:
        emp = Employee.objects.create(user=User.objects.create_user(username=emp_id,
                                                                    password=user_inputs.get('txt_emp_pwd'),
                                                                    email=user_inputs.get('txt_emp_email'),
                                                                    first_name=user_inputs.get('txt_emp_fname'),
                                                                    last_name=user_inputs.get('txt_emp_lname'),
                                                                    ),
                                    Tenantid=Tenant.objects.first() ,
                                    Employee_id=emp_id,
                                    is_admin=user_inputs.get('chk_isadmin'),
                                    status=user_inputs.get('rdo_emp_status'))
        # cust.comm
        # except:
        #     return render(request, 'contract_customer.html', {})
    return render(request, 'contract_customer.html', {})

def increment_primary_number(table):
    try:
        last_primary = table.objects.all().order_by('customer_id').last()
    except:
        return 'BRIO0001'
    primary_no = last_primary.customer_id
    new_primary_no = str(int(primary_no[4:]) + 1)
    new_primary_no = primary_no[0:-(len(new_primary_no))] + new_primary_no
    return new_primary_no

def increment_emp_number(table):
    try:
        last_primary = table.objects.all().order_by('Employee_id').last()
    except:
        return '0001'
    primary_no = last_primary.Employee_id
    new_primary_no = str(int(primary_no) + 1)
    new_primary_no = primary_no[0:-(1)] + new_primary_no
    return new_primary_no