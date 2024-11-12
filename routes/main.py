from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/create_game')
def create_game():
    return render_template('create_game.html')

@bp.route('/settings')
def settings():
    return render_template('settings.html')
