from flask import Flask, render_template
from models.url_model import Urls
from core.chars_regenerate import shorten_url
from core import app, db

@app.route("/")
def hello_world():
    return render_template('index.html')
