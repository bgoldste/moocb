from moocb.models import Goal, User, TimeLog
import sys


# def getTotalTime(name):
# 	try:
# 		user = User.objects.get(username = name)
# 		goal = Goal.objects.get(user=user)
# 		timelogs = TimeLog.objects.filter(goal=goal)
# 		return {'user': user ,'goal': goal.url, 'timelogs': timelogs}
# 	except:
# 		print "Unexpected error:", sys.exc_info()[0]
# 		return {'status': 'error', 'message': 'no user %s found' % name}


def addTime(goal, time):
	TimeLog(goal= goal, time_to_add= time).save()

def getTotalTime(goal):
	total = 0

	for log in TimeLog.objects.filter(goal=goal):
		total += log.time_to_add
	return total


