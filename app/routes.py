from flask import render_template, redirect, flash, url_for

from app.forms import LoginForm
from . import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lim_QgyG'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, title='Lim-QgyG', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Login requested for user {},remember_me={}'.format(login_form.username.data, login_form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=login_form, title="登录")


