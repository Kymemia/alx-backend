#!/usr/bin/env python3

"""
class definition for the configuration of Flask-Babel
"""


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
