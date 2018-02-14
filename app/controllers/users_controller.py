from app.models.users import User
from flask import jsonify
from flask_restful import Resource


class UsersController(Resource):
    def get(self):
        users = map(lambda user: user.as_dict(), User.query.all())
        return jsonify(users)
