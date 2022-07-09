from flask import Flask, render_template
from models.url_model import Urls

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
