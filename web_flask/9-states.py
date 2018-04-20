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


@app.route('/states')
def states():
    states = []
    for key, val in storage.all('State').items():
        states.append(val)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_by_id(id=None):

    # Get all cities that match with state_id (from <uuid:id>)
    cities = []
    for key, val in storage.all('City').items():
        if val.state_id == str(id):
            cities.append(val)

    # Get the name of the state
    name = None
    for key, val in storage.all('State').items():
        if val.id == str(id):
            name = val.name

    # set err and return if the id didn't match any states
    if len(cities) == 0 and name == None:
        return render_template('9-states.html', err=1)

    return render_template('9-states.html', name=name, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
