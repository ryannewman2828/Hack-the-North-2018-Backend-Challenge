from app.models.skills import Skill
from flask import jsonify
from sqlalchemy.sql import func
from sqlalchemy import distinct
from flask_restful import Resource
from app.models.database import db_session


class SkillController(Resource):
    def get(self):
        skills_stats = db_session.query(Skill.name,
                                        func.avg(Skill.rating).label('average'),
                                        func.count(Skill.user_id).label('count'))\
            .group_by(Skill.name).all()
        skills_stats = map(lambda skill: {'skill': skill[0], 'average': skill[1], 'users': skill[2]},
                           skills_stats)
        return jsonify(skills_stats)
