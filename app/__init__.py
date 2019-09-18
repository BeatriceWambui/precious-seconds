from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .auth import auth as auth
    from .main import main as main
    app.register_blueprint(auth)
    app.register_blueprint(main)
    db.init_app(app)
    return app