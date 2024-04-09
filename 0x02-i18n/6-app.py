#!/usr/bin/env python3
"""Module for home page"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_requests():
    """executed before all other functions"""
    user = get_user()
    g.user = user


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """return best match"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home_page() -> str:
    """renders index.html"""
    if g.user:
        msg = _("You are logged in as %(username)s.", username=g.user.name)
    else:
        msg = _("You are not logged in.")
        print('Hey')
    return render_template('5-index.html',
                           home_title=_("Welcome to Holberton"),
                           home_header=_("Hello world!"), msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
