#!/usr/bin/python3

'''This script starts a Flask web application with a variable route that has a
default value, routes for numbers, and a template'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list')
def states_list():
    states = []
    for key, val in storage.all('State').items():
        states.append(val)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
