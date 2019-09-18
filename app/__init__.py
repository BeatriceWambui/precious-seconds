from flask import Flask


def create_app():
    app = Flask(__name__)
    from .auth import auth as auth
    from .main import main as main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app