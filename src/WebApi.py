import MettlerToledo
from flask import Flask, jsonify

# set FLASK_APP=WebApi.py
# run python -m flask run

app = Flask("ScaleAPI")
scale = MettlerToledo.Scale()


@app.route('/getWeight')
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
        return jsonify({"status": scale.pingScale()})
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})


@app.route('/reset')
def reset():
    try:

    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})
