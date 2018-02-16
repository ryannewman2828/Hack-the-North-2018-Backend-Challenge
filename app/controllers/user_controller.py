from app.models.users import User
from app.models.skills import Skill
from flask import request
from flask_restful import Resource
from app.models.database import db_session

string_args = ["name", "picture", "company", "email", "phone", "country"]
float_args = ["latitude", "longitude"]


class UserController(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            user = user.as_dict()
            skills = Skill.query.filter(Skill.user_id == int(user_id)).all()
            user['skills'] = map(lambda skill: skill.as_dict(), skills)
            return {"user": user}, 200
        return {"error": "User not Found"}, 404

    def put(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            args = request.get_json(silent=True)
            for key, value in args.items():
                if args[key] is not None:
                    if (key in string_args and isinstance(args[key], str)) or \
                            (key in float_args and isinstance(args[key], float)):
                        setattr(user, key, args[key])
            db_session.commit()
            return {"user": user.as_dict()}, 200
        return {"error": "User not found"}, 404
