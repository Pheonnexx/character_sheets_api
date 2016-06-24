from flask import jsonify
from app import app


@app.route('/')
@app.route('/hello')
def index():
    message = "Hello"
    return message


@app.route('/character/<name>')
def character(name):
    return_character = _get_character(name)
    return jsonify(return_character)


def _get_character(name):
    return_character = {
        "name": name,
        "character_name": "Erica",
        "game_system": "Dungeons and Dragons 5th",
        "character_details": {
            "level": 5,
            "race": "dwarf"
        }
    }
    return return_character
