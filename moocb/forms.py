from django.contrib.auth.models import User
from moocb.models import  Goal, Incentive, get_end
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe
from django.forms import widgets

class UserWidget(widgets.TextInput):
    def render(self, name, value, attrs=None):
        return mark_safe(u'''<div class="entry container">
								
								<div class="col-xs-2">
								    <img class='form-pic' src="/static/moocb/email.png">

								</div>
								  
								<div class="col-xs-10">%s</div>
						    </div>


     ''' % (super(UserWidget, self).render(name, value, attrs)))

class PasswordWidget(widgets.TextInput):
    def render(self, name, value, attrs=None):
        return mark_safe(u'''<div class="entry container">
								
								<div class="col-xs-2">
								    <img class='form-pic' src="/static/moocb/lock.png">

								</div>
								  
								<div class="col-xs-10">%s</div>
						    </div>


     ''' % (super(PasswordWidget, self).render(name, value, attrs)))




class UserForm(ModelForm):
	
	class Meta:
		model = User
		fields = ( 'email', 'password')
	#username = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'text-center form-control entry'}))
	email = forms.CharField(widget=UserWidget(attrs={'placeholder': 'email', 'class': 'form-control text-center entry-2'}))
	password = forms.CharField(widget=PasswordWidget(attrs={'placeholder': 'password', 'type': 'password', 'class': 'form-control text-center entry-2'}))

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
	total_pledge = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter a Dollar value', 'class': 'text-center form-control entry'}))
	



		