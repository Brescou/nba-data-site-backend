from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.service.db_mongo import Mongo

jwt = JWTManager()

cors = CORS()

mongo = Mongo()
