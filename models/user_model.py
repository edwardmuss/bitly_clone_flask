from sqlalchemy import DateTime
from datetime import datetime
from flask_login import UserMixin
from core import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, username, password):
        self.username = username
        self.password = password