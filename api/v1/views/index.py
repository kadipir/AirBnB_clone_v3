#!/usr/bin/python3

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route("/status")
def api_status():
    """status of api"""
    response = {'status':'OK'}
    return jsonify(response)


@app_views.route("/stats")
def get_stats():
    """retrieves the number of each objects by type"""
    stats = {
            "amenities" : storage.count("Amenity"),
            "cities" : storage.count("City"),
            "places" : storage.count("Place"),
            "reviews" : storage.count("Review"),
            "states" : storage.count("State"),
            "users" : storage.count("User")
            }
    return jsonify(stats)
