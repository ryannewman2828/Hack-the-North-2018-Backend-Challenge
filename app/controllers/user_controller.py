from app.models.users import User
from flask import jsonify
from flask_restful import Resource


class UserController(Resource):
    def get(self, user_id):
        users = User.query.get(user_id).as_dict()
        return jsonify(users)
