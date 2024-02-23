#!/usr/bin/python3
import flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def homePage():
    """a function to display hello HBNB at the route '/'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnbPage():
    """a function to display HBNB at the route '/hbnb"""
    return "HBNB"

if __name__ == '__main':
    app.run(debug=True, host='0.0.0.0', port='5000')
