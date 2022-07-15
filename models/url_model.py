from email.policy import default
from sqlalchemy import DateTime, Integer
from datetime import datetime
from core import db

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, nullable=True, default=0)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10), nullable=False, unique=True)
    hits = db.Column("hits", db.Integer, nullable=False, default=0)
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, user_id, long, short, hits=0):
        self.user_id = user_id
        self.long = long
        self.short = short
        self.hits = hits