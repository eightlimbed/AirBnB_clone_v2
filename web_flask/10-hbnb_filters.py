#!/usr/bin/python3

'''This script starts a Flask web application with a route for hbnb filters drop
down menu'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/hbnb_filters')
def states():
    states, cities, amenities = [], [], []
    for key, val in storage.all('State').items():
        states.append(val)
    for key, val in storage.all('City').items():
        states.append(val)
    for key, val in storage.all('Amenity').items():
        states.append(val)
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
