import json
from urllib.request import urlopen
from flask import Flask, jsonify, redirect, render_template, request, url_for
from models.location_model import Location
from models.url_model import Urls
from core.chars_regenerate import shorten_url_generate
from flask_login import login_required, current_user
from core.auth import *
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
            short_url = shorten_url_generate()
            print(short_url)
            if current_user.is_authenticated:
                user_id = current_user.id
            else:
                user_id = 0
            hits = 0
            new_url = Urls(user_id, url_received, short_url, hits)
            db.session.add(new_url)
            db.session.commit()
            # return redirect(url_for("display_short_url", url=short_url))
        return jsonify({'output': base_url + '/' + short_url})
        # return jsonify({'error' : 'Error!'})
    else:
        return render_template('index.html')

@app.route('/<short_url>')
def redirection(short_url):
    qry = Urls.query.filter_by(short=short_url).first()
    url = 'http://api.ipstack.com/{}?access_key=f9b547690e6c34ecc473436fa95d132c'.format("102.167.67.171")
    # request.remote_addr
    response = urlopen(url)
    data = json.load(response)
    country = data['country_name']
    city = data['city']

    if qry:
        url_id =qry.id_
        hits =qry.hits
        qry.hits =  hits+1
        db.session.merge(qry)
        db.session.commit()

        user_location = Location(url_id, country, city)
        db.session.add(user_location)
        db.session.commit()

        return redirect(qry.long)
    else:
        return f'<h1>Url doesnt exist</h1>'

@app.route('/all-urls')
def display_all():
    return render_template('all-urls.html', vals=Urls.query.all(), base_url=base_url)

@app.route('/user-location')
def user_location():
    return render_template('all-locations.html', vals=Location.query.all(), base_url=base_url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(request.referrer)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
        flash('Username or Password is incorrect', 'error')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('You have sucessfully Registered, Please Login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('index.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been sucessfully Logged out, Please Login again.', 'success')
    return redirect(url_for('login'))
