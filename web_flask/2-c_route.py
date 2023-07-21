#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from markupsafe import escape
# Create Flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_cText(text):
    text = text.replace("_", " ")
    return "C %s" % (text)


# Start Flask web application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
