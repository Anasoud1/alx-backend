#!/usr/bin/env python3
"""basic Flask app """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def get_index():
    """render a basic html file"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
