#!/usr/bin/env python3
"""Module for home page"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page() -> str:
    """renders index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
