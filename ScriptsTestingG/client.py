import requests as req
import json

with open('example_1.json')as f:
    data = json.load(f)

print(data)

urlp = 'http://172.17.0.2:80/pcncserver'
resp = req.post(urlp,json= data)
