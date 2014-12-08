from django.contrib.auth.models import User
from moocb.models import  Goal
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')




class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ('name', 'time_goal', 'start_date', 'end_date', 'url')