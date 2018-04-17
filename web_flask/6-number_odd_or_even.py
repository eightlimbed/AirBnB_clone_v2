#!/usr/bin/python3

'''This script starts a Flask web application with a variable route that has a
default value, routes for numbers, and a template'''

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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


@app.route('/number_template/<int:n>')
def number_template(n):
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
