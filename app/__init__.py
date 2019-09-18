from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .auth import auth as auth
    from .main import main as main
    app.register_blueprint(auth)
    app.register_blueprint(main)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    return app