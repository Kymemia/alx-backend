#!/usr/bin/env python3
"""
class definition
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_CHOICE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    or app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """
    method definition to render index.html'
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
