#!/usr/bin/env python3

"""
implementation of get_locale function with babel.locale selector.
request.accept_languages is used to determine
the best match with our supported languages
"""
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)

babel = Babel(app)


def get_locale():
    """
    method definition that determines the best match
    with the supported languages.
    """
    return request.accept_languages.best_match(["en", "fr"])


babel.localeselector_func = get_locale


if __name__ == "__main__":
    app.run(debug=True)
