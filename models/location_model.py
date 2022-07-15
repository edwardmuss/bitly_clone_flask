from email.policy import default
from sqlalchemy import DateTime, Integer
from datetime import datetime
from core import db

class Location(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    url_id = db.Column("url_id", db.Integer, nullable=False)
    country = db.Column("country", db.String())
    city = db.Column("city", db.String(10), nullable=False)
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, url_id, country, city):
        self.url_id = url_id
        self.country = country
        self.city = city