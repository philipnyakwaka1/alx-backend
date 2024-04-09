#!/usr/bin/env python3
"""Module for home page"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
app = Flask(__name__)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
#babel = Babel(app)


#@babel.localeselector
def get_locale():
    """return best match"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)
@app.route('/')
def home_page() -> str:
    """renders index.html"""
    return render_template('3-index.html',
                           home_title=_("Welcome to Holberton"),
                           home_header=_("Hello world!"))


if __name__ == '__main__':
    app.run(debug=True)
