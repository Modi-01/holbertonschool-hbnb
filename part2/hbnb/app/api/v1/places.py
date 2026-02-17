from flask_restx import Namespace, Resource
from app.services import facade

ns = Namespace("places", description="Place operations")


@ns.route("/")
class PlacesCollection(Resource):
    def get(self):
        
        return {"message": "GET /places"}, 200

    def post(self):
        
        return {"message": "POST /places"}, 201


@ns.route("/<string:place_id>")
class PlaceItem(Resource):
    def get(self, place_id):
        
        return {"message": f"GET /places/{place_id}"}, 200
