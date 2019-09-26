import os
import sys
import json
import requests as req
import time

app = Flask(__name__)

@app.route("/pcncserver",methods=['GET', 'POST'])
def get_pcnc_server_info():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    content = request.json
    print(content)
    if bisimulator(content) is True:
        print('Hit Frenetic...')
        hitFrenetic(content)

    return '', 300


def bisimulator(data):
    print('In Bisimulation')
    print(data)
    time.sleep(5)
    return True

def hitFrenetic(data):
    urlp = 'http://172.17.0.3:80/freneticserver'
    resp = req.post(urlp,json= data)

if __name__ == "__main__":
    app.run(host='pcnc', port=80, debug=True)
