import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///chess_game.db'  # Chemin vers le fichier SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optionnel, désactive les notifications de modification

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
