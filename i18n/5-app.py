#!/usr/bin/env python3
"""
A Flask web application that mocks a user login system and displays.
"""

from flask import Flask, request, g, render_template
from typing import Optional, Dict, Any

app = Flask(__name__)

users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


@app.before_request
def before_request() -> None:
    """
    Set user information globally before each request.
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    Render the index page.
    :return: Rendered HTML content.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
