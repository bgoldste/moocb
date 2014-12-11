import requests, json

#r = requests.post('https://salty-inlet-9116.herokuapp.com/add/?user=5483c08&time=1000000', data={'hi' : 'asda'})
r = requests.post('https://127.0.0.1:8000/add/?user=1&time=50&goal=1', data={'hi' : 'asda'})

#and probs do something else with the response....
print r.text
