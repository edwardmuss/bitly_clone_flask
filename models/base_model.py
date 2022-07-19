from sqlalchemy import DateTime, Integer
import json
import datetime
import jwt
from flask_login import UserMixin
from core import db, app

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.now)
    updated_at = db.Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def get_reset_token(self, expiration=300):
        reset_token = jwt.encode(
            {
                "user_id": self.id,
                "exp": datetime.datetime.utcnow()
                        + datetime.timedelta(seconds=expiration)
            }, 
        app.config['SECRET_KEY'],
        algorithm="HS256"
        )
        return reset_token

    @staticmethod
    def verify_reset_token(token):
        try:
            data = jwt.decode(
                token,
                app.config['SECRET_KEY'],
                leeway=datetime.timedelta(seconds=10),
                algorithms=["HS256"]
            )
            user_id = jsonify(data['user_id'])
            # id = int(user_id)
            data_json = json.dumps(data)
            id  = data_json[12]
        except:
            return None
        return User.query.get(id)
        # return jsonify(data['user_id'])

    def __init__(self, username, email, image_file, password):
        self.username = username
        self.email = email
        self.image_file = image_file
        self.password = password

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('user.id'), nullable=True, default=0)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10), nullable=False, unique=True)
    hits = db.Column("hits", db.Integer, nullable=False, default=0)
    created_at = db.Column(DateTime, default=datetime.datetime.now)
    updated_at = db.Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self, user_id, long, short, hits=0):
        self.user_id = user_id
        self.long = long
        self.short = short
        self.hits = hits

class Location(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    url_id = db.Column("url_id", db.Integer, db.ForeignKey('urls.id_'), nullable=False)
    country = db.Column("country", db.String())
    city = db.Column("city", db.String(10), nullable=False)
    created_at = db.Column(DateTime, default=datetime.datetime.now)
    updated_at = db.Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self, url_id, country, city):
        self.url_id = url_id
        self.country = country
        self.city = city