from flask import Flask, request
from model import model_min_vertex_cover
from config import static_folder

app = Flask(__name__, static_folder=static_folder)


@app.route('/file/<path:path>')
def static_proxy(path):
    print(path)

    return app.send_static_file(path)


@app.route('/vertexcover', methods=['POST'])
def vertex_cover():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        res = model_min_vertex_cover(request.json)

        return str(res)


@app.route('/debug', methods=['POST', 'GET'])
def display():

    if request.method == 'POST' and request.headers['Content-Type']=='application/json':
        return str(request.json)

    return str(request)


app.run(port=8000)