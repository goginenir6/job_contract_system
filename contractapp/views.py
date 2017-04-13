"""contract system all views declared here"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'login.html', {})


# @login_required
# def home(request):
#     return render(request,'home.html')
 
# def login(request):
#     # import pdb; pdb.set_trace()
#     if request.method == 'POST':
#         try:
#             user = authenticate(username= request.POST.get("inputEmail"),
#                       password= request.POST.get("inputPassword"))
#             if user is not None:
#                 auth_login(request,user)
#                 return HttpResponseRedirect('home')
#             else:
#                 return render(request, 'login.html',{
#             'login_message' : 'Please Enter correct username and password.',})
#         except:
#             return render(request, 'login.html',{
#             'login_message' : 'Enter the username and password correctly',})

# def pageredirect(request, name):
#     """dynamic link to get urls"""
#     if name != "":
#         return render(request, name+'.html')
#     else:
#         return home


# def createpsc(request):
#     if request.method == "POST":
#         import pdb;pdb.set_trace()
#         body_unicode = request.body.decode('utf-8')
#         data = json.loads(body_unicode)
#         print data
#     return render( 'createPSC.html', data)
