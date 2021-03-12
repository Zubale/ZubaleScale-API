import WeightComms
from flask import Flask, jsonify

#set FLASK_APP=WebApi.py
#run python -m flask run

app = Flask("ScaleAPI")
port = WeightComms.scale.checkPorts()[0]
scale = WeightComms.scale(port=port.name)

@app.route('/')
def weightOnScale():
    try:
        return jsonify({"kg":scale.getWeight()})
    except Exception as e:
        return jsonify({"error":str(e)})


@app.route('/status')
def statusOnScale():
    return jsonify({"status": scale.getStatus()})

@app.route('/ports')
def portsOnPC():
    print(scale.checkPorts())
    return jsonify({"ports": [x.name] for x in scale.checkPorts()})

def setPort():
    #todo port change and reload
    pass


