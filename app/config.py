class Config:
    SECRET_KEY = "tixnova-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///tixnova.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    QR_ROTATION_SECONDS = 30

    DEFAULT_RESALE_CAP_PERCENT = 10