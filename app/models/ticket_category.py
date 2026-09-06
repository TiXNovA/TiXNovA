#  TEMPORARY MODEL — Teeksha ke real Auth module se replace hoga (Day 6)
from app import db


class TicketCategory(db.Model):
    __tablename__ = "ticket_categories"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    category_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    quantity_sold = db.Column(db.Integer, default=0)

    def is_sold_out(self):
        return self.quantity_sold >= self.total_quantity

    def available_count(self):
        return self.total_quantity - self.quantity_sold