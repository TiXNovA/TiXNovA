from app import create_app, db
from app.models.user import User
from app.models.event import Event
from app.models.ticket_category import TicketCategory
from app.models.ticket import Ticket

app = create_app()

with app.app_context():
    db.create_all()
    print("All Day 2 models created successfully!")

    import sqlite3
    conn = sqlite3.connect("instance/tixnova.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Tables in database:", cursor.fetchall())
    conn.close()