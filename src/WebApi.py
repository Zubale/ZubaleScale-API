import MettlerToledo, threading
from flask import Flask, jsonify
from socketserver import TCPServer
from ScaleHandler import ScaleHandler

# set FLASK_APP=WebApi.py
# run python -m flask run

def launchScaleServer():
    try:
        syslog = TCPServer((ScaleHandler.IP_AD, ScaleHandler.TCP_PORT), ScaleHandler)
        print("Scale server starts")
        syslog.serve_forever(poll_interval=1)

    except Exception as e:
        print("Error", e)



t = threading.Thread(target=launchScaleServer)
t.daemon = True
t.start()
scale = MettlerToledo.Scale()
app = Flask("ScaleAPI")




@app.route('/getWeight')
def weightOnScale():
    try:
        return jsonify({"kg": scale.getWeight})
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
        scale.reset()
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})

@app.route('/reboot')
def reset():
    try:
        exit()
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})
