from flask import Flask
from config import Config
from routes import auth, main, game

app = Flask(__name__)
app.config.from_object(Config)

# Enregistrer les Blueprints sans initialiser la base de données
app.register_blueprint(auth.bp)
app.register_blueprint(main.bp)
app.register_blueprint(game.bp)

if __name__ == '__main__':
    app.run(debug=True)
