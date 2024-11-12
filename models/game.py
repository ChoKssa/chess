from . import db

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    player_white = db.Column(db.Integer, db.ForeignKey('users.id'))
    player_black = db.Column(db.Integer, db.ForeignKey('users.id'))
    moves = db.Column(db.Text)  # Stocke les coups en texte pour le moment
