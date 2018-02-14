from sqlalchemy import Column, ForeignKey, Integer, String
from app.models.database import Base


#TODO: REPLACE COLUMN TYPES
class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=False)
    rating = Column(Integer, unique=False)
    user_id = Column(Integer, ForeignKey("users.id"), unique=False)

    def __init__(self, name, rating, user_id):
        self.name = name
        self.rating = rating
        self.user_id = user_id

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
