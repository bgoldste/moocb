from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

# from django.http import *
# from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from moocb.models import Goal , User
import json
from forms import UserForm, GoalForm

def home(request):
    
    # html = "<html><body>Guiseppe is my moocbuddy</body></html>" 
    # return HttpResponse(html)
    return render_to_response('moocb/home.html')


def login_user(request):
    logout(request)
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print user
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
    return HttpResponseRedirect('/login/')

@csrf_exempt
def add_time(request):
    #how to do for multiple goals?
    context = RequestContext(request)
    print request
    print 'calling add time view' , request.POST #, (request.Post == True)
    if request.POST:

        print "post detected!"
        _id = request.GET.get('user', 0)
        try:
            
            context['user'] = 'adsasdasdadasd' #User.objects.get(id = _id)

            goal = Goal.objects.filter(user = User.objects.get(id = _id))[0]
            goal.time_worked = goal.time_worked + int(request.GET.get('time', 0))
            goal.save()
            context['course'] = goal

        except:
            context['user'] =  "not found for id: " + str(_id)
        data = {}
        context['user'] = 'asda'
        return HttpResponse(json.dumps(data), content_type="application/json")

        
    # 5483c154c5cbe516f21d5f08
    # 5483d7bec5cbe518fe34eb84
    # 5483d889c5cbe5190bc1d834

    context['time'] = request.GET.get('time', 'no time found' )
    context['user_id'] = request.user.id
   
    return render_to_response('moocb/add.html', context)



def add_user(request):
    context = RequestContext(request)
    logout(request)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            print new_user
            print 'form username' , form.cleaned_data['username']
            print 'form pw' , form.cleaned_data['password']
            #new_user = authenticate(username='ben', password='1')

            print 'new_user object ' , new_user
            print request
            #hack!
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)

            # redirect, or however you want to get to the main vie
            return HttpResponseRedirect('/me/')
            #return render_to_response('moocb/me.html', context_instance=RequestContext(request))
    else:
        form = UserForm() 
    return render_to_response( 'moocb/adduser.html', {'form': form},  context_instance=RequestContext(request))

@login_required
def add_goal (request):
    context = RequestContext(request)
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            new_goal = Goal (user= request.user, **form.cleaned_data)
            new_goal.save()
            return HttpResponseRedirect('/me/')
    else:
        form = GoalForm() 

    return render_to_response( 'moocb/addgoal.html', {'form': form},  context_instance=RequestContext(request))


