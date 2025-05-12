#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, render_template, request
from os import getenv
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration for languages and time zone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Selects the best matching locale from the user's browser preferences."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """hello world"""
    return render_template("3-index.html", message="Welcome to Holberton")


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
