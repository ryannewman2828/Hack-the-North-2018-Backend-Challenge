from sqlalchemy import Column, Integer, String, Float
from app.models.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=False)
    picture = Column(String(64), unique=False)
    company = Column(String(64), unique=False)
    email = Column(String(64), unique=True)
    phone = Column(String(64), unique=True)
    country = Column(String(64), unique=False)
    longitude = Column(Float, unique=False)
    latitude = Column(Float, unique=False)

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
