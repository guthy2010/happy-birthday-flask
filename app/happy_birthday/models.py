
from app.database import db

# Establish database tables

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    dateOfBirth = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, dateOfBirth):
        self.username = username
        self.dateOfBirth = dateOfBirth