from flask import Flask, jsonify

app = Flask(__name__)

routes = [
    {'route': 'http://127.0.0.1/', 'description': 'Index containing a list of all routes'}
]


@app.route("/")
def index():
    return jsonify(routes)

