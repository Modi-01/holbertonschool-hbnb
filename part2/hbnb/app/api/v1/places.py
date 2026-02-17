from flask_restx import Namespace, Resource
from flask import request
from app.services import facade

ns = Namespace("places", description="Place operations")


def _place_to_dict(place, include_reviews=True):
    data = place.to_dict() if hasattr(place, "to_dict") else {
        "id": place.id,
        "name": place.name,
        "description": place.description,
        "price_per_night": place.price_per_night,
        "latitude": place.latitude,
        "longitude": place.longitude,
    }

    # Map model fields to API expected fields
    data["title"] = place.name
    data["price"] = place.price_per_night

    # Owner details
    owner = getattr(place, "owner", None)
    data["owner"] = owner.to_dict() if owner and hasattr(owner, "to_dict") else None
    data["owner_id"] = owner.id if owner else None

    # Amenities
    amenities = getattr(place, "amenity", [])
    data["amenities"] = [
        a.to_dict() if hasattr(a, "to_dict") else {"id": a.id, "name": a.name}
        for a in amenities
    ]

    # Reviews (Task 5 requirement)
    if include_reviews:
        reviews = getattr(place, "review", [])
        data["reviews"] = [
            r.to_dict() if hasattr(r, "to_dict") else {
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.author.id if getattr(r, "author", None) else None
            }
            for r in reviews
        ]

    return data


@ns.route("/")
class PlacesCollection(Resource):
    def get(self):
        places = facade.get_all_places()
        return [_place_to_dict(p, include_reviews=False) for p in places], 200

    def post(self):
        data = request.get_json(silent=True) or {}
        try:
            place = facade.create_place_from_api(data)
            return _place_to_dict(place, include_reviews=True), 201
        except ValueError as e:
            return {"error": str(e)}, 400


@ns.route("/<string:place_id>")
class PlaceItem(Resource):
    def get(self, place_id):
        place = facade.get_place(place_id)
        if place is None:
            return {"error": "place not found"}, 404
        return _place_to_dict(place, include_reviews=True), 200

    def put(self, place_id):
        data = request.get_json(silent=True) or {}
        if not data:
            return {"error": "request body is required"}, 400

        try:
            place = facade.update_place_from_api(place_id, data)
            return _place_to_dict(place, include_reviews=True), 200
        except ValueError as e:
            if "not found" in str(e).lower():
                return {"error": "place not found"}, 404
            return {"error": str(e)}, 400


@ns.route("/<string:place_id>/reviews")
class PlaceReviewList(Resource):
    def get(self, place_id):
        try:
            reviews = facade.get_reviews_by_place(place_id)
            # return simplified review list as in examples
            out = []
            for r in reviews:
                out.append({
                    "id": r.id,
                    "text": r.text,
                    "rating": r.rating
                })
            return out, 200
        except ValueError as e:
            if "place not found" in str(e).lower():
                return {"error": "place not found"}, 404
            return {"error": str(e)}, 400
