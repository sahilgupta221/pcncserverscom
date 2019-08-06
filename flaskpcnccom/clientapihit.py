#!/usr/bin/env python3

import requests as req
import json

myobj = {'somekey': 'myvalue'}
urlp = 'http://pcnc1.local/pcncserver'
#resp = req.post(urlp, data = json.dumps(myobj))

resp = req.request(method='GET', url="http://pcnc1.local/pcncserver")
print(resp.text)
#print(resp.json())

