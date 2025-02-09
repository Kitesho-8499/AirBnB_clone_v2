#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def homePage():
    """a function to display hello HBNB at the route '/'"""
    return "Hello HBNB!"

if __name__ == '__main':
    app.run(debug=True, host='0.0.0.0', port='5000')
