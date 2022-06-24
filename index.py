import flask
from flask import Flask, jsonify, request
from model.user import User
from model.user_repository import UserRepository
from model.club_repository import ClubRepository

app = Flask(__name__)

routes = [
    {
        'route': '/',
        'description': 'Index containing a list of all routes'
    },
    {
        'route': '/clubs',
        'description': 'Endpoint for providing all clubs data'
    },
    {
        'route': '/clubs/<club_id>',
        'description': 'Endpoint for providing singular club data'
    }
]


# TODO reformat into controllers
@app.route('/')
def index():
    return jsonify(routes)


@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    user = User(user_data)
    user_repository = UserRepository()
    user_repository.save(user)

    response = jsonify(user_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/clubs')
def clubs():
    club_repository = ClubRepository()
    clubs_list = club_repository.get_list()
    return jsonify(clubs_list)


@app.route('/clubs/<club_id>')
def club(club_id):
    club_repository = ClubRepository()
    club = club_repository.load_by_id(club_id)
    return jsonify(club)