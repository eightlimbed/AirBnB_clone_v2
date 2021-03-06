#!/usr/bin/python3

'''This script starts a Flask web application with a variable route that has a
default value and a route for numbers'''

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def py_route(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number_route(n):
    if type(n) is int:
        return str(n) + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
