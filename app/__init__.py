# third-party imports
from flask import Flask
from app.database import init_db

# local imports
from instance.config import app_config

# db initialization
init_db()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app
