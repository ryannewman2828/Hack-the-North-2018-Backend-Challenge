# third-party imports
from flask import Flask
from flask_restful import Api
from app.models.database import init_db
from app.controllers.user_controller import UserController
from app.controllers.users_controller import UsersController

# local imports
from instance.config import app_config

# db initialization
init_db()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')
api = Api(app)

api.add_resource(UsersController, 'users/')
api.add_resource(UserController, 'users/<string:todo_id>')

from app.controllers import *
