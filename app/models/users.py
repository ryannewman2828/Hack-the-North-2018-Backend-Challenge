from sqlalchemy import Column, ForeignKey, Integer, String
from app.models.database import Base

#TODO: REPLACE COLUMN TYPES
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=False)
    picture = Column(String(100), unique=False)
    company = Column(String(100), unique=False)
    email = Column(String(120), unique=True)
    phone = Column(String(100), unique=True)
    country = Column(String(100), unique=False)
    longitude = Column(String(100), unique=False)
    latitude = Column(String(100), unique=False)

    def __init__(self, user=None):
        self.name = user['name']
        self.picture = user['picture']
        self.company = user['company']
        self.email = user['email']
        self.phone = user['phone']
        self.longitude = user['longitude']
        self.latitude = user['latitude']

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
