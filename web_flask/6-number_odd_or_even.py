#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_pythonText(text="is cool"):
    if text != "is cool":
        text = text.replace("_", " ")
    return "Python %s" % (text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_render(n):
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def template_render_even_odd(n):
    return render_template("6-number_odd_or_even.html", num=n)


# Start Flask web application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
