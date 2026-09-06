#  TEMPORARY MODEL — Teeksha ke real Auth module se replace hoga (Day 6)
# from datetime import datetime
from datetime import datetime
from app import db


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    organizer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    resale_cap_percent = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)