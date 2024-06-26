#!/usr/bin/env python3
"""Module for home page"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home_page() -> str:
    """renders index.html"""
    return render_template('0-index.html')

if __name__== '__main__':
    app.run(debug=True)