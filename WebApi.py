import WeightComms
from flask import Flask, jsonify

#set FLASK_APP=WebApi.py
#run python -m flask run

app = Flask("ScaleAPI")
scale = WeightComms.scale()

@app.route('/')
def weightOnScale():
    try:
        return jsonify({"kg":scale.getWeight()})
    except Exception as e:
        return jsonify({"error":str(e)})


@app.route('/status')
def statusOnScale():
    return jsonify({"status": scale.getStatus()})


