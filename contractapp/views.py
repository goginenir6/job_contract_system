"""contract system all views declared here"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login

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
            user = authenticate(username=request.POST.get("username"),
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


def pageredirect(request, name):
    """dynamic link to get urls"""
    if name != "":
        return render(request, name+'.html')
    else:
        return home

def createpsc(request):
    """ save psc """
    import  pdb
    pdb.set_trace()
    return pageredirect(request, 'createCSC')

# def createpsc(request):
#     if request.method == "POST":
#         import pdb;pdb.set_trace()
#         body_unicode = request.body.decode('utf-8')
#         data = json.loads(body_unicode)
#         print data
#     return render( 'createPSC.html', data)
