from flask import Blueprint, render_template, request

bp = Blueprint('game', __name__)

@bp.route('/game/<int:game_id>')
def game(game_id):
    # Load and display game
    pass
