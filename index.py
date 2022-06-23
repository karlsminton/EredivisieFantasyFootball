from flask import Flask, jsonify, request
from model.user import User
from model.user_repository import UserRepository

app = Flask(__name__)

routes = [
    {
        'route': 'http://127.0.0.1/', 'description': 'Index containing a list of all routes'
    }
]


# TODO reformat into controllers
@app.route("/")
def index():
    return jsonify(routes)


@app.route('/register', methods=["POST"])
def register():
    user_data = request.get_json()
    User()
    UserRepository().save()
