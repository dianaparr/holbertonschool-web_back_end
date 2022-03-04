#!/usr/bin/env python3
""" Module to basic Babel setup """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ This class is used to configure Flask app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def welcome():
    """ A single route / """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ Function get locate to determine the best match
        with supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
