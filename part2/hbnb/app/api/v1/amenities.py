#!/usr/bin/python3
from flask_restx import Namespace, Resource
from flask import request

from app.services import facade

ns = Namespace("amenities", description="Amenity operations")
