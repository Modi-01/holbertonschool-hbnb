#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields

from app.services import facade

api = Namespace("amenities", description="Amenity operations")

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})
