#!/usr/bin/python3
"""
returns json
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', strict_slashes=False)
def status():
    """ returns status """
    return jsonify({"status": "OK"})

@app_views.route("/stats", strict_slashes=False)
def stats():
    """ retrieves the number of each objects by type"""
    d = {"amenities": storage.count("Amenity"), "cities": storage.count("City"), 
	"places": storage.count("Place"), "reviews": storage.count("Review"),
	"states": storage.count("Stata"), "users": storage.count("User")}
    return jsonify(d)    
