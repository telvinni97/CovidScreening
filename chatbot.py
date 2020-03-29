from flask import Flask
from flask import send_file
from flask import jsonify, request
import json

import http.client
import mimetypes
import json

app = Flask(__name__)

@app.route('/mental', methods=['POST'])
def mental_send():
    return send_file('responses/mental.json')

@app.route('/tips', methods=['POST'])
def tips_send():
    return send_file('responses/tips.json')

@app.route('/pass_time', methods=['POST'])
def pass_time_send():
    return send_file('responses/pass_time.json')

@app.route('/help', methods=['POST'])
def help_send():
    return send_file('responses/help.json')

@app.route('/info', methods=['POST'])
def info_send():
    return send_file('responses/info.json')

@app.route('/stats', methods=['POST'])
def stats_send():
    conn = http.client.HTTPSConnection("corona.lmao.ninja")
    payload = ''
    headers = {}
    conn.request("GET", "/all", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)

    numCases = data["cases"]
    numDeaths = data["deaths"]
    numRecovered = data["recovered"]

    message = (
        f'There are {numCases} confirmed cases.'
        f' There have been {numDeaths} deaths.'
        f' There have been {numRecovered} recoveries.'
    )

    return jsonify(actions=[{'say': {'speech': message}}])
