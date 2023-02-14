#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from os import getenv
from api.v1.views import app_views
from models import storage
from flask import Flask, Blueprint, jsonify
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session"""
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    """returns a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404

def page_not_found(e):
if __name__ == '__main__':
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
