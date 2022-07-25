from flask import Flask, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_redmail import RedMail
import os

base_url = os.getenv("BASE_URL")

app = Flask(__name__, static_folder="../static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'

# RedMail configs
app.config["EMAIL_HOST"] = "smtp.zoho.com"
app.config["EMAIL_PORT"] = 587
app.config["EMAIL_USERNAME"] = "info@cloudrebue.co.ke"
app.config["EMAIL_PASSWORD"] = "Blogger@99%"
app.config["EMAIL_SENDER"] = "info@cloudrebue.co.ke"
email = RedMail(app)

# Flask Mail Configs
app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'info@cloudrebue.co.ke'
app.config['MAIL_PASSWORD'] = 'Blogger@99%'
mail = Mail(app)

db = SQLAlchemy(app)

# create tables
@app.before_first_request
def create_tables():
    db.create_all()
