from django.db import models
from djangotoolbox.fields import ListField

from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Subscriber(models.Model):
	email_address = models.EmailField(unique=True)

	def __unicode__(self):
		return u'%s' % (self.email_address)	

class UserInfo(models.Model):
    user = models.OneToOneField(User)
    goal = models.CharField(max_length=300)
    def __unicode__(self):
    	return u'%s' % (self.user)	

class Goal(models.Model):
	user = models.ForeignKey(User)

	name = models.CharField(max_length=300)
	url = models.CharField(max_length=100)

	start_date = models.DateField(default=datetime.now)
	end_date = models.DateField()
	time_worked = models.IntegerField(default=0)
	last_worked = models.DateField(blank=True, null=True)
	def __unicode__(self):
		return u'%s' % (self.name)	