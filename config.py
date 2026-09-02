import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "tixnova-secret-key"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(BASE_DIR, "tixnova.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False