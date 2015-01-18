from django.contrib.auth.models import User
from moocb.models import  Goal, Incentive, get_end
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget

class UserForm(ModelForm):
	
	class Meta:
		model = User
		fields = ( 'email', 'password')
	#username = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'text-center form-control entry'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'text-center form-control entry'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password', 'type': 'password', 'class': 'text-center form-control entry'}))

class GoalForm(ModelForm):
	class Meta:
		model = Goal
		fields = ( 'url', 'time_goal', 'end_date', )
	#name = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'name your course', 'class': 'text-center form-control entry'}))
	url= forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'https://class.coursera.org/db', 'class': 'text-center form-control entry'}))
	end_date =  forms.DateField(widget=SelectDateWidget(attrs={'class': 'form-control entry date-entry text-center'} ),initial= get_end)
	time_goal = forms.CharField( widget=forms.TextInput(attrs={ 'class': 'text-center form-control entry-small'}), initial= 5)


class IncentiveForm(ModelForm):
	class Meta:
		model = Incentive
		fields = ( 'total_pledge',)
	total_pledge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'How much you pledge to finish your goal', 'class': 'text-center form-control entry'}))
	



		