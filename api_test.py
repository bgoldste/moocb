import requests, json

r = requests.post('http://127.0.0.1:8000/add/?user=5483c08&time=1000000', data={'hi' : 'asda'})

#and probs do something else with the response....
print r.text
