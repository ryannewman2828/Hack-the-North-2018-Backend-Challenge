from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import app.models
import requests


engine = create_engine('sqlite:////Users/ryannewman/Documents/Side Projects/Hack-the-North-2018-Backend-Challenge/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.create_all(bind=engine)

json = requests.get('https://htn-interviews.firebaseio.com/users.json?download').json()
for user_data in json:
    user = app.models.User(user_data)
    db_session.add(user)
    db_session.flush()
    for skill in user_data['skills']:
        skill = app.models.Skill(skill['name'], skill['rating'], user.id)
        db_session.add(skill)
db_session.commit()
