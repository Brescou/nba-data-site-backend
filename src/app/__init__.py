from flask import Flask
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from .api.v1 import v1_blueprint

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(v1_blueprint, url_prefix="/api/v1")

    global mongo
    mongo = MongoClient(app.config["MONGO_URI"])
    jwt.init_app(app)

    return app

mongo = None
jwt = JWTManager()
