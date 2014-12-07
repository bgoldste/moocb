import requests, json

r = requests.post('http://127.0.0.1:8000/add/?user=5483c154c5cbe516f21d5f08&time=1000000')

#and probs do something else with the response....
print r.text
