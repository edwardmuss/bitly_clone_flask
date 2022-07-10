from flask import Flask, redirect, render_template, request, url_for
from models.url_model import Urls
from core.chars_regenerate import shorten_url
from core import app
from core.routes import web
from flask_moment import Moment

moment = Moment(app)
moment = Moment()
moment.init_app(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
