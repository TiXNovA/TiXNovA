from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    @app.route("/")
    def home():
        return "Welcome to TiXNovA!"

    return app


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
    