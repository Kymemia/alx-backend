#!/usr/bin/env python3

"""
instantiation of the Babel object in my app
that's stored in a module-level named, babel.
"""
from flask_babel import Babel
from flask import Flask, render_template, request
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    method definition to configure available languages in my app.
    """
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    return best_match if best_match else app.config['BABEL_DEFAULT_LOCALE']


babel.localeselector_func = get_locale


@app.route('/')
def index():
    """
    method definition that renders index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
