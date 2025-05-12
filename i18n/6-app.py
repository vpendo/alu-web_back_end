#!/usr/bin/env python3
"""
A Flask web application that mocks a user login system.
"""

from typing import Optional, Dict, Any
from flask import Flask, request, g, render_template

app = Flask(__name__)

users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

SUPPORTED_LOCALES = ['en', 'fr']


def get_user() -> Optional[Dict[str, Any]]:
    """
    Get user by ID from the users dictionary.
    :return: A user dictionary if found, otherwise None.
    """
    try:
        user_id: Optional[str] = request.args.get('login_as')
        if user_id is not None:
            return users.get(int(user_id))
    except (ValueError, TypeError):
        return None
    return None


def get_locale() -> str:
    """
    Determine the best locale to use based on URL parameters, user settings.
    :return: The best locale to use.
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale

    # Locale from user settings
    if g.user and g.user['locale'] in SUPPORTED_LOCALES:
        return g.user['locale']

    # Locale from request headers
    locale = request.accept_languages.best_match(SUPPORTED_LOCALES)
    if locale:
        return locale

    # Default locale
    return 'en'


@app.before_request
def before_request() -> None:
    """
    Set user and locale information globally before each request.
    """
    g.user = get_user()
    g.locale = get_locale()


@app.route('/')
def index() -> str:
    """
    Render the index page.
    :return: Rendered HTML content.
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
