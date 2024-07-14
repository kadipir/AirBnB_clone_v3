#!/usr/bin/python3
"""
Flask application
"""

from os import getenv
from flask import Flask, jsonify
import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, root_dir)
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_engine(exception):
    """ method that calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """retrieves the number of each objects by type"""
    response = {"error" : "Not  found"}
    return jsonify(response), 404

if __name__ == "__main__":
    HOST = getenv('BNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run( debug = True, host = HOST, port = PORT, threaded = True)
