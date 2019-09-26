from __future__ import print_function
from flask import Flask, jsonify, request
import os
import sys
import json

app = Flask(__name__)
@app.route("/freneticserver",methods=['GET', 'POST'])
def get_frenetic_server_info():
    content = request.json
    print(content)
    dataPlane()
    return '', 300

def dataPlane():
    myCmd1 = os.popen('eval $(opam config env)').read()
    os.system(myCmd1)
    myCmd2 = os.popen('frenetic -h').read()
    os.system(myCmd2)

if __name__ == "__main__":
    app.run(host='frenetic', port=80, debug=True)
