from webapp import app
from flask import jsonify, render_template, flash, redirect, url_for, request
from webapp.forms import LoginForm
from webapp.models import User
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return jsonify({'This': 'is', 'A': 'test'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if(form.validate_on_submit()):
        user = User.load_user(form.username.data)
        if(user and User.check_password(user['Password'], form.password.data)):
            user_obj = User(username=user['Name'])
            login_user(user_obj)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash('Invalid username or password')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))