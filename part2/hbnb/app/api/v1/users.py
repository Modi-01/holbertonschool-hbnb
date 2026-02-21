#!/usr/bin/python3
from flask_restx import Namespace, Resource

from app.services import facade

ns = Namespace("users", description="User operations")


@ns.route("/")
class UsersCollection(Resource):
    def get(self):
        """
        GET /api/v1/users/
        Return list of all users (without password)
        """
        users = facade.list_users()
        return [u.to_dict() for u in users], 200

    def post(self):
        """
        POST /api/v1/users/
        Create a new user
        """
        data = request.get_json(silent=True) or {}

        try:
            user = facade.create_user(
                email=data.get("email"),
                password=data.get("password"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                is_admin=data.get("is_admin", False),
            )
            return user.to_dict(), 201

        except ValueError as e:
            msg = str(e).lower()
            if "unique" in msg or "already" in msg:
                return {"error": str(e)}, 409
            return {"error": str(e)}, 400


@ns.route("/<string:user_id>")
class UserItem(Resource):
    def get(self, user_id):
        """
        GET /api/v1/users/<user_id>
        Return user by id (without password)
        """
        user = facade.get_user(user_id)
        if user is None:
            return {"error": "user not found"}, 404
        return user.to_dict(), 200

    def put(self, user_id):
        """
        PUT /api/v1/users/<user_id>
        Update user data (without password in response)
        """
        data = request.get_json(silent=True) or {}

         
        if not data:
            return {"error": "request body is required"}, 400

        for field in ("id", "created_at", "updated_at"):
            data.pop(field, None)

        data.pop("email", None)

        try:
            user = facade.update_user(user_id, data)
            return user.to_dict(), 200

        except ValueError as e:
            if "not found" in str(e).lower():
                return {"error": "user not found"}, 404
            return {"error": str(e)}, 400
