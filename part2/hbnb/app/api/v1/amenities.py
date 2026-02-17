#!/usr/bin/python3
from flask_restx import Namespace, Resource
from flask import request

from app.services import facade

ns = Namespace("amenities", description="Amenity operations")

@ns.route("/")
class AmenitiesCollection(Resource):
    def get(self):
        """
        GET /api/v1/amenities/
        Return list of amenities
        """
        amenities = facade.amenities.list_all()
        return [a.to_dict() for a in amenities], 200
def post(self):
        """
        POST /api/v1/amenities/
        Create a new amenity
        """
        data = request.get_json(silent=True) or {}

        name = data.get("name")
        if not name:
            return {"error": "name is required"}, 400
try:
            amenity = facade.create_amenity(name)
            return amenity.to_dict(), 201
        except ValueError as e:
            return {"error": str(e)}, 400
            
