from flask import Flask, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os

base_url = "http://127.0.0.1:5000"

app = Flask(__name__, static_folder="../static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shorty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'

db = SQLAlchemy(app)

# create tables
@app.before_first_request
def create_tables():
    db.create_all()
