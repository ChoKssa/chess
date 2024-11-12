from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importez les modèles ici pour qu'ils soient disponibles via `models`
from .user import User
from .game import Game
