from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/grader/')
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                # Done!
                return HttpResponseRedirect('/')
            else:
                # Account if disabled
                return HttpResponse('Your account is disabled')
        else:
            # Invalid login
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse('Invalid login' )
    else:
        return HttpResponse("Login")

@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def home(request):
    return HttpResponseRedirect('/grader/')