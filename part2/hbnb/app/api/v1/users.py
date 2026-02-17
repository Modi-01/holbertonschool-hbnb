from flask_restx import Namespace, Resource

from app.services import facade

ns = Namespace("users", description="User operations")


@ns.route("/")
class UsersCollection(Resource):
    def get(self):
        
        return {"message": "GET /users"}, 200

    def post(self):
        
        return {"message": "POST /users"}, 201


@ns.route("/<string:user_id>")
class UserItem(Resource):
    def get(self, user_id):
        
        return {"message": f"GET /users/{user_id}"}, 200
