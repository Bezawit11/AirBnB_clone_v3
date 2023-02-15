#!/usr/bin/python3
""" View for City objects that handles default API actions """
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.place import Place 
from models.review import Review


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
def reviews(place_id):
    """ Retrieves the list of all review objects corresponding to id"""
    place_review = {}
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    p = storage.all("Review")
    for i in p:
        if i.place_id == place_id:
            place_review.append(i.to_dict())
    return jsonify(place_review)


@app_views.route('/reviews/<review_id>', methods=['GET'])
def r_review_id(review_id):
    """ Retrieves a review object """
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def del_review(review_id):
    """ Deletes a review object """
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """ Creates a review object """
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    new_review = request.get_json()
    if not new_review:
        abort(400, "Not a JSON")
    if "user_id" not in new_review:
        abort(400, "Missing user_id")
    user = storage.get("User", new_review['user_id'])
    if user is None:
        abort(404)
    review = Review(**new_review)
    review.place_id = place_id
    storage.new(review)
    storage.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'])
def put_review(review_id):
    """ Updates a review object """
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    review_request = request.get_json()
    if not review_request:
        abort(400, "Not a JSON")
    for k, v in review_request.items():
        if k not in ['id', 'user_id', 'place_id', 'text', 'created_at', 'updated_at']:
            setattr(review, k, v)
    storage.save()
    return jsonify(review.to_dict()), 200
