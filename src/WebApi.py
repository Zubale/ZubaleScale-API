import WeightComms
from flask import Flask, jsonify

# set FLASK_APP=WebApi.py
# run python -m flask run

app = Flask("ScaleAPI")
port = WeightComms.scale.checkPorts()[0]
scale = WeightComms.scale(port=port.name)


@app.route('/')
def weightOnScale():
    try:
        return jsonify({"kg": scale.getWeight()})
    except TypeError as e:
        return jsonify({"error": "TyperError: " + str(e)})
    except FloatingPointError as e:
        return jsonify({"error": "ValueError: " + str(e)})
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})


@app.route('/status')
def statusOnScale():
    try:
        return jsonify({"status": scale.getStatus()})
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})


@app.route('/ports')
def portsOnPC():
    try:
        print(scale.checkPorts())
        return jsonify({"ports": [x.name] for x in scale.checkPorts()})
    except IOError as io:
        return jsonify({"error": "Port Error: " + str(io)})
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})


@app.route('/reset')
def reset():
    try:
        port = WeightComms.scale.checkPorts()[0].name
        scale.setPort(port)
        return jsonify({"port": port})
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})
