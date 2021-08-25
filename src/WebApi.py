import src.MettlerToledo as MettlerToledo, threading
from flask import Flask, jsonify
from socketserver import TCPServer
from src.ScaleHandler import ScaleHandler

# set FLASK_APP=WebApi.py
# run python -m flask run

def launchScaleServer():
    try:
        print("Scale server starts")
        syslog = TCPServer((ScaleHandler.IP_AD, ScaleHandler.TCP_PORT), ScaleHandler)
        syslog.serve_forever(poll_interval=1)

    except Exception as e:
        print("Error", e)


print("Starting tcp sever")
t = threading.Thread(target=launchScaleServer)
t.daemon = True
t.start()
print("Tcp server running")

print("Starting rest server")

print("Instantiating scale controller")
scale = MettlerToledo.Scale()
print("Finished instantiating scale controller")

app = Flask("ScaleAPI")

print("Started rest server")




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


@app.route('/resetScale')
def reset():
    try:
        scale.reset()
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})

@app.route('/rebootScale')
def reboot():
    try:
        exit()
    except Exception as e:
        return jsonify({"error": str(e), "info": str(e.__traceback__)})
