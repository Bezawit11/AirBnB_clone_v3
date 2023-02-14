#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
import os
from api.v1.views import app_views
from models import storage
from flask import Flask, Blueprint
app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    try:
        host = os.environ.get('HBNB_API_HOST')
    except:
        host = '0.0.0.0'
    try:
        port = os.environ.get('HBNB_API_PORT')
    except:
        port = '5000'
    app.run(host=host, port=port)
