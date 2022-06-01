import os.path
from flask import Flask, Response
import threading
import drums
import json


host_name = "0.0.0.0"
port = 23336
app = Flask(__name__)

theServer = threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False))


@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"

# def flaskThread():
#     app.run()

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))+"/html/"

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/', methods=['GET'])
def metrics():  # pragma: no cover
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_resource(path):  # pragma: no cover
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)


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

def append(name, val, addComma = False):
    str = ""
    str += '"' + name + '" : "' + val + '"'
    if addComma:
        str += ', '
    return str

@app.route("/status")
def getStatus():
    data = '{' 
    data += append("num_instruments", str(drums.num_instruments), True)
    data += append("beats", str(drums.beats), True)
    data += append("bpm", str(drums.bpm), True)
    data += append("clicks", str(drums.clicks))
    data += '}'
    return data

@app.route("/beats/<int:val>")
def setBeats(val):
    print("val" + str(val))
    if (val > 0 and val < 65):
        drums.beats = int(val//1)
    data = '{' 
    data += append("beats", str(drums.beats))
    data += '}'
    return data

@app.route("/bpm/<int:val>")
def setBPM(val):
    print("val" + str(val))
    if (val > 0 and val < 1000):
        drums.bpm = int(val//1)
    data = '{' 
    data += append("bpm", str(drums.bpm), True)
    data += '}'
    return data

@app.route("/set/<int:val_x>/<int:val_y>")
def setClick(val_x, val_y):
    if (val_x >= 0 and val_x < drums.beats and val_y >= 0 and val_y < drums.num_instruments):
        drums.clicks[val_y][val_x] = 1
    return str(drums.clicks[val_y][val_x])

@app.route("/get/<int:val_x>/<int:val_y>")
def getClick(val_x, val_y):
    return str(drums.clicks[val_y][val_x])