#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    path = '8-cities_by_states.html'
    states = storage.all(State)

    # sort State object alphabetically by name
    # sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
