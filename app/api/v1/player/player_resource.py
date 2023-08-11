from flask import request
from flask_restful import Resource

class Player(Resource):
    def get(self):

        return {'message': 'Player GET'}, 200

class Players(Resource):
    def get(self):
        return {'message': 'Players GET'}, 200