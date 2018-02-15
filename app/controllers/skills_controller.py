from app.models.skills import Skill
from flask import jsonify, request
from sqlalchemy.sql import func
from flask_restful import Resource
from app.models.database import db_session


class SkillController(Resource):
    def get(self):
        frequency = request.args.get('frequency')
        rating = request.args.get('rating')
        if rating is None:
            rating = 0
        if frequency is None:
            frequency = 0
        print frequency
        skills_stats = db_session.query(Skill.name,
                                        func.avg(Skill.rating).label('average'),
                                        func.count(Skill.user_id).label('count'))\
            .group_by(Skill.name)\
            .having(func.count(Skill.user_id) > int(frequency)) \
            .having(func.avg(Skill.rating) > int(rating)) \
            .all()
        skills_stats = map(lambda skill: {'skill': skill[0], 'average': skill[1], 'users': skill[2]},
                           skills_stats)
        return jsonify(skills_stats)
