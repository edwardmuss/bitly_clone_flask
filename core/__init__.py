from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

base_url = "http://127.0.0.1:5000/"

app = Flask(__name__, static_folder="../static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shorty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# create tables
@app.before_first_request
def create_tables():
    db.create_all()
