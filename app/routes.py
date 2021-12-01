from flask import render_template

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
