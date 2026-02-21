from flask_restx import Namespace, Resource
from flask import request
from app.services import facade

ns = Namespace("reviews", description="Review operations")


def _review_to_dict(review):
    return {
        "id": review.id,
        "text": review.text,
        "rating": review.rating,
        "user_id": review.author.id if getattr(review, "author", None) else None,
        "place_id": review.place.id if getattr(review, "place", None) else None,
    }



    def post(self):
        data = request.get_json(silent=True) or {}
        try:
            review = facade.create_review_from_api(data)
            return _review_to_dict(review), 201
        except ValueError as e:
            return {"error": str(e)}, 400

@api.expect(review_model, validate=True)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
class ReviewItem(Resource):
    def get(self, review_id):
        review = facade.get_review(review_id)
        if review is None:
            return {"error": "review not found"}, 404
        return _review_to_dict(review), 200

    def put(self, review_id):
        data = request.get_json(silent=True) or {}
        if not data:
            return {"error": "request body is required"}, 400
        try:
            review = facade.update_review_from_api(review_id, data)
            return {"message": "Review updated successfully"}, 200
        except ValueError as e:
            if "not found" in str(e).lower():
                return {"error": "review not found"}, 404
            return {"error": str(e)}, 400

    def delete(self, review_id):
        try:
            facade.delete_review_from_api(review_id)
            return {"message": "Review deleted successfully"}, 200
        except ValueError as e:
            if "not found" in str(e).lower():
                return {"error": "review not found"}, 404
            return {"error": str(e)}, 400
