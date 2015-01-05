from django.db import models
from djangotoolbox.fields import ListField
from moocb import settings



from django.core.validators import MaxValueValidator, MinValueValidator
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
	user = models.OneToOneField(User)

	name = models.CharField(max_length=300)
	url = models.URLField(max_length=300)
	time_goal = models.PositiveIntegerField( null=True)

	start_date = models.DateField(default=datetime.now)
	end_date = models.DateField(default=datetime(2015, 2, 14, 0, 0))
	time_worked = models.PositiveIntegerField(default=0)

	last_worked = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return u'%s' % (self.name)	



class Incentive(models.Model):
	goal = models.OneToOneField(Goal)

	#
	total_pledge = models.PositiveIntegerField(default=3000)
	amount_refunded = models.PositiveIntegerField(default= 0)

	refund_increment = models.FloatField(default= 0.25, validators = [MinValueValidator(0.0),])

	is_paid = models.BooleanField(default=False)



	def __unicode__(self):
		return u'Incentive for %s: %s' % (self.goal.name, self.total_pledge)


	@property
	def total_dollars(self):
		return '%.2f' % ( self.total_pledge / 100.0)




class TimeLog(models.Model):

	#todo - order by date
	
	goal = models.ForeignKey(Goal)

	date = models.DateField(default=datetime.now)
	time_to_add = models.PositiveIntegerField()

	def __unicode__(self):
		return u'%s : %s : time added: %d' % (self.goal.name, self.date, self.time_to_add)	

	class Meta:
		ordering = ["date"]













