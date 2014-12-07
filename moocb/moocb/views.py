from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# from django.http import *
# from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home(request):
    
    # html = "<html><body>Guiseppe is my moocbuddy</body></html>" 
    # return HttpResponse(html)
    return render_to_response('moocb/home.html')


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/me/')
    return render_to_response('moocb/login.html', context_instance=RequestContext(request))





