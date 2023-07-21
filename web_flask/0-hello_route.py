#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
# Create Flask application
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Start Flask web application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
