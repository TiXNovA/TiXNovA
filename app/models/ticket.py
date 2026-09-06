from datetime import datetime
from app import db


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("ticket_categories.id"), nullable=False)
    current_owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    original_price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(
        db.Enum("active", "resold", "used", "cancelled", name="ticket_status"),
        default="active", nullable=False
    )
    totp_secret = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)