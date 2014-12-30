from moocb.models import Goal, User
import requests, json
from django.core.management.base import BaseCommand, CommandError







#r = requests.post('https://salty-inlet-9116.herokuapp.com/add/?user=5483c08&time=1000000', data={'hi' : 'asda'})
#r = requests.post('https://salty-inlet-9116.herokuapp.com/add/?user=2&time=50&goal=3', data={'hi' : 'asda'})
#r = requests.post('http://127.0.0.1:8000/add/?user=1&time=50&goal=1', data={'hi' : 'asda'})


def add_test():
	for i in range(5):
		for j in range(5):
			url = 'https://salty-inlet-9116.herokuapp.com/add/?user=%d&time=50&goal=%d' % (i, j)
			r = requests.post(url,  data={'hi' : 'asda'})

							   
			#r = requests.post('http://127.0.0.1:8000/add/?user=%d&time=50&goal=%d' % (i, j),  data={'hi' : 'asda'})
			print 'user ', i , 'goal ', j, r.text, url 


def login_test():
	
	print 'login_test'
	#for user in User.objects.all():
	#url = 'http://127.0.0.1:8000/login_json/' 
	url = "https://salty-inlet-9116.herokuapp.com/login_json/"
	# print user.username
	# print user.password
	print url
	r = requests.post(url, data = {'username':'test', 'password': 1})
	print r.text

def select_goal_test():
	print 'running select_goal_test'
	url = 'http://127.0.0.1:8000/select_goal/'
	print url 
	r = requests.post(url)
	print r.text




class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
    	parser.add_argument('poll_id', nargs='+', type=int)
    def handle(self, *args, **options):
    	login_test()
    	select_goal_test()