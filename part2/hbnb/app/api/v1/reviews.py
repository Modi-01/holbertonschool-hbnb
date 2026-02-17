from flask_restx import Namespace, Resource
from app.services import facade

ns = Namespace("reviews", description="Review operations")


@ns.route("/")
class ReviewsCollection(Resource):
    def get(self):
        
        return {"message": "GET /reviews"}, 200

    def post(self):
        
        return {"message": "POST /reviews"}, 201
