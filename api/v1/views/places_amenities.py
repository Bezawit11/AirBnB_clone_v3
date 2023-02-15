#!/usr/bin/python3
"""
view for the link between Place objects and Amenity objects
"""

from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.place import Place
from models.amenity import Amenity

@app_views.route('places/<place_id>/amenities', methods=['GET'])
def amenity(place_id):
    """ Retrieves the list of all amenity objects corresponding to id"""
    place_amenity = {}
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    p = storage.all("Amenity")
    for i in p:
        if i.place_id == place_id:
            place_amenity.append(i)
    return jsonify(place_amenity)

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'])
def del_amenity(review_id):
    """ Deletes amenity object """
    amenity = storage.get("Amenity", amenity_id)
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'],
                 strict_slashes=False)
def post_amenity(place_id):
    """ Creates amenity object """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    if amenity in place.amenities:
        return (jsonify(amenity.to_dict()), 201)
      
