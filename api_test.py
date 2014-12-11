import requests, json

#r = requests.post('https://salty-inlet-9116.herokuapp.com/add/?user=5483c08&time=1000000', data={'hi' : 'asda'})
r = requests.post('https://salty-inlet-9116.herokuapp.com/add/?user=2&time=50&goal=3', data={'hi' : 'asda'})

#and probs do something else with the response....
print r.text
