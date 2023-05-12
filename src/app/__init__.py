from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from .api.v1 import v1_blueprint
import logging


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(v1_blueprint, url_prefix="/api/v1")

    global mongo
    mongo = MongoClient(app.config["MONGO_URI"])
    jwt.init_app(app)
    configure_logging(app)

    return app


def configure_logging(app):
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config['LOG_LEVEL'])


mongo = None
jwt = JWTManager()
