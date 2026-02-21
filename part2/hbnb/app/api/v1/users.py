#!/usr/bin/python3
from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade
import re

api = Namespace("users", description="User operations")
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})
