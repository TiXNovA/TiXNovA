#  TEMPORARY MODEL — Teeksha ke real Auth module se replace hoga (Day 6)
# from datetime import datetime
from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="buyer")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)