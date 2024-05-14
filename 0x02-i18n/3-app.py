#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Flask Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """function to determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index3() -> str:
    """return index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
