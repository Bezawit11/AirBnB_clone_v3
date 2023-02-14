#!/usr/bin/python3
"""
returns json
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ returns status """
    status = {"status": "OK"}
    return jsonify(status)
