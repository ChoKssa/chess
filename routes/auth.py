from flask import Blueprint, render_template, request

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for login (no DB for now)
        return redirect('/home')
    return render_template('login.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Logic for signup (no DB for now)
        return redirect('/login')
    return render_template('signup.html')
