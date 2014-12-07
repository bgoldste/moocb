from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.
class Subscriber(models.Model):
	email_address = models.EmailField(unique=True)

	def __unicode__(self):
		return u'%s' % (self.email_address)	