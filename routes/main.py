from flask import Blueprint, render_template, redirect, url_for, request

bp = Blueprint('main', __name__)

parties = []

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/create_game', methods=['POST'])
def create_game():
    party_name = f"Party {len(parties) + 1}"
    parties.append(party_name)
    return redirect(url_for('main.join_party'))

@bp.route('/join-party')
def join_party():
    return render_template('join_party.html', parties=parties)

@bp.route('/waiting')
def waiting():
    return render_template('waiting.html')

@bp.route('/settings')
def settings():
    return render_template('settings.html')
