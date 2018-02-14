# third-party imports
from flask import Flask
from app.models.database import init_db

# local imports
from instance.config import app_config

# db initialization
init_db()
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')

from app.controllers import *
