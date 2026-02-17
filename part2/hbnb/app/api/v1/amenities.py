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
