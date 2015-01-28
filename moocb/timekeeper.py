from moocb.models import Goal, User, TimeLog
import sys


def getTotalTime(name):
	try:
		user = User.objects.get(username = name)
		goal = Goal.objects.get(user=user)
		timelogs = TimeLog.objects.filter(goal=goal)
		return {'user': user ,'goal': goal.url, 'timelogs': timelogs}
	except:
		print "Unexpected error:", sys.exc_info()[0]
		return {'status': 'error', 'message': 'no user %s found' % name}