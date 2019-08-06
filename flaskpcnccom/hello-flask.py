from __future__ import print_function
from flask import Flask, jsonify, request
import os
import sys
import json

app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

os.environ["PATH"] += os.pathsep +  "/home/pi/.opam/default/bin/frenetics"
os.environ["PATH"] += os.pathsep + "/home/pi/.opam/default/bin/frenetic.openflow"

@app.route("/pcncserver")
def get_pcnc_server_info():
    myCmd = os.popen('frenetic help').read()
    os.system(myCmd)
    app.logger.info(myCmd)
    return myCmd
#    return jsonify(incomes)

@app.route('/pcncserver', methods=['POST'])
def provide_pcnc_server_info():
#  os.system('')
#  print(request.get_json(), file=sys.stderr)
#  print(request.get_json())
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    data = json.loads(request.data)
    app.logger.info(data)
    print(data["somekey"])
    return '', 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


