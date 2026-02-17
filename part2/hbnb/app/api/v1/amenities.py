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


@ns.route("/<string:amenity_id>")
class AmenityItem(Resource):
    def get(self, amenity_id):
        amenity = facade.amenities.get(amenity_id)
        if amenity is None:
            return {"error": "amenity not found"}, 404
        return amenity.to_dict(), 200

    def put(self, amenity_id):
        data = request.get_json(silent=True) or {}

        try:
            amenity = facade.update_amenity(amenity_id, data)
            return amenity.to_dict(), 200
        except ValueError as e:
            if "not found" in str(e).lower():
                return {"error": "amenity not found"}, 404
            return {"error": str(e)}, 400

    def delete(self, amenity_id):
        deleted = facade.delete_amenity(amenity_id)
        if deleted is None:
            return {"error": "amenity not found"}, 404
        return {}, 204
