from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# from django.http import *
# from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from moocb.models import Goal 
import json

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


@login_required
def me(request):
    context = RequestContext(request)

    context['user'] = request.user

    context['goals'] = Goal.objects.filter(user = request.user.id)
    return render_to_response('moocb/me.html', context)


def logout_user(request):
    logout(request)
    return render_to_response('moocb/login.html')

@csrf_exempt
def add_time(request):
    #how to do for multiple goals?
    context = RequestContext(request)
    
    
    if request.POST:
        _id = request.GET.get('user', 0)
        try:
            
            context['user'] = User.objects.get(id = _id)

            goal = Goal.objects.filter(user = User.objects.get(id = _id))[0]
            goal.time_worked = goal.time_worked + int(request.GET.get('time', 0))
            goal.save()
            context['course'] = goal

        except:
            context['user'] =  "not found for id: " + str(_id)
        data = {}
        return HttpResponse(json.dumps(data), content_type="application/json")

        
    # 5483c154c5cbe516f21d5f08
    # 5483d7bec5cbe518fe34eb84
    # 5483d889c5cbe5190bc1d834

    context['time'] = request.GET.get('time', 'no time found' )
    
    return render_to_response('moocb/add.html', context)






