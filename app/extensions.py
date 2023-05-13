from app.service.db_mongo import Mongo

mongo = Mongo()

from flask_jwt_extended import JWTManager

jwt = JWTManager()

from flask_cors import CORS

cors = CORS()

from flask_restful import Api

api = Api()