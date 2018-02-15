from app.models.users import User
from flask import jsonify, request
from flask_restful import Resource
from app.models.database import db_session


class UserController(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            user = user.as_dict()
            return jsonify(user)
        return {"error": "User not Found"}, 404

    def put(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            args = request.get_json(silent=True)
            for key, value in args.items():
                if args[key] is not None:
                    setattr(user, key, args[key])
            db_session.commit()
            return jsonify(user.as_dict())
        return {"error": "User not found"}, 404
