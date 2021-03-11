import WeightComms
from flask import Flask, jsonify

#set FLASK_APP=WebApi.py
#run python -m flask run

app = Flask("ScaleAPI")
scale = WeightComms.scale()

@app.route('/')
def weightOnScale():
    #todo errors
    return jsonify({"kg":scale.getWeight()})


@app.route('/status')
def statusOnScale():
    return jsonify({"status": scale.getStatus()})


