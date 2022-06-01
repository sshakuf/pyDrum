from flask import Flask
import threading
import drums

host_name = "0.0.0.0"
port = 23336
app = Flask(__name__)

theServer = threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# def flaskThread():
#     app.run()

def serverStop():
    theServer.stop()


def serverStart():
    theServer.start()


@app.route("/start")
def mixerStart():
    drums.Play(True)
    return "<p>Playing</p>"


@app.route("/stop")
def mixerStop():
    drums.Play(False)
    return "<p>Stopped</p>"
