from flask import Flask, jsonify, redirect, render_template, request, url_for
from models.url_model import Urls
from core.chars_regenerate import shorten_url
from core import *

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form["url"]
        found_url = Urls.query.filter_by(long=url_received).first()

        if found_url:
            # return redirect(url_for("display_short_url", url=found_url.short))
            # return found_url
            short_url = found_url.short
            # return jsonify({'output':'Your Name is ' + url_received + ', right?'})
        else:
            short_url = shorten_url()
            print(short_url)
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            # return redirect(url_for("display_short_url", url=short_url))
        return jsonify({'output': base_url + '/' + short_url})
        # return jsonify({'error' : 'Error!'})
    else:
        return render_template('index.html')

@app.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return f'<h1>Url doesnt exist</h1>'

@app.route('/all-urls')
def display_all():
    return render_template('all-urls.html', vals=Urls.query.all(), base_url=base_url)