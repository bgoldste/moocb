from django.contrib import admin
from moocb.models import Subscriber, UserInfo, Goal
from django.contrib.auth.models import User



admin.site.register(Subscriber)
admin.site.register(UserInfo)
admin.site.register(Goal)