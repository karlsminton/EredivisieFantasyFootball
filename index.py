from flask import Flask, jsonify, request
from model.user import User
from model.user_repository import UserRepository
from model.club import Club
from model.club_repository import ClubRepository

app = Flask(__name__)

routes = [
    {
        'route': 'http://127.0.0.1/', 'description': 'Index containing a list of all routes'
    }
]


# TODO reformat into controllers
@app.route('/')
def index():
    return jsonify(routes)


@app.route('/register', methods=["POST"])
def register():
    user_data = request.get_json()
    User()
    UserRepository().save()


@app.route('/clubs')
def clubs():
    club_repository = ClubRepository()
    clubs_list = club_repository.get_list()
    return jsonify(clubs_list)
