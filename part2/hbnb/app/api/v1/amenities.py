from flask_restx import Namespace, Resource
from app.services import facade

ns = Namespace("amenities", description="Amenity operations")


@ns.route("/")
class AmenitiesCollection(Resource):
    def get(self):
        
        return {"message": "GET /amenities"}, 200

    def post(self):
        
        return {"message": "POST /amenities"}, 201
