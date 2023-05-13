from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.configs.config import DevelopmentConfig

app = Flask(__name__)
CORS(app)
app.config.from_object(DevelopmentConfig)
app.secret_key = app.config["JWT_SECRET_KEY"]
jwt = JWTManager(app)

api = Api(app, prefix="/v1")

mongo = MongoClient(app.config["MONGO_URI"])


