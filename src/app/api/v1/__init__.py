from flask import Blueprint
from flask_restful import Api

v1_blueprint = Blueprint('v1', __name__)
api = Api(v1_blueprint)

