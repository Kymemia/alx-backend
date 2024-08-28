#!/usr/bin/env python3

"""
get_locale function that detects if the incoming requests contain
a locale argument and if said value is a supported locale, return it.
Else, resort to the previous default behavior
"""
from flask import request, g, Flask, render_template
from flask_babel import Babel
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    class definition that contains the app's configurations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

def get_locale():
    """
    function definition
    """
    locale = request.args.get('locale')
    logging.debug(f"Requested locale: {locale}")
    if locale and locale in app.config['LANGUAGES']:
        logging.debug(f"Using locale from URL: {locale}")
        return locale
    best_match = request.accept_languages.best_match(app.config["LANGUAGES"])
    logging.debug(f"Best match from header: {best_match}")
    return best_match

babel.localeselector_func = get_locale

@app.route('/')
def index():
    """
    method definition to render an index file
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
