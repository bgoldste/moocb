from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render_to_response

# from django.http import *
# from django.shortcuts import render_to_response,redirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from moocb.models import Goal , User, TimeLog
import json
from forms import UserForm, GoalForm
import sys
from django.core import serializers




def home(request):
    
    return render_to_response('moocb/home2.html')


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


@csrf_exempt
def login_user_json(request):
    try:
        logout(request)
        username = 'ben'
        password = '1'
        print request.POST
       
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                goal = Goal.objects.filter(user = user)[0]
                data = {
                    'type': 'user_login',
                    'status': 'success',
                    'user': user.username,
                    'userid': user.id,
                    'goal': {
                            'name': goal.name, 
                            'id': goal.id,
                            'url': goal.url,
                            'time_goal': goal.time_goal,
                            'last_worked': goal.last_worked,
                            'start_date': str(goal.start_date),
                            'end_date': str(goal.end_date),
                            'time_worked': goal.time_worked,
                            },
                }


                return HttpResponse(json.dumps(data), content_type="application/json")
        data = {
            'type': 'user_login',
            'status': 'fail',
            'msg' :'non fatal inval login. is it an active user?',
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        data = {
           'type': 'user_login',
           'status': 'fail',
           'msg' : str(sys.exc_info()[0] ),
        }
        
        
        return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def select_goal(request):
    context = RequestContext(request)
    try:
        if request.user.is_authenticated():
            data = {'user': request.user.id }
        else:
            data = {'msg' : 'user not found?'}
        return HttpResponse(json.dumps(data), content_type="application/json")

    except:
        data = {'msg': str(sys.exc_info()[0] )}

    return HttpResponse(json.dumps(data), content_type="application/json")



@login_required
def me(request):
    try:
        context = RequestContext(request)

        context['user'] = request.user

        context['goal'] = Goal.objects.get(user = request.user.id)
        context['time_logs'] = TimeLog.objects.filter(goal = context['goal'])
        return render_to_response('moocb/me.html', context)
    except:
       return HttpResponseRedirect('/addgoal/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@csrf_exempt
def add_time(request):
    
    context = RequestContext(request)
    print request
    print 'calling add time view' , request.POST #, (request.Post == True)
    data = {}
    if request.POST:

        print "post detected!"
        
       
        try:
            print "getting user id"
            user_id =  request.GET.get('user', None)
            print "getting goal id"
            goal_id = request.GET.get('goal', None)
            print "getting time id"
            time = request.GET.get('time', None)
            print 'user_id :', user_id, 'goal_id ', goal_id, 'time ', time
            print user_id and goal_id and time
            print 'pixxa'
            if user_id and goal_id and time:
                print 'if statement running'
                user = User.objects.get(id=user_id)
                print user
                goal = Goal.objects.get(id=goal_id)
                print "user", user, 'goal', goal
                print 'goal user', goal.user

                if goal.user.id == user.id:
                    print "goal time", goal.time_worked
                    goal.time_worked = goal.time_worked + int(time)
                    goal.save()
                    print " new goal time", goal.time_worked
                    time_left = goal.time_goal - goal.time_worked
                    data = {
                    'goal' : goal.name, 
                    'time_added' : time,
                    'new_goal_time': goal.time_worked,
                    'time_left_to_goal' : time_left,
                    'user' : user.username,

                    }
                else:
                    data = {'msg': 'goal and id dont match '}
                    print "not true"
               

             
            else:
                data = {'msg': 'not enough parameters included, make sure to include user goal and time'}
                print "not true"
            print 'after loop'

        except:
            print 'error'
            data = {'msg': str(sys.exc_info()[0] )}

        print 'pre return'
      
        
    else:
        raise Http404
    return HttpResponse(json.dumps(data), content_type="application/json")

        
    # 5483c154c5cbe516f21d5f08
    # 5483d7bec5cbe518fe34eb84
    # 5483d889c5cbe5190bc1d834

    # context['time'] = request.GET.get('time', 'no time found' )
    # context['user_id'] = request.user.id
   
    # return render_to_response('moocb/add.html', context)



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
            return HttpResponseRedirect('/addgoal/')
            #return render_to_response('moocb/me.html', context_instance=RequestContext(request))
    else:
        form = UserForm() 
    return render_to_response( 'moocb/adduser.html', {'form': form},  context_instance=RequestContext(request))

@login_required
def add_goal (request):

    context = RequestContext(request)
    if (Goal.objects.filter(user = request.user.id)):
        return HttpResponseRedirect('/me/')

    else:
        if request.method == "POST":
            form = GoalForm(request.POST)
            if form.is_valid():
                new_goal = Goal (user= request.user, **form.cleaned_data)
                new_goal.save()
                return HttpResponseRedirect('/me/')
        else:
            form = GoalForm() 

    return render_to_response( 'moocb/addgoal.html', {'form': form},  context_instance=RequestContext(request))


