#!/usr/bin/env python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with States and their Cities."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
